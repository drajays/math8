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
    4: "CH04-sec-cube-numbers-or-perfect-cubes",
    5: "CH05-sec-numbers-in-general-form",
    6: "CH06-sec-union-of-sets",
    7: "CH07-sec-percentage",
    8: "CH08-sec-simple-interest",
    9: "CH09-sec-direct-variation",
    10: "CH10-sec-fundamental-concepts",
    11: "CH11-sec-factors-of-algebraic-expressions",
    12: "CH12-sec-equations",
    13: "CH13-sec-quadrilateral",
    14: "CH14-sec-construction-of-quadrilaterals",
    18: "CH18-sec-drawing-2-d-representation-of-3-d-objects",
    19: "CH19-sec-area-and-perimeter-of-some-plane-figures",
    20: "CH20-sec-data-handling",
    16: "CH16-sec-coordinate-system",
    17: "CH17-sec-line-symmetry",
}

TOPIC_BY_CH = {n: f"math-ch{n}" for n in range(1, 21)}


def step(rule, why, math):
    return {"rule": rule, "why": why, "math": math}


def mk_q(batch, global_num, chapter, question, answer, steps, *, local_label=None, linked_note_id=None, diagram=None, subtopic=None, batch_num=None):
    bnum = batch_num if batch_num is not None else global_num - (batch - 1) * 50
    lid = f"Q-GEM-B{batch:02d}-{global_num:03d}"
    out = {
        "id": lid,
        "chapter": chapter,
        "batch": batch,
        "batchNum": bnum,
        "globalNum": global_num,
        "localLabel": local_label or f"Q{global_num}",
        "topicId": TOPIC_BY_CH[chapter],
        "type": "practice",
        "subtopic": subtopic or f"Gemini Open Glassbox · Batch {batch}",
        "question": question,
        "answer": answer,
        "options": [],
        "glassboxSteps": steps,
        "linked_note_id": linked_note_id or NOTE_BY_CH.get(chapter, f"CH{chapter:02d}-sec-introduction"),
        "source": f"gemini-batch-{batch:02d}",
    }
    if diagram:
        out["diagram"] = diagram
    return out


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


def batch_02():
    B = 2
    qs = []

    ch3 = [
        (51, "Evaluate: $\\sqrt{0.04}+\\sqrt{0.09}+\\sqrt{0.16}$.", "$0.9$",
         [step("Fractions", "$0.04=\\dfrac{4}{100}$, $0.09=\\dfrac{9}{100}$, $0.16=\\dfrac{16}{100}$.", "Convert decimals"),
          step("Roots", "$\\sqrt{\\dfrac{4}{100}}=0.2$, $\\sqrt{\\dfrac{9}{100}}=0.3$, $\\sqrt{\\dfrac{16}{100}}=0.4$.", "Take square roots"),
          step("Add", "$0.2+0.3+0.4=0.9$.", "$0.9$")]),
        (52, "Find $\\sqrt{\\dfrac{625}{1296}}\\times\\sqrt{\\dfrac{1296}{625}}$.", "$1$",
         [step("Combine", "$\\sqrt{\\dfrac{625}{1296}\\times\\dfrac{1296}{625}}$.", "One radical"),
          step("Cancel", "Fractions are reciprocals → product is $1$.", "$\\sqrt{1}=1$")]),
        (53, "Area of a square field is $5184\\,\\text{m}^2$. Find the side.", "$72\\,\\text{m}$",
         [step("Formula", "Side$^2$ = Area.", "$\\text{Side}=\\sqrt{5184}$"),
          step("Factor", "$5184=2^6\\times 3^4$.", "Pair primes"),
          step("Root", "$(2^3)(3^2)=72$.", "$72\\,\\text{m}$")]),
        (54, "Two consecutive odd numbers have squares summing to $514$. Find them.", "$15$ and $17$",
         [step("Let", "Numbers $x$ and $x+2$.", "$x^2+(x+2)^2=514$"),
          step("Test", "$15^2=225$, $17^2=289$.", "$225+289=514$")]),
        (55, "Find $\\sqrt{0.00059049}$.", "$0.0243$",
         [step("Fraction", "$\\dfrac{59049}{10^8}$.", "$\\sqrt{10^8}=10^4$"),
          step("Root top", "$\\sqrt{59049}=243$.", "$\\dfrac{243}{10000}=0.0243$")]),
        (56, "Using $(a-b)^2=a^2-2ab+b^2$, find $48^2$.", "$2304$",
         [step("Split", "$48=50-2$, so $a=50$, $b=2$.", "$(50-2)^2$"),
          step("Expand", "$2500-200+4$.", "$2304$")]),
        (57, "Smallest number to multiply by $9408$ to get a perfect square.", "$3$",
         [step("Factor", "$9408=2^6\\times 3\\times 7^2$.", "Unpaired factor: $3$"),
          step("Answer", "Multiply by $3$.", "$3$")]),
        (58, "Find $\\sqrt{1225}$ and verify by long division.", "$35$",
         [step("Factor", "$1225=5^2\\times 7^2$.", "$5\\times 7=35$"),
          step("Long div.", "Groups $\\overline{12}|\\overline{25}$ → $35$.", "$35$")]),
    ]
    for gn, qu, ans, st in ch3:
        qs.append(mk_q(B, gn, 3, qu, ans, st, local_label=f"Ch3-Q{gn-40}"))

    ch4 = [
        (59, "Find $12^3$ using $(a+b)^3=a^3+3a^2b+3ab^2+b^3$.", "$1728$",
         [step("Split", "$12=10+2$.", "Plug into identity"),
          step("Calculate", "$1000+600+120+8$.", "$1728$")]),
        (60, "Find $\\sqrt[3]{17576}$ by prime factorisation.", "$26$",
         [step("Factor", "$17576=2^3\\times 13^3$.", "Groups of three"),
          step("Root", "$2\\times 13=26$.", "$26$")]),
        (61, "Smallest number to divide $8788$ so quotient is a perfect cube.", "$4$",
         [step("Factor", "$8788=2^2\\times 13^3$.", "Unpaired $2$s"),
          step("Divide", "Remove $2^2$.", "$4$")]),
        (62, "Find $\\sqrt[3]{0.000216}$.", "$0.06$",
         [step("Fraction", "$\\dfrac{216}{10^6}$.", "$\\sqrt[3]{216}=6$"),
          step("Result", "$\\dfrac{6}{100}=0.06$.", "$0.06$")]),
        (63, "Cube of a number is $17576$. Find the number.", "$26$",
         [step("Same as Q60", "$\\sqrt[3]{17576}$.", "$26$")]),
        (64, "Find $\\sqrt[3]{13824}$ by estimation.", "$24$",
         [step("Ones", "Ends in $4$ → ones digit $4$.", "$4^3$ ends in $4$"),
          step("Tens", "Group $13|824$ → tens digit $2$.", "$24$")]),
        (65, "Smallest cube divisible by $6$, $9$, and $15$.", "$27000$",
         [step("LCM", "LCM$(6,9,15)=90$.", "Factor $90=2\\times 3^2\\times 5$"),
          step("Cube", "Need triplets: multiply by $2^2\\times 3\\times 5^2$.", "$27000$")]),
        (66, "Evaluate $\\sqrt[3]{0.000729}$.", "$0.09$",
         [step("Fraction", "$\\dfrac{729}{10^6}$.", "$9/100$")]),
        (67, "Two consecutive numbers whose cubes sum to $1729$.", "$9$ and $10$",
         [step("Cubes", "$9^3=729$, $10^3=1000$.", "$729+1000=1729$")]),
        (68, "Find $\\sqrt[3]{32768}$.", "$32$",
         [step("Estimate", "Ones digit $2$; tens from group $32$.", "$32$")]),
        (69, "Which are perfect cubes? $216$, $1000$, $1728$, $1331$.", "All four",
         [step("Check", "$6^3=216$, $10^3=1000$, $12^3=1728$, $11^3=1331$.", "All perfect cubes")]),
        (70, "Smallest multiplier for $8788$ to become a perfect cube.", "$2$",
         [step("Factor", "$8788=2^2\\times 13^3$.", "Need one more $2$")]),
        (71, "Find $\\sqrt[3]{0.000000008}$.", "$0.002$",
         [step("Fraction", "$\\dfrac{8}{10^9}$.", "$2/1000$")]),
        (72, "Volume of cube is $17576\\,\\text{cm}^3$. Find side.", "$26\\,\\text{cm}$",
         [step("Side", "$\\sqrt[3]{17576}=26$.", "$26\\,\\text{cm}$")]),
        (73, "Find $\\sqrt[3]{0.001331}$.", "$1.1$",
         [step("Fraction", "$\\dfrac{1331}{1000}$.", "$11/10$")]),
    ]
    for gn, qu, ans, st in ch4:
        qs.append(mk_q(B, gn, 4, qu, ans, st, local_label=f"Ch4-Q{gn-58}"))

    ch5 = [
        (74, "Find digit $a$ if $67a3$ is divisible by $9$.", "$a=2$",
         [step("Sum", "$6+7+a+3=16+a$.", "Must be multiple of $9$"),
          step("Solve", "$16+a=18$.", "$a=2$")]),
        (75, "4-digit number starting with $5$, divisible by $11$, odd−even digit sums equal.", "e.g. $5005$",
         [step("Form", "$5xyz$.", "$(5+y)-(x+z)=0$"),
          step("Example", "$x=0,z=5,y=0$ → $5005$.", "$5005$")]),
        (76, "Missing digit in $5\\_3$ for divisibility by $11$.", "$8$",
         [step("Odds", "$5+3=8$.", "Evens: $x$"),
          step("Solve", "$8-x=0$.", "$x=8$")]),
        (77, "If $3A+4B=5C$ (digits), find one solution.", "$A=2,B=1,C=2$",
         [step("Test", "$3(2)+4(1)=10$.", "$5C=10$, $C=2$")]),
        (78, "Smallest 4-digit number divisible by $2,3,4,5,6$.", "$1020$",
         [step("LCM", "LCM$=60$.", "$60\\times 17=1020$")]),
        (79, "Smallest 3-digit number: remainder $3$ mod $7$, remainder $2$ mod $5$.", "$122$",
         [step("List", "$7k+3$: $17,52,87,122,\\ldots$", "Check mod $5$"),
          step("Answer", "$122$.", "$122$")]),
        (80, "Test divisibility of $1729$ by $7$, $11$, $13$.", "Div by $7$ and $13$; not by $11$",
         [step("$7$", "$1729\\div 7=247$.", "Yes"),
          step("$11$", "$16-3=13$.", "No"),
          step("$13$", "$1729\\div 13=133$.", "Yes")]),
        (81, "Find $x$ if $2x3$ is divisible by $9$.", "$x=4$",
         [step("Sum", "$5+x=9$.", "$x=4$")]),
        (82, "3-digit number divisible by $11$ with digit sum $12$. Find all.", "$165,264,363,462,561,660$",
         [step("Middle", "$y=6$.", "$x+z=6$"),
          step("List", "Pairs summing to $6$.", "Six numbers")]),
        (83, "Remainder when $987654321$ is divided by $9$.", "$0$",
         [step("Sum digits", "$45$.", "Divisible by $9$")]),
        (84, "If divisible by $3$ and $5$, must be divisible by ___?", "$15$",
         [step("Concept", "Product of coprime divisors.", "$15$")]),
        (85, "Smallest number leaving remainder $1$ when divided by $2,3,4,5,6$.", "$61$",
         [step("LCM", "LCM$=60$.", "$60+1=61$")]),
        (86, "Is $1729$ a Hardy–Ramanujan number (two cube sums)?", "Yes",
         [step("Way 1", "$12^3+1^3=1729$.", ""),
          step("Way 2", "$10^3+9^3=1729$.", "Yes")]),
        (87, "Missing digit in $4\\_28$ for divisibility by $11$.", "$9$",
         [step("Diff", "$(x+8)-6=x+2$.", "$x+2=11$, $x=9$")]),
        (88, "2-digit number equals $4\\times$ sum of its digits. Find all.", "$12,24,36,48$",
         [step("Equation", "$10x+y=4(x+y)$.", "$2x=y$"),
          step("List", "$x=1\\ldots 4$.", "Four answers")]),
    ]
    for gn, qu, ans, st in ch5:
        qs.append(mk_q(B, gn, 5, qu, ans, st, local_label=f"Ch5-Q{gn-73}"))

    ch6 = [
        (89, "$A=\\{1,2,3,4,5\\}$, $B=\\{3,4,5,6,7\\}$. Find $A\\cup B$ and $A\\cap B$.", "$A\\cup B=\\{1,2,3,4,5,6,7\\}$, $A\\cap B=\\{3,4,5\\}$",
         [step("Union", "All elements without repeat.", "$\\{1,2,3,4,5,6,7\\}$"),
          step("Intersection", "Common elements.", "$\\{3,4,5\\}$")]),
        (90, "Set of all even prime numbers.", "$\\{2\\}$",
         [step("Primes", "Only $2$ is even and prime.", "$\\{2\\}$")]),
        (91, "$n(A)=15$, $n(B)=12$, $n(A\\cap B)=7$. Find $n(A\\cup B)$.", "$20$",
         [step("Formula", "$n(A\\cup B)=n(A)+n(B)-n(A\\cap B)$.", "$15+12-7=20$")]),
        (92, "Roster form: (i) natural numbers $<10$ (ii) primes between $10$ and $20$.", "(i) $\\{1,\\ldots,9\\}$ (ii) $\\{11,13,17,19\\}$",
         [step("(i)", "Natural numbers from $1$.", "$\\{1,2,3,4,5,6,7,8,9\\}$"),
          step("(ii)", "Primes in range.", "$\\{11,13,17,19\\}$")]),
        (93, "$A=\\{x:x\\text{ multiple of }3\\}$, $B=\\{x:x\\text{ multiple of }4\\}$. Find $A\\cap B$.", "Multiples of $12$",
         [step("Overlap", "LCM of $3$ and $4$.", "$\\{12,24,36,\\ldots\\}$")]),
        (94, "Venn diagram for $A\\cup B$ when $A$, $B$ are disjoint.", "Two separate circles, both shaded",
         [step("Disjoint", "No common elements.", "Shade both circles for union")]),
        (95, "$U=\\{1,\\ldots,10\\}$, $A=\\{1,3,5,7,9\\}$. Find $A'$.", "$\\{2,4,6,8,10\\}$",
         [step("Complement", "Evens in universe.", "$\\{2,4,6,8,10\\}$")]),
        (96, "Cardinal number of distinct letters in MATHEMATICS.", "$8$",
         [step("Unique", "$\\{M,A,T,H,E,I,C,S\\}$.", "$8$")]),
        (97, "$n(A\\cup B)=35$, $n(A)=20$, $n(B)=18$. Find $n(A\\cap B)$.", "$3$",
         [step("Formula", "$35=20+18-x$.", "$x=3$")]),
        (98, "Set-builder form of $\\{2,4,6,8,10\\}$.", "$\\{x\\mid x\\text{ even natural}, x\\le 10\\}$",
         [step("Rule", "Even naturals up to $10$.", "Set-builder notation")]),
        (99, "$A=\\{2,4,6,8\\}$, $B=\\{1,2,3,4,5\\}$. Find $A-B$ and $B-A$.", "$A-B=\\{6,8\\}$, $B-A=\\{1,3,5\\}$",
         [step("$A-B$", "Remove overlap from $A$.", "$\\{6,8\\}$"),
          step("$B-A$", "Remove overlap from $B$.", "$\\{1,3,5\\}$")]),
        (100, "Prove $A\\cup A=A$ and $A\\cap A=A$.", "Both identities hold",
         [step("Union", "Combining $A$ with itself gives $A$.", "$A\\cup A=A$"),
          step("Intersection", "Overlap of $A$ with itself is $A$.", "$A\\cap A=A$")]),
    ]
    for gn, qu, ans, st in ch6:
        qs.append(mk_q(B, gn, 6, qu, ans, st, local_label=f"Ch6-Q{gn-88}"))

    return qs


def batch_03():
    B = 3
    qs = []
    N7 = "CH07-sec-percentage"
    N7PL = "CH07-sec-profit-and-loss"
    N7D = "CH07-sec-discount"
    N8SI = "CH08-sec-simple-interest"
    N8CI = "CH08-sec-deducing-a-formula-for-compound-interest"
    N6O = "CH06-sec-overlapping-intersecting-sets"
    N6C = "CH06-sec-complement-of-a-set"

    ch6 = [
        (101, "$U=\\{1,\\ldots,20\\}$, $A=$ multiples of $3$, $B=$ multiples of $5$. Find $n(A\\cup B)$.", "$9$",
         [step("Build sets", "$A=\\{3,6,9,12,15,18\\}$, $B=\\{5,10,15,20\\}$.", "Within universe"),
          step("Union", "$A\\cup B=\\{3,5,6,9,10,12,15,18,20\\}$.", "No duplicates"),
          step("Count", "$n(A\\cup B)=9$.", "$9$")], N6O),
        (102, "Roster form of $\\{x\\mid x^2=9,\\,x\\in\\mathbb{N}\\}$.", "$\\{3\\}$",
         [step("Solve", "$x^2=9$ gives $x=\\pm 3$.", "Square roots"),
          step("Natural", "$-3\\notin\\mathbb{N}$.", "$\\{3\\}$")], N6O),
        (103, "$n(A)=25$, $n(B)=30$, $n(A\\cap B)=10$. Find $n(A'\\cap B')$.", "$n(U)-45$ (needs $n(U)$)",
         [step("$n(A\\cup B)$", "$25+30-10=45$.", "Standard formula"),
          step("De Morgan", "$(A\\cup B)'=A'\\cap B'$.", "Outside both circles"),
          step("Trap", "Need $n(U)$ for exact count.", "$n(U)-45$")], N6C),
    ]
    for gn, qu, ans, st, nid in ch6:
        qs.append(mk_q(B, gn, 6, qu, ans, st, local_label=f"Ch6-Q{gn-88}", linked_note_id=nid))

    ch7_pct = [
        (104, "Convert $\\dfrac{3}{8}$ into percentage.", "$37.5\\%$",
         [step("Formula", "$\\dfrac{3}{8}\\times 100$.", "$300/8$"),
          step("Answer", "$37.5\\%$.", "$37.5\\%$")]),
        (105, "What percent of $80$ is $24$?", "$30\\%$",
         [step("Fraction", "$24/80$.", "Part over whole"),
          step("Percent", "$\\dfrac{24}{80}\\times 100=30\\%$.", "$30\\%$")]),
        (106, "Find $35\\%$ of $400$.", "$140$",
         [step("Translate", "$\\dfrac{35}{100}\\times 400$.", "'Of' means multiply"),
          step("Calculate", "Zeros cancel → $35\\times 4$.", "$140$")]),
        (107, "If $25\\%$ of a number is $75$, find the number.", "$300$",
         [step("Equation", "$\\dfrac{25}{100}x=75$.", "$x/4=75$"),
          step("Solve", "$x=75\\times 4$.", "$300$")]),
        (108, "A number increased by $20\\%$ becomes $360$. Find original.", "$300$",
         [step("Percent", "New = $120\\%$ of original.", "$1.2x=360$"),
          step("Solve", "$x=360/1.2$.", "$300$")]),
        (109, "Express $0.075$ as a percentage.", "$7.5\\%$",
         [step("Rule", "Multiply decimal by $100$.", "$0.075\\times 100=7.5\\%$")]),
        (110, "Price rises from ₹$250$ to ₹$300$. Find percentage increase.", "$20\\%$",
         [step("Difference", "$300-250=50$.", "Over original"),
          step("Percent", "$\\dfrac{50}{250}\\times 100=20\\%$.", "$20\\%$")]),
        (111, "Class of $50$ students: $60\\%$ girls. How many boys?", "$20$",
         [step("Boys %", "$100-60=40\\%$.", "Rest of class"),
          step("Calculate", "$\\dfrac{40}{100}\\times 50$.", "$20$ boys")]),
        (112, "$15\\%$ discount on article marked ₹$800$. Selling price?", "₹$680$",
         [step("Pay", "$100-15=85\\%$ of marked price.", "$\\dfrac{85}{100}\\times 800$"),
          step("SP", "$85\\times 8$.", "₹$680$")]),
        (113, "If $40\\%$ of a number is $240$, find $75\\%$ of it.", "$450$",
         [step("Find number", "$x=240\\times 100/40=600$.", "Original"),
          step("$75\\%$", "$\\dfrac{75}{100}\\times 600$.", "$450$")]),
        (114, "Convert $125\\%$ to fraction in lowest terms.", "$\\dfrac{5}{4}$",
         [step("Over 100", "$125/100$.", "Divide by $25$"),
          step("Answer", "$5/4$.", "$\\dfrac{5}{4}$")]),
        (115, "Score $45$ out of $60$. Percentage?", "$75\\%$",
         [step("Fraction", "$45/60=3/4$.", "$\\times 100$"),
          step("Answer", "$75\\%$.", "$75\\%$")]),
        (116, "$12.5\\%$ of a number is $75$. Find the number.", "$600$",
         [step("Equation", "$\\dfrac{12.5}{100}x=75$.", "$12.5x=7500$"),
          step("Solve", "$x=7500/12.5$.", "$600$")]),
        (117, "Population $54000$ increases $8\\%$ per year. Population after $2$ years?", "$62986$ (approx.)",
         [step("Year 1", "$54000\\times 1.08=58320$.", "Compound growth"),
          step("Year 2", "$58320\\times 1.08=62985.6$.", "Round → $62986$")]),
        (118, "What percent is $\\dfrac{3}{5}$ of $\\dfrac{4}{7}$?", "$105\\%$",
         [step("Ratio", "$\\dfrac{3/5}{4/7}\\times 100$.", "Flip and multiply"),
          step("Simplify", "$\\dfrac{21}{20}\\times 100$.", "$105\\%$")]),
        (119, "Number decreased $25\\%$ becomes $225$. Find original.", "$300$",
         [step("Left", "$75\\%$ of original.", "$\\dfrac{3}{4}x=225$"),
          step("Solve", "$x=225\\times\\dfrac{4}{3}$.", "$300$")]),
        (120, "Find $120\\%$ of $250$.", "$300$",
         [step("Calculate", "$\\dfrac{120}{100}\\times 250$.", "$1.2\\times 250=300$")]),
        (121, "If $30\\%$ of $x=45\\%$ of $y$, find ratio $x:y$.", "$3:2$",
         [step("Equation", "$30x=45y$.", "Clear denominators"),
          step("Ratio", "$x/y=45/30=3/2$.", "$3:2$")]),
    ]
    for gn, qu, ans, st in ch7_pct:
        qs.append(mk_q(B, gn, 7, qu, ans, st, local_label=f"Ch7-Q{gn-103}", linked_note_id=N7))

    ch7_pl = [
        (122, "Buy ₹$800$, sell ₹$960$. Profit percent?", "$20\\%$",
         [step("Profit", "$960-800=160$.", "SP − CP"),
          step("Percent", "$\\dfrac{160}{800}\\times 100$.", "$20\\%$ on CP")], N7PL),
        (123, "Sell watch ₹$720$ at $10\\%$ loss. Find CP.", "₹$800$",
         [step("SP", "$90\\%$ of CP $=720$.", "Loss $10\\%$"),
          step("CP", "$720\\times 100/90$.", "₹$800$")], N7PL),
        (124, "CP ₹$450$, profit $20\\%$. Find SP.", "₹$540$",
         [step("SP", "$120\\%$ of CP.", "$1.2\\times 450=540$")], N7PL),
        (125, "$10\\%$ discount, $20\\%$ profit. CP ₹$500$. Marked price?", "₹$666.67$",
         [step("SP", "$1.2\\times 500=600$.", "$20\\%$ profit"),
          step("MP", "$600$ is $90\\%$ of MP.", "$600/0.9=666.67$")], N7D),
        (126, "Buy ₹$1200$, sell at $15\\%$ loss. SP?", "₹$1020$",
         [step("SP", "$85\\%$ of CP.", "$0.85\\times 1200=1020$")], N7PL),
        (127, "Mark $25\\%$ above CP, $10\\%$ discount. Profit %?", "$12.5\\%$",
         [step("Assume CP", "CP $=100$, MP $=125$.", "Easy numbers"),
          step("SP", "$125-12.5=112.5$.", "Profit $12.5$ on $100$")], N7D),
        (128, "SP ₹$720$ after $10\\%$ discount. Marked price?", "₹$800$",
         [step("Relation", "$720=90\\%$ of MP.", "$720/0.9$"),
          step("MP", "₹$800$.", "₹$800$")], N7D),
        (129, "Buy $12$ for ₹$240$, sell at ₹$25$ each. Profit %?", "$25\\%$",
         [step("Per item", "CP $=20$, SP $=25$.", "Profit $5$"),
          step("Percent", "$5/20\\times 100$.", "$25\\%$")], N7PL),
        (130, "CP ₹$600$, SP ₹$540$. Loss %?", "$10\\%$",
         [step("Loss", "$60$.", "$60/600\\times 100=10\\%$")], N7PL),
        (131, "$15\\%$ gain, SP ₹$920$. Find CP.", "₹$800$",
         [step("Equation", "$1.15\\times\\text{CP}=920$.", "$920/1.15$"),
          step("CP", "₹$800$.", "₹$800$")], N7PL),
        (132, "MP ₹$800$, $10\\%$ discount, $20\\%$ profit. CP?", "₹$600$",
         [step("SP", "$0.9\\times 800=720$.", "After discount"),
          step("CP", "$720/1.2$.", "₹$600$")], N7D),
        (133, "Two articles sold ₹$1200$ each: $20\\%$ gain and $20\\%$ loss. Overall result?", "$4\\%$ loss",
         [step("CPs", "CP$_1=1000$, CP$_2=1500$.", "Same SP trick"),
          step("Overall", "Cost $2500$, sold $2400$.", "$100/2500=4\\%$ loss")], N7PL),
        (134, "MP ₹$500$, SP ₹$425$. Discount %?", "$15\\%$",
         [step("Discount", "$75$.", "On MP"),
          step("Percent", "$75/500\\times 100$.", "$15\\%$")], N7D),
        (135, "Buy $10\\%$ below MP, sell $10\\%$ above MP. Profit %?", "$22.22\\%$",
         [step("Let MP", "MP $=100$, CP $=90$, SP $=110$.", "Easy numbers"),
          step("Profit", "$20/90\\times 100$.", "$22.22\\%$")], N7PL),
        (136, "CP of $10$ articles = SP of $9$ articles. Profit %?", "$11.11\\%$",
         [step("Let CP", "CP per article $=10$.", "10 CP = 9 SP"),
          step("Percent", "SP $=100/9$, profit $=10/9$.", "$11.11\\%$")], N7PL),
        (137, "$8\\%$ discount, $15\\%$ profit. CP ₹$850$. MP?", "₹$1062.5$",
         [step("SP", "$1.15\\times 850=977.5$.", "Profit first"),
          step("MP", "$977.5/0.92$.", "₹$1062.5$")], N7D),
        (138, "CP ₹$750$, loss $12\\%$. SP?", "₹$660$",
         [step("SP", "$88\\%$ of CP.", "$0.88\\times 750=660$")], N7PL),
        (139, "MP ₹$1200$, discount $15\\%$, profit $20\\%$. CP?", "₹$850$",
         [step("SP", "$0.85\\times 1200=1020$.", "Discount"),
          step("CP", "$1020/1.2$.", "₹$850$")], N7D),
    ]
    for gn, qu, ans, st, nid in ch7_pl:
        qs.append(mk_q(B, gn, 7, qu, ans, st, local_label=f"Ch8-Q{gn-121}", linked_note_id=nid))

    ch8_int = [
        (140, "Simple interest on ₹$5000$ for $3$ years at $8\\%$ p.a.", "₹$1200$",
         [step("Formula", "$\\text{SI}=PRT/100$.", "$(5000\\times 8\\times 3)/100$"),
          step("SI", "$50\\times 24$.", "₹$1200$")], N8SI),
        (141, "Amount and CI on ₹$8000$ for $2$ years at $10\\%$ compounded annually.", "Amount ₹$9680$, CI ₹$1680$",
         [step("Year 1", "$8000+800=8800$.", "$10\\%$ on principal"),
          step("Year 2", "$8800+880=9680$.", "Interest on new amount"),
          step("CI", "$9680-8000$.", "₹$1680$")], N8CI),
        (142, "Amounts to ₹$9800$ after $5$ years and ₹$12005$ after $8$ years at SI. Rate?", "$12\\%$",
         [step("3-year SI", "$12005-9800=2205$.", "Equal yearly interest"),
          step("Yearly", "$2205/3=735$.", "Find principal"),
          step("Rate", "P $=6125$.", "$735/6125\\times 100=12\\%$")], N8SI),
        (143, "Principal if SI for $4$ years at $6.25\\%$ is ₹$2500$.", "₹$10000$",
         [step("Formula", "$2500=(P\\times 6.25\\times 4)/100$.", "$25P/100$"),
          step("P", "$(2500\\times 100)/25$.", "₹$10000$")], N8SI),
        (144, "CI on ₹$16000$ for $9$ months at $20\\%$ p.a. compounded quarterly.", "₹$2522$",
         [step("Quarters", "$n=3$, rate $5\\%$ per quarter.", "$A=P(1.05)^3$"),
          step("Amount", "$16000\\times 1.157625$.", "CI $=18522-16000$")], N8CI),
        (145, "Difference CI−SI for $2$ years at $5\\%$ is ₹$15$. Find sum.", "₹$6000$",
         [step("Shortcut", "$15=P(0.05)^2$.", "2-year difference"),
          step("P", "$15/0.0025$.", "₹$6000$")], N8CI),
        (146, "Time for ₹$5000$ to amount to ₹$6655$ at $10\\%$ CI p.a.", "$3$ years",
         [step("Equation", "$6655=5000(1.1)^n$.", "$1.331=(1.1)^n$"),
          step("Power", "$1.1^3=1.331$.", "$3$ years")], N8CI),
        (147, "Sum becomes $4$ times in $4$ years at CI. Rate?", "$41.4\\%$ (approx.)",
         [step("Formula", "$4P=P(1+R/100)^4$.", "$4=(1+R/100)^4$"),
          step("Root", "$\\sqrt[4]{4}=\\sqrt{2}\\approx 1.414$.", "$R\\approx 41.4\\%$")], N8CI),
        (148, "SI on ₹$25000$ for $146$ days at $6\\%$ p.a.", "₹$600$",
         [step("Time", "$T=146/365=2/5$ year.", "Convert days"),
          step("SI", "$(25000\\times 6\\times 2/5)/100$.", "₹$600$")], N8SI),
        (149, "Amount and CI on ₹$12500$ for $9$ months at $8\\%$ compounded quarterly.", "Amount ₹$13265.1$, CI ₹$765.1$",
         [step("Quarters", "$n=3$, rate $2\\%$.", "$A=12500(1.02)^3$"),
          step("CI", "$13265.1-12500$.", "₹$765.1$")], N8CI),
        (150, "SI on sum for $2$ years at $4\\%$ is ₹$320$. Find CI same period.", "₹$326.4$",
         [step("Principal", "$P=4000$.", "From SI formula"),
          step("CI", "Year 1: $160$; Year 2: $166.4$.", "$326.4$ total")], N8CI),
    ]
    for gn, qu, ans, st, nid in ch8_int:
        qs.append(mk_q(B, gn, 8, qu, ans, st, local_label=f"Ch9-Q{gn-139}", linked_note_id=nid))

    return qs


def batch_04():
    B = 4
    qs = []
    N8SI = "CH08-sec-simple-interest"
    N8CI = "CH08-sec-deducing-a-formula-for-compound-interest"
    N9D = "CH09-sec-direct-variation"
    N9I = "CH09-sec-inverse-variation"
    N10 = "CH10-sec-fundamental-concepts"
    N10D = "CH10-sec-distributive-law"
    N10I = "CH10-sec-a-2-2ab-b-2"

    ch8 = [
        (151, "Find principal if CI for $2$ years at $10\\%$ is ₹$420$.", "₹$2000$",
         [step("2-year CI", "$121\\%-100\\%=21\\%$ of principal.", "CI rate block"),
          step("Equation", "$0.21P=420$.", "Solve"),
          step("P", "$420/0.21$.", "₹$2000$")], N8CI),
        (152, "Amount ₹$1331$ in $3$ years at $10\\%$ CI. Find principal.", "₹$1000$",
         [step("Formula", "$1331=P(1.1)^3$.", "Plug values"),
          step("Power", "$(1.1)^3=1.331$.", "$P=1331/1.331$"),
          step("P", "₹$1000$.", "₹$1000$")], N8CI),
        (153, "₹$8000$ amounts to ₹$9261$ in $3$ years at CI. Rate?", "$5\\%$",
         [step("Ratio", "$9261/8000=(21/20)^3$.", "Cube root both sides"),
          step("Rate", "$21/20=1+R/100$.", "$R=5\\%$")], N8CI),
        (154, "CI−SI on ₹$8000$ for $3$ years is ₹$61$. Find rate.", "$5\\%$",
         [step("3-yr diff", "$61=8000\\times r^2(3+r)$.", "Test clean rates"),
          step("Test $5\\%$", "$r=0.05$ gives $61$.", "$5\\%$")], N8CI),
        (155, "Time to double money at $10\\%$ CI p.a.", "$\\approx 7.27$ years (between $7$ and $8$)",
         [step("Equation", "$2P=P(1.1)^n$.", "$2=(1.1)^n$"),
          step("Check", "$(1.1)^7\\approx 1.948$, $(1.1)^8\\approx 2.143$.", "$\\approx 7.27$ yr")], N8CI),
        (156, "SI on ₹$18000$ for $2$ yr $4$ mo at $7.5\\%$ p.a.", "₹$3150$",
         [step("Time", "$T=2+4/12=7/3$ years.", "Convert months"),
          step("SI", "$\\dfrac{18000\\times 7.5\\times 7/3}{100}$.", "$60\\times 7.5\\times 7$"),
          step("Answer", "₹$3150$.", "₹$3150$")], N8SI),
        (157, "Amount ₹$4410$ in $2$ yr, ₹$4851$ in $3$ yr at CI. Rate?", "$10\\%$",
         [step("1-yr interest", "$4851-4410=441$.", "On ₹$4410$"),
          step("Rate", "$441/4410\\times 100$.", "$10\\%$")], N8CI),
        (158, "CI on ₹$10000$ for $1\\dfrac{1}{2}$ yr at $8\\%$ compounded half-yearly.", "₹$1248.64$",
         [step("Setup", "$n=3$, quarterly rate $4\\%$.", "$A=10000(1.04)^3$"),
          step("CI", "$11248.64-10000$.", "₹$1248.64$")], N8CI),
        (159, "SI ₹$720$ for $3$ yr at $8\\%$. Find CI same sum, period, rate.", "₹$779.136$",
         [step("Principal", "$P=3000$.", "From SI formula"),
          step("CI years", "$240+259.20+279.936$.", "₹$779.136$")], N8CI),
    ]
    for gn, qu, ans, st, nid in ch8:
        qs.append(mk_q(B, gn, 8, qu, ans, st, local_label=f"Ch9-Q{gn-139}", linked_note_id=nid))

    ch9 = [
        (160, "$x\\propto y$, $x=12$ when $y=4$. Find $x$ when $y=15$.", "$45$",
         [step("Constant", "$x/y=12/4=3$.", "Direct variation"),
          step("Solve", "$x=15\\times 3$.", "$45$")], N9D),
        (161, "$15$ workers build wall in $48$ hr. Workers for $30$ hr?", "$24$",
         [step("Inverse", "$15\\times 48=x\\times 30$.", "Worker-hours fixed"),
          step("Solve", "$x=720/30$.", "$24$ workers")], N9I),
        (162, "$5$ kg potatoes cost ₹$75$. Cost of $12$ kg?", "₹$180$",
         [step("Per kg", "₹$15$/kg$.", "Direct"),
          step("Cost", "$15\\times 12$.", "₹$180$")], N9D),
        (163, "$y$ varies inversely as $x$; $y=8$ when $x=6$. Find $y$ when $x=4$.", "$12$",
         [step("Constant", "$xy=48$.", "Inverse"),
          step("Solve", "$y=48/4$.", "$12$")], N9I),
        (164, "Car travels $360$ km in $5$ hr. Distance in $7$ hr?", "$504$ km",
         [step("Speed", "$72$ km/h.", "Direct"),
          step("Distance", "$72\\times 7$.", "$504$ km")], N9D),
        (165, "$10$ pipes fill tank in $24$ min. Time for $15$ pipes?", "$16$ min",
         [step("Work", "$10\\times 24=240$ pipe-min.", "Inverse"),
          step("Time", "$240/15$.", "$16$ min")], N9I),
        (166, "$x\\propto y^2$; $x=12$ when $y=2$. Find $x$ when $y=5$.", "$75$",
         [step("Constant", "$12=k\\times 4$, $k=3$.", "$x=3y^2$"),
          step("Solve", "$3\\times 25$.", "$75$")], N9D),
        (167, "$8$ men finish work in $12$ days. Days for $6$ men?", "$16$",
         [step("Man-days", "$96$.", "Inverse"),
          step("Days", "$96/6$.", "$16$ days")], N9I),
        (168, "Same speed: $240$ km in $4$ hr. Time for $360$ km?", "$6$ hr",
         [step("Speed", "$60$ km/h.", "Distance/time direct"),
          step("Time", "$360/60$.", "$6$ hr")], N9D),
        (169, "$x\\propto y$; $y=15$ when $x=45$. Find $x$ when $y=25$.", "$75$",
         [step("Ratio", "$x/y=3$.", "Direct"),
          step("Solve", "$x=3\\times 25$.", "$75$")], N9D),
        (170, "$500$ men, provisions $24$ days. Reinforcement $100$ men. Days left?", "$20$",
         [step("Rations", "$12000$ man-days.", "Inverse"),
          step("Days", "$12000/600$.", "$20$ days")], N9I),
        (171, "$8$ kg rice ₹$240$. Cost of $15$ kg?", "₹$450$",
         [step("Per kg", "₹$30$.", "Direct"),
          step("Cost", "$30\\times 15$.", "₹$450$")], N9D),
        (172, "$x$ inversely as $y$; $x=30$, $y=8$. Find $x$ when $y=12$.", "$20$",
         [step("Constant", "$xy=240$.", "Inverse"),
          step("Solve", "$x=20$.", "$20$")], N9I),
        (173, "$12$ men in $15$ days. Men for $20$ days?", "$9$",
         [step("Work", "$180$ man-days.", "Inverse"),
          step("Men", "$180/20$.", "$9$")], N9I),
        (174, "Weight $\\propto$ volume: $20$ cm³ weighs $50$ g. Weight of $35$ cm³?", "$87.5$ g",
         [step("Density", "$2.5$ g/cm³.", "Direct"),
          step("Weight", "$2.5\\times 35$.", "$87.5$ g")], N9D),
    ]
    for gn, qu, ans, st, nid in ch9:
        qs.append(mk_q(B, gn, 9, qu, ans, st, local_label=f"Ch10-Q{gn-159}", linked_note_id=nid))

    ch10_alg = [
        (175, "Add: $3x^2-5xy+7y^2$ and $-2x^2+8xy-3y^2$.", "$x^2+3xy+4y^2$",
         [step("Like terms", "Combine $x^2$, $xy$, $y^2$.", "Coefficients"),
          step("Answer", "$x^2+3xy+4y^2$.", "$x^2+3xy+4y^2$")]),
        (176, "Subtract $(5a-3b+2c)$ from $(8a+4b-7c)$.", "$3a+7b-9c$",
         [step("Order", "$(8a+4b-7c)-(5a-3b+2c)$.", "Flip signs"),
          step("Combine", "Group like terms.", "$3a+7b-9c$")]),
        (177, "Multiply $(3x+4y)(2x-5y)$.", "$6x^2-7xy-20y^2$",
         [step("FOIL", "Distribute both terms.", "$6x^2-15xy+8xy-20y^2$"),
          step("Combine", "$-15xy+8xy$.", "$6x^2-7xy-20y^2$")]),
        (178, "Divide $12x^3-8x^2+6x$ by $2x$.", "$6x^2-4x+3$",
         [step("Termwise", "Divide each term by $2x$.", "Subtract exponents"),
          step("Answer", "$6x^2-4x+3$.", "$6x^2-4x+3$")]),
        (179, "Simplify $(2x+3y)^2-(2x-3y)^2$.", "$24xy$",
         [step("Expand", "Both squares.", "Subtract"),
          step("Cancel", "$x^2,y^2$ cancel.", "$24xy$")]),
        (180, "Value of $3x^2-5x+7$ when $x=-2$.", "$29$",
         [step("Substitute", "$3(4)-5(-2)+7$.", "Order of ops"),
          step("Calculate", "$12+10+7$.", "$29$")]),
        (181, "Add $4x^2y-3xy^2+7xy$, $-2x^2y+5xy^2-3xy$, $6x^2y-xy^2+2xy$.", "$8x^2y+xy^2+6xy$",
         [step("Group", "Match exponents exactly.", "Like terms"),
          step("Answer", "$8x^2y+xy^2+6xy$.", "$8x^2y+xy^2+6xy$")]),
        (182, "Multiply $(x+3)(x-3)(x^2+9)$.", "$x^4-81$",
         [step("First pair", "$(x+3)(x-3)=x^2-9$.", "Difference of squares"),
          step("Second", "$(x^2-9)(x^2+9)$.", "$x^4-81$")]),
        (183, "$a+b=7$, $ab=12$. Find $a^2+b^2$.", "$25$",
         [step("Identity", "$(a+b)^2=a^2+2ab+b^2$.", "$49=a^2+24+b^2$"),
          step("Solve", "$a^2+b^2=25$.", "$25$")]),
        (184, "Divide $6x^3+11x^2-39x-65$ by $2x-5$.", "$3x^2+13x+13$",
         [step("Long div.", "$6x^3/2x=3x^2$.", "Repeat steps"),
          step("Answer", "No remainder.", "$3x^2+13x+13$")]),
        (185, "Simplify $(3x+2y+5z)-(x-y+2z)+(2x+3y-z)$.", "$4x+6y+2z$",
         [step("Signs", "Distribute minus.", "Group"),
          step("Answer", "$4x+6y+2z$.", "$4x+6y+2z$")]),
        (186, "Product $(x+y+z)(x-y+z)$.", "$x^2+2xz+z^2-y^2$",
         [step("Group", "$((x+z)+y)((x+z)-y)$.", "A²−B²"),
          step("Expand", "$(x+z)^2-y^2$.", "$x^2+2xz+z^2-y^2$")]),
        (187, "$x=2,y=-1,z=3$. Evaluate $2x^2y-3xy^2+5xyz$.", "$-44$",
         [step("Substitute", "Plug values.", "Exponents first"),
          step("Calculate", "$-8-6-30$.", "$-44$")]),
        (188, "Subtract $3a^2-2ab+5b^2$ from $5a^2+3ab-2b^2$.", "$2a^2+5ab-7b^2$",
         [step("Order", "Second minus first.", "Flip signs"),
          step("Combine", "Like terms.", "$2a^2+5ab-7b^2$")]),
        (189, "Multiply $(2x-3y)(4x^2+6xy+9y^2)$.", "$8x^3-27y^3$",
         [step("Identity", "$(A-B)(A^2+AB+B^2)=A^3-B^3$.", "$A=2x,B=3y$"),
          step("Answer", "$8x^3-27y^3$.", "$8x^3-27y^3$")]),
        (190, "Divide $8x^3-27$ by $2x-3$.", "$4x^2+6x+9$",
         [step("Factor", "$8x^3-27=(2x-3)(4x^2+6x+9)$.", "Difference of cubes"),
          step("Quotient", "Cancel divisor.", "$4x^2+6x+9$")]),
        (191, "Coefficient of $x^2$ in $(x-3)(2x+5)(3x-1)$.", "$-5$",
         [step("First pair", "$2x^2-x-15$.", "Multiply by $(3x-1)$"),
          step("Hunt $x^2$", "$-2x^2-3x^2$.", "Coeff $-5$")]),
        (192, "$x+\\dfrac{1}{x}=5$. Find $x^2+\\dfrac{1}{x^2}$.", "$23$",
         [step("Square", "$(x+1/x)^2=25$.", "Expand"),
          step("Solve", "$x^2+2+1/x^2=25$.", "$23$")]),
        (193, "Add $(a^2+b^2+c^2)+(2ab+2bc+2ca)$ and simplify.", "$(a+b+c)^2$",
         [step("Write out", "All terms.", "Recognise identity"),
          step("Answer", "$(a+b+c)^2$.", "$(a+b+c)^2$")]),
        (194, "Simplify $3(x+y)^2-2(x-y)^2+5xy$ when $x=1,y=2$.", "$35$",
         [step("Substitute", "$3(9)-2(1)+10$.", "Evaluate"),
          step("Answer", "$27-2+10$.", "$35$")]),
    ]
    for gn, qu, ans, st in ch10_alg:
        nid = N10D if gn in (177, 182, 186, 189, 190, 191) else N10
        qs.append(mk_q(B, gn, 10, qu, ans, st, local_label=f"Ch11-Q{gn-174}", linked_note_id=nid))

    ch10_id = [
        (195, "Expand $(3x+5y)^2$ using identity.", "$9x^2+30xy+25y^2$",
         [step("Identity", "$(A+B)^2=A^2+2AB+B^2$.", "$A=3x,B=5y$"),
          step("Expand", "Square each part.", "$9x^2+30xy+25y^2$")]),
        (196, "Find $(98)^2$ using $(a+b)^2$ identity.", "$9604$",
         [step("Split", "$(90+8)^2$.", "Addition identity"),
          step("Calculate", "$8100+1440+64$.", "$9604$")]),
        (197, "Expand $(x-7)(x+7)$.", "$x^2-49$",
         [step("Identity", "$(A-B)(A+B)=A^2-B^2$.", "$x^2-49$")]),
        (198, "Find $(102)^3$ using identity.", "$1061208$",
         [step("Split", "$(100+2)^3$.", "Cube identity"),
          step("Calculate", "$1000000+60000+1200+8$.", "$1061208$")]),
        (199, "Expand $(2x+3y+4z)^2$.", "$4x^2+9y^2+16z^2+12xy+24yz+16xz$",
         [step("Identity", "$(A+B+C)^2$ formula.", "Plug $2x,3y,4z$"),
          step("Answer", "Expand all cross terms.", "Full expansion")]),
        (200, "Find $103\\times 97$ using identity.", "$9991$",
         [step("Pattern", "$(100+3)(100-3)$.", "$A^2-B^2$"),
          step("Calculate", "$10000-9$.", "$9991$")]),
    ]
    for gn, qu, ans, st in ch10_id:
        qs.append(mk_q(B, gn, 10, qu, ans, st, local_label=f"Ch12-Q{gn-194}", linked_note_id=N10I))

    return qs


def batch_05():
    B = 5
    qs = []
    N10I = "CH10-sec-a-2-2ab-b-2"
    N11 = "CH11-sec-factors-of-algebraic-expressions"
    N12E = "CH12-sec-equations"
    N12W = "CH12-sec-word-problems"
    WP = {232, 234, 236, 238, 240, 242, 244, 246, 248, 250}

    ch10_id = [
        (201, "Expand $(x+y+z)^2$.", "$x^2+y^2+z^2+2xy+2yz+2zx$",
         [step("Identity", "$(A+B+C)^2$ formula.", "$A=x,B=y,C=z$"),
          step("Answer", "Plug in terms.", "Full expansion")]),
        (202, "Find $(52)^2$ using $(a-b)^2$ identity.", "$2704$",
         [step("Split", "$(60-8)^2$.", "Subtraction identity"),
          step("Calculate", "$3600-960+64$.", "$2704$")]),
        (203, "Expand $\\left(x+\\dfrac{1}{x}\\right)^2$.", "$x^2+2+\\dfrac{1}{x^2}$",
         [step("Identity", "$(A+B)^2$ with $B=1/x$.", "Middle term cancels"),
          step("Answer", "$x^2+2+1/x^2$.", "Expanded form")]),
        (204, "Find $99^3$ using identity.", "$970299$",
         [step("Split", "$(100-1)^3$.", "Cube identity"),
          step("Calculate", "$1000000-30000+300-1$.", "$970299$")]),
        (205, "Expand $(a-b)^3$.", "$a^3-3a^2b+3ab^2-b^3$",
         [step("Formula", "$(a-b)^3$ identity.", "Standard expansion")]),
        (206, "Find $(105)^2-(95)^2$ using identity.", "$2000$",
         [step("Diff squares", "$(105+95)(105-95)$.", "$(200)(10)$"),
          step("Answer", "$2000$.", "$2000$")]),
        (207, "Expand $(2x-3y)^3$.", "$8x^3-36x^2y+54xy^2-27y^3$",
         [step("Identity", "$(A-B)^3$.", "$A=2x,B=3y$"),
          step("Expand", "Apply powers.", "Full expansion")]),
        (208, "Find $48\\times 52$ using identity.", "$2496$",
         [step("Pattern", "$(50-2)(50+2)$.", "$50^2-2^2$"),
          step("Answer", "$2500-4$.", "$2496$")]),
        (209, "Expand $(x+y)^3$.", "$x^3+3x^2y+3xy^2+y^3$",
         [step("Formula", "$(a+b)^3$ identity.", "Standard expansion")]),
        (210, "Find $(1001)^2$ using identity.", "$1002001$",
         [step("Split", "$(1000+1)^2$.", "$(A+B)^2$"),
          step("Calculate", "$1000000+2000+1$.", "$1002001$")]),
        (211, "Expand $(a+b+c)(a-b+c)$.", "$a^2+c^2-b^2+2ac$",
         [step("Group", "$((a+c)+b)((a+c)-b)$.", "Difference of squares"),
          step("Expand", "$(a+c)^2-b^2$.", "$a^2+c^2-b^2+2ac$")]),
        (212, "Find $997\\times 1003$ using identity.", "$999991$",
         [step("Pattern", "$(1000-3)(1000+3)$.", "$A^2-B^2$"),
          step("Answer", "$1000000-9$.", "$999991$")]),
    ]
    for gn, qu, ans, st in ch10_id:
        qs.append(mk_q(B, gn, 10, qu, ans, st, local_label=f"Ch12-Q{gn-194}", linked_note_id=N10I))

    ch11 = [
        (213, "Factorise $12x^2-27$.", "$3(2x-3)(2x+3)$",
         [step("GCF", "$3(4x^2-9)$.", "Pull out $3$"),
          step("Diff squares", "$(2x)^2-(3)^2$.", "$3(2x-3)(2x+3)$")]),
        (214, "Factorise $x^2+5x+6$.", "$(x+2)(x+3)$",
         [step("Split", "Numbers multiply to $6$, add to $5$.", "$2$ and $3$"),
          step("Answer", "$(x+2)(x+3)$.", "$(x+2)(x+3)$")]),
        (215, "Factorise $4x^2-9y^2$.", "$(2x-3y)(2x+3y)$",
         [step("Identify", "$(2x)^2-(3y)^2$.", "Difference of squares")]),
        (216, "Factorise $x^3-8$.", "$(x-2)(x^2+2x+4)$",
         [step("Cubes", "$x^3-2^3$.", "Difference of cubes")]),
        (217, "Factorise $2x^2+7x+6$.", "$(x+2)(2x+3)$",
         [step("Split", "$ac=12$, use $3,4$.", "$2x^2+4x+3x+6$"),
          step("Group", "$2x(x+2)+3(x+2)$.", "$(x+2)(2x+3)$")]),
        (218, "Factorise $3x^2-12x$.", "$3x(x-4)$",
         [step("GCF", "Common factor $3x$.", "$3x(x-4)$")]),
        (219, "Factorise $x^2-14x+49$.", "$(x-7)^2$",
         [step("Perfect sq.", "$-7$ and $-7$.", "$(x-7)^2$")]),
        (220, "Factorise $8x^3-27y^3$.", "$(2x-3y)(4x^2+6xy+9y^2)$",
         [step("Cubes", "$(2x)^3-(3y)^3$.", "Difference of cubes")]),
        (221, "Factorise $x^2-5x-14$.", "$(x-7)(x+2)$",
         [step("Factors", "Multiply to $-14$, add to $-5$.", "$-7$ and $2$")]),
        (222, "Factorise $5x^2-20$.", "$5(x-2)(x+2)$",
         [step("GCF", "$5(x^2-4)$.", "Then diff squares")]),
        (223, "Factorise $x^3+27$.", "$(x+3)(x^2-3x+9)$",
         [step("Sum cubes", "$x^3+3^3$.", "Standard formula")]),
        (224, "Factorise $6x^2+11x-35$.", "$(2x+7)(3x-5)$",
         [step("Split", "$ac=-210$, use $21,-10$.", "Group and factor")]),
        (225, "Factorise $9x^2-24xy+16y^2$.", "$(3x-4y)^2$",
         [step("Perfect sq.", "$(3x)^2$ and $(4y)^2$.", "Middle $-24xy$ fits")]),
        (226, "Factorise $x^2-\\dfrac{1}{x^2}$.", "$\\left(x-\\dfrac{1}{x}\\right)\\left(x+\\dfrac{1}{x}\\right)$",
         [step("Diff squares", "$A=x,B=1/x$.", "Factor form")]),
        (227, "Factorise $2x^3+16$.", "$2(x+2)(x^2-2x+4)$",
         [step("GCF", "$2(x^3+8)$.", "Sum of cubes inside")]),
        (228, "Factorise $x^2+2xy+y^2-z^2$.", "$(x+y-z)(x+y+z)$",
         [step("Group", "$(x+y)^2-z^2$.", "Difference of squares")]),
        (229, "Factorise $12x^2-7x-10$.", "$(4x-5)(3x+2)$",
         [step("Split", "$ac=-120$, use $-15,8$.", "Group and factor")]),
        (230, "Factorise $(x+y)^3-(x-y)^3$.", "$2y(3x^2+y^2)$",
         [step("Expand", "Subtract cubes.", "Cancel terms"),
          step("GCF", "$6x^2y+2y^3$.", "$2y(3x^2+y^2)$")]),
    ]
    for gn, qu, ans, st in ch11:
        qs.append(mk_q(B, gn, 11, qu, ans, st, local_label=f"Ch13-Q{gn-212}", linked_note_id=N11))

    ch12 = [
        (231, "Solve $3(2x-1)-2(3x+5)=5(x-3)$.", "$x=\\dfrac{2}{5}$",
         [step("Expand", "$6x-3-6x-10=5x-15$.", "$-13=5x-15$"),
          step("Solve", "$2=5x$.", "$x=2/5$")]),
        (232, "Sum of three consecutive even numbers is $48$. Find them.", "$14,16,18$",
         [step("Let", "$x,x+2,x+4$.", "$3x+6=48$"),
          step("Solve", "$x=14$.", "$14,16,18$")]),
        (233, "Solve $\\dfrac{2x+3}{5}-\\dfrac{x-2}{3}=\\dfrac{4}{15}$.", "$x=-15$",
         [step("LCM $15$", "Clear fractions.", "$3(2x+3)-5(x-2)=4$"),
          step("Solve", "$x+19=4$.", "$x=-15$")]),
        (234, "One number is $12$ more than another; sum is $48$.", "$18$ and $30$",
         [step("Let", "Smaller $x$, bigger $x+12$.", "$2x+12=48$"),
          step("Answer", "$x=18$.", "$18$ and $30$")]),
        (235, "Solve $5x-3(3x-7)=2(x+5)-4$.", "$x=\\dfrac{5}{2}$",
         [step("Expand", "$-4x+21=2x+6$.", "Collect terms"),
          step("Solve", "$15=6x$.", "$x=5/2$")]),
        (236, "Father is $3\\times$ son's age; in $12$ yr father is $2\\times$ son. Present ages?", "Son $12$, father $36$",
         [step("Let", "Son $x$, father $3x$.", "Future ages"),
          step("Equation", "$3x+12=2(x+12)$.", "Son $12$, father $36$")]),
        (237, "Solve $\\dfrac{x+1}{2}+\\dfrac{x+2}{3}=\\dfrac{x+3}{4}+4$.", "$x=\\dfrac{43}{7}$",
         [step("LCM $12$", "Clear fractions.", "Distribute"),
          step("Solve", "$10x+14=3x+57$.", "$x=43/7$")]),
        (238, "Divide ₹$500$ between A and B in ratio $3:2$.", "A ₹$300$, B ₹$200$",
         [step("Parts", "$3x+2x=500$.", "$x=100$"),
          step("Shares", "A $300$, B $200$.", "₹$300$, ₹$200$")]),
        (239, "Solve $4(2x-3)-3(x+2)=5(x-4)+7$.", "No solution",
         [step("Expand", "$5x-18=5x-13$.", "Subtract $5x$"),
          step("Result", "$-18=-13$ false.", "No solution")]),
        (240, "Denominator exceeds numerator by $3$; adding $2$ to both gives $4/5$.", "$\\dfrac{10}{13}$",
         [step("Fraction", "$\\dfrac{x}{x+3}$.", "After adding $2$"),
          step("Cross-multiply", "$5(x+2)=4(x+5)$.", "$x=10$ → $10/13$")]),
        (241, "Solve $2(x-3)+3(x-2)=4(x-1)-5$.", "$x=3$",
         [step("Expand", "$5x-12=4x-9$.", "Collect"),
          step("Answer", "$x=3$.", "$x=3$")]),
        (242, "Man is $4\\times$ son's age; in $16$ yr man is $2\\times$ son. Present ages?", "Son $8$, man $32$",
         [step("Let", "Son $x$, man $4x$.", "Future condition"),
          step("Solve", "$4x+16=2(x+16)$.", "Son $8$, man $32$")]),
        (243, "Solve $\\dfrac{3x-2}{4}-\\dfrac{2x+3}{5}=\\dfrac{x-1}{3}$.", "$x=46$",
         [step("LCM $60$", "Clear fractions.", "Distribute"),
          step("Solve", "$21x-66=20x-20$.", "$x=46$")]),
        (244, "Two-digit number: digit sum $9$; reversing digits adds $27$.", "$36$",
         [step("Digits", "$x+y=9$.", "Reversed equation"),
          step("Solve", "$y-x=3$, get $x=3,y=6$.", "$36$")]),
        (245, "Solve $7x-5(2x-3)=3(x+4)-8$.", "$x=\\dfrac{11}{6}$",
         [step("Expand", "$-3x+15=3x+4$.", "Collect"),
          step("Answer", "$11=6x$.", "$x=11/6$")]),
        (246, "Train $360$ km: $10$ km/h faster saves $1$ hour. Find speed.", "$50$ km/h",
         [step("Times", "$360/v-360/(v+10)=1$.", "Clear fractions"),
          step("Quadratic", "$v^2+10v-3600=0$.", "$v=50$ km/h")]),
        (247, "Solve $\\dfrac{5x+3}{4}=\\dfrac{3x-2}{5}+2$.", "$x=\\dfrac{17}{13}$",
         [step("LCM $20$", "Clear fractions.", "Distribute"),
          step("Solve", "$25x+15=12x+32$.", "$x=17/13$")]),
        (248, "Ages ratio $5:3$; after $6$ years ratio $7:5$. Present ages?", "A $15$, B $9$",
         [step("Let", "$5x$ and $3x$.", "Future ratio"),
          step("Solve", "$5(5x+6)=7(3x+6)$.", "A $15$, B $9$")]),
        (249, "Solve $2(x+3)-3(x-2)=4(x-5)+7$.", "$x=5$",
         [step("Expand", "$-x+12=4x-13$.", "Collect"),
          step("Answer", "$25=5x$.", "$x=5$")]),
        (250, "Rectangle length $3\\times$ breadth; perimeter $64$ cm.", "Breadth $8$ cm, length $24$ cm",
         [step("Let", "Breadth $x$, length $3x$.", "$2(4x)=64$"),
          step("Answer", "$x=8$.", "Breadth $8$ cm, length $24$ cm")]),
    ]
    for gn, qu, ans, st in ch12:
        nid = N12W if gn in WP else N12E
        qs.append(mk_q(B, gn, 12, qu, ans, st, local_label=f"Ch14-Q{gn-230}", linked_note_id=nid))

    return qs


def batch_06():
    B = 6
    qs = []
    N13P = "CH13-sec-n-2-times3-2n-rightarrow-3n-6-2n"
    N13Q = "CH13-sec-quadrilateral"
    N14C = "CH14-sec-steps-of-construction"
    N18D = "CH18-sec-drawing-2-d-representation-of-3-d-objects"
    N18P = "CH18-sec-polyhedron"

    ch13_poly = [
        (251, "Sum of interior angles of a hexagon.", "$720^\\circ$",
         [step("Formula", "$(n-2)\\times 180$, $n=6$.", "$(6-2)\\times 180$"),
          step("Answer", "$4\\times 180$.", "$720^\\circ$")]),
        (252, "Each interior angle of regular polygon is $135^\\circ$. Number of sides?", "$8$",
         [step("Exterior", "$180-135=45^\\circ$.", "Exterior trick"),
          step("Sides", "$360/45$.", "$8$ (octagon)")]),
        (253, "Each exterior angle of a regular octagon.", "$45^\\circ$",
         [step("Rule", "Exterior sum $360^\\circ$.", "$360/8$"),
          step("Answer", "$45^\\circ$.", "$45^\\circ$")]),
        (254, "Interior angle sum $1260^\\circ$. Number of sides?", "$9$",
         [step("Equation", "$(n-2)\\times 180=1260$.", "$n-2=7$"),
          step("Answer", "$n=9$.", "Nonagon")]),
        (255, "Quadrilateral angles in ratio $2:3:5:6$. Find all angles.", "$45^\\circ,67.5^\\circ,112.5^\\circ,135^\\circ$",
         [step("Sum", "Quadrilateral sum $360^\\circ$.", "$16x=360$"),
          step("Angles", "$x=22.5$.", "Multiply each ratio")]),
        (256, "Number of diagonals in a heptagon.", "$14$",
         [step("Formula", "$\\dfrac{n(n-3)}{2}$, $n=7$.", "$7\\times 4/2$"),
          step("Answer", "$14$.", "$14$ diagonals")]),
        (257, "Each exterior angle $24^\\circ$. Number of sides?", "$15$",
         [step("Divide", "$360/24$.", "$15$ sides")]),
        (258, "Hexagon interior angles in ratio $2:3:4:5:6:7$. Find all.", "$53.33^\\circ,80^\\circ,106.67^\\circ,133.33^\\circ,160^\\circ,186.67^\\circ$",
         [step("Sum", "Hexagon sum $720^\\circ$.", "$27x=720$"),
          step("Scale", "$x=80/3$.", "Multiply each ratio")]),
        (259, "Each interior angle of regular $15$-gon.", "$156^\\circ$",
         [step("Exterior", "$360/15=24^\\circ$.", "$180-24$"),
          step("Answer", "$156^\\circ$.", "$156^\\circ$")]),
        (260, "Polygon has $20$ diagonals. Number of sides?", "$8$",
         [step("Equation", "$\\dfrac{n(n-3)}{2}=20$.", "$n^2-3n-40=0$"),
          step("Factor", "$(n-8)(n+5)=0$.", "$n=8$")]),
        (261, "Sum of all exterior angles of any polygon.", "$360^\\circ$",
         [step("Rule", "Universal geometry fact.", "Always $360^\\circ$")]),
        (262, "Pentagon: three equal angles, other two $100^\\circ$ and $120^\\circ$.", "$106\\dfrac{2}{3}^\\circ$ each",
         [step("Sum", "Pentagon sum $540^\\circ$.", "$3x+220=540$"),
          step("Solve", "$3x=320$.", "$106.67^\\circ$ each")]),
        (263, "Regular polygon: each interior angle $144^\\circ$. Sides?", "$10$",
         [step("Exterior", "$36^\\circ$.", "$360/36$"),
          step("Answer", "Decagon.", "$10$ sides")]),
        (264, "Exterior angles ratio $1:2:3:4:5$ (regular assumed). Sides?", "$5$",
         [step("Count", "Five ratio parts → five angles.", "Pentagon"),
          step("Note", "True regular polygon needs equal angles.", "$5$ sides")]),
        (265, "Each interior angle of regular nonagon.", "$140^\\circ$",
         [step("Exterior", "$360/9=40^\\circ$.", "$180-40$"),
          step("Answer", "$140^\\circ$.", "$140^\\circ$")]),
    ]
    for gn, qu, ans, st in ch13_poly:
        qs.append(mk_q(B, gn, 13, qu, ans, st, local_label=f"Ch15-Q{gn-250}", linked_note_id=N13P))

    ch13_quad = [
        (266, "Parallelogram ABCD: $\\angle A=65^\\circ$. Find all angles.", "$65^\\circ,115^\\circ,65^\\circ,115^\\circ$",
         [step("Opposite", "$\\angle C=65^\\circ$.", "Adjacent sum $180^\\circ$"),
          step("Others", "$\\angle B=\\angle D=115^\\circ$.", "All four angles")]),
        (267, "Rhombus diagonals $16$ cm and $12$ cm. Find side.", "$10$ cm",
         [step("Half diags", "Right triangle $8$ and $6$.", "Pythagoras"),
          step("Side", "$8^2+6^2=100$.", "$10$ cm")]),
        (268, "Rectangle: length $3$ cm more than breadth; perimeter $34$ cm.", "Breadth $7$ cm, length $10$ cm",
         [step("Let", "Breadth $x$, length $x+3$.", "$2(2x+3)=34$"),
          step("Solve", "$x=7$.", "Breadth $7$, length $10$")]),
        (269, "Square diagonals $10\\sqrt{2}$ cm. Find side.", "$10$ cm",
         [step("Pythagoras", "$2s^2=(10\\sqrt{2})^2$.", "$s^2=100$"),
          step("Side", "$s=10$ cm.", "$10$ cm")]),
        (270, "Parallelogram ABCD: $AB=2x+3$, $BC=x+7$. Find $x$ (rhombus case).", "$x=4$",
         [step("Rhombus", "Adjacent sides equal.", "$2x+3=x+7$"),
          step("Solve", "$x=4$.", "$x=4$")]),
        (271, "Prove rectangle diagonals are equal and bisect each other.", "Proved via SAS congruence",
         [step("Triangles", "$\\triangle ADC\\cong\\triangle BCD$.", "SAS"),
          step("Conclude", "$AC=BD$; parallelogram diagonals bisect.", "Both properties")]),
        (272, "Rhombus: one angle $60^\\circ$. Find all angles.", "$60^\\circ,120^\\circ,60^\\circ,120^\\circ$",
         [step("Parallelogram rules", "Opposite equal.", "Adjacent supplementary")]),
        (273, "Parallelogram diagonals $8$ cm and $6$ cm. Find area (rhombus case).", "$24$ cm²",
         [step("Rhombus area", "$\\dfrac{1}{2}d_1 d_2$.", "$\\dfrac{1}{2}\\times 8\\times 6$"),
          step("Answer", "$24$ cm².", "$24$ cm²")]),
        (274, "Trapezium ABCD: $AB\\parallel DC$, $AB=8$, $DC=12$, height $5$. Area?", "$50$ cm²",
         [step("Formula", "$\\dfrac{1}{2}(8+12)\\times 5$.", "Parallel sides"),
          step("Answer", "$50$ cm².", "$50$ cm²")]),
        (275, "Prove diagonals of a rectangle are equal.", "Same proof as Q271",
         [step("SAS", "Congruent triangles.", "$AC=BD$")]),
        (276, "Kite: unequal sides $5$ cm and $7$ cm. Perimeter?", "$24$ cm",
         [step("Sides", "$5,5,7,7$.", "Two pairs adjacent"),
          step("Perimeter", "$24$ cm.", "$24$ cm")]),
        (277, "Prove rhombus diagonals bisect at right angles.", "Proved via SSS congruence",
         [step("Four triangles", "All congruent.", "Central angles equal"),
          step("Right angle", "$360/4=90^\\circ$.", "$90^\\circ$")]),
        (278, "Parallelogram: diagonals meet at $O$, $AO=3$ cm. Find $AC$.", "$6$ cm",
         [step("Bisect", "Diagonals halve each other.", "$AC=2\\times AO$"),
          step("Answer", "$6$ cm.", "$6$ cm")]),
        (279, "Rhombus diagonals $16$ cm and $12$ cm. Area?", "$96$ cm²",
         [step("Formula", "$\\dfrac{1}{2}\\times 16\\times 12$.", "$8\\times 12$"),
          step("Answer", "$96$ cm².", "$96$ cm²")]),
        (280, "Square: each angle $90^\\circ$. Prove all sides equal.", "Definition / congruent triangles",
         [step("Logic", "Square defined with equal sides.", "Or from equal diagonals at $90^\\circ$")]),
    ]
    for gn, qu, ans, st in ch13_quad:
        qs.append(mk_q(B, gn, 13, qu, ans, st, local_label=f"Ch16-Q{gn-265}", linked_note_id=N13Q))

    ch14 = [
        (281, "Construct quadrilateral ABCD: $AB=4$, $BC=3.5$, $CD=5$, $DA=4.5$, $AC=6$ cm.", "See steps",
         [step("Diagonal", "Draw $AC=6$ cm.", "Anchor line"),
          step("Arcs", "Find $B$ above, $D$ below.", "Connect sides")], N14C),
        (282, "Construct parallelogram: $AB=5$, $BC=4$, $\\angle ABC=60^\\circ$.", "See steps",
         [step("Base", "$AB=5$ cm, $60^\\circ$ at $B$.", "Mark $C$ at $4$ cm"),
          step("Complete", "Arcs for $D$.", "Join sides")], N14C),
        (283, "Construct rhombus with diagonals $6$ cm and $8$ cm.", "See steps",
         [step("Diagonal", "Draw $8$ cm horizontal.", "Perpendicular bisector"),
          step("Second", "Mark $3$ cm above/below centre.", "Connect vertices")], N14C),
        (284, "Construct rectangle: sides $5$ cm and $3.5$ cm.", "See steps",
         [step("Base", "$5$ cm with $90^\\circ$ at ends.", "Mark height $3.5$ cm"),
          step("Top", "Connect $C$ and $D$.", "Rectangle complete")], N14C),
        (285, "Construct square of side $4.5$ cm.", "See steps",
         [step("Same as rectangle", "Base $4.5$ cm.", "$90^\\circ$ verticals"),
          step("Top", "Cut at $4.5$ cm.", "Square complete")], N14C),
        (286, "Construct quadrilateral: $AB=4$, $BC=3$, $CD=5$, $DA=6$, $BD=7$ cm.", "See steps",
         [step("Diagonal", "Draw $BD=7$ cm.", "Arcs for $A$ and $C$"),
          step("Connect", "Join all vertices.", "Quadrilateral done")], N14C),
        (287, "Construct kite: sides $5$ cm and $7$ cm, diagonal $8$ cm.", "See steps",
         [step("Diagonal", "Draw $8$ cm line.", "Arcs $5$ and $7$ from ends"),
          step("Kite", "Connect intersection points.", "Kite shape")], N14C),
        (288, "Construct parallelogram: sides $4$, $3$ cm, diagonal $5$ cm.", "See steps",
         [step("Base", "$AB=4$ cm.", "Arcs $5$ from $A$, $3$ from $B$"),
          step("Complete", "Find $D$, join.", "Parallelogram")], N14C),
        (289, "Construct rhombus: side $5$ cm, diagonal $6$ cm.", "See steps",
         [step("Diagonal", "$AC=6$ cm.", "Arcs radius $5$ from $A,C$"),
          step("Connect", "Mark $B,D$.", "Rhombus")], N14C),
        (290, "Construct rectangle: perimeter $24$ cm, length $7$ cm.", "See steps",
         [step("Breadth", "$B=5$ cm.", "From perimeter"),
          step("Draw", "$7\\times 5$ rectangle.", "Construct")], N14C),
        (291, "Construct square with diagonal $6$ cm.", "See steps",
         [step("Diagonal", "$AC=6$ cm.", "Perpendicular bisector"),
          step("Vertices", "Mark $3$ cm each way.", "Square")], N14C),
        (292, "Construct quadrilateral: sides $3,4,5,6$ cm, diagonal $7$ cm.", "See steps",
         [step("Diagonal", "$AC=7$ cm.", "Arcs for $B$ and $D$"),
          step("Connect", "Sides in order.", "Quadrilateral")], N14C),
    ]
    for gn, qu, ans, st, nid in ch14:
        qs.append(mk_q(B, gn, 14, qu, ans, st, local_label=f"Ch17-Q{gn-280}", linked_note_id=nid))

    ch18 = [
        (293, "Draw net of cuboid $4\\times 3\\times 2$ cm.", "Six connected rectangles",
         [step("Layout", "Central $4\\times 3$.", "Attach $4\\times 2$ and $3\\times 2$ faces"),
          step("Lid", "One more $4\\times 3$.", "Unfolded box")], N18D),
        (294, "Isometric view of cube side $3$ cm.", "See steps",
         [step("Dots", "Vertical $3$ dots.", "Diagonals $3$ each way"),
          step("Close", "Build top face.", "3D block")], N18D),
        (295, "Front, side, top views of cylinder on base.", "Rectangle, rectangle, circle",
         [step("Front/Side", "Looks like rectangle.", "Side view same"),
          step("Top", "Circle.", "Three views")], N18D),
        (296, "Edges, vertices, faces of triangular prism?", "$9$ edges, $6$ vertices, $5$ faces",
         [step("Count", "2 triangles + 3 rectangles.", "Euler check"),
          step("Verify", "$F+V=E+2$.", "$5+6=9+2$")], N18P),
        (297, "Net of square pyramid: base $4$ cm, slant height $5$ cm.", "Square + four triangles",
         [step("Base", "$4\\times 4$ square.", "Triangles on each side"),
          step("Height", "Triangle height $5$ cm.", "Star shape")], N18D),
        (298, "Verify Euler's formula for tetrahedron.", "Verified: $4+4=6+2$",
         [step("Count", "$F=4,V=4,E=6$.", "Plug in formula"),
          step("Check", "$8=8$.", "Verified")], N18P),
        (299, "2-D representation of cuboid with hidden edges dotted.", "See steps",
         [step("Draw", "Two offset rectangles.", "Connect corners"),
          step("Hidden", "Dotted back edges.", "Solid sketch")], N18D),
        (300, "How many edges does a pentagonal prism have?", "$15$",
         [step("Count", "5 bottom + 5 top + 5 vertical.", "$5+5+5$"),
          step("Answer", "$15$ edges.", "$15$")], N18P),
    ]
    for gn, qu, ans, st, nid in ch18:
        qs.append(mk_q(B, gn, 18, qu, ans, st, local_label=f"Ch18-Q{gn-292}", linked_note_id=nid))

    return qs


def batch_07():
    B = 7
    qs = []
    N18D = "CH18-sec-drawing-2-d-representation-of-3-d-objects"
    N18P = "CH18-sec-polyhedron"
    N19A = "CH19-sec-area-and-perimeter-of-some-plane-figures"
    N19V = "CH19-sec-volume-and-capacity"
    N20D = "CH20-sec-data-handling"
    N20G = "CH20-sec-represent-the-above-data-by-a-double-bar-graph"

    def put(gn, ch, qu, ans, st, label, nid, diagram=None):
        qs.append(mk_q(B, gn, ch, qu, ans, st, local_label=label, linked_note_id=nid, diagram=diagram))

    # Ch18 wrap-up (301-304)
    put(301, 18, "Draw the net of a cone with radius $3$ cm and height $4$ cm.", "Circle + sector; slant $5$ cm",
        [step("Base", "Circle $r=3$ cm.", "Flat base"),
         step("Sector", "$3^2+4^2=25$, slant $=5$ cm.", "Pizza-slice net")], "Ch18-Q9", N18D, "cone-net")
    put(302, 18, "Vertices, edges, faces of a hexagonal pyramid?", "$7$ faces, $7$ vertices, $12$ edges",
        [step("Faces", "1 hex base + 6 triangles.", "$F=7$"),
         step("Count", "$V=7$, $E=12$.", "Euler: $7+7=12+2$")], "Ch18-Q10", N18P, "hex-pyramid")
    put(303, 18, "Isometric view of cuboid $4\\times 3\\times 2$ units.", "See diagram",
        [step("Start", "Pick dot; draw $4$ and $3$ isometric axes.", "Height $2$"),
         step("Close", "Parallel lines complete box.", "Isometric cuboid")], "Ch18-Q11", N18D, "isometric-cuboid-4x3x2")
    put(304, 18, "Verify Euler's formula for a square pyramid.", "Verified: $10=10$",
        [step("Count", "$F=5,V=5,E=8$.", "Square base + 4 triangles"),
         step("Formula", "$5+5=8+2$.", "Verified")], "Ch18-Q12", N18P, "square-pyramid")

    # Ch19 area (305-324)
    area = [
        (305, "Trapezium: parallel sides $25$ cm, $13$ cm; height $8$ cm.", "$152$ cm²", "trapezium-area"),
        (306, "Trapezium area $480$ cm²; height $15$ cm. Sum of parallel sides?", "$64$ cm", None),
        (307, "Regular hexagon side $6$ cm.", "$54\\sqrt{3}$ cm² ($\\approx 93.53$)", "regular-hexagon"),
        (308, "Parallel sides ratio $3:5$, height $12$ cm, area $480$ cm².", "$30$ cm and $50$ cm", None),
        (309, "Polygon vertices $(0,0),(4,0),(4,3),(2,5),(0,3)$. Area?", "$16$ sq units", "polygon-house-coords"),
        (310, "Trapezium parallel $20,12$ cm; non-parallel $10,8$ cm.", "$\\approx 124.8$ cm²", "trapezium-area"),
        (311, "Regular pentagon side $10$ cm.", "$172$ cm²", None),
        (312, "Trapezium area $384$ cm²; one side $16$ cm, height $12$ cm.", "Other side $48$ cm", "trapezium-area"),
        (313, "Regular octagon side $8$ cm.", "$\\approx 308.99$ cm²", "regular-hexagon"),
        (314, "Field trapezium: parallel $25$ m, $10$ m; sides $14$ m, $13$ m.", "$196$ m²", "trapezium-field"),
        (315, "Regular hexagon side $8$ cm.", "$96\\sqrt{3}$ cm² ($\\approx 166.27$)", "regular-hexagon"),
        (316, "Rhombus diagonals $16$ cm, $12$ cm.", "$96$ cm²", "rhombus-diagonals"),
        (317, "Polygon $A(1,1),B(4,1),C(6,4),D(4,7),E(1,4)$. Area?", "$19.5$ sq units", "polygon-pentagon-coords"),
        (318, "Trapezium area $300$ cm²; sides ratio $2:3$, height $10$ cm.", "$24$ cm and $36$ cm", "trapezium-area"),
        (319, "Regular decagon side $5$ cm.", "$\\approx 192.25$ cm²", None),
        (320, "Trapezium parallel $20,30$ cm; non-parallel $13,14$ cm.", "$\\approx 311.75$ cm²", "trapezium-area"),
        (321, "Regular heptagon side $7$ cm.", "$\\approx 178.07$ cm²", None),
        (322, "Rhombus area $240$ cm²; one diagonal $16$ cm.", "Other diagonal $30$ cm", "rhombus-diagonals"),
        (323, "Polygon $(0,0),(5,0),(7,3),(4,6),(1,4)$. Area?", "$27.5$ sq units", "polygon-split-coords"),
        (324, "Trapezium area $540$ cm²; ratio $4:5$, height $12$ cm.", "$40$ cm and $50$ cm", "trapezium-area"),
    ]
    area_steps = {
        305: [step("Formula", "$\\dfrac{1}{2}(25+13)\\times 8$.", "$19\\times 8=152$")],
        306: [step("Equation", "$480=\\dfrac{1}{2}S\\times 15$.", "$S=64$ cm")],
        307: [step("6 triangles", "$6\\times\\dfrac{\\sqrt{3}}{4}\\times 36$.", "$54\\sqrt{3}$ cm²")],
        308: [step("Let", "$3x,5x$.", "$480=6\\times 8x$, $x=10$")],
        309: [step("Split", "Rectangle $4\\times 3=12$.", "Roof triangle area $4$"),
               step("Total", "$12+4$.", "$16$ sq units")],
        310: [step("Triangle", "Heron's on sides $8,10,8$.", "Height $\\approx 7.8$ cm"),
               step("Area", "$\\dfrac{1}{2}\\times 32\\times 7.8$.", "$\\approx 124.8$ cm²")],
        311: [step("Formula", "$\\approx 1.72\\times 100$.", "$172$ cm²")],
        312: [step("Solve", "$384=6(16+b)$.", "$b=48$ cm")],
        313: [step("Formula", "$2(1+\\sqrt{2})\\times 64$.", "$\\approx 308.99$ cm²")],
        314: [step("Heron", "Triangle base $15$, sides $13,14$.", "Height $11.2$ m"),
               step("Area", "$\\dfrac{1}{2}\\times 35\\times 11.2$.", "$196$ m²")],
        315: [step("Hexagon", "$6\\times\\dfrac{\\sqrt{3}}{4}\\times 64$.", "$96\\sqrt{3}$ cm²")],
        316: [step("Formula", "$\\dfrac{1}{2}\\times 16\\times 12$.", "$96$ cm²")],
        317: [step("Split", "Trapezium $12$ + triangle $7.5$.", "$19.5$ sq units")],
        318: [step("Ratio", "$300=5\\times 5x$.", "$x=12$")],
        319: [step("Decagon", "$7.69\\times 25$.", "$\\approx 192.25$ cm²")],
        320: [step("Heron", "Triangle base $10$.", "Height $\\approx 12.47$ cm"),
               step("Area", "$25\\times 12.47$.", "$\\approx 311.75$ cm²")],
        321: [step("Heptagon", "$3.634\\times 49$.", "$\\approx 178.07$ cm²")],
        322: [step("Formula", "$240=8d_2$.", "$d_2=30$ cm")],
        323: [step("Strip method", "Triangles + trapeziums − excess.", "$27.5$ sq units")],
        324: [step("Ratio", "$540=6\\times 9x$.", "$x=10$")],
    }
    for gn, qu, ans, dia in area:
        put(gn, 19, qu, ans, area_steps[gn], f"Ch19-Q{gn-304}", N19A, dia)

    # Ch19 volume (325-344)
    vol = [
        (325, "Volume of cuboid $8\\times 6\\times 4$ cm.", "$192$ cm³", "cuboid-dims"),
        (326, "Cube total surface area $150$ cm². Volume?", "$125$ cm³", "cuboid-dims"),
        (327, "Cylinder $r=7$ m, $h=10$ m. Capacity in litres?", "$1{,}540{,}000$ L", "cylinder-tank"),
        (328, "Cuboid volume $3600$ cm³; $L=40$, $B=30$. Height?", "$3$ cm", "cuboid-dims"),
        (329, "Surface area of cube side $7$ cm.", "$294$ cm²", "cuboid-dims"),
        (330, "Cylinder volume $1540$ cm³, $h=10$ cm. Radius?", "$7$ cm", "cylinder-tank"),
        (331, "Cylinder $r=3.5$ cm, $h=10$ cm. Volume?", "$385$ cm³", "cylinder-tank"),
        (332, "Cuboid TSA $236$ cm²; $L=8$, $B=6$. Height and volume?", "$H=5$ cm, Vol $240$ cm³", "cuboid-dims"),
        (333, "Cylinder $r=7$ cm, $h=20$ cm full of water. Litres?", "$3.08$ L", "cylinder-tank"),
        (334, "Cube surface area $384$ cm². Volume?", "$512$ cm³", "cuboid-dims"),
        (335, "Cylinder volume $3080$ cm³, $r=7$ cm. Height?", "$20$ cm", "cylinder-tank"),
        (336, "Cuboid volume $2400$ cm³; $L:B:H=4:3:2$. Dimensions?", "$4\\sqrt[3]{100}$, $3\\sqrt[3]{100}$, $2\\sqrt[3]{100}$ cm", "cuboid-dims"),
        (337, "Curved surface area: cylinder $r=3.5$ cm, $h=20$ cm.", "$440$ cm²", "cylinder-tank"),
        (338, "Cube volume $729$ cm³. Total surface area?", "$486$ cm²", "cuboid-dims"),
        (339, "Cylinder holds $3080$ L, $r=7$ m. Height?", "$0.02$ m (2 cm)", "cylinder-tank"),
        (340, "Cuboid $L:B:H=3:2:1$, TSA $88$ cm². Volume?", "$48$ cm³", "cuboid-dims"),
        (341, "Cylinder TSA $440$ cm², $h=10$ cm. Radius and volume?", "$r\\approx 4.74$ cm, Vol $\\approx 707$ cm³", "cylinder-tank"),
        (342, "Cylinder diameter $14$ cm, height $15$ cm. Volume?", "$2310$ cm³", "cylinder-tank"),
        (343, "Cube side $6$ cm; cuboid $8\\times 6\\times h$ same volume. Find $h$.", "$4.5$ cm", "cuboid-dims"),
        (344, "Cylinder $r=3.5$ m, $h=4$ m. Capacity in kilolitres?", "$154$ kL", "cylinder-tank"),
    ]
    vol_steps = {
        325: [step("Multiply", "$8\\times 6\\times 4$.", "$192$ cm³")],
        326: [step("Face", "One face $25$ cm² → side $5$.", "Vol $125$ cm³")],
        327: [step("Volume", "$\\dfrac{22}{7}\\times 49\\times 10=1540$ m³.", "$1.54\\times 10^6$ L")],
        328: [step("Equation", "$3600=1200H$.", "$H=3$ cm")],
        329: [step("6 faces", "$6\\times 49$.", "$294$ cm²")],
        330: [step("Solve", "$1540=\\dfrac{22}{7}r^2\\times 10$.", "$r=7$ cm")],
        331: [step("Calculate", "$\\dfrac{22}{7}\\times 3.5^2\\times 10$.", "$385$ cm³")],
        332: [step("TSA", "$118=48+14H$.", "$H=5$, Vol $240$ cm³")],
        333: [step("Volume", "$3080$ cm³.", "$3.08$ L")],
        334: [step("Side", "$\\sqrt{64}=8$.", "$8^3=512$ cm³")],
        335: [step("Equation", "$3080=154h$.", "$h=20$ cm")],
        336: [step("Ratio", "$24x^3=2400$.", "$x=\\sqrt[3]{100}$")],
        337: [step("CSA", "$2\\pi rh$.", "$440$ cm²")],
        338: [step("Side 9", "TSA $6\\times 81$.", "$486$ cm²")],
        339: [step("Convert", "$3.08$ m³.", "$h=0.02$ m")],
        340: [step("TSA", "$22x^2=88$, $x=2$.", "Vol $48$ cm³")],
        341: [step("Quadratic", "Solve for $r$.", "Vol $\\approx 707$ cm³")],
        342: [step("Radius 7", "$154\\times 15$.", "$2310$ cm³")],
        343: [step("Equal vol", "$216=48h$.", "$h=4.5$ cm")],
        344: [step("Volume", "$154$ m³.", "$154$ kL")],
    }
    for gn, qu, ans, dia in vol:
        put(gn, 19, qu, ans, vol_steps[gn], f"Ch20-Q{gn-324}", N19V, dia)

    # Ch20 data (345-350)
    put(345, 20,
        "Frequency table (class width $10$): marks $45,48,45,55,58,55,55,55,60,65,68,62,68,60,65,72,75,70,78,75,70,78,80,82,85,82,85,88,90,92$.",
        "See table: 40–50:3, 50–60:5, 60–70:7, 70–80:7, 80–90:6, 90–100:2",
        [step("Buckets", "Group by tens.", "Tally frequencies"),
         step("Table", "40–50 through 90–100.", "Complete distribution")], "Ch21-Q1", N20D, "histogram-frequency")
    put(346, 20,
        "Draw a bar graph: Class 6→52, 7→48, 8→45, 9→38, 10→30 students.",
        "See bar graph",
        [step("Axes", "X: classes; Y: students.", "Scale to 60"),
         step("Bars", "Separate rectangles per class.", "See diagram")], "Ch21-Q2", N20G, "bar-graph-classes")
    put(347, 20,
        "Books read per month: 0 books→10, 1–2→15, 3–5→20, 5+→5 students. Construct pie chart.",
        "Slices: $72^\\circ,108^\\circ,144^\\circ,36^\\circ$",
        [step("Total", "$50$ students.", "$360/50=7.2^\\circ$ each"),
         step("Angles", "Multiply each group.", "Pie slices")], "Ch21-Q3", N20G, "pie-chart-books")
    put(348, 20,
        "Mean, median, mode of: $12,15,18,12,20,15,18,12,25,15$.",
        "Mean $16.2$; median $15$; modes $12$ and $15$",
        [step("Order", "Sort data.", "Mean $162/10$"),
         step("Median/Mode", "Middle values; most frequent.", "Bimodal")], "Ch21-Q4", N20D, None)
    put(349, 20,
        "Histogram: 0–10→5, 10–20→8, 20–30→12, 30–40→15, 40–50→10.",
        "See histogram (touching bars)",
        [step("Continuous", "Bars must touch.", "Height = frequency"),
         step("Draw", "Blocks on axis 0–50.", "See diagram")], "Ch21-Q5", N20G, "histogram-frequency")
    put(350, 20,
        "Pie chart: total expenditure ₹$60000$; food sector $30\\%$.",
        "₹$18000$ on food",
        [step("Percent", "$30\\%$ of $60000$.", "$0.3\\times 60000$"),
         step("Answer", "₹$18000$.", "₹$18000$")], "Ch21-Q6", N20D, "pie-chart-books")

    return qs


def batch_08():
    B = 8
    qs = []
    N20D = "CH20-sec-data-handling"
    N20G = "CH20-sec-represent-the-above-data-by-a-double-bar-graph"
    N20P = "CH20-sec-likely"
    N16C = "CH16-sec-coordinates-of-a-point"
    N16L = "CH16-sec-linear-graphs"
    N17S = "CH17-sec-line-symmetry"
    N17R = "CH17-sec-rotational-symmetry"

    def put(gn, ch, qu, ans, st, label, nid, diagram=None):
        qs.append(mk_q(B, gn, ch, qu, ans, st, local_label=label, linked_note_id=nid, diagram=diagram))

    # Ch21 data continued (351-362) → textbook Ch 20
    put(351, 20, "Probability of an even number on a fair die.", "$\\dfrac{1}{2}$",
        [step("Outcomes", "$\\{1,2,3,4,5,6\\}$.", "Even: $\\{2,4,6\\}$"),
         step("Probability", "$3/6$.", "$1/2$")], "Ch21-Q7", N20P, None)
    put(352, 20, "Study hours: $2,3,4,2,5,3,4,6,3,2$. Mean, median, mode?", "Mean $3.4$; median $3$; modes $2$ and $3$",
        [step("Sort", "$2,2,2,3,3,3,4,4,5,6$.", "Sum $34$"),
         step("Stats", "Mean $3.4$; median $3$.", "Bimodal $2,3$")], "Ch21-Q8", N20D, None)
    put(353, 20, "Double bar graph: Student A vs B in Math ($80/75$), Science ($70/85$), English ($88/82$), Hindi ($76/80$), SST ($90/85$).",
        "See double bar graph",
        [step("Axes", "Subjects on X; marks on Y.", "Two bars per subject"),
         step("Legend", "Different colours for A and B.", "See diagram")], "Ch21-Q9", N20G, "double-bar-students")
    put(354, 20, "Class of $40$: $25$ like cricket, $20$ football, $10$ both. Only cricket, only football, neither?",
        "Only cricket $15$; only football $10$; neither $5$",
        [step("Venn", "Overlap $10$ first.", "Only C $=25-10$"),
         step("Neither", "$40-35$.", "$15,10,5$")], "Ch21-Q10", N20D, "venn-two-sets")
    put(355, 20, "Frequency polygon: classes $10$–$20\\to4$, $20$–$30\\to7$, $30$–$40\\to12$, $40$–$50\\to8$, $50$–$60\\to5$.",
        "See frequency polygon",
        [step("Midpoints", "$(15,4),(25,7),(35,12),(45,8),(55,5)$.", "Plot and join"),
         step("Close", "Drop to axis at $5$ and $65$.", "Polygon")], "Ch21-Q11", N20G, "frequency-polygon")
    put(356, 20, "Mean of $5$ numbers is $18$. Excluding one, mean of rest is $16$. Excluded number?", "$26$",
        [step("Totals", "$5\\times18=90$.", "$4\\times16=64$"),
         step("Diff", "$90-64$.", "$26$")], "Ch21-Q12", N20D, None)
    put(357, 20, "Pie chart: Transport $30\\%$, Food $25\\%$, Education $20\\%$, Rent $15\\%$, Others $10\\%$.",
        "Angles: $108^\\circ,90^\\circ,72^\\circ,54^\\circ,36^\\circ$",
        [step("360°", "Multiply each $\\%$ by $360$.", "Draw slices"),
         step("Angles", "Listed above.", "See diagram")], "Ch21-Q13", N20G, "pie-expenditure")
    put(358, 20, "Probability of drawing a red card from a deck of $52$.", "$\\dfrac{1}{2}$",
        [step("Count", "$26$ red cards.", "$26/52$"),
         step("Simplify", "$1/2$.", "$1/2$")], "Ch21-Q14", N20P, None)
    put(359, 20, "Median of $20$ marks: $45,55,60,72,80,65,58,75,68,82,90,48,55,70,85,62,78,55,68,92$.", "$68$",
        [step("Sort", "Smallest to largest.", "20 values"),
         step("Median", "Average of 10th and 11th.", "$68$")], "Ch21-Q15", N20D, None)
    put(360, 20, "Bar graph monthly rainfall (mm): Jan $20$, Feb $30$, Mar $45$, Apr $60$, May $80$.",
        "See bar graph",
        [step("Axes", "Months vs mm.", "Scale to $90$"),
         step("Bars", "Heights as given.", "See diagram")], "Ch21-Q16", N20G, "bar-rainfall")
    put(361, 20, "Mode of: $5,8,5,12,8,5,15,8,12,5,8$.", "Modes $5$ and $8$",
        [step("Count", "$5$ appears $4$ times; $8$ appears $4$ times.", "Tie"),
         step("Answer", "Bimodal.", "$5$ and $8$")], "Ch21-Q17", N20D, None)
    put(362, 20, "Survey $100$ people: $40$ read A, $30$ read B, $20$ both. Only A, only B, neither?",
        "Only A $20$; only B $10$; neither $50$",
        [step("Venn", "Both $20$.", "Only A $20$, only B $10$"),
         step("Neither", "$100-50$.", "$50$")], "Ch21-Q18", N20D, "venn-two-sets")

    # Ch22 probability (363-377) → Ch 20
    prob = [
        (363, "Bag: $5$ red, $3$ blue. P(red)?", "$5/8$"),
        (364, "Die: P(number $>4$)?", "$1/3$"),
        (365, "Deck: P(king or queen)?", "$2/13$"),
        (366, "Two coins: P(at least one head)?", "$3/4$"),
        (367, "Box: $4$ red, $3$ green, $5$ blue. P(green)?", "$1/4$"),
        (368, "Two dice: P(sum $=7$)?", "$1/6$"),
        (369, "Letter from PROBABILITY: P(vowel)?", "$4/11$"),
        (370, "Die: P(odd number)?", "$1/2$"),
        (371, "Bag $7$ white, $5$ black: P(both white, without replacement)?", "$7/22$"),
        (372, "Three coin tosses: P(exactly $2$ heads)?", "$3/8$"),
        (373, "Deck: P(red ace or black king)?", "$1/13$"),
        (374, "P(event)$=0.35$. P(not event)?", "$0.65$"),
        (375, "Two dice: P(sum is prime)?", "$5/12$"),
        (376, "Bag $3$R,$4$B,$5$G: P(not blue)?", "$2/3$"),
        (377, "Die: P(multiple of $3$)?", "$1/3$"),
    ]
    prob_st = {
        363: [step("Total", "$8$ balls.", "P $=5/8$")],
        364: [step("Winners", "$\\{5,6\\}$.", "$2/6=1/3$")],
        365: [step("Cards", "$4+4=8$.", "$8/52=2/13$")],
        366: [step("Outcomes", "HH,HT,TH,TT.", "3 of 4")],
        367: [step("Total", "$12$.", "$3/12=1/4$")],
        368: [step("Pairs", "6 ways sum 7.", "$6/36=1/6$")],
        369: [step("Vowels", "O,A,I,I.", "$4/11$")],
        370: [step("Odds", "$\\{1,3,5\\}$.", "$1/2$")],
        371: [step("Multiply", "$7/12\\times6/11$.", "$7/22$")],
        372: [step("List", "8 outcomes.", "3 winners")],
        373: [step("Cards", "4 winning.", "$1/13$")],
        374: [step("Complement", "$1-0.35$.", "$0.65$")],
        375: [step("Prime sums", "15 ways.", "$5/12$")],
        376: [step("Not blue", "8 of 12.", "$2/3$")],
        377: [step("Multiples", "$\\{3,6\\}$.", "$1/3$")],
    }
    for gn, qu, ans in prob:
        put(gn, 20, qu, ans, prob_st[gn], f"Ch22-Q{gn-362}", N20P, None)

    # Ch23 graphs (378-389) → Ch 16
    put(378, 16, "Plot $(2,3),(-2,3),(-2,-3),(2,-3)$ and join. Name the figure.", "Rectangle",
        [step("Plot", "Four corners.", "Connect"),
         step("Shape", "Opposite sides equal.", "Rectangle")], "Ch23-Q1", N16C, "coord-rectangle")
    put(379, 16, "Draw graph of $y=2x+1$.", "Straight line through $(0,1),(1,3),(2,5)$",
        [step("Table", "$x=0,1,2$.", "Plot points"),
         step("Line", "Join with ruler.", "See diagram")], "Ch23-Q2", N16L, "line-graph-linear")
    put(380, 16, "Point $3$ right, $4$ above origin.", "$(3,4)$",
        [step("From origin", "Right $+x$, up $+y$.", "$(3,4)$")], "Ch23-Q3", N16C, "coord-rectangle")
    put(381, 16, "Graph $y=3x-2$. Find $y$ when $x=4$.", "$y=10$",
        [step("Graph", "Plot line.", "Read or substitute"),
         step("Substitute", "$3(4)-2$.", "$10$")], "Ch23-Q4", N16L, "line-graph-linear")
    put(382, 16, "Plot $A(1,2),B(3,2),C(3,5),D(1,5)$. Name figure.", "Rectangle",
        [step("Sides", "Width $2$, height $3$.", "Rectangle")], "Ch23-Q5", N16C, "coord-rectangle")
    put(383, 16, "Line through $(2,3)$ and $(4,7)$.", "See graph",
        [step("Plot", "Two points.", "Extend line")], "Ch23-Q6", N16L, "line-graph-linear")
    put(384, 16, "Midpoint of segment joining $(2,5)$ and $(6,9)$.", "$(4,7)$",
        [step("Formula", "Average of coordinates.", "$(4,7)$")], "Ch23-Q7", N16C, None)
    put(385, 16, "Draw graph of $y=-x+4$.", "Line through $(0,4)$ and $(4,0)$",
        [step("Intercepts", "$(0,4),(4,0)$.", "Negative slope")], "Ch23-Q8", N16L, "line-graph-negative-slope")
    put(386, 16, "Plot $(0,0),(3,0),(3,4),(0,4)$. Name figure.", "Rectangle",
        [step("Axes", "On coordinate axes.", "Rectangle")], "Ch23-Q9", N16C, "coord-rectangle")
    put(387, 16, "Graph $2x+3y=6$.", "Line through $(3,0)$ and $(0,2)$",
        [step("Intercepts", "$x$-intercept $3$.", "$y$-intercept $2$")], "Ch23-Q10", N16L, "line-graph-linear")
    put(388, 16, "Distance between $(3,4)$ and $(7,9)$.", "$\\sqrt{41}$",
        [step("Diffs", "$\\Delta x=4$, $\\Delta y=5$.", "Pythagoras"),
         step("Distance", "$\\sqrt{16+25}$.", "$\\sqrt{41}$")], "Ch23-Q11", N16C, None)
    put(389, 16, "Graph $y=x^2$ for $x=-2,-1,0,1,2$.", "Parabola",
        [step("Table", "$(-2,4),(-1,1),(0,0),(1,1),(2,4)$.", "Plot"),
         step("Curve", "Smooth U-shape.", "Parabola")], "Ch23-Q12", N16L, "parabola-yx2")

    # Ch24 symmetry (390-401) → Ch 17
    sym = [
        (390, "Lines of symmetry of a square?", "$4$", "square-lines-symmetry", N17S),
        (391, "Lines of symmetry of equilateral triangle?", "$3$", "triangle-lines-symmetry", N17S),
        (392, "Lines of symmetry of regular pentagon?", "$5$", None, N17S),
        (393, "Reflect letter A about vertical centre line.", "Same letter A", "reflect-letter-a", N17S),
        (394, "Lines of symmetry of a circle?", "Infinite", None, N17S),
        (395, "Lines of symmetry of regular hexagon?", "$6$", "hexagon-lines-symmetry", N17S),
        (396, "Rotational symmetry: H, N, S, Z?", "All four", None, N17R),
        (397, "Reflect figure across given symmetry line.", "Mirror image",
         None, N17S),
        (398, "Lines of symmetry of isosceles triangle?", "$1$", "triangle-lines-symmetry", N17S),
        (399, "Order of rotational symmetry of square?", "$4$", "square-lines-symmetry", N17R),
        (400, "Figure with exactly $2$ lines of symmetry.", "Rectangle (or rhombus)", "coord-rectangle", N17S),
        (401, "Capital letters with both line and rotational symmetry?", "H, I, O, X", None, N17R),
    ]
    sym_st = {
        390: [step("Square", "Vertical, horizontal, two diagonals.", "$4$")],
        391: [step("Triangle", "From each vertex to midpoint.", "$3$")],
        392: [step("Regular", "Equals number of sides.", "$5$")],
        393: [step("Mirror", "Vertical line through centre.", "Unchanged A")],
        394: [step("Circle", "Any diameter.", "Infinite")],
        395: [step("Hexagon", "6 lines.", "$6$")],
        396: [step("180° test", "All look same upside down.", "All four")],
        397: [step("Measure", "Equal distance from line.", "Mirror image")],
        398: [step("Isosceles", "One fold line.", "$1$")],
        399: [step("90° turns", "Looks same 4 times.", "Order $4$")],
        400: [step("Rectangle", "Vertical and horizontal only.", "Not diagonals")],
        401: [step("Check letters", "Line + 180° rotation.", "H,I,O,X")],
    }
    for gn, qu, ans, dia, nid in sym:
        put(gn, 17, qu, ans, sym_st[gn], f"Ch24-Q{gn-389}", nid, dia)

    return qs


def batch_09():
    """Advanced HOTS · Adv-Q1–Q50 · global Q402–451."""
    B = 9
    ST = "Gemini Advanced HOTS · Batch 9"
    qs = []
    adv = [0]

    N1 = "CH01-sec-rational-numbers"
    N2 = "CH02-sec-laws-of-exponents"
    N3 = "CH03-sec-square-numbers-or-perfect-squares"
    N4 = "CH04-sec-cube-numbers-or-perfect-cubes"
    N5 = "CH05-sec-numbers-in-general-form"
    N6 = "CH06-sec-union-of-sets"
    N7 = "CH07-sec-percentage"
    N8 = "CH08-sec-simple-interest"
    N9 = "CH09-sec-direct-variation"
    N10 = "CH10-sec-fundamental-concepts"
    N11 = "CH11-sec-factors-of-algebraic-expressions"
    N12 = "CH12-sec-equations"
    N13 = "CH13-sec-quadrilateral"
    N19 = "CH19-sec-area-and-perimeter-of-some-plane-figures"
    N20 = "CH20-sec-data-handling"
    N20P = "CH20-sec-likely"
    N16 = "CH16-sec-linear-graphs"
    N17S = "CH17-sec-line-symmetry"
    N17R = "CH17-sec-rotational-symmetry"

    def put(ch, qu, ans, st, nid, diagram=None):
        adv[0] += 1
        n = adv[0]
        gn = 401 + n
        qs.append(mk_q(B, gn, ch, qu, ans, st, local_label=f"Adv-Q{n}", linked_note_id=nid,
                       diagram=diagram, subtopic=ST, batch_num=n))

    # Q1–Q8: Rationals & exponents
    put(1, "Prove that the sum of any two rational numbers is always a rational number. Give two examples.",
        "If $\\dfrac{a}{b}$ and $\\dfrac{c}{d}$ are rationals ($b,d\\neq0$), then $\\dfrac{a}{b}+\\dfrac{c}{d}=\\dfrac{ad+bc}{bd}$ is rational. Examples: $\\dfrac12+\\dfrac13=\\dfrac56$; $-\\dfrac34+\\dfrac14=-\\dfrac12$.",
        [step("Definition", "Rational = $\\dfrac{\\text{integer}}{\\text{non-zero integer}}$.", "Take $\\dfrac{a}{b}$, $\\dfrac{c}{d}$."),
         step("Add", "Common denominator $bd$.", "$\\dfrac{ad+bc}{bd}$"),
         step("Closure", "$ad+bc$ and $bd$ are integers; $bd\\neq0$.", "Sum is rational"),
         step("Examples", "Compute two sums.", "$\\dfrac56$, $-\\dfrac12$")], N1)

    put(1, "If $\\dfrac{a}{b}$ is rational ($b\\neq0$), prove that its additive inverse is $-\\dfrac{a}{b}$.",
        "Additive inverse of $\\dfrac{a}{b}$ is $-\\dfrac{a}{b}$ because $\\dfrac{a}{b}+\\left(-\\dfrac{a}{b}\\right)=\\dfrac{0}{b}=0$.",
        [step("Definition", "$x$ is inverse of $y$ if $x+y=0$.", "Test $-\\dfrac{a}{b}$."),
         step("Add", "Same denominator.", "$\\dfrac{a-a}{b}=\\dfrac{0}{b}=0$"),
         step("Conclusion", "Sum is zero.", "They are additive inverses.")], N1)

    put(1, "Find five rational numbers between $-\\dfrac{3}{5}$ and $\\dfrac{2}{3}$ such that their average is zero.",
        "$-\\dfrac12$, $-\\dfrac14$, $0$, $\\dfrac14$, $\\dfrac12$ (sum $=0$ ⇒ average $=0$).",
        [step("Average trick", "Average $0$ ⇒ total sum $0$.", "Pick symmetric pairs around $0$."),
         step("Interval", "$-\\dfrac35\\approx-0.6$, $\\dfrac23\\approx0.67$ straddle $0$.", "Use $\\pm\\dfrac14$, $\\pm\\dfrac12$."),
         step("Fifth number", "Add $0$ without changing sum.", "Five numbers listed.")], N1)

    put(10, "If $\\left(x+\\dfrac{1}{x}\\right)=3$, find $x^3+\\dfrac{1}{x^3}$.",
        "$18$",
        [step("Cube identity", "$(A+B)^3=A^3+B^3+3AB(A+B)$.", "Cube both sides."),
         step("Expand", "$x^3+\\dfrac{1}{x^3}+3\\cdot1\\cdot3=27$.", "Middle product $x\\cdot\\dfrac1x=1$."),
         step("Solve", "$x^3+\\dfrac{1}{x^3}+9=27$.", "$18$")], N10)

    put(2, "Simplify with positive exponents: $\\left[\\left(-\\dfrac{3}{4}\\right)^{-2}\\times\\left(-\\dfrac{3}{4}\\right)^{-3}\\right]\\div\\left(-\\dfrac{3}{4}\\right)^{-5}$.",
        "$1$",
        [step("Multiply powers", "Add exponents in bracket.", "$\\left(-\\dfrac34\\right)^{-5}$"),
         step("Divide", "Subtract exponents: $-5-(-5)=0$.", "$\\left(-\\dfrac34\\right)^0=1$")], N2)

    put(2, "If $2^{x-1}=8$ and $3^{2y-1}=81$, find $x+y$.",
        "$6.5$",
        [step("Match bases", "$8=2^3$, $81=3^4$.", "Equate exponents."),
         step("Solve", "$x-1=3\\Rightarrow x=4$; $2y-1=4\\Rightarrow y=2.5$.", "$x+y=6.5$")], N2)

    put(4, "Find the smallest number which when multiplied by $8788$ gives a perfect cube. Also find the cube root of the result.",
        "Smallest multiplier $2$; product $17576$; cube root $26$.",
        [step("Factorise", "$8788=2^2\\times13^3$.", "Need one more $2$."),
         step("Multiply", "$8788\\times2=17576=2^3\\times13^3$.", "Perfect cube."),
         step("Cube root", "$\\sqrt[3]{17576}=2\\times13$.", "$26$")], N4)

    put(10, "Using $(a-b)^3=a^3-3a^2b+3ab^2-b^3$, find the cube of $97$.",
        "$912673$",
        [step("Rewrite", "$97=(100-3)^3$.", "$A=100$, $B=3$."),
         step("Expand", "$1000000-90000+2700-27$.", "Apply identity."),
         step("Compute", "Left to right.", "$912673$")], N10)

    # Q9–Q15: Sets & commercial math
    put(5, "A number divided by $7$ leaves remainder $5$; divided by $5$ leaves remainder $3$. Find the smallest 3-digit such number.",
        "$103$",
        [step("Trick", "$7-5=5-3=2$.", "Number $+2$ is divisible by $7$ and $5$."),
         step("LCM", "Multiples of $\\text{lcm}(7,5)=35$ minus $2$.", "$33,68,103,138,\\ldots$"),
         step("3-digit", "First $\\geq100$.", "$103$")], N5)

    put(6, "If $A=\\{x:x\\text{ is a multiple of }4\\text{ between }1\\text{ and }30\\}$ and $B=\\{x:x\\text{ is a multiple of }6\\text{ between }1\\text{ and }30\\}$, find $A\\cup B$ and $A\\cap B$.",
        "$A=\\{4,8,12,16,20,24,28\\}$; $B=\\{6,12,18,24\\}$; $A\\cup B=\\{4,6,8,12,16,18,20,24,28\\}$; $A\\cap B=\\{12,24\\}$.",
        [step("List sets", "Multiples in $(1,30)$.", "Write $A$ and $B$."),
         step("Union", "All distinct elements.", "$9$ elements."),
         step("Intersection", "Multiples of $\\text{lcm}(4,6)=12$.", "$\\{12,24\\}$")], N6, "venn-two-sets")

    put(6, "If $n(A)=25$, $n(B)=30$, $n(A\\cup B)=45$, find $n(A'\\cap B')$.",
        "$n(U)-45$ (needs universal set size $n(U)$; by De Morgan $n(A'\\cap B')=n(U)-n(A\\cup B)$).",
        [step("De Morgan", "$A'\\cap B'=(A\\cup B)'$.", "Complement of union."),
         step("Trick", "$n(U)$ not given.", "Answer $n(U)-45$.")], N6)

    put(7, "A number is increased by $20\\%$ and then decreased by $20\\%$. Find the net percentage change.",
        "Net $4\\%$ decrease ($96\\%$ of original).",
        [step("Base $100$", "After $+20\\%$: $120$.", "Then $-20\\%$ of $120$."),
         step("Final", "$120\\times0.80=96$.", "Net change $-4\\%$")], N7)

    put(7, "A shopkeeper marks goods $40\\%$ above CP, then allows successive discounts of $10\\%$ and $5\\%$. Find overall profit $\\%$.",
        "$19.7\\%$ profit",
        [step("CP $100$", "MP $=140$.", "After $10\\%$: $126$."),
         step("Second discount", "$126\\times0.95=119.70$.", "Profit $19.7\\%$ on CP $100$")], N7)

    put(8, "Difference between CI and SI on a sum for $3$ years at $10\\%$ p.a. is ₹$93$. Find the sum.",
        "₹$3000$",
        [step("3-year diff formula", "$\\text{Diff}=P\\times r^2\\times(3+r)$, $r=0.1$.", "$93=P\\times0.01\\times3.1$"),
         step("Solve", "$P=93/0.031$.", "₹$3000$")], N8)

    put(8, "A sum amounts to ₹$1331$ in $3$ years and ₹$1728$ in $6$ years at CI. Find the rate $\\%$ p.a.",
        "$9\\dfrac{1}{11}\\%$ (≈ $9.09\\%$)",
        [step("3-year block", "$1728=1331\\left(1+\\dfrac{R}{100}\\right)^3$.", "Years 3–6 behave like new investment."),
         step("Ratio", "$\\dfrac{1728}{1331}=\\left(\\dfrac{12}{11}\\right)^3$.", "Cube root both sides."),
         step("Rate", "$1+\\dfrac{R}{100}=\\dfrac{12}{11}$.", "$R=\\dfrac{100}{11}\\%$")], N8)

    # Q16–Q24: Algebra & equations
    put(9, "If $x$ varies directly as $y^2$ and $x=4$ when $y=2$, find $x$ when $y=5$.",
        "$25$",
        [step("Direct variation", "$x=ky^2$.", "Find $k$."),
         step("Constant", "$4=k\\cdot4\\Rightarrow k=1$.", "$x=5^2=25$")], N9)

    put(9, "$12$ men complete work in $15$ days at $8$ h/day. How many men finish in $20$ days at $6$ h/day?",
        "$12$ men",
        [step("Man-hours", "$12\\times15\\times8=1440$.", "Work fixed."),
         step("New crew", "$M\\times20\\times6=1440$.", "$M=12$")], N9)

    put(10, "If $\\left(x+\\dfrac{1}{x}\\right)^2=9$, find $x^3+\\dfrac{1}{x^3}$.",
        "$\\pm18$",
        [step("Square root", "$x+\\dfrac1x=\\pm3$.", "Two cases."),
         step("Cube identity", "$(x+\\dfrac1x)^3=x^3+\\dfrac1{x^3}+3(x+\\dfrac1x)$.", "Substitute $\\pm3$."),
         step("Results", "$+3\\Rightarrow18$; $-3\\Rightarrow-18$.", "$\\pm18$")], N10)

    put(11, "Factorise completely: $x^3-3x^2-9x-5$.",
        "$(x+1)^2(x-5)$",
        [step("Trial root", "$x=-1$ gives $0$.", "Factor $(x+1)$."),
         step("Divide", "Quotient $x^2-4x-5$.", "Factor quadratic."),
         step("Answer", "$(x+1)(x-5)$ with repeated root.", "$(x+1)^2(x-5)$")], N11)

    put(10, "If $a+b+c=0$, prove that $a^3+b^3+c^3=3abc$.",
        "Proved using $a^3+b^3+c^3-3abc=(a+b+c)(a^2+b^2+c^2-ab-bc-ca)$; RHS $=0$ when $a+b+c=0$.",
        [step("Identity", "Standard cubic identity.", "RHS has factor $(a+b+c)$."),
         step("Given", "$a+b+c=0$.", "Entire RHS $=0$."),
         step("Rearrange", "$a^3+b^3+c^3=3abc$.", "QED")], N10)

    put(12, "Solve: $\\dfrac{2x-3}{x+2}-\\dfrac{3x-2}{x-3}=\\dfrac{5}{6}$.",
        "$x=\\dfrac{-73\\pm\\sqrt{10081}}{22}$ (irrational roots)",
        [step("LCD", "Denominator $(x+2)(x-3)$.", "Cross-multiply."),
         step("Expand numerators", "Top: $-x^2-13x+13$.", "Equation $\\dfrac{-x^2-13x+13}{x^2-x-6}=\\dfrac56$."),
         step("Clear fractions", "$11x^2+73x-108=0$.", "Quadratic formula gives irrational roots.")], N12)

    put(12, "Ages of A and B are in ratio $7:5$. After $6$ years the ratio will be $4:3$. Find present ages.",
        "A $=42$ years, B $=30$ years",
        [step("Present", "$7x$ and $5x$.", "Future: add $6$."),
         step("Equation", "$\\dfrac{7x+6}{5x+6}=\\dfrac43$.", "Cross-multiply."),
         step("Solve", "$21x+18=20x+24\\Rightarrow x=6$.", "A $42$, B $30$")], N12)

    put(13, "In parallelogram $ABCD$, diagonals meet at $O$. If $AO=(3x+2)$ cm and $OC=(5x-4)$ cm, find $AC$.",
        "$22$ cm",
        [step("Property", "Diagonals bisect each other.", "$AO=OC$."),
         step("Solve", "$3x+2=5x-4\\Rightarrow x=3$.", "$AO=11$ cm."),
         step("Full diagonal", "$AC=2\\times AO$.", "$22$ cm")], N13, "parallelogram-diagonals")

    put(13, "Diagonals of a rhombus are in ratio $3:4$. If area is $384$ cm², find the diagonals.",
        "$24$ cm and $32$ cm",
        [step("Let diagonals", "$3x$ and $4x$.", "Area $\\dfrac12 d_1 d_2=384$."),
         step("Equation", "$\\dfrac12\\cdot3x\\cdot4x=384\\Rightarrow6x^2=384$.", "$x=8$."),
         step("Lengths", "$3x=24$, $4x=32$.", "Done.")], N13, "rhombus-diagonals")

    # Q25–Q30: Mensuration, stats, probability
    put(19, "Find the area of a regular hexagon with side $10$ cm (using equilateral triangles).",
        "$150\\sqrt3$ cm² (≈ $259.8$ cm²)",
        [step("Split", "6 equilateral triangles.", "Area $=6\\times\\dfrac{\\sqrt3}{4}s^2$."),
         step("Substitute", "$s=10$.", "$6\\times25\\sqrt3=150\\sqrt3$")], N19, "regular-hexagon")

    put(19, "A trapezium has parallel sides in ratio $2:5$. Distance between them is $12$ cm. Area $420$ cm². Find parallel sides.",
        "$20$ cm and $50$ cm",
        [step("Let sides", "$2x$ and $5x$.", "Area formula."),
         step("Solve", "$420=\\dfrac12(7x)(12)=42x$.", "$x=10$."),
         step("Sides", "$20$ cm, $50$ cm.", "")], N19, "trapezium-area")

    put(19, "Cuboid volume $2400$ cm³. Length : breadth : height $=4:3:2$. Find total surface area.",
        "$52\\times100^{2/3}$ cm² (≈ $1120.3$ cm²)",
        [step("Dimensions", "$4x,3x,2x$; $24x^3=2400$.", "$x^3=100$."),
         step("TSA", "$2(lb+bh+hl)=52x^2$.", "$52\\times100^{2/3}$ cm²")], N19)

    put(19, "Cylindrical tank radius $7$ m. Water fills $\\dfrac34$ of height; water volume $4620$ m³. Find full tank height.",
        "$40$ m",
        [step("Water height", "$\\dfrac34 h$.", "$4620=\\pi r^2\\cdot\\dfrac34 h$."),
         step("Substitute", "$\\pi=\\dfrac{22}{7}$, $r=7$.", "$4620=115.5h$."),
         step("Height", "$h=40$ m.", "")], N19, "cylinder-tank")

    put(20, "Mean of $15$ numbers is $18$. Mean of first $8$ is $16$; mean of last $8$ is $19$. Find the $8$th number.",
        "$10$",
        [step("Totals", "Overall sum $270$.", "Halves sum to $128+152=280$."),
         step("Overlap trick", "8th counted twice.", "$280-270=10$")], N20)

    put(20, "Two dice thrown. Probability sum is neither $7$ nor $11$.",
        "$\\dfrac{7}{9}$",
        [step("Unwanted sums", "7: $6$ ways; 11: $2$ ways.", "$8/36=2/9$."),
         step("Complement", "$1-2/9$.", "$7/9$")], N20P)

    # Q31–Q40: Heavy algebra & identities
    put(10, "If $\\left(x+\\dfrac{1}{x}\\right)=5$, find $x^4+\\dfrac{1}{x^4}$.",
        "$527$",
        [step("Square once", "$x^2+\\dfrac{1}{x^2}=23$.", "From $(x+\\dfrac1x)^2=25$."),
         step("Square again", "$(x^2+\\dfrac1{x^2})^2=x^4+\\dfrac1{x^4}+2$.", "$529-2=527$")], N10)

    put(10, "Simplify: $(a+b+c)^3-(a+b-c)^3-6c(a+b)^2+2c^3$.",
        "$4c^3$",
        [step("Substitute", "$X=a+b$.", "$(X+c)^3-(X-c)^3-6cX^2+2c^3$."),
         step("Cube difference", "Leaves $6X^2c+2c^3$.", "Cancel $6cX^2$."),
         step("Result", "$2c^3+2c^3$.", "$4c^3$")], N10)

    put(11, "Factorise $x^3+y^3+z^3-3xyz$ when $x+y+z=0$.",
        "$0$",
        [step("Identity", "$x^3+y^3+z^3-3xyz=(x+y+z)(\\cdots)$.", "Use Q20 result."),
         step("Given", "$x+y+z=0$.", "Whole expression $=0$.")], N11)

    put(12, "A two-digit number: tens digit is twice the units digit. If $18$ is **subtracted** (typo fix: not added), digits reverse. Find the number.",
        "$42$",
        [step("Setup", "Tens $=2y$, units $=y$; number $21y$.", "Reversed $12y$."),
         step("Equation", "$21y-18=12y$.", "$9y=18\\Rightarrow y=2$."),
         step("Number", "Tens $4$, units $2$.", "$42$")], N12)

    put(13, "Prove that the diagonals of a parallelogram bisect each other.",
        "Proved by ASA congruence of $\\triangle AOD$ and $\\triangle COB$ (opposite sides equal; alternate angles equal) ⇒ $AO=OC$, $DO=OB$.",
        [step("Draw", "Diagonals meet at $O$.", "Compare $\\triangle AOD$, $\\triangle COB$."),
         step("ASA", "$AD=CB$; alternate interior angles equal.", "Triangles congruent."),
         step("Conclusion", "Corresponding parts equal.", "Diagonals bisect each other.")], N13, "parallelogram-diagonals")

    put(3, "Find the smallest square number divisible by each of $8$, $12$ and $15$.",
        "$3600$",
        [step("LCM", "$\\text{lcm}(8,12,15)=120$.", "Factor $120=2^3\\cdot3\\cdot5$."),
         step("Make square", "Need partners for lone $2,3,5$.", "Multiply by $2\\times3\\times5=30$."),
         step("Answer", "$120\\times30$.", "$3600$")], N3)

    put(2, "If $3^{2x-1}=81$ and $5^{y-2}=625$, find $x+y$.",
        "$8.5$",
        [step("Bases", "$81=3^4$, $625=5^4$.", "Equate exponents."),
         step("Solve", "$x=2.5$, $y=6$.", "$x+y=8.5$")], N2)

    put(8, "CI on a sum for $2$ years at $10\\%$ is ₹$420$. Find SI for same sum, period and rate.",
        "₹$400$",
        [step("Find P", "CI $21\\%$ of P $=420$.", "$P=2000$."),
         step("SI", "$\\dfrac{2000\\times10\\times2}{100}$.", "₹$400$")], N8)

    put(7, "Shopkeeper buys at $20\\%$ discount on MP ₹$1200$, sells at $25\\%$ profit on CP. Find SP.",
        "₹$1200$",
        [step("CP", "$20\\%$ off ₹$1200$ → CP ₹$960$.", "Profit on CP."),
         step("SP", "$25\\%$ of $960=240$.", "SP $=1200$")], N7)

    put(9, "If $x$ varies inversely as $y$ and $y=12$ when $x=8$, find $x$ when $y=16$.",
        "$6$",
        [step("Inverse", "$xy=k$.", "$k=96$."),
         step("New $x$", "$x\\cdot16=96$.", "$x=6$")], N9)

    # Q41–Q50: Extreme word problems
    put(12, "Solve: $\\dfrac{x+3}{2x-1}=\\dfrac{x-2}{x+4}$.",
        "$x=6\\pm\\sqrt{46}$",
        [step("Cross-multiply", "$(x+3)(x+4)=(2x-1)(x-2)$.", "Expand."),
         step("Quadratic", "$x^2-12x-10=0$.", "Formula: $\\dfrac{12\\pm\\sqrt{184}}{2}$."),
         step("Simplify root", "$\\sqrt{184}=2\\sqrt{46}$.", "$6\\pm\\sqrt{46}$")], N12)

    put(12, "Father's age is $4$ times son's. After $8$ years father will be $2.5$ times as old as son. Find present ages.",
        "Son $8$, father $32$",
        [step("Present", "Son $x$, father $4x$.", "Future ages $+8$."),
         step("Equation", "$4x+8=2.5(x+8)$.", "$1.5x=12$."),
         step("Ages", "$x=8$.", "Son $8$, father $32$")], N12)

    put(13, "In rhombus $ABCD$, $\\angle ABC=120^\\circ$, side $10$ cm. Find $\\angle ADC$ and diagonals.",
        "$\\angle ADC=120^\\circ$; diagonals $10$ cm and $10\\sqrt3$ cm",
        [step("Angles", "Opposite angles equal.", "$\\angle ADC=120^\\circ$; acute angles $60^\\circ$."),
         step("Short diagonal", "$\\triangle ABD$ equilateral.", "$BD=10$ cm."),
         step("Long diagonal", "Half-diagonals in right triangle.", "$AC=10\\sqrt3$ cm")], N13, "rhombus-diagonals")

    put(19, "Trapezium: parallel sides $20$ cm and $30$ cm; non-parallel sides equal; height $12$ cm. Find area.",
        "$300$ cm²",
        [step("Area formula", "Needs parallel sides and height only.", "$\\dfrac12(20+30)\\times12$."),
         step("Compute", "$25\\times12$.", "$300$ cm²")], N19, "trapezium-area")

    put(19, "Cylinder radius $7$ cm, water height $15$ cm. Spherical balls radius $1.75$ cm dropped until water rises $5.25$ cm. How many balls?",
        "$36$ spheres",
        [step("Rise volume", "$\\pi\\cdot7^2\\cdot5.25=257.25\\pi$.", "Starting height is irrelevant."),
         step("One sphere", "$\\dfrac43\\pi(1.75)^3\\approx7.146\\pi$.", "Divide volumes."),
         step("Count", "$257.25/7.146$.", "$36$ exactly")], N19, "cylinder-spheres-rise")

    put(20, "Mean, median and mode of a distribution are $45$, $48$ and $50$. State the empirical relationship between them.",
        "For moderately skewed data: $\\text{Mode}\\approx3(\\text{Median})-2(\\text{Mean})$.",
        [step("Empirical rule", "Mode–Median–Mean relation.", "$\\text{Mode}\\approx3\\times48-2\\times45=54$ (approximate)."),
         step("State formula", "This is the standard relationship asked.", "Formula above.")], N20)

    put(20, "Bag: $4$ red, $5$ blue, $6$ green. Three balls drawn. Probability all three different colours.",
        "$\\dfrac{24}{91}$",
        [step("One order", "R then B then G: $\\dfrac{4}{15}\\cdot\\dfrac{5}{14}\\cdot\\dfrac{6}{13}=\\dfrac{4}{91}$.", "Multiply by orders."),
         step("Permutations", "$3!=6$ colour orders.", "$6\\times\\dfrac{4}{91}=\\dfrac{24}{91}$")], N20P)

    put(16, "Draw the graph of $y=x^2-4$ and find $x$-axis intercepts.",
        "Parabola through $(-2,0)$ and $(2,0)$",
        [step("Set $y=0$", "$x^2-4=0$.", "$x=\\pm2$."),
         step("Graph", "U-shaped parabola shifted down $4$.", "Intercepts $(\\pm2,0)$")], N16, "parabola-yx2-minus4")

    put(17, "How many lines of symmetry does a regular octagon have? What is its order of rotational symmetry?",
        "$8$ lines of symmetry; rotational symmetry of order $8$.",
        [step("Regular polygon", "Lines of symmetry $=$ number of sides.", "$8$ lines."),
         step("Rotation", "Looks same after $360/8=45^\\circ$.", "Order $8$")], N17S, "octagon-lines-symmetry")

    put(10, "If $\\dfrac{a}{b}+\\dfrac{b}{a}=5$, find $\\dfrac{a^3}{b^3}+\\dfrac{b^3}{a^3}$.",
        "$110$",
        [step("Substitute", "Let $x=\\dfrac{a}{b}$.", "$x+\\dfrac1x=5$."),
         step("Cube", "$125=x^3+\\dfrac1{x^3}+15$.", "Same as Adv-Q4 pattern."),
         step("Answer", "$125-15$.", "$110$")], N10)

    return qs


def batch_10():
    """Advanced HOTS · Adv-Q51–Q100 · global Q452–501."""
    B = 10
    ST = "Gemini Advanced HOTS · Batch 10"
    qs = []
    adv = [50]

    N5 = "CH05-sec-numbers-in-general-form"
    N7 = "CH07-sec-percentage"
    N8 = "CH08-sec-simple-interest"
    N9 = "CH09-sec-direct-variation"
    N10 = "CH10-sec-fundamental-concepts"
    N11 = "CH11-sec-factors-of-algebraic-expressions"
    N12 = "CH12-sec-equations"
    N13 = "CH13-sec-quadrilateral"
    N16 = "CH16-sec-linear-graphs"
    N19 = "CH19-sec-area-and-perimeter-of-some-plane-figures"
    N20 = "CH20-sec-data-handling"
    N20P = "CH20-sec-likely"

    def put(ch, qu, ans, st, nid, diagram=None):
        adv[0] += 1
        n = adv[0]
        gn = 451 + (n - 50)
        qs.append(mk_q(B, gn, ch, qu, ans, st, local_label=f"Adv-Q{n}", linked_note_id=nid,
                       diagram=diagram, subtopic=ST, batch_num=n - 50))

    # Q51–Q64: Heavy algebra & identities
    put(10, "Prove that $(a+b)^3-(a-b)^3=2b(3a^2+b^2)$.",
        "Proved: expand cubes, subtract → $6a^2b+2b^3=2b(3a^2+b^2)$.",
        [step("Expand cubes", "$(a+b)^3=a^3+3a^2b+3ab^2+b^3$.", "$(a-b)^3=a^3-3a^2b+3ab^2-b^3$."),
         step("Subtract", "$a^3$ and $3ab^2$ cancel.", "$6a^2b+2b^3$"),
         step("Factor", "GCF $2b$.", "$2b(3a^2+b^2)$")], N10)

    put(11, "Factorise: $8x^3+27y^3+64z^3-72xyz$.",
        "$(2x+3y+4z)(4x^2+9y^2+16z^2-6xy-12yz-8xz)$",
        [step("Identity", "$A^3+B^3+C^3-3ABC=(A+B+C)(\\cdots)$.", "$A=2x$, $B=3y$, $C=4z$."),
         step("Check", "$-3(2x)(3y)(4z)=-72xyz$.", "Identity applies."),
         step("Factor", "Plug into formula.", "Product above.")], N11)

    put(12, "A two-digit number is $4$ times the sum of its digits. If $9$ is added, the digits reverse. Find the number.",
        "$12$",
        [step("Setup", "Number $10x+y$.", "Digits $x,y$."),
         step("First rule", "$10x+y=4(x+y)$.", "$2x=y$."),
         step("Second rule", "$(10x+y)+9=10y+x$.", "$x-y=-1$; with $y=2x$ get $x=1$, $y=2$."),
         step("Answer", "Tens $1$, units $2$.", "$12$")], N12)

    put(13, "In parallelogram $ABCD$, $AB=2x+5$, $BC=3x-8$, $CD=x+12$. Find $x$ and all sides.",
        "$x=7$; sides $19,13,19,13$ cm",
        [step("Opposite sides", "$AB=CD$.", "$2x+5=x+12$."),
         step("Solve", "$x=7$.", "Substitute."),
         step("Sides", "$AB=CD=19$; $BC=AD=13$.", "Done.")], N13, "parallelogram-diagonals")

    put(19, "Find the area of a regular pentagon with side $8$ cm.",
        "$110.08$ cm²",
        [step("Formula", "Area $\\approx1.72\\times\\text{side}^2$.", "Standard pentagon multiplier."),
         step("Compute", "$1.72\\times64$.", "$110.08$ cm²")], N19, "polygon-pentagon-coords")

    put(19, "Cuboid: length $=$ breadth $+2$ cm, height $=$ breadth $-1$ cm, volume $240$ cm³. Find dimensions.",
        "Breadth $6$ cm, length $8$ cm, height $5$ cm",
        [step("Let breadth", "$x$; volume $(x+2)(x)(x-1)=240$.", "Trial and error."),
         step("Try $x=6$", "$(8)(6)(5)=240$.", "Perfect match."),
         step("Dimensions", "$6,8,5$ cm.", "")], N19, "cuboid-dims")

    put(19, "Cylinder: CSA $440$ cm², volume $1540$ cm³. Find radius and height.",
        "$r=7$ cm, $h=10$ cm",
        [step("Divide formulas", "$\\dfrac{\\pi r^2 h}{2\\pi rh}=\\dfrac{1540}{440}$.", "$\\dfrac r2=3.5\\Rightarrow r=7$."),
         step("Height", "$2\\pi rh=440$.", "$h=10$ cm")], N19, "cylinder-tank")

    put(20, "Marks: $45,55,60,72,80,65,58,75,68,82$. Find mean deviation from the mean.",
        "$9.4$",
        [step("Mean", "Sum $660$.", "Mean $66$."),
         step("Deviations", "Absolute distances from $66$.", "Sum $94$."),
         step("MD", "$94/10$.", "$9.4$")], N20)

    put(20, "Two cards drawn from a deck of $52$. Probability both are kings.",
        "$\\dfrac{1}{221}$",
        [step("First king", "$4/52=1/13$.", "Without replacement."),
         step("Second king", "$3/51=1/17$.", "Multiply."),
         step("Answer", "$1/13\\times1/17$.", "$1/221$")], N20P)

    put(16, "Draw the graph of $3x-2y=6$ and find the area of the triangle formed with the coordinate axes.",
        "Area $=3$ square units; intercepts $(2,0)$ and $(0,-3)$.",
        [step("Intercepts", "$x$-intercept $(2,0)$; $y$-intercept $(0,-3)$.", "Plot line."),
         step("Triangle", "Base $2$, height $3$ with origin.", "$\\dfrac12\\times2\\times3=3$")], N16, "line-intercept-triangle")

    put(10, "If $\\left(x+\\dfrac{1}{x}\\right)=4$, find $x^5+\\dfrac{1}{x^5}$.",
        "$724$",
        [step("Square", "$x^2+\\dfrac1{x^2}=14$.", "From $(x+\\dfrac1x)^2=16$."),
         step("Cube", "$x^3+\\dfrac1{x^3}=52$.", "Cube identity with $4$."),
         step("Multiply", "$(x^2+\\dfrac1{x^2})(x^3+\\dfrac1{x^3})=728$.", "Middle term $x+\\dfrac1x=4$."),
         step("Answer", "$728-4$.", "$724$")], N10)

    put(10, "Simplify: $(a+b)^3+(b+c)^3+(c+a)^3-3(a+b)(b+c)(c+a)$.",
        "$2(a^3+b^3+c^3-3abc)$",
        [step("Substitute", "$X=a+b$, $Y=b+c$, $Z=c+a$.", "$X^3+Y^3+Z^3-3XYZ$."),
         step("Sum", "$X+Y+Z=2(a+b+c)$.", "Standard identity."),
         step("Result", "Evaluates to $2(a^3+b^3+c^3-3abc)$.", "")], N10)

    put(11, "Factorise: $x^4+4$ (Sophie Germain identity).",
        "$(x^2-2x+2)(x^2+2x+2)$",
        [step("Add/subtract", "$x^4+4x^2+4-4x^2$.", "Complete square."),
         step("Difference of squares", "$(x^2+2)^2-(2x)^2$.", "Factor."),
         step("Answer", "Two quadratics.", "$(x^2-2x+2)(x^2+2x+2)$")], N11)

    put(12, "Sum of digits of a two-digit number is $9$. If the number is multiplied by $4$, digits reverse. Find the number.",
        "No integer solution as written (textbook typo). If multiplied by $4.5$, answer is $18$; if increased by $45$, $27\\to72$ also works.",
        [step("Test candidates", "Digits sum $9$: $18,27,36,45,54,63,72,81$.", "Multiply each by $4$."),
         step("Check", "None gives reversed digits.", "Impossible as stated."),
         step("Likely typo", "$\\times4.5$: $18\\times4.5=81$.", "Or $+45$ variant.")], N12)

    # Q65–Q77: Geometry proofs & tricks
    put(13, "Kite $ABCD$: $AB=AD=5$ cm, $CB=CD=13$ cm. One diagonal is $24$ cm — find diagonals.",
        "Trap: max diagonal $\\leq18$ cm, so $24$ cm is impossible. If short diagonal $BD=8$ cm, long diagonal $AC=15$ cm.",
        [step("Impossible data", "Longest stretch $5+13=18$ cm.", "$24$ cm cannot fit."),
         step("Assume $BD=8$", "Half $=4$.", "Pythagoras on top/bottom triangles."),
         step("Long diagonal", "$3+12$.", "$AC=15$ cm")], N13, "kite-diagonals")

    put(19, "Trapezium field: parallel sides $40$ m and $25$ m; non-parallel sides $13$ m and $14$ m. Plough at ₹$5$/m².",
        "₹$1820$",
        [step("Inner triangle", "Base $15$ m; sides $13,14$.", "Heron area $84$ m²."),
         step("Height", "$84=\\dfrac12\\times15\\times h$.", "$h=11.2$ m."),
         step("Trapezium area", "$\\dfrac12(40+25)\\times11.2=364$ m².", "Cost $364\\times5=$ ₹$1820$")], N19, "trapezium-field")

    put(19, "Cylinder $r=7$ cm, $h=20$ cm melted into spheres $r=1.75$ cm. How many spheres?",
        "$137$ whole spheres ($960/7\\approx137.14$)",
        [step("Cylinder vol", "$980\\pi$.", "Sphere vol $\\dfrac{343\\pi}{48}$."),
         step("Divide", "Cancel $\\pi$; simplify.", "$960/7$."),
         step("Whole spheres", "Take integer part.", "$137$")], N19, "cylinder-tank")

    put(20, "Mean of $20$ numbers is $15$. Each number is multiplied by $3$, then $5$ is added. New mean?",
        "$50$",
        [step("Rule", "Same operation on all data changes mean the same way.", "Apply to mean."),
         step("Compute", "$15\\times3+5$.", "$50$")], N20)

    put(20, "Bag: $5$ red, $4$ blue. Two drawn without replacement. P(second is red | first was blue)?",
        "$5/8$",
        [step("Given", "First ball blue.", "$8$ balls left, $5$ red."),
         step("Answer", "$5/8$.", "")], N20P)

    put(16, "Draw the graph of $y=|x|$ and describe its symmetry.",
        "V-shaped graph through origin; symmetric about the $y$-axis.",
        [step("Shape", "$|-2|=|2|=2$.", "Cannot go below $x$-axis."),
         step("Symmetry", "Mirror across $y$-axis.", "Vertex at $(0,0)$")], N16, "abs-graph-v")

    put(10, "If $\\dfrac{a}{b}=\\dfrac34$, find $\\dfrac{a^3+b^3}{a^3-b^3}$.",
        "$-\\dfrac{91}{37}$",
        [step("Substitute", "$a=3$, $b=4$.", "Compute cubes."),
         step("Numerator", "$27+64=91$.", "Denominator $27-64=-37$."),
         step("Answer", "$-91/37$.", "")], N10)

    put(5, "Prove: if a number is divisible by $9$, the sum of its digits is divisible by $9$.",
        "For $100a+10b+c=9(11a+b)+(a+b+c)$; first part divisible by $9$, so digit sum must be too.",
        [step("3-digit form", "$100a+10b+c$.", "Split place values."),
         step("Rearrange", "$9(11a+b)+(a+b+c)$.", "Digit sum $a+b+c$."),
         step("Conclusion", "Divisibility by $9$ forces digit sum divisible by $9$.", "QED")], N5)

    put(8, "CI on a sum for $1\\dfrac12$ years at $8\\%$ p.a. compounded half-yearly is ₹$306$. Find the sum.",
        "₹$2448.70$ (approx.)",
        [step("Half-yearly", "Rate $4\\%$, $n=3$ periods.", "$A=P(1.04)^3$."),
         step("CI", "$0.124864P=306$.", "$P\\approx2448.70$")], N8)

    put(7, "Two horses sold at ₹$4000$ each: $25\\%$ gain on one, $25\\%$ loss on other. Overall profit or loss $\\%$?",
        "$6.25\\%$ loss",
        [step("Shortcut", "Equal SP, equal gain/loss rates → net loss.", "$\\text{Loss}\\%=r^2/100$."),
         step("Compute", "$25^2/100$.", "$6.25\\%$ loss")], N7)

    put(9, "If $x\\propto y$ and $y\\propto z$, prove $x\\propto z$.",
        "$x=k_1y$, $y=k_2z$ ⇒ $x=(k_1k_2)z$ ⇒ $x\\propto z$.",
        [step("Direct laws", "$x=k_1y$, $y=k_2z$.", "Substitute."),
         step("Combine", "$x=(k_1k_2)z$.", "Product of constants is constant."),
         step("Conclusion", "$x\\propto z$.", "QED")], N9)

    put(12, "Solve: $\\dfrac{2}{x-3}+\\dfrac{3}{x+2}=\\dfrac{5}{x-1}$.",
        "$x=7$",
        [step("Combine left", "$\\dfrac{5x-5}{x^2-x-6}=\\dfrac{5}{x-1}$.", "Numerator $5(x-1)$."),
         step("Cancel $5$", "$\\dfrac{x-1}{x^2-x-6}=\\dfrac{1}{x-1}$.", "Cross-multiply."),
         step("Solve", "$x^2-2x+1=x^2-x-6$.", "$x=7$")], N12)

    put(13, "In a parallelogram, one angle is $30^\\circ$ more than twice the smallest angle. Find all angles.",
        "$50^\\circ,130^\\circ,50^\\circ,130^\\circ$",
        [step("Let smallest", "$x$; adjacent $2x+30$.", "Supplementary pair."),
         step("Equation", "$x+(2x+30)=180$.", "$x=50$."),
         step("Angles", "Opposite pairs equal.", "$50^\\circ,130^\\circ$ each pair")], N13, "parallelogram-diagonals")

    # Q78–Q100: Ultimate brain busters
    put(19, "Find the area of a regular octagon with side $10$ cm.",
        "$200(1+\\sqrt2)$ cm² (≈ $482.8$ cm²)",
        [step("Formula", "Area $=2(1+\\sqrt2)\\times\\text{side}^2$.", "Substitute $s=10$."),
         step("Compute", "$2(1+\\sqrt2)\\times100$.", "$200(1+\\sqrt2)$ cm²")], N19, "octagon-lines-symmetry")

    put(19, "Cylindrical tank $r=3.5$ m, $h=6$ m full of water. How many $7$-litre buckets?",
        "$33000$ buckets",
        [step("Volume", "$231$ m³.", "$\\pi r^2 h$."),
         step("Litres", "$231000$ L.", "Divide by $7$."),
         step("Buckets", "$33000$.", "")], N19, "cylinder-tank")

    put(20, "Mean $=52$, variance $=144$. Find coefficient of variation.",
        "≈ $23.07\\%$",
        [step("SD", "$\\sqrt{144}=12$.", "CV formula."),
         step("CV", "$(12/52)\\times100$.", "$300/13\\approx23.07\\%$")], N20)

    put(20, "Three cards from a deck of $52$. Probability all same suit.",
        "≈ $0.0129$ ($\\approx1.3\\%$)",
        [step("One suit path", "Hearts: $13/52\\times12/51\\times11/50$.", "Any suit same probability."),
         step("Multiply", "Simplify fraction.", "≈ $0.0129$")], N20P)

    put(10, "If $\\left(x+\\dfrac{1}{x}\\right)=6$, find $x^6+\\dfrac{1}{x^6}$.",
        "$39202$",
        [step("Square", "$x^2+\\dfrac1{x^2}=34$.", "From $36$."),
         step("Cube the square", "$34^3=39304$.", "$x^6+\\dfrac1{x^6}+3(34)=39304$."),
         step("Answer", "$39304-102$.", "$39202$")], N10)

    put(11, "Factorise: $x^4-16$.",
        "$(x-2)(x+2)(x^2+4)$",
        [step("First DOS", "$(x^2-4)(x^2+4)$.", "Factor $x^2-4$ again."),
         step("Answer", "$(x-2)(x+2)(x^2+4)$.", "")], N11)

    put(5, "Number divided by $3,4,5$ leaves remainders $2,3,4$. Find smallest such number.",
        "$59$",
        [step("Gap trick", "$3-2=4-3=5-4=1$.", "Number $+1$ divisible by $3,4,5$."),
         step("LCM", "$\\text{lcm}(3,4,5)=60$.", "$60-1=59$")], N5)

    put(19, "Rectangle: length $5$ cm more than breadth; diagonal $13$ cm. Find area.",
        "≈ $72$ cm² ($B\\approx6.35$ cm, $L\\approx11.35$ cm)",
        [step("Pythagoras", "$B^2+(B+5)^2=169$.", "$2B^2+10B-144=0$."),
         step("Quadratic", "$B^2+5B-72=0$.", "$B\\approx6.35$."),
         step("Area", "$L\\times B$.", "≈ $72$ cm²")], N19)

    put(19, "Trapezium: parallel sides $18$ cm and $12$ cm; equal legs $5$ cm each. Find area.",
        "$60$ cm²",
        [step("Isosceles", "Triangle base $(18-12)/2=3$ cm.", "Height from Pythagoras $=4$ cm."),
         step("Area", "$\\dfrac12(18+12)\\times4$.", "$60$ cm²")], N19, "trapezium-area")

    put(19, "Sphere $r=6$ cm melted into cones $r=3$ cm, $h=4$ cm. How many cones?",
        "$24$ cones",
        [step("Sphere", "$288\\pi$.", "Cone $12\\pi$ each."),
         step("Divide", "$288\\pi/12\\pi$.", "$24$")], N19)

    put(20, "Mean of $25$ observations is $36$. Mean of first $13$ is $32$; mean of last $13$ is $40$. Find $13$th observation.",
        "$36$",
        [step("Totals", "Overall $900$.", "Halves $416+520=936$."),
         step("Overlap", "$13$th counted twice.", "$936-900=36$")], N20)

    put(20, "Bag: $6$ red, $4$ white. Draw without replacement until white appears. P(white on 4th draw)?",
        "$2/21$",
        [step("Pattern", "RRRW.", "Sequential probabilities."),
         step("Multiply", "$(6/10)(5/9)(4/8)(4/7)$.", "$2/21$")], N20P)

    put(16, "Draw the graph of $y=2x^2-8$. Find vertex and axis of symmetry.",
        "Vertex $(0,-8)$; axis of symmetry $x=0$ (the $y$-axis).",
        [step("Parabola", "U-shape, coefficient $2>0$.", "Shift down $8$."),
         step("Vertex", "At $x=0$, $y=-8$.", "Axis $x=0$")], N16, "parabola-y2x2-minus8")

    put(10, "If $\\dfrac{a}{b}=\\dfrac57$, find $\\dfrac{a^2+b^2}{a^2-b^2}$.",
        "$-\\dfrac{37}{12}$",
        [step("Substitute", "$a=5$, $b=7$.", "Compute."),
         step("Answer", "$(25+49)/(25-49)$.", "$-37/12$")], N10)

    put(8, "CI for $2$ years at $5\\%$ is ₹$51$. Find SI for $3$ years at $6\\%$ on same sum.",
        "₹$89.56$ (approx.)",
        [step("Find P", "Effective CI rate $10.25\\%$.", "$P\\approx497.56$."),
         step("SI", "$497.56\\times6\\times3/100$.", "₹$89.56$")], N8)

    put(7, "Buys at $15\\%$ discount, sells at $20\\%$ profit, gain ₹$85$. Find marked price.",
        "₹$500$",
        [step("CP", "$0.2y=85\\Rightarrow y=425$.", "Cost price."),
         step("MP", "$0.85x=425$.", "₹$500$")], N7)

    put(9, "If $x\\propto y$ and $x\\propto\\dfrac1z$, and $x=12$ when $y=8,z=4$, find $x$ when $y=10,z=5$.",
        "$12$",
        [step("Joint variation", "$x=k(y/z)$.", "$k=6$ from $12=k(2)$."),
         step("New value", "$x=6(10/5)$.", "$12$")], N9)

    put(12, "Solve: $\\dfrac{x-2}{x+3}+\\dfrac{x+3}{x-2}=\\dfrac{10}{3}$.",
        "$x=-5.5$ or $x=4.5$",
        [step("Let $U$", "$U=\\dfrac{x-2}{x+3}$; second term $=1/U$.", "$U+1/U=10/3$."),
         step("Quadratic in $U$", "$3U^2-10U+3=0$.", "$U=3$ or $U=1/3$."),
         step("Back-substitute", "Two linear equations.", "$-5.5$, $4.5$")], N12)

    put(13, "Rhombus: diagonals in ratio $2:3$, area $384$ cm². Find side.",
        "$4\\sqrt{26}$ cm (≈ $20.39$ cm)",
        [step("Diagonals", "$2x,3x$; $3x^2=384$.", "$x=8\\sqrt2$."),
         step("Half-diagonals", "$8\\sqrt2$, $12\\sqrt2$.", "Side $=\\sqrt{128+288}=4\\sqrt{26}$")], N13, "rhombus-diagonals")

    put(19, "Cylinder diameter $14$ m, height $10$ m. Water filled to $7$ m. Volume in kilolitres?",
        "$1078$ kilolitres",
        [step("Water volume", "$r=7$, $h=7$.", "$\\pi r^2 h=1078$ m³."),
         step("Convert", "$1$ m³ $=1$ kilolitre.", "$1078$ kL")], N19, "cylinder-tank")

    put(20, "Mode $=45$, median $=50$, mean $=55$. Comment on skewness.",
        "Positively skewed (right-skewed): Mean $>$ Median $>$ Mode.",
        [step("Compare", "Mean $55>$ median $50>$ mode $45$.", "Long tail toward higher values."),
         step("Conclusion", "Positive skew.", "")], N20)

    put(20, "Two dice thrown. Probability product is a prime number.",
        "$1/6$",
        [step("Prime product", "Need $1\\times p$ with $p\\in\\{2,3,5\\}$.", "Six ordered pairs."),
         step("Probability", "$6/36$.", "$1/6$")], N20P)

    put(16, "Draw the graph of $x^2+y^2=25$ and find intersection with $y=x$.",
        "Circle centre $(0,0)$, radius $5$; intersections $\\left(\\pm\\sqrt{12.5},\\pm\\sqrt{12.5}\\right)$ (≈ $\\pm3.53$).",
        [step("Circle", "$x^2+y^2=25$.", "Radius $5$ at origin."),
         step("Substitute $y=x$", "$2x^2=25$.", "$x=\\pm\\sqrt{12.5}$."),
         step("Points", "$y=x$ gives matching coordinates.", "≈ $(3.53,3.53)$ and $(-3.53,-3.53)$")], N16, "circle-line-intersect")

    return qs


BUILDERS = {1: batch_01, 2: batch_02, 3: batch_03, 4: batch_04, 5: batch_05, 6: batch_06, 7: batch_07, 8: batch_08, 9: batch_09, 10: batch_10}


def build(batch_num: int):
    if batch_num not in BUILDERS:
        raise SystemExit(f"No builder for batch {batch_num}")
    BATCHES_DIR.mkdir(parents=True, exist_ok=True)
    data = {
        "batch": batch_num,
        "title": f"Gemini Advanced HOTS · Batch {batch_num}" if batch_num >= 9 else f"Gemini Open Glassbox · Batch {batch_num}",
        "questions": BUILDERS[batch_num](),
    }
    qs = data["questions"]
    data["count"] = len(qs)
    data["globalRange"] = [qs[0]["globalNum"], qs[-1]["globalNum"]] if qs else [(batch_num - 1) * 50 + 1, batch_num * 50]
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
