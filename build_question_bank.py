#!/usr/bin/env python3
"""Build the KV Class VIII glass-box question bank from PaddleOCR JSON. (v2 verified-solver)
Every question is extracted once (same ids, no duplication). Solutions by priority:
 1. sympy-backed VERIFIED solver (linear/proportion eqns, numeric expressions, reciprocals).
 2. small hand-checked conceptual-MCQ table.
 3. honest worked-method scaffold (lists options, gives the approach, NEVER fabricates an answer).
Run: python3 build_question_bank.py  -> rewrites question-bank.generated.js and re-embeds into HTML."""
import json, re
from fractions import Fraction
import sympy as sp
from sympy import symbols, Eq, latex
from sympy.parsing.sympy_parser import (parse_expr, standard_transformations,
    implicit_multiplication_application, convert_xor)

JSON_PATH = "maths-class-viii-question-bank.pdf_by_PaddleOCR-VL-1.6.json"
OUT_PATH  = "question-bank.generated.js"
HTML_PATH = "Glass-Box Math.html"

CHAPTER_NAMES = {"1":"Rational Numbers","2":"Linear Equations","3":"Quadrilaterals",
 "4":"Practical Geometry","5":"Data Handling","6":"Squares & Square Roots",
 "7":"Cubes & Cube Roots","8":"Comparing Quantities","9":"Algebraic Expressions",
 "10":"Visualizing Solids","11":"Mensuration","12":"Exponents & Powers",
 "13":"Direct & Inverse Proportion","14":"Factorisation","15":"Graphs","16":"Playing with Numbers"}

CHAPTER_METHOD = {
 "1":"Use properties of rational numbers (closure, commutativity, associativity, distributivity), additive inverse and reciprocal; take a common denominator before adding/subtracting.",
 "2":"Form a linear equation, clear fractions by the LCM of denominators, collect the variable on one side and constants on the other, then divide by the coefficient. Verify by substitution.",
 "3":"Apply the polygon angle-sum ((n-2)*180 deg) and the properties of the specific quadrilateral (sides, angles, diagonals).",
 "4":"Follow the ruler-and-compass steps in order; a unique quadrilateral needs five independent measurements.",
 "5":"Organise the data, then apply the right formula (mean = sum/observations, mode = most frequent, median = middle value, probability = favourable/total).",
 "6":"Use prime factorisation in pairs for square roots, the identity a^2-b^2=(a-b)(a+b), or long division for large/decimal square roots.",
 "7":"Group prime factors in triples for cube roots; a perfect cube has each prime a multiple of three times.",
 "8":"Translate percentage / profit-loss / discount / interest into the standard formula (e.g. SI = PRT/100) and substitute.",
 "9":"Apply algebraic identities ((a+-b)^2, a^2-b^2, (x+a)(x+b)) and exponent laws; multiply term by term and collect like terms.",
 "10":"Use Euler's formula F+V-E=2; count faces, edges and vertices from the net or figure.",
 "11":"Pick the correct mensuration formula (area / surface area / volume) for the named shape and substitute dimensions in consistent units.",
 "12":"Apply exponent laws (a^m*a^n=a^(m+n), (a^m)^n=a^(mn), a^-n=1/a^n) and equate powers when bases match.",
 "13":"Decide direct (ratio constant) or inverse (product constant) variation, set up the proportion, and solve.",
 "14":"Factorise by common factor, grouping, or an identity (a^2-b^2, perfect-square trinomial); check by expanding.",
 "15":"Plot points on the Cartesian plane, read coordinates as (x, y), and interpret the graph.",
 "16":"Use divisibility tests and place value (e.g. a two-digit number = 10a+b) to set up and solve the puzzle."}

SKIP_RE = re.compile(r"Prepared by|Page\s*[-\u2013]?\s*\d|KENDRIYA|VIDYALAYA|Copy to:|MY FATHER|"
 r"question bank|worksheets for|May God bless|Yours sincerely|Donimalai|Bangalore|"
 r"Regional Office|Dated:|Dear Shri|Mathematics is one", re.I)

def load_text():
    with open(JSON_PATH, encoding="utf-8") as f: data = json.load(f)
    parts=[]
    for page in data:
        pr = page.get("prunedResult", page)
        for b in pr.get("parsing_res_list", []):
            c=b.get("block_content","")
            if c: parts.append(c)
    return "\n".join(parts)

def clean_latex(s):
    s=re.sub(r"\$\$([^$]+)\$\$", r" $\1$ ", s); s=re.sub(r"\s+"," ",s).strip()
    s=re.sub(r"\\underline\{\\text\{\}\}","______",s); s=re.sub(r"\\underline\{[^}]+\}","",s)
    return s

def parse_options(text):
    opts={}
    for m in re.finditer(r"\(([a-d])\)\s*([^()]+?)(?=\([a-d]\)|$)", text, re.I|re.S):
        opts[m.group(1).lower()]=clean_latex(m.group(2).strip())
    return opts

def strip_options(text):
    return re.split(r"\([a-d]\)", text, maxsplit=1, flags=re.I)[0].strip()

X,Y=symbols("x y")
T=standard_transformations+(implicit_multiplication_application, convert_xor)

def _ftex(v):
    try: r=sp.Rational(v)
    except Exception: return sp.latex(v)
    if r.q==1: return str(r.p)
    return f"{'-' if r.p<0 else ''}\\dfrac{{{abs(r.p)}}}{{{r.q}}}"

def _norm(s):
    s=s.replace("$","").strip()
    s=re.sub(r"\\left\s*","",s); s=re.sub(r"\\right\s*","",s)
    s=re.sub(r"(-?\d+)\\?d?frac\{(\d+)\}\{(\d+)\}", r"(\1+\2/\3)", s)
    for _ in range(3):
        s=re.sub(r"\\dfrac\{([^{}]+)\}\{([^{}]+)\}", r"((\1)/(\2))", s)
        s=re.sub(r"\\frac\{([^{}]+)\}\{([^{}]+)\}", r"((\1)/(\2))", s)
    s=re.sub(r"\\sqrt\{([^{}]+)\}", r"sqrt(\1)", s); s=re.sub(r"\\sqrt\s*(\d+)", r"sqrt(\1)", s)
    s=s.replace("\\times","*").replace("\\cdot","*").replace("\\div","/").replace("^","**")
    s=re.sub(r"\\[a-zA-Z]+","",s).replace("{","(").replace("}",")")
    s=re.sub(r"[^0-9xyXY+\-*/(). qrt]","",s)
    return re.sub(r"\s+","",s)

def _parse(s): return parse_expr(_norm(s), transformations=T, local_dict={"x":X,"y":Y})

def solve_linear(stem):
    if re.match(r"\s*if\b", stem, re.I): return None
    if re.search(r"identity|product of|prove|verif|graph|table", stem, re.I): return None
    body=re.sub(r"^(solve|find)\b[^-0-9(\\]*","",stem,flags=re.I).strip().rstrip(".")
    if body.count("=")!=1 or not re.search(r"x|y",body): return None
    var="x" if re.search(r"x",body) else "y"; v=X if var=="x" else Y
    try:
        ls,rs=body.split("=",1); L,R=_parse(ls),_parse(rs)
        if not (L.free_symbols or R.free_symbols): return None
        if (L.free_symbols|R.free_symbols)-{v}: return None
        sols=[s for s in sp.solve(Eq(L,R),v) if not s.free_symbols and s.is_real is not False]
        if len(sols)!=1: return None
        sol=sp.nsimplify(sols[0])
        if sp.simplify(L.subs(v,sol)-R.subs(v,sol))!=0: return None
        Ln,Ld=sp.fraction(sp.together(L)); Rn,Rd=sp.fraction(sp.together(R))
        steps=[{"rule":"Given","why":"Write the equation as stated.","math":f"{latex(L)} = {latex(R)}"}]
        if Ld!=1 and Rd!=1:
            lhs,rhs=sp.expand(Ln*Rd),sp.expand(Rn*Ld)
            steps.append({"rule":"Cross-multiply","why":"For a/b = c/d, multiply across the equals sign: a*d = b*c.","math":f"{latex(lhs)} = {latex(rhs)}"})
            poly=sp.expand(lhs-rhs)
        else:
            den=sp.lcm([Ld,Rd])
            if den!=1:
                lhs,rhs=sp.expand(sp.cancel(L*den)),sp.expand(sp.cancel(R*den))
                steps.append({"rule":"Clear fractions","why":f"Multiply every term by the LCM of the denominators ({latex(den)}) so no fractions remain.","math":f"{latex(lhs)} = {latex(rhs)}"})
                poly=sp.expand(lhs-rhs)
            else: poly=sp.expand(L-R)
        poly=sp.expand(poly); a,b=poly.coeff(v,1),poly.coeff(v,0)
        if a==0: return None
        steps.append({"rule":"Collect terms","why":f"Move every {var}-term to one side and the constants to the other.","math":f"{latex(a*v)} = {latex(-b)}"})
        steps.append({"rule":"Solve","why":f"Divide both sides by the coefficient of {var} ({latex(a)}).","math":f"{var} = {_ftex(sol)}"})
        steps.append({"rule":"Verify","why":"Substitute the value back \u2014 both sides are equal.","math":f"{var} = {_ftex(sol)}\\;\\checkmark"})
        return {"question":stem,"steps":steps,"answer":f"{var} = {_ftex(sol)}"}
    except Exception: return None

def solve_arith(stem):
    body=re.sub(r"^(find( the value of)?|simplify( and give the answer)?|evaluate|compute|what is|how much is)\s*:?\s*","",stem,flags=re.I).strip().rstrip(".?:").strip()
    leftover=re.sub(r"sqrt","",re.sub(r"\\[a-zA-Z]+","",body))
    if re.search(r"[A-Za-z]{2,}",leftover): return None
    if not re.search(r"[+\-*/]|\^|frac|sqrt",body): return None
    try:
        expr=_parse(body)
        if expr.free_symbols: return None
        val=sp.simplify(expr)
        if val.free_symbols: return None
        ans=_ftex(val) if val.is_rational else latex(sp.nsimplify(val,rational=False))
        show=re.sub(r"\s+"," ",body.replace("$",""))
        return {"question":stem,"steps":[{"rule":"Given","why":"Write the expression to be evaluated.","math":show},
            {"rule":"Compute","why":"Apply BODMAS \u2014 brackets and powers first, then \u00d7/\u00f7, then +/\u2212.","math":f"{show} = {ans}"}],"answer":ans}
    except Exception: return None

def solve_reciprocal(stem):
    if "?" in stem or "multiply" in stem.lower(): return None
    m=re.search(r"reciprocal of\s*\$?\s*(-?\d+\\?d?frac\{\d+\}\{\d+\}|-?\\?d?frac\{\d+\}\{\d+\}|-?\d+(?:\.\d+)?)",stem,re.I)
    if not m: return None
    try:
        val=sp.Rational(_parse(m.group(1)))
        if val==0: return None
        rec=sp.Rational(1)/val
        return {"question":stem,"steps":[{"rule":"Given","why":"Identify the number.","math":_ftex(val)},
            {"rule":"Reciprocal","why":"The reciprocal of a non-zero number inverts it (numerator \u2194 denominator).","math":f"\\dfrac{{1}}{{{_ftex(val)}}} = {_ftex(rec)}"}],"answer":_ftex(rec)}
    except Exception: return None

def solve_verified(stem): return solve_linear(stem) or solve_reciprocal(stem) or solve_arith(stem)

def mcq_knowledge(text,opts):
    low=text.lower()
    pairs=[(r"associative property is not followed","d","Among the listed sets, the non-associative case lives with the rationals."),
        (r"identity for the addition","b","Adding zero leaves any rational unchanged: a + 0 = a."),
        (r"multiplicative identity","a","Multiplying by 1 leaves the value unchanged: a \u00d7 1 = a."),
        (r"zero has.*reciprocal","d","Zero has no reciprocal \u2014 no number times 0 gives 1."),
        (r"their own reciprocals","b","Only 1 and -1 satisfy x = 1/x."),
        (r"product of two rational","d","Closure: a rational times a rational is again rational.")]
    for pat,letter,why in pairs:
        if re.search(pat,low) and letter in opts:
            return glass_mcq(text,opts,letter,opts[letter],why)
    return None

def glass_mcq(text,opts,letter,ans,why):
    q=strip_options(text); opt_lines=" \\quad ".join(f"({k})\\;{v}" for k,v in sorted(opts.items()))
    return {"question":q,"steps":[{"rule":"Given","why":"Read the question and list every option.","math":q},
        {"rule":"Analyse","why":why,"math":opt_lines if opt_lines else q},
        {"rule":"Select","why":"The option that satisfies the rule is the answer.","math":f"({letter})\\;{ans}"}],
        "answer":f"({letter}) {ans}"}

def match_option(computed,opts):
    c=str(computed).replace(" ","")
    for k,v in opts.items():
        v2=re.sub(r"\\dfrac\{([^}]+)\}\{([^}]+)\}",r"\1/\2",v.replace("$","").replace(" ",""))
        v2=re.sub(r"\\frac\{([^}]+)\}\{([^}]+)\}",r"\1/\2",v2)
        if c==v2: return k,v
    try:
        cv=float(Fraction(c)) if "/" in c else float(c)
        for k,v in opts.items():
            vv=re.sub(r"[^\d./-]","",v.replace("$",""))
            if not vv: continue
            fv=float(Fraction(vv)) if "/" in vv else float(vv)
            if abs(cv-fv)<1e-9: return k,opts[k]
    except Exception: pass
    return None,None

def scaffold(stem,ch,opts):
    method=CHAPTER_METHOD.get(ch,"Identify the rule or formula for this topic, apply it step by step, and check your result.")
    steps=[{"rule":"Given","why":"Restate the problem clearly.","math":stem},
        {"rule":"Method","why":method,"math":"\\text{Apply the rule above, showing each step.}"}]
    if opts:
        opt_lines=" \\quad ".join(f"({k})\\;{v}" for k,v in sorted(opts.items()))
        steps.append({"rule":"Options","why":"Test each option against the rule; the one that satisfies it is correct.","math":opt_lines})
    else:
        steps.append({"rule":"Answer","why":"Carry the method through to the final value or statement.","math":"\\text{Your worked answer}"})
    return {"question":stem,"steps":steps,"answer":"? (work it out using the method above)"}

def build_solution(qtext,qtype,ch,opts):
    stem=strip_options(qtext)
    if qtype=="MCQ" and opts:
        comp=solve_verified(stem)
        if comp:
            letter,aval=match_option(re.sub(r"^.*?=\s*","",comp["answer"]),opts)
            if letter:
                why=comp["steps"][-2]["why"] if len(comp["steps"])>1 else "Compute, then match to the option."
                return glass_mcq(stem,opts,letter,aval,why)
        know=mcq_knowledge(qtext,opts)
        if know: return know
        return scaffold(stem,ch,opts)
    comp=solve_verified(stem)
    if comp: return comp
    return scaffold(stem,ch,opts)

def parse_sections(full):
    full=re.sub(r"<div[^>]*>.*?</div>","",full,flags=re.S)
    chunks=re.split(r"(?=#\s*MCQ|PRACTICE QUESTIONS|ASSIGNMENT|HOTS|VALUE BASED QUESTIONS)",full)
    items=[]; sec_idx=0
    for chunk in chunks:
        if len(chunk.strip())<20: continue
        ch_m=re.search(r"CHAPTER\s*[-\u2013]\s*(\d+)",chunk,re.I)
        ch=str(int(ch_m.group(1))) if ch_m else "0"
        if ch=="0": continue
        if "MCQ" in chunk[:120]:
            stype="MCQ"; sec_m=re.search(r"MCQ WORKSHEET[-\sIVXL]*",chunk,re.I)
            sec=chunk[sec_m.start():sec_m.start()+40] if sec_m else "MCQ"
        elif chunk.strip().startswith("PRACTICE"): stype="PRACTICE"; sec="Practice Questions"
        elif "ASSIGNMENT" in chunk[:80]: stype="ASSIGNMENT"; sec="Assignment"
        else: stype="OTHER"; sec="Questions"
        sec_idx+=1
        for m in re.finditer(r"(?:^|\n)\s*(\d+)\.\s*(.+?)(?=\n\s*\d+\.\s|\nPrepared by|\nPage\s*[-\u2013]?\s*\d|\Z)",chunk,re.S):
            num,body=m.group(1),clean_latex(m.group(2).strip())
            if len(body)<8 or SKIP_RE.search(body[:80]): continue
            opts=parse_options(body); sol=build_solution(body,stype,ch,opts)
            items.append({"id":f"qb-{ch}-{sec_idx}-{num}","ch":ch,"chName":CHAPTER_NAMES.get(ch,f"Chapter {ch}"),
                "sec":sec.strip()[:48],"type":stype,"num":int(num),"question":sol["question"],
                "steps":sol["steps"],"answer":sol["answer"],"opts":opts})
    return items

def main():
    full=load_text(); items=parse_sections(full)
    verified=sum(1 for i in items if not i["answer"].startswith("?"))
    print(f"Extracted {len(items)} problems")
    print(f"  Verified / concrete answers : {verified}")
    print(f"  Honest method scaffolds      : {len(items)-verified}")
    by_ch={}
    for i in items: by_ch[i["ch"]]=by_ch.get(i["ch"],0)+1
    for ch in sorted(by_ch,key=lambda x:int(x)): print(f"  Ch {ch:>2}: {by_ch[ch]}")
    with open(OUT_PATH,"w",encoding="utf-8") as f:
        f.write("/* Auto-generated from KV Class VIII Question Bank OCR (v2, verified solver) */\n")
        f.write("const QUESTION_BANK = "); json.dump(items,f,ensure_ascii=False,separators=(",",":")); f.write(";\n")
        f.write(f"const QB_META = {{total:{len(items)},chapters:{len(by_ch)},verified:{verified}}};\n")
    print(f"Wrote {OUT_PATH} ({len(open(OUT_PATH).read())//1024} KB)")
    marker="<!-- QUESTION_BANK_DATA -->"; html=open(HTML_PATH,encoding="utf-8").read()
    if marker not in html: print("Warning: marker not found \u2014 skip embed"); return
    start=html.index(marker); end=html.index("</script>",start)+len("</script>")
    data=open(OUT_PATH,encoding="utf-8").read()
    html=html[:start]+marker+"\n<script>\n"+data+"\n</script>"+html[end:]
    open(HTML_PATH,"w",encoding="utf-8").write(html)
    print(f"Embedded into {HTML_PATH} ({len(html)//1024} KB total)")
    import shutil
    shutil.copy2(HTML_PATH, "index.html")
    print("Synced index.html for GitHub Pages")

if __name__=="__main__": main()
