#!/usr/bin/env python3
"""Add Batch 1 detailed solutions to chapter practice session files."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "chapters"

META = {
    1: ("math-ch1", "CH01-sec-rational-numbers", "Rational Numbers"),
    2: ("math-ch2", "CH02-sec-exponents-and-powers", "Exponents and Powers"),
    3: ("math-ch3", "CH03-sec-squares-and-square-roots", "Squares and Square Roots"),
    4: ("math-ch4", "CH04-sec-cubes-and-cube-roots", "Cubes and Cube Roots"),
    5: ("math-ch5", "CH05-sec-playing-with-numbers", "Playing with Numbers"),
}


def q(ch, num, question, answer, steps, explanation):
    topic, note, _ = META[ch]
    return {
        "id": f"Q-CH{ch:02d}-B01-{num:03d}",
        "chapter": ch,
        "topicId": topic,
        "type": "practice",
        "subtopic": "Batch 1 · Detailed Solutions",
        "question": question,
        "answer": answer,
        "options": [],
        "glassboxSteps": steps,
        "explanation": explanation,
        "linked_note_id": note,
        "source": "practice-session",
    }


BATCH = []

# ── Chapter 1: Q1–9 ──────────────────────────────────────────────────────────

BATCH.append(q(1, 1,
    "Add the following rational numbers and verify the commutative property: $-\\dfrac{5}{7}$ and $\\dfrac{3}{8}$.",
    "Both sums equal $-\\dfrac{19}{56}$. Commutative property verified.",
    [
        {"rule": "Concept", "why": "Commutative property of addition: $a + b = b + a$.", "math": "a + b = b + a"},
        {"rule": "Compute $a + b$", "why": "LCM of 7 and 8 is 56.", "math": "-\\dfrac{5}{7} + \\dfrac{3}{8} = \\dfrac{-40 + 21}{56} = -\\dfrac{19}{56}"},
        {"rule": "Compute $b + a$", "why": "Same LCM.", "math": "\\dfrac{3}{8} + \\left(-\\dfrac{5}{7}\\right) = \\dfrac{21 - 40}{56} = -\\dfrac{19}{56}"},
        {"rule": "Conclusion", "why": "Both sums are equal.", "math": "-\\dfrac{19}{56} = -\\dfrac{19}{56}\\; \\checkmark"},
    ],
    "LCM 56: $-\\frac{5}{7}+\\frac{3}{8} = \\frac{3}{8}+(-\\frac{5}{7}) = -\\frac{19}{56}$. Verified.",
))

BATCH.append(q(1, 2,
    "Verify the associative property for addition of rational numbers using: $-\\dfrac{3}{5}$, $\\dfrac{2}{7}$, and $-\\dfrac{1}{2}$.",
    "LHS $=$ RHS $= -\\dfrac{57}{70}$. Associative property verified.",
    [
        {"rule": "Concept", "why": "Associative property: $(a+b)+c = a+(b+c)$.", "math": "(a+b)+c = a+(b+c)"},
        {"rule": "LHS", "why": "First add $-\\frac{3}{5}+\\frac{2}{7}$ (LCM 35), then add $-\\frac{1}{2}$ (LCM 70).", "math": "\\left(-\\dfrac{3}{5}+\\dfrac{2}{7}\\right)+\\left(-\\dfrac{1}{2}\\right) = -\\dfrac{57}{70}"},
        {"rule": "RHS", "why": "First add $\\frac{2}{7}+(-\\frac{1}{2})$ (LCM 14), then add $-\\frac{3}{5}$ (LCM 70).", "math": "-\\dfrac{3}{5}+\\left(\\dfrac{2}{7}+\\left(-\\dfrac{1}{2}\\right)\\right) = -\\dfrac{57}{70}"},
        {"rule": "Conclusion", "why": "LHS = RHS.", "math": "-\\dfrac{57}{70} = -\\dfrac{57}{70}\\; \\checkmark"},
    ],
    "LHS = RHS = $-\\frac{57}{70}$. Associative property verified.",
))

BATCH.append(q(1, 3,
    "Find the additive inverse of each of the following:\n\n(i) $-\\dfrac{7}{9}$\n\n(ii) $\\dfrac{5}{-11}$\n\n(iii) $-\\dfrac{3}{4} + \\dfrac{2}{5}$",
    "(i) $\\dfrac{7}{9}$ · (ii) $\\dfrac{5}{11}$ · (iii) $\\dfrac{7}{20}$",
    [
        {"rule": "Concept", "why": "Additive inverse of $x$ is $-x$ such that $x + (-x) = 0$.", "math": "x + (-x) = 0"},
        {"rule": "(i)", "why": "Change the sign.", "math": "\\text{Additive inverse of } -\\dfrac{7}{9} = \\dfrac{7}{9}"},
        {"rule": "(ii)", "why": "$\\frac{5}{-11} = -\\frac{5}{11}$; change sign.", "math": "\\dfrac{5}{11}"},
        {"rule": "(iii)", "why": "Simplify first: LCM of 4 and 5 is 20.", "math": "-\\dfrac{3}{4}+\\dfrac{2}{5} = -\\dfrac{7}{20};\\quad \\text{inverse} = \\dfrac{7}{20}"},
    ],
    "(i) $\\frac{7}{9}$ · (ii) $\\frac{5}{11}$ · (iii) $-\\frac{3}{4}+\\frac{2}{5}=-\\frac{7}{20}$ → inverse $\\frac{7}{20}$.",
))

BATCH.append(q(1, 4,
    "Represent the following on the number line:\n\n(i) $-\\dfrac{3}{4}$\n\n(ii) $\\dfrac{5}{3}$\n\n(iii) $-\\dfrac{7}{2}$",
    "(i) Between 0 and $-1$, 3rd mark left of 0 · (ii) $1\\dfrac{2}{3}$, 2nd mark after 1 · (iii) $-3\\dfrac{1}{2}$, halfway between $-3$ and $-4$",
    [
        {"rule": "(i) $-\\dfrac{3}{4}$", "why": "Between 0 and $-1$; divide into 4 equal parts; 3rd mark left of 0.", "math": "-1 < -\\dfrac{3}{4} < 0"},
        {"rule": "(ii) $\\dfrac{5}{3}$", "why": "$\\frac{5}{3} = 1\\frac{2}{3}$; between 1 and 2, divide into 3 parts; 2nd mark after 1.", "math": "1\\dfrac{2}{3}"},
        {"rule": "(iii) $-\\dfrac{7}{2}$", "why": "$-\\frac{7}{2} = -3\\frac{1}{2}$; exactly halfway between $-3$ and $-4$.", "math": "-3\\dfrac{1}{2}"},
    ],
    "(i) $-\\frac{3}{4}$ between 0 and $-1$ · (ii) $1\\frac{2}{3}$ · (iii) $-3\\frac{1}{2}$.",
))

BATCH.append(q(1, 5,
    "Simplify and verify the distributive property: $-\\dfrac{3}{5} \\times \\left(\\dfrac{2}{7} + \\left(-\\dfrac{1}{3}\\right)\\right)$.",
    "LHS $=$ RHS $= \\dfrac{1}{35}$. Distributive property verified.",
    [
        {"rule": "Concept", "why": "$a(b+c) = ab + ac$.", "math": "a \\times (b+c) = (a \\times b) + (a \\times c)"},
        {"rule": "LHS — bracket", "why": "LCM of 7 and 3 is 21.", "math": "\\dfrac{2}{7} - \\dfrac{1}{3} = \\dfrac{6-7}{21} = -\\dfrac{1}{21}"},
        {"rule": "LHS — multiply", "why": "Negative × Negative = Positive.", "math": "-\\dfrac{3}{5} \\times \\left(-\\dfrac{1}{21}\\right) = \\dfrac{3}{105} = \\dfrac{1}{35}"},
        {"rule": "RHS", "why": "Distribute and add; LCM of 35 and 5 is 35.", "math": "-\\dfrac{6}{35} + \\dfrac{1}{5} = \\dfrac{-6+7}{35} = \\dfrac{1}{35}"},
        {"rule": "Conclusion", "why": "LHS = RHS.", "math": "\\dfrac{1}{35} = \\dfrac{1}{35}\\; \\checkmark"},
    ],
    "LHS = RHS = $\\frac{1}{35}$. Distributive property verified.",
))

BATCH.append(q(1, 6,
    "A rational number is such that when we multiply it by $\\dfrac{5}{2}$ and add $\\dfrac{2}{3}$ to the product, we get $\\dfrac{17}{6}$. Find the rational number.",
    "The rational number is $\\dfrac{13}{15}$.",
    [
        {"rule": "Set up", "why": "Let the number be $x$.", "math": "x \\cdot \\dfrac{5}{2} + \\dfrac{2}{3} = \\dfrac{17}{6}"},
        {"rule": "Isolate $x$ term", "why": "Subtract $\\frac{2}{3}$ from both sides.", "math": "x \\cdot \\dfrac{5}{2} = \\dfrac{17}{6} - \\dfrac{4}{6} = \\dfrac{13}{6}"},
        {"rule": "Solve for $x$", "why": "Multiply both sides by $\\frac{2}{5}$.", "math": "x = \\dfrac{13}{6} \\times \\dfrac{2}{5} = \\dfrac{26}{30} = \\dfrac{13}{15}"},
    ],
    "$\\frac{5}{2}x + \\frac{2}{3} = \\frac{17}{6}$ → $x = \\frac{13}{15}$.",
))

BATCH.append(q(1, 7,
    "Find five rational numbers between $-\\dfrac{3}{5}$ and $\\dfrac{1}{2}$.",
    "Examples: $-\\dfrac{1}{2}$, $-\\dfrac{3}{10}$, $0$, $\\dfrac{1}{5}$, $\\dfrac{2}{5}$ (other valid answers exist)",
    [
        {"rule": "Equalise denominators", "why": "LCM of 5 and 2 is 10.", "math": "-\\dfrac{3}{5} = -\\dfrac{6}{10},\\quad \\dfrac{1}{2} = \\dfrac{5}{10}"},
        {"rule": "Identify integers between", "why": "Between $-6$ and $5$ on the numerator scale.", "math": "-5,\\; -4,\\; -3,\\; -2,\\; -1,\\; 0,\\; 1,\\; 2,\\; 3,\\; 4"},
        {"rule": "Pick any five", "why": "Convert back to simplified fractions.", "math": "-\\dfrac{5}{10},\\; -\\dfrac{3}{10},\\; 0,\\; \\dfrac{2}{10},\\; \\dfrac{4}{10} \\Rightarrow -\\dfrac{1}{2},\\; -\\dfrac{3}{10},\\; 0,\\; \\dfrac{1}{5},\\; \\dfrac{2}{5}"},
    ],
    "Equalise to tenths: $-\\frac{6}{10}$ to $\\frac{5}{10}$. Five examples: $-\\frac{1}{2}, -\\frac{3}{10}, 0, \\frac{1}{5}, \\frac{2}{5}$.",
))

BATCH.append(q(1, 8,
    "If $\\dfrac{a}{b} = \\dfrac{3}{5}$ and $\\dfrac{c}{d} = \\dfrac{7}{9}$, find $\\left(\\dfrac{a}{b} + \\dfrac{c}{d}\\right) \\times \\left(\\dfrac{a}{b} - \\dfrac{c}{d}\\right)$ and simplify.",
    "$-\\dfrac{496}{2025}$",
    [
        {"rule": "Identity", "why": "$(x+y)(x-y) = x^2 - y^2$.", "math": "\\left(\\dfrac{3}{5}+\\dfrac{7}{9}\\right)\\left(\\dfrac{3}{5}-\\dfrac{7}{9}\\right) = \\left(\\dfrac{3}{5}\\right)^2 - \\left(\\dfrac{7}{9}\\right)^2"},
        {"rule": "Square each fraction", "why": "Compute $\\frac{9}{25}$ and $\\frac{49}{81}$.", "math": "\\dfrac{9}{25} - \\dfrac{49}{81}"},
        {"rule": "Common denominator", "why": "LCM of 25 and 81 is 2025.", "math": "\\dfrac{9 \\times 81 - 49 \\times 25}{2025} = \\dfrac{729 - 1225}{2025} = -\\dfrac{496}{2025}"},
    ],
    "Difference of squares: $(\\frac{3}{5})^2 - (\\frac{7}{9})^2 = -\\frac{496}{2025}$.",
))

BATCH.append(q(1, 9,
    "The sum of two rational numbers is $-\\dfrac{5}{6}$. If one of the numbers is $\\dfrac{2}{3}$, find the other. Also verify the result.",
    "The other number is $-\\dfrac{3}{2}$.",
    [
        {"rule": "Set up", "why": "Let unknown be $x$.", "math": "x + \\dfrac{2}{3} = -\\dfrac{5}{6}"},
        {"rule": "Solve", "why": "LCM of 6 and 3 is 6.", "math": "x = -\\dfrac{5}{6} - \\dfrac{4}{6} = -\\dfrac{9}{6} = -\\dfrac{3}{2}"},
        {"rule": "Verify", "why": "Check the sum.", "math": "-\\dfrac{3}{2} + \\dfrac{2}{3} = -\\dfrac{9}{6} + \\dfrac{4}{6} = -\\dfrac{5}{6}\\; \\checkmark"},
    ],
    "$x + \\frac{2}{3} = -\\frac{5}{6}$ → $x = -\\frac{3}{2}$. Verified.",
))

# ── Chapter 2: Q10–18 ────────────────────────────────────────────────────────

BATCH.append(q(2, 1,
    "Simplify: $\\dfrac{a^3 \\cdot b^2 \\cdot c^4}{a^2 \\cdot b^3 \\cdot c}$ and express in simplest form.",
    "$\\dfrac{a c^3}{b}$",
    [
        {"rule": "Quotient law", "why": "$\\frac{x^m}{x^n} = x^{m-n}$.", "math": "\\dfrac{x^m}{x^n} = x^{m-n}"},
        {"rule": "Apply to each base", "why": "Subtract exponents for $a$, $b$, $c$.", "math": "a^{1} \\cdot b^{-1} \\cdot c^{3}"},
        {"rule": "Simplest form", "why": "Write negative exponent as reciprocal.", "math": "\\dfrac{a c^3}{b}"},
    ],
    "Quotient law: $\\frac{ac^3}{b}$.",
))

BATCH.append(q(2, 2,
    "If $2^5 \\cdot 3^4 \\cdot 5^2 = 2^m \\cdot 3^n \\cdot 5^p$, find $m$, $n$, $p$.",
    "$m = 5$, $n = 4$, $p = 2$",
    [
        {"rule": "Concept", "why": "By unique prime factorisation, exponents of matching bases must be equal.", "math": "2^5 \\cdot 3^4 \\cdot 5^2 = 2^m \\cdot 3^n \\cdot 5^p"},
        {"rule": "Compare exponents", "why": "Match each prime base.", "math": "m = 5,\\; n = 4,\\; p = 2"},
    ],
    "Unique prime factorisation → $m=5$, $n=4$, $p=2$.",
))

BATCH.append(q(2, 3,
    "Evaluate: $(3^0 + 4^0 + 5^0) \\times (2^{-3} + 3^{-2})$.",
    "$\\dfrac{17}{24}$",
    [
        {"rule": "Zero exponent", "why": "Any non-zero number to power 0 equals 1.", "math": "3^0 + 4^0 + 5^0 = 1 + 1 + 1 = 3"},
        {"rule": "Negative exponents", "why": "$x^{-n} = \\frac{1}{x^n}$.", "math": "2^{-3} + 3^{-2} = \\dfrac{1}{8} + \\dfrac{1}{9}"},
        {"rule": "Add fractions", "why": "LCM of 8 and 9 is 72.", "math": "3 \\times \\left(\\dfrac{9+8}{72}\\right) = 3 \\times \\dfrac{17}{72} = \\dfrac{17}{24}"},
    ],
    "$(1+1+1)(\\frac{1}{8}+\\frac{1}{9}) = 3 \\times \\frac{17}{72} = \\frac{17}{24}$.",
))

BATCH.append(q(2, 4,
    "Simplify and express with positive exponents: $\\dfrac{x^{-3} y^2}{x^2 y^{-4}} \\cdot (x y^{-1})$.",
    "$\\dfrac{y^5}{x^4}$",
    [
        {"rule": "Simplify fraction", "why": "Apply quotient law inside the fraction.", "math": "x^{-5} y^{6}"},
        {"rule": "Multiply", "why": "Add exponents when multiplying like bases.", "math": "x^{-4} y^{5}"},
        {"rule": "Positive exponents", "why": "Move negative exponents to denominator.", "math": "\\dfrac{y^5}{x^4}"},
    ],
    "Simplify → $x^{-4}y^5$ → $\\frac{y^5}{x^4}$.",
))

BATCH.append(q(2, 5,
    "Find the value of $x$ if: $\\dfrac{5^{x-1} \\cdot 3^{2x-3}}{15^{x-2}} = 1$.",
    "No integer solution for $x$ ($3^{x-1} = \\frac{1}{5}$). If denominator were $15^{x-1}$, then $x = 2$.",
    [
        {"rule": "Factorise 15", "why": "$15 = 5 \\times 3$.", "math": "15^{x-2} = 5^{x-2} \\cdot 3^{x-2}"},
        {"rule": "Quotient rule", "why": "Subtract exponents for each base.", "math": "5^{1} \\cdot 3^{x-1} = 1"},
        {"rule": "Analyse", "why": "$5 \\cdot 3^{x-1} = 1$ implies $3^{x-1} = \\frac{1}{5}$, which has no integer solution.", "math": "3^{x-1} = \\dfrac{1}{5}"},
    ],
    "$5 \\cdot 3^{x-1} = 1$ → no integer $x$. Note: if denominator were $15^{x-1}$, then $x=2$.",
))

BATCH.append(q(2, 6,
    "Express $0.00000000837$ in standard form (scientific notation).",
    "$8.37 \\times 10^{-9}$",
    [
        {"rule": "Concept", "why": "Standard form: $A \\times 10^n$ where $1 \\le A < 10$.", "math": "A \\times 10^n"},
        {"rule": "Shift decimal", "why": "Move decimal 9 places right to get 8.37.", "math": "8.37 \\times 10^{-9}"},
    ],
    "Move decimal 9 places → $8.37 \\times 10^{-9}$.",
))

BATCH.append(q(2, 7,
    "Simplify: $\\left[\\dfrac{a^{m+n}}{a^m}\\right]^n \\cdot \\left[\\dfrac{a^{n-p}}{a^n}\\right]^m$.",
    "$a^{n^2 - pm}$",
    [
        {"rule": "First bracket", "why": "Quotient then power rule: $(x^a)^b = x^{ab}$.", "math": "\\left[a^{(m+n)-m}\\right]^n = a^{n^2}"},
        {"rule": "Second bracket", "why": "Same rules.", "math": "\\left[a^{(n-p)-n}\\right]^m = a^{-pm}"},
        {"rule": "Multiply", "why": "Add exponents.", "math": "a^{n^2} \\cdot a^{-pm} = a^{n^2 - pm}"},
    ],
    "First bracket $a^{n^2}$, second $a^{-pm}$ → $a^{n^2-pm}$.",
))

BATCH.append(q(2, 8,
    "If $a = 2$, $b = 3$, evaluate: $\\dfrac{a^b + b^a}{a^{b-1} + b^{a-1}}$.",
    "$\\dfrac{17}{7}$",
    [
        {"rule": "Substitute", "why": "Replace $a=2$, $b=3$.", "math": "\\dfrac{2^3 + 3^2}{2^{2} + 3^{1}}"},
        {"rule": "Evaluate", "why": "Compute powers.", "math": "\\dfrac{8 + 9}{4 + 3} = \\dfrac{17}{7}"},
    ],
    "$\\frac{8+9}{4+3} = \\frac{17}{7}$.",
))

BATCH.append(q(2, 9,
    "Prove that $\\dfrac{a^m}{a^n} = a^{m-n}$ using laws of exponents (for positive integers $m > n$).",
    "Proved: cancelling $n$ factors of $a$ leaves $m-n$ factors.",
    [
        {"rule": "Definition", "why": "$a^m$ is $a$ multiplied $m$ times; $a^n$ is $a$ multiplied $n$ times.", "math": "a^m = \\underbrace{a \\cdot a \\cdots a}_{m \\text{ times}}"},
        {"rule": "Division", "why": "Since $m > n$, cancel $n$ factors of $a$ from numerator and denominator.", "math": "\\dfrac{a^m}{a^n} = \\underbrace{a \\cdot a \\cdots a}_{m-n \\text{ times}}"},
        {"rule": "Conclusion", "why": "Remaining product equals $a^{m-n}$.", "math": "a^{m-n}\\; \\checkmark"},
    ],
    "Cancel $n$ factors of $a$ → $a^{m-n}$. Proved.",
))

# ── Chapter 3: Q19–27 ────────────────────────────────────────────────────────

BATCH.append(q(3, 1,
    "Find the square of:\n\n(i) $0.07$\n\n(ii) $1.5$\n\n(iii) $\\dfrac{25}{36}$",
    "(i) $0.0049$ · (ii) $2.25$ · (iii) $\\dfrac{625}{1296}$",
    [
        {"rule": "(i)", "why": "$0.07 \\times 0.07$; 2 decimal places × 2 = 4.", "math": "0.0049"},
        {"rule": "(ii)", "why": "$1.5 \\times 1.5$.", "math": "2.25"},
        {"rule": "(iii)", "why": "Square numerator and denominator separately.", "math": "\\left(\\dfrac{25}{36}\\right)^2 = \\dfrac{625}{1296}"},
    ],
    "(i) 0.0049 · (ii) 2.25 · (iii) $\\frac{625}{1296}$.",
))

BATCH.append(q(3, 2,
    "Find the square root of $7921$ by prime factorisation method and verify by division method.",
    "$\\sqrt{7921} = 89$",
    [
        {"rule": "Prime factorisation", "why": "Test primes; $7921 = 89 \\times 89$.", "math": "\\sqrt{7921} = 89"},
        {"rule": "Division method", "why": "Pair digits: $\\overline{79}\\,\\overline{21}$. Largest square $\\le 79$ is $64=8^2$.", "math": "8^2 = 64;\\; \\text{remainder } 15;\\; \\text{bring down } 21 \\Rightarrow 1521"},
        {"rule": "Verify", "why": "$169 \\times 9 = 1521$; remainder 0.", "math": "89\\; \\checkmark"},
    ],
    "Prime factorisation and long division both give $\\sqrt{7921} = 89$.",
))

BATCH.append(q(3, 3,
    "The area of a square field is $5184\\,\\text{m}^2$. Find the length of its side and perimeter.",
    "Side $= 72\\,\\text{m}$; Perimeter $= 288\\,\\text{m}$",
    [
        {"rule": "Side length", "why": "Side $= \\sqrt{5184}$. Long division: $\\overline{51}\\,\\overline{84}$.", "math": "\\sqrt{5184} = 72\\,\\text{m}"},
        {"rule": "Perimeter", "why": "Perimeter $= 4 \\times$ side.", "math": "4 \\times 72 = 288\\,\\text{m}"},
    ],
    "Side = 72 m; perimeter = 288 m.",
))

BATCH.append(q(3, 4,
    "Find the smallest number by which $2592$ must be multiplied so that the product is a perfect square.",
    "$2$",
    [
        {"rule": "Prime factorise", "why": "Break 2592 into prime powers.", "math": "2592 = 2^5 \\cdot 3^4"},
        {"rule": "Pair factors", "why": "Perfect square needs even powers for every prime.", "math": "2^5 \\text{ has one unpaired } 2"},
        {"rule": "Answer", "why": "Multiply by 2 to make $2^6$.", "math": "2"},
    ],
    "$2592 = 2^5 \\cdot 3^4$ → multiply by 2.",
))

BATCH.append(q(3, 5,
    "Find the square root of $0.00059049$.",
    "$0.0243$",
    [
        {"rule": "Rewrite", "why": "Express as fraction over power of 10.", "math": "0.00059049 = \\dfrac{59049}{10^8}"},
        {"rule": "Numerator root", "why": "$\\sqrt{59049} = 243$.", "math": "243"},
        {"rule": "Result", "why": "Divide by $10^4$.", "math": "\\dfrac{243}{10000} = 0.0243"},
    ],
    "$\\sqrt{59049}/10^4 = 0.0243$.",
))

BATCH.append(q(3, 6,
    "Evaluate: $\\sqrt{0.09} + \\sqrt{0.0064} - \\sqrt{0.0004}$ and simplify.",
    "$0.36$",
    [
        {"rule": "Each root", "why": "Square root halves decimal places for perfect squares.", "math": "\\sqrt{0.09}=0.3,\\; \\sqrt{0.0064}=0.08,\\; \\sqrt{0.0004}=0.02"},
        {"rule": "Calculate", "why": "Add and subtract.", "math": "0.3 + 0.08 - 0.02 = 0.36"},
    ],
    "$0.3 + 0.08 - 0.02 = 0.36$.",
))

BATCH.append(q(3, 7,
    "A gardener wants to plant $2025$ trees in his garden so that the number of trees in each row equals the number of rows. Find the number of rows.",
    "$45$ rows",
    [
        {"rule": "Set up", "why": "If rows $=$ trees per row $= x$, then $x^2 = 2025$.", "math": "x^2 = 2025"},
        {"rule": "Square root", "why": "Ends in 25 → root ends in 5; $\\sqrt{2025} = 45$.", "math": "x = 45"},
    ],
    "$x^2 = 2025$ → $x = 45$ rows.",
))

BATCH.append(q(3, 8,
    "Find the value of $\\sqrt{3 + 2\\sqrt{2}} + \\sqrt{3 - 2\\sqrt{2}}$.",
    "$2\\sqrt{2}$",
    [
        {"rule": "Perfect squares", "why": "$3 + 2\\sqrt{2} = (\\sqrt{2}+1)^2$ and $3 - 2\\sqrt{2} = (\\sqrt{2}-1)^2$.", "math": "(\\sqrt{2}+1)^2,\\; (\\sqrt{2}-1)^2"},
        {"rule": "Simplify", "why": "Take square roots and add.", "math": "(\\sqrt{2}+1) + (\\sqrt{2}-1) = 2\\sqrt{2}"},
    ],
    "$(\\sqrt{2}+1) + (\\sqrt{2}-1) = 2\\sqrt{2}$.",
))

BATCH.append(q(3, 9,
    "Using an algebraic identity, find $(98)^2$ without actual multiplication.",
    "$9604$",
    [
        {"rule": "Identity", "why": "Use $(a-b)^2 = a^2 - 2ab + b^2$ with $a=100$, $b=2$.", "math": "(100-2)^2"},
        {"rule": "Expand", "why": "Substitute and compute.", "math": "10000 - 400 + 4 = 9604"},
    ],
    "$(100-2)^2 = 10000 - 400 + 4 = 9604$.",
))

# ── Chapter 4: Q28–35 ────────────────────────────────────────────────────────

BATCH.append(q(4, 1,
    "Find the cube of:\n\n(i) $-7$\n\n(ii) $2.5$\n\n(iii) $\\dfrac{5}{6}$",
    "(i) $-343$ · (ii) $15.625$ · (iii) $\\dfrac{125}{216}$",
    [
        {"rule": "(i)", "why": "Negative × negative × negative = negative.", "math": "(-7)^3 = -343"},
        {"rule": "(ii)", "why": "$2.5 \\times 2.5 \\times 2.5$.", "math": "15.625"},
        {"rule": "(iii)", "why": "Cube numerator and denominator.", "math": "\\left(\\dfrac{5}{6}\\right)^3 = \\dfrac{125}{216}"},
    ],
    "(i) $-343$ · (ii) 15.625 · (iii) $\\frac{125}{216}$.",
))

BATCH.append(q(4, 2,
    "Find the cube root of $17576$ by prime factorisation method.",
    "$26$",
    [
        {"rule": "Factorise", "why": "Divide repeatedly by 2, then recognise $13^3$.", "math": "17576 = 2^3 \\cdot 13^3"},
        {"rule": "Cube root", "why": "Take one factor from each group of three.", "math": "2 \\times 13 = 26"},
    ],
    "$17576 = 2^3 \\cdot 13^3$ → $\\sqrt[3]{17576} = 26$.",
))

BATCH.append(q(4, 3,
    "Find the smallest number by which $8788$ must be divided so that the quotient is a perfect cube.",
    "$4$",
    [
        {"rule": "Factorise", "why": "$8788 = 2^2 \\cdot 13^3$.", "math": "2^2 \\cdot 13^3"},
        {"rule": "Identify unpaired factor", "why": "$13^3$ forms a complete group; $2^2$ does not.", "math": "\\text{Divide by } 2^2 = 4"},
    ],
    "$8788 = 2^2 \\cdot 13^3$ → divide by 4.",
))

BATCH.append(q(4, 4,
    "The volume of a cube is $216\\,\\text{cm}^3$. Find its edge and total surface area.",
    "Edge $= 6\\,\\text{cm}$; TSA $= 216\\,\\text{cm}^2$",
    [
        {"rule": "Edge", "why": "Volume $= \\text{edge}^3$.", "math": "\\sqrt[3]{216} = 6\\,\\text{cm}"},
        {"rule": "TSA", "why": "TSA $= 6 \\times \\text{edge}^2$.", "math": "6 \\times 36 = 216\\,\\text{cm}^2"},
    ],
    "Edge = 6 cm; TSA = 216 cm².",
))

BATCH.append(q(4, 5,
    "Evaluate: $\\sqrt[3]{0.000216} + \\sqrt[3]{0.000008} - \\sqrt[3]{0.000001}$.",
    "$0.07$",
    [
        {"rule": "Each cube root", "why": "Cube root reduces decimal places by a factor of 3.", "math": "0.06 + 0.02 - 0.01"},
        {"rule": "Calculate", "why": "Add and subtract.", "math": "0.07"},
    ],
    "$0.06 + 0.02 - 0.01 = 0.07$.",
))

BATCH.append(q(4, 6,
    "Find the cube root of $13824$.",
    "$24$",
    [
        {"rule": "Group digits", "why": "Group in threes from the right: $\\overline{13}\\,\\overline{824}$.", "math": "\\overline{13}\\,\\overline{824}"},
        {"rule": "Units digit", "why": "824 ends in 4; only $4^3=64$ ends in 4 → units digit 4.", "math": "\\text{units digit } 4"},
        {"rule": "Tens digit", "why": "$2^3=8 \\le 13 < 27=3^3$ → tens digit 2.", "math": "\\sqrt[3]{13824} = 24"},
    ],
    "Estimation: groups $\\overline{13}\\,\\overline{824}$ → cube root 24.",
))

BATCH.append(q(4, 7,
    "If $\\sqrt[3]{a/b} = \\dfrac{5}{6}$, find $a/b$ and $a + b$.",
    "$a/b = \\dfrac{125}{216}$; $a + b = 341$",
    [
        {"rule": "Cube both sides", "why": "Reverse the cube root.", "math": "\\dfrac{a}{b} = \\left(\\dfrac{5}{6}\\right)^3 = \\dfrac{125}{216}"},
        {"rule": "Sum", "why": "If $a=125$, $b=216$ in simplest form.", "math": "a + b = 125 + 216 = 341"},
    ],
    "$a/b = \\frac{125}{216}$; $a+b = 341$.",
))

BATCH.append(q(4, 8,
    "Find the cube root of $42875$.",
    "$35$",
    [
        {"rule": "Group digits", "why": "$\\overline{42}\\,\\overline{875}$.", "math": "\\overline{42}\\,\\overline{875}"},
        {"rule": "Units digit", "why": "875 ends in 5; only cubes ending in 5 come from numbers ending in 5.", "math": "\\text{units digit } 5"},
        {"rule": "Tens digit", "why": "$3^3=27 < 42 < 64=4^3$ → tens digit 3.", "math": "\\sqrt[3]{42875} = 35"},
    ],
    "Grouping method → cube root 35.",
))

# ── Chapter 5: Q36–40 ────────────────────────────────────────────────────────

BATCH.append(q(5, 1,
    "Find the value of $A$ and $B$ if the number $5A3B$ is divisible by $99$ (use divisibility rules).",
    "No valid single-digit pair $(A, B)$ exists (conditions for 9 and 11 contradict).",
    [
        {"rule": "Divisibility by 11", "why": "Alternating sum: $(A+B) - 8$ must be 0 or $\\pm 11$.", "math": "A + B = 8"},
        {"rule": "Divisibility by 9", "why": "Sum of digits $= 8 + (A+B) = 16$.", "math": "16 \\text{ is not divisible by } 9"},
        {"rule": "Conclusion", "why": "The two rules contradict — no solution.", "math": "\\text{No valid } (A, B)"},
    ],
    "Rule for 11 → $A+B=8$; rule for 9 → sum = 16 (not divisible by 9). No solution.",
))

BATCH.append(q(5, 2,
    "A number is formed by two digits. The sum of its digits is $9$. If $27$ is added to the number, the digits are reversed. Find the number.",
    "$36$",
    [
        {"rule": "Algebraic form", "why": "Two-digit number: $10x + y$.", "math": "x + y = 9"},
        {"rule": "Reversal condition", "why": "$(10x+y)+27 = 10y+x$.", "math": "9y - 9x = 27 \\Rightarrow y - x = 3"},
        {"rule": "Solve", "why": "Add equations: $2y=12$.", "math": "y=6,\\; x=3 \\Rightarrow 36"},
    ],
    "$x+y=9$, $y-x=3$ → number 36.",
))

BATCH.append(q(5, 3,
    "Using the generalised form, prove that a number is divisible by $9$ if the sum of its digits is divisible by $9$.",
    "Proved.",
    [
        {"rule": "Generalised form", "why": "4-digit number $abcd = 1000a + 100b + 10c + d$.", "math": "abcd = 1000a + 100b + 10c + d"},
        {"rule": "Rewrite", "why": "Express as multiples of 9 plus digit sum.", "math": "= 9(111a + 11b + c) + (a+b+c+d)"},
        {"rule": "Conclusion", "why": "First part is a multiple of 9; divisibility depends on digit sum.", "math": "\\text{Divisible by 9 iff } (a+b+c+d) \\text{ is divisible by 9}"},
    ],
    "$abcd = 9(111a+11b+c) + (a+b+c+d)$. Proved.",
))

BATCH.append(q(5, 4,
    "Find the missing digits in: $\\_\\,4\\,\\_\\,5\\,\\_$ is divisible by $11$ (use alternating sum rule).",
    "Example: $24453$ (any digits with $A+B+C=9$, $A \\neq 0$)",
    [
        {"rule": "Alternating sum", "why": "Odd positions: $A, B, C$. Even positions: $4, 5$.", "math": "(A+B+C) - 9 = 0 \\text{ or } 11"},
        {"rule": "Condition", "why": "Since $A,B,C$ are single digits, $A+B+C = 9$.", "math": "A + B + C = 9"},
        {"rule": "Example", "why": "Let $A=2, B=4, C=3$.", "math": "24453"},
    ],
    "$A+B+C=9$. Example: 24453.",
))

BATCH.append(q(5, 5,
    "A three-digit number $4ab$ is divisible by $3$ and $11$. If $a + b = 6$, find $a$ and $b$.",
    "No solution ($a+b=6$ forces digit sum $10$, not divisible by 3).",
    [
        {"rule": "Divisibility by 3", "why": "Sum of digits $= 4 + a + b = 4 + 6 = 10$.", "math": "10 \\text{ is not divisible by } 3"},
        {"rule": "Conclusion", "why": "Given $a+b=6$ contradicts divisibility by 3.", "math": "\\text{No valid } (a, b)"},
    ],
    "Digit sum = 10 (not divisible by 3). Impossible with $a+b=6$.",
))


def merge_chapter(ch: int, new_questions: list):
    path = DATA / f"chapter_{ch:02d}_practice_session.json"
    if path.exists():
        data = json.loads(path.read_text())
        existing = data.get("questions", [])
        existing_ids = {q["id"] for q in existing}
        for nq in new_questions:
            if nq["id"] not in existing_ids:
                existing.append(nq)
        questions = existing
        title = data.get("title", f"{META[ch][2]} · Practice Session")
        if "Batch 1" not in title:
            title = f"{META[ch][2]} · Test Paper & Batch 1"
    else:
        questions = new_questions
        title = f"{META[ch][2]} · Batch 1"

    out = {
        "title": title,
        "chapter": ch,
        "count": len(questions),
        "questions": questions,
    }
    path.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
    return len(new_questions), len(questions)


def main():
    by_ch = {i: [] for i in range(1, 6)}
    for item in BATCH:
        by_ch[item["chapter"]].append(item)

    for ch in range(1, 6):
        added, total = merge_chapter(ch, by_ch[ch])
        print(f"Chapter {ch}: added {added} batch questions (total {total})")


if __name__ == "__main__":
    main()
