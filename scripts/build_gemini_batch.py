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
}

TOPIC_BY_CH = {n: f"math-ch{n}" for n in range(1, 21)}


def step(rule, why, math):
    return {"rule": rule, "why": why, "math": math}


def mk_q(batch, global_num, chapter, question, answer, steps, *, local_label=None, linked_note_id=None):
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
        "linked_note_id": linked_note_id or NOTE_BY_CH.get(chapter, f"CH{chapter:02d}-sec-introduction"),
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


BUILDERS = {1: batch_01, 2: batch_02, 3: batch_03}


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
