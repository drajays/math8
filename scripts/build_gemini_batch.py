#!/usr/bin/env python3
"""Build data/batches/batch_NN.json from structured Gemini open-glassbox content."""
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
BATCHES_DIR = REPO / "data" / "batches"

NOTE_BY_CH = {
    1: "CH01-sec-rational-numbers",
    2: "CH02-sec-laws-of-exponents",
    3: "CH03-sec-square-numbers-or-perfect-squares",
}

TOPIC_BY_CH = {n: f"math-ch{n}" for n in range(1, 21)}


def step(rule, why, math):
    return {"rule": rule, "why": why, "math": math}


def mk_q(batch, global_num, chapter, question, answer, steps, *, local_label=None):
    bnum = global_num - (batch - 1) * 50
    lid = f"Q-GEM-B{batch:02d}-{global_num:03d}"
    return {
        "id": lid,
        "chapter": chapter,
        "batch": batch,
        "batchNum": bnum,
        "globalNum": global_num,
        "localLabel": local_label or f"Q{global_num}",
        "topicId": TOPIC_BY_CH[chapter],
        "type": "practice",
        "subtopic": f"Gemini Open Glassbox · Batch {batch}",
        "question": question,
        "answer": answer,
        "options": [],
        "glassboxSteps": steps,
        "linked_note_id": NOTE_BY_CH.get(chapter, f"CH{chapter:02d}-sec-introduction"),
        "source": f"gemini-batch-{batch:02d}",
    }


def batch_01():
    B = 1
    qs = []

    # —— Chapter 1: Rational Numbers (Q1–Q20) ——
    qs.append(mk_q(B, 1, 1,
        "Write the additive inverse of each: (i) $1$ (ii) $-\\dfrac{1}{9}$ (iii) $-\\dfrac{2}{3}$ (iv) $2$ (v) $-\\dfrac{9}{1}$",
        "(i) $-1$ (ii) $\\dfrac{1}{9}$ (iii) $\\dfrac{2}{3}$ (iv) $-2$ (v) $9$",
        [step("Concept", "Additive inverse changes the sign.", "Additive inverse of $a$ is $-a$."),
         step("Apply", "Flip the sign of each number.", "(i) $-1$, (ii) $\\dfrac{1}{9}$, (iii) $\\dfrac{2}{3}$, (iv) $-2$, (v) $9$")]))

    qs.append(mk_q(B, 2, 1,
        "Find the multiplicative inverse of: (i) $-\\dfrac{5}{8}$ (ii) $\\dfrac{3}{-7}$ (iii) $-1$ (iv) $1$",
        "(i) $-\\dfrac{8}{5}$ (ii) $-\\dfrac{7}{3}$ (iii) $-1$ (iv) $1$",
        [step("Concept", "Reciprocal = flip numerator and denominator; sign unchanged.", "$\\text{Reciprocal of }\\dfrac{p}{q}=\\dfrac{q}{p}$"),
         step("Apply", "Flip each fraction.", "(i) $-\\dfrac{8}{5}$, (ii) $-\\dfrac{7}{3}$, (iii) $-1$ (self-reciprocal), (iv) $1$")]))

    qs.append(mk_q(B, 3, 1,
        "The product of two rational numbers is $2$. If one number is $\\dfrac{1}{7}$, find the other.",
        "$14$",
        [step("Set up", "Let the unknown be $x$.", "$\\dfrac{1}{7} \\times x = 2$"),
         step("Isolate", "Multiply both sides by the reciprocal $\\dfrac{7}{1}$.", "$x = 2 \\times 7 = 14$")]))

    qs.append(mk_q(B, 4, 1,
        "Find five rational numbers between $1$ and $2$.",
        "$\\dfrac{7}{6},\\dfrac{8}{6},\\dfrac{9}{6},\\dfrac{10}{6},\\dfrac{11}{6}$",
        [step("Rewrite", "Use a common denominator larger than $5$.", "$1=\\dfrac{6}{6}$, $2=\\dfrac{12}{6}$"),
         step("Pick five", "Choose fractions strictly between $\\dfrac{6}{6}$ and $\\dfrac{12}{6}$.", "$\\dfrac{7}{6},\\dfrac{4}{3},\\dfrac{3}{2},\\dfrac{5}{3},\\dfrac{11}{6}$")]))

    qs.append(mk_q(B, 5, 1,
        "Show that rational numbers are closed under $+$, $-$, $\\times$, $\\div$ (except $\\div 0$).",
        "Each operation on two rationals gives another rational.",
        [step("Addition", "Example: $\\dfrac{1}{2}+\\dfrac{1}{3}=\\dfrac{5}{6}$ (rational).", "$\\dfrac{5}{6}$"),
         step("Subtraction", "$\\dfrac{1}{2}-\\dfrac{1}{3}=\\dfrac{1}{6}$.", "$\\dfrac{1}{6}$"),
         step("Multiplication", "$\\dfrac{1}{2}\\times\\dfrac{1}{3}=\\dfrac{1}{6}$.", "$\\dfrac{1}{6}$"),
         step("Division", "$\\dfrac{1}{2}\\div\\dfrac{1}{3}=\\dfrac{3}{2}$ (non-zero divisor).", "$\\dfrac{3}{2}$")]))

    qs.append(mk_q(B, 6, 1, "Find five rational numbers smaller than $5$.",
        "$4,\\,3,\\,2,\\,1,\\,0$",
        [step("Concept", "Rationals include integers and fractions less than $5$.", "Any $q<5$ works."),
         step("Answer", "Pick five simple values.", "$4,3,2,1,0$")]))

    qs.append(mk_q(B, 7, 1,
        "Verify commutative property of addition for $\\dfrac{2}{3}$ and $-\\dfrac{5}{7}$.",
        "Both orders give $-\\dfrac{1}{21}$.",
        [step("Order A", "$\\dfrac{2}{3}+\\left(-\\dfrac{5}{7}\\right)$, LCM $21$.", "$\\dfrac{14}{21}-\\dfrac{15}{21}=-\\dfrac{1}{21}$"),
         step("Order B", "$-\\dfrac{5}{7}+\\dfrac{2}{3}$.", "$-\\dfrac{15}{21}+\\dfrac{14}{21}=-\\dfrac{1}{21}$")]))

    qs.append(mk_q(B, 8, 1,
        "Verify associative property of multiplication for $-\\dfrac{3}{5}$, $\\dfrac{2}{7}$, $\\dfrac{1}{4}$.",
        "Both groupings give $-\\dfrac{3}{70}$.",
        [step("Group left", "$\\left[-\\dfrac{3}{5}\\times\\dfrac{2}{7}\\right]\\times\\dfrac{1}{4}$.", "$-\\dfrac{6}{140}=-\\dfrac{3}{70}$"),
         step("Group right", "$-\\dfrac{3}{5}\\times\\left[\\dfrac{2}{7}\\times\\dfrac{1}{4}\\right]$.", "$-\\dfrac{3}{70}$")]))

    qs.append(mk_q(B, 9, 1, "Find additive and multiplicative inverses of $-\\dfrac{7}{9}$.",
        "Additive: $\\dfrac{7}{9}$; Multiplicative: $-\\dfrac{9}{7}$.",
        [step("Additive", "Change sign.", "$\\dfrac{7}{9}$"),
         step("Multiplicative", "Flip fraction.", "$-\\dfrac{9}{7}$")]))

    qs.append(mk_q(B, 10, 1,
        "Represent on the number line: (i) $\\dfrac{3}{4}$ (ii) $-\\dfrac{5}{3}$ (iii) $\\dfrac{7}{2}$",
        "(i) between $0$ and $1$ (ii) left of $0$ (iii) $3.5$",
        [step("(i)", "Divide unit into $4$ parts; mark $3$.", "$\\dfrac{3}{4}$"),
         step("(ii)", "$-\\dfrac{5}{3}=-1\\dfrac{2}{3}$ left of zero.", "$-\\dfrac{5}{3}$"),
         step("(iii)", "$\\dfrac{7}{2}=3.5$.", "$3.5$")]))

    qs.append(mk_q(B, 11, 1,
        "Fill in: (i) $\\underline{\\ ?\\ }\\div(-3)=-\\dfrac{4}{15}$ (ii) Numbers that are their own reciprocals.",
        "(i) $\\dfrac{4}{5}$ (ii) $1$ and $-1$",
        [step("(i)", "Multiply both sides by $-3$.", "$x=\\left(-\\dfrac{4}{15}\\right)(-3)=\\dfrac{4}{5}$"),
         step("(ii)", "Flip $1$ and $-1$ gives the same value.", "$1,-1$")]))

    qs.append(mk_q(B, 12, 1,
        "Prove $\\dfrac{a}{b}\\times\\dfrac{c}{d}=\\dfrac{c}{d}\\times\\dfrac{a}{b}$ for rationals.",
        "Both sides equal $\\dfrac{ac}{bd}$.",
        [step("LHS", "Multiply numerators and denominators.", "$\\dfrac{ac}{bd}$"),
         step("RHS", "Commutative multiplication of integers.", "$\\dfrac{ca}{db}=\\dfrac{ac}{bd}$")]))

    qs.append(mk_q(B, 13, 1, "Find three rational numbers between $-\\dfrac{1}{2}$ and $\\dfrac{3}{4}$.",
        "$-\\dfrac{1}{4},\\,0,\\,\\dfrac{1}{4}$",
        [step("Common denom.", "$-\\dfrac{1}{2}=-\\dfrac{2}{4}$, compare to $\\dfrac{3}{4}$.", "Between $-\\dfrac{2}{4}$ and $\\dfrac{3}{4}$"),
         step("Pick three", "Choose values in between.", "$-\\dfrac{1}{4},0,\\dfrac{1}{4}$")]))

    qs.append(mk_q(B, 14, 1,
        "Sum of two rationals is $-\\dfrac{5}{6}$. One is $\\dfrac{2}{3}$. Find the other.",
        "$-\\dfrac{3}{2}$",
        [step("Equation", "$x+\\dfrac{2}{3}=-\\dfrac{5}{6}$.", "$x=-\\dfrac{5}{6}-\\dfrac{2}{3}$"),
         step("Solve", "LCM $6$.", "$x=-\\dfrac{5}{6}-\\dfrac{4}{6}=-\\dfrac{9}{6}=-\\dfrac{3}{2}$")]))

    qs.append(mk_q(B, 15, 1,
        "Simplify: $\\left(-\\dfrac{3}{8}\\right)+\\dfrac{5}{12}-\\left(-\\dfrac{7}{24}\\right)+\\dfrac{1}{6}$.",
        "$\\dfrac{1}{2}$",
        [step("Signs", "$-\\left(-\\dfrac{7}{24}\\right)=+\\dfrac{7}{24}$.", "Combine over LCM $24$"),
         step("Convert", "$-\\dfrac{9}{24}+\\dfrac{10}{24}+\\dfrac{7}{24}+\\dfrac{4}{24}$.", "$\\dfrac{12}{24}=\\dfrac{1}{2}$")]))

    qs.append(mk_q(B, 16, 1, "Express $0.\\overline{3}$ as $\\dfrac{p}{q}$.",
        "$\\dfrac{1}{3}$",
        [step("Let", "$x=0.333\\ldots$", "$x=0.\\overline{3}$"),
         step("Multiply", "$10x=3.333\\ldots$; subtract: $9x=3$.", "$x=\\dfrac{3}{9}=\\dfrac{1}{3}$")]))

    qs.append(mk_q(B, 17, 1,
        "If $x=\\dfrac{2}{3}$, $y=-\\dfrac{5}{4}$, find $(x+y)(x-y)$.",
        "$-\\dfrac{161}{144}$",
        [step("$x+y$", "LCM $12$.", "$-\\dfrac{7}{12}$"),
         step("$x-y$", "$\\dfrac{2}{3}+\\dfrac{5}{4}=\\dfrac{23}{12}$.", "$(x+y)(x-y)=-\\dfrac{161}{144}$")]))

    qs.append(mk_q(B, 18, 1,
        "Which are rational? (i) $\\sqrt{2}$ (ii) $0$ (iii) $-\\dfrac{7}{2}$ (iv) $\\pi$",
        "(ii) and (iii) only.",
        [step("(i)(iv)", "Non-terminating non-repeating decimals.", "Irrational"),
         step("(ii)(iii)", "$0=\\dfrac{0}{1}$, $-\\dfrac{7}{2}$ is $\\dfrac{p}{q}$.", "Rational")]))

    qs.append(mk_q(B, 19, 1, "Find $x$ if $\\dfrac{3x-5}{4}=\\dfrac{2x+1}{3}$.",
        "$x=19$",
        [step("Cross-multiply", "$3(3x-5)=4(2x+1)$.", "$9x-15=8x+4$"),
         step("Solve", "$x=19$.", "$x=19$")]))

    qs.append(mk_q(B, 20, 1,
        "Prove: a rational number plus its additive inverse is zero.",
        "$\\dfrac{a}{b}+\\left(-\\dfrac{a}{b}\\right)=0$.",
        [step("Let", "Number $\\dfrac{a}{b}$, inverse $-\\dfrac{a}{b}$.", "Add numerators"),
         step("Result", "$\\dfrac{a-a}{b}=\\dfrac{0}{b}=0$.", "$0$")]))

    # —— Chapter 2: Exponents (Q21–Q40) ——
    ch2 = [
        (21, "Simplify with positive exponents: $(-4)^5\\div(-4)^8$.", "$\\dfrac{1}{(-4)^3}$",
         [step("Division rule", "$(-4)^{5-8}=(-4)^{-3}$.", "Negative exponent → reciprocal." )]),
        (22, "Evaluate: $a^2\\times a^3\\times a^{-5}$.", "$1$",
         [step("Add powers", "$a^{2+3-5}=a^0$.", "$a^0=1$")]),
        (23, "Express $4^{-3}$ as a power of base $2$.", "$2^{-6}$",
         [step("Rewrite", "$4=2^2$.", "$(2^2)^{-3}=2^{-6}$")]),
        (24, "Find $x$: $\\left(\\dfrac{11}{9}\\right)^3\\left(\\dfrac{9}{11}\\right)^6=\\left(\\dfrac{11}{9}\\right)^{2x-1}$.", "$x=-1$",
         [step("Match bases", "$\\left(\\dfrac{9}{11}\\right)^6=\\left(\\dfrac{11}{9}\\right)^{-6}$.", "$3-6=2x-1$"),
          step("Solve", "$-3=2x-1$.", "$x=-1$")]),
        (25, "Simplify: $(2^{-3}\\times 2^{-4})\\div 2^{-7}$.", "$1$",
         [step("Inside", "$2^{-7}$.", "$2^{-7}\\div 2^{-7}=2^0=1$")]),
        (26, "Express $0.00000000000837$ in standard form.", "$8.37\\times 10^{-12}$",
         [step("Shift decimal", "12 places right.", "$8.37\\times 10^{-12}$")]),
        (27, "Find $(5^0+6^0+7^0)\\times 8^0$.", "$3$",
         [step("Zero power", "Each term is $1$.", "$(1+1+1)\\times 1=3$")]),
        (28, "Simplify $(3^{-5}\\times 3^{-7})\\div 3^{-10}$ (positive exponent).", "$\\dfrac{1}{3^2}$",
         [step("Steps", "$3^{-12}\\div 3^{-10}=3^{-2}$.", "$\\dfrac{1}{9}$")]),
        (29, "Write $149600000$ in standard form.", "$1.496\\times 10^8$",
         [step("Notation", "Decimal after first digit.", "$1.496\\times 10^8$")]),
        (30, "If $\\left(\\dfrac{2}{3}\\right)^x=\\dfrac{8}{27}$, find $x$.", "$x=3$",
         [step("Rewrite RHS", "$\\dfrac{8}{27}=\\left(\\dfrac{2}{3}\\right)^3$.", "$x=3$")]),
        (31, "Simplify $(5^{-3}\\times 5^{-4})\\div 5^{-7}$ in exponential form.", "$5^0$",
         [step("Rules", "Product then quotient of powers.", "$5^0$")]),
        (32, "Find $(-3)^{-4}\\times(-3)^{-2}$.", "$\\dfrac{1}{729}$",
         [step("Add", "$(-3)^{-6}=\\dfrac{1}{(-3)^6}$.", "$\\dfrac{1}{729}$")]),
        (33, "Express $0.0000056$ in standard form.", "$5.6\\times 10^{-6}$",
         [step("Shift", "6 places right.", "$5.6\\times 10^{-6}$")]),
        (34, "If $2^x=32$ and $3^y=81$, find $x+y$.", "$9$",
         [step("Solve", "$x=5$, $y=4$.", "$x+y=9$")]),
        (35, "Simplify $\\left[\\left(-\\dfrac{2}{3}\\right)^3\\left(-\\dfrac{2}{3}\\right)^{-5}\\right]\\div\\left(-\\dfrac{2}{3}\\right)^{-2}$.", "$1$",
         [step("Bracket", "Power adds to $(-2/3)^{-2}$.", "Divide same base → exponent $0$")]),
        (36, "Write $3.45\\times 10^6$ in usual form.", "$3450000$",
         [step("Move decimal", "6 places right.", "$3450000$")]),
        (37, "Prove $(a^m)^n=a^{mn}$.", "Proven by repeated multiplication.",
         [step("Meaning", "$(a^m)^n=a^m\\times\\cdots$ ($n$ times).", "Add $m$ exactly $n$ times → $mn$")]),
        (38, "Find $x$ if $\\left(\\dfrac{5}{4}\\right)^{-x}=\\left(\\dfrac{4}{5}\\right)^3$.", "$x=3$",
         [step("Reciprocal", "$\\left(\\dfrac{4}{5}\\right)^3=\\left(\\dfrac{5}{4}\\right)^{-3}$.", "$-x=-3$")]),
        (39, "Simplify $2^{-3}\\times 3^{-3}\\times 6^3$.", "$1$",
         [step("Combine", "$6^{-3}\\times 6^3$.", "$6^0=1$")]),
        (40, "Express $0.000000567$ in standard form.", "$5.67\\times 10^{-7}$",
         [step("Shift", "7 places right.", "$5.67\\times 10^{-7}$")]),
    ]
    for gn, qu, ans, st in ch2:
        qs.append(mk_q(B, gn, 2, qu, ans, st, local_label=f"Ch2-Q{gn-20}"))

    # —— Chapter 3: Squares (Q41–Q50) ——
    ch3 = [
        (41, "Find $35^2$ using $(a+b)^2=a^2+2ab+b^2$.", "$1225$",
         [step("Split", "$35=30+5$.", "$(30+5)^2=900+300+25$"),
          step("Sum", "$1225$.", "$1225$")]),
        (42, "Find $\\sqrt{1296}$ by prime factorisation.", "$36$",
         [step("Factor", "$1296=2^4\\times 3^4$.", "Pair primes"),
          step("Root", "$2^2\\times 3^2=36$.", "$36$")]),
        (43, "Smallest number to divide $9408$ to get a perfect square.", "$3$",
         [step("Factor", "$9408=2^6\\times 3\\times 7^2$.", "Unpaired factor: $3$"),
          step("Answer", "Divide by $3$.", "$3$")]),
        (44, "Find $\\sqrt{0.0064}$.", "$0.08$",
         [step("Fraction", "$\\dfrac{64}{10000}$.", "$\\dfrac{8}{100}=0.08$")]),
        (45, "Square is $7744$. Find the number.", "$88$",
         [step("Factor", "$7744=2^6\\times 11^2$.", "$\\sqrt{7744}=88$")]),
        (46, "Find $\\sqrt{7921}$ by long division.", "$89$",
         [step("Groups", "$\\overline{79}|\\overline{21}$.", "Trial: $89^2=7921$")]),
        (47, "How many non-square integers lie strictly between $25^2$ and $26^2$?", "$50$",
         [step("Formula", "Between $n^2$ and $(n+1)^2$: $2n$ numbers.", "$2\\times 25=50$")]),
        (48, "Smallest square divisible by $6$, $9$, and $15$.", "$900$",
         [step("LCM", "LCM$(6,9,15)=90$.", "Make perfect square: $90\\times 10=900$")]),
        (49, "Remainder when $529$ is divided by $23$.", "$0$",
         [step("Recognise", "$529=23^2$.", "Exact division → remainder $0$")]),
        (50, "Find $\\sqrt{5776}$.", "$76$",
         [step("Estimate", "Between $70^2$ and $80^2$; ends in $6$.", "$76^2=5776$")]),
    ]
    for gn, qu, ans, st in ch3:
        qs.append(mk_q(B, gn, 3, qu, ans, st, local_label=f"Ch3-Q{gn-40}"))

    return qs


BUILDERS = {1: batch_01}


def build(batch_num: int):
    if batch_num not in BUILDERS:
        raise SystemExit(f"No builder for batch {batch_num}")
    BATCHES_DIR.mkdir(parents=True, exist_ok=True)
    data = {
        "batch": batch_num,
        "title": f"Gemini Open Glassbox · Batch {batch_num}",
        "count": 50,
        "globalRange": [(batch_num - 1) * 50 + 1, batch_num * 50],
        "questions": BUILDERS[batch_num](),
    }
    out = BATCHES_DIR / f"batch_{batch_num:02d}.json"
    out.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    by_ch = {}
    for q in data["questions"]:
        by_ch[q["chapter"]] = by_ch.get(q["chapter"], 0) + 1
    print(f"Wrote {out} ({len(data['questions'])} questions)")
    print("  By chapter:", dict(sorted(by_ch.items())))


if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    build(n)
