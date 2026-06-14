#!/usr/bin/env python3
"""Add Batch 3 detailed solutions (Q79–118) to chapter practice session files."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "chapters"

META = {
    9: ("math-ch9", "CH09-sec-direct-and-inverse-variation", "Direct and Inverse Variation"),
    10: ("math-ch10", "CH10-sec-algebraic-expressions-and-identities", "Algebraic Expressions and Identities"),
    11: ("math-ch11", "CH11-sec-factorisation", "Factorisation"),
    12: ("math-ch12", "CH12-sec-linear-equations-and-inequalities-in-one-variabl", "Linear Equations and Inequalities"),
}


def q(ch, num, question, answer, steps, explanation, note_id=None):
    topic, default_note, _ = META[ch]
    return {
        "id": f"Q-CH{ch:02d}-B03-{num:03d}",
        "chapter": ch,
        "topicId": topic,
        "type": "practice",
        "subtopic": "Batch 3 · Detailed Solutions",
        "question": question,
        "answer": answer,
        "options": [],
        "glassboxSteps": steps,
        "explanation": explanation,
        "linked_note_id": note_id or default_note,
        "source": "practice-session",
    }


BATCH = []

# ── Chapter 9: Q79–86 (Direct & Inverse Variation) ───────────────────────────

BATCH.append(q(9, 1,
    "If $x$ varies directly as $y$ and $x = 12$ when $y = 4$, find $x$ when $y = 15$.",
    "$x = 45$",
    [
        {"rule": "Concept", "why": "Direct variation: $\\frac{x_1}{y_1} = \\frac{x_2}{y_2}$.", "math": "\\dfrac{12}{4} = \\dfrac{x}{15}"},
        {"rule": "Solve", "why": "Simplify and cross-multiply.", "math": "3 = \\dfrac{x}{15} \\Rightarrow x = 45"},
    ],
    "$\\frac{12}{4} = \\frac{x}{15}$ → $x = 45$.",
))

BATCH.append(q(9, 2,
    "If $10$ men can complete a work in $12$ days, how many men are required to complete the same work in $8$ days?",
    "$15$ men",
    [
        {"rule": "Concept", "why": "Inverse variation: $m_1 d_1 = m_2 d_2$.", "math": "10 \\times 12 = m_2 \\times 8"},
        {"rule": "Solve", "why": "Divide.", "math": "120 = 8 m_2 \\Rightarrow m_2 = 15"},
    ],
    "$10 \\times 12 = 8 m_2$ → 15 men.",
))

BATCH.append(q(9, 3,
    "A car travels $360$ km in $5$ hours. How much distance will it travel in $7$ hours at the same speed?",
    "$504$ km",
    [
        {"rule": "Speed", "why": "Direct variation of distance and time.", "math": "\\dfrac{360}{5} = 72 \\text{ km/h}"},
        {"rule": "Distance", "why": "Multiply speed by 7 hours.", "math": "72 \\times 7 = 504 \\text{ km}"},
    ],
    "Speed 72 km/h → 504 km in 7 h.",
))

BATCH.append(q(9, 4,
    "If $15$ pipes of the same diameter can fill a tank in $36$ minutes, how many pipes are needed to fill it in $20$ minutes?",
    "$27$ pipes",
    [
        {"rule": "Concept", "why": "Inverse variation: $p_1 t_1 = p_2 t_2$.", "math": "15 \\times 36 = p_2 \\times 20"},
        {"rule": "Solve", "why": "540 = 20 $p_2$.", "math": "p_2 = 27"},
    ],
    "$15 \\times 36 = 20 p_2$ → 27 pipes.",
))

BATCH.append(q(9, 5,
    "$x$ varies inversely as $y$. When $x = 15$, $y = 4$. Find $y$ when $x = 20$.",
    "$y = 3$",
    [
        {"rule": "Constant", "why": "$xy = k$.", "math": "k = 15 \\times 4 = 60"},
        {"rule": "Solve", "why": "Substitute $x = 20$.", "math": "20y = 60 \\Rightarrow y = 3"},
    ],
    "$k = 60$ → $y = 3$ when $x = 20$.",
))

BATCH.append(q(9, 6,
    "A garrison of $500$ men had provisions for $24$ days. A reinforcement of $100$ men arrived. For how many days will the food last now?",
    "$20$ days",
    [
        {"rule": "Total man-days", "why": "Food fixed.", "math": "500 \\times 24 = 12000"},
        {"rule": "New days", "why": "600 men share the same total.", "math": "600 \\times d = 12000 \\Rightarrow d = 20"},
    ],
    "12000 man-days ÷ 600 men = 20 days.",
))

BATCH.append(q(9, 7,
    "The cost of $5$ kg potatoes is ₹$75$. Find the cost of $8$ kg. Also: with a fixed budget of ₹$75$, if price rises from ₹$15$/kg to ₹$25$/kg, how many kg can be bought?",
    "₹$120$ for 8 kg; $3$ kg at ₹$25$/kg with fixed ₹$75$ budget",
    [
        {"rule": "Direct (cost vs kg)", "why": "Cost per kg = 75/5.", "math": "15 \\times 8 = 120"},
        {"rule": "Inverse (budget fixed)", "why": "Quantity × price = constant budget.", "math": "75 / 25 = 3 \\text{ kg}"},
    ],
    "8 kg costs ₹120; at ₹25/kg, ₹75 buys 3 kg.",
))

BATCH.append(q(9, 8,
    "$6$ men or $10$ women can finish a piece of work in $24$ days. In how many days will $12$ men and $15$ women finish the work?",
    "$6\\dfrac{6}{7}$ days",
    [
        {"rule": "Convert to women", "why": "$6$ men $= 10$ women → $1$ man $= \\frac{5}{3}$ women.", "math": "12 \\text{ men} = 20 \\text{ women}"},
        {"rule": "Total workforce", "why": "20 + 15 = 35 women.", "math": "35 \\text{ women}"},
        {"rule": "Inverse variation", "why": "$10 \\times 24 = 35 \\times d$.", "math": "d = \\dfrac{240}{35} = \\dfrac{48}{7} = 6\\dfrac{6}{7}"},
    ],
    "35 women-equivalent → $\\frac{48}{7}$ days.",
))

# ── Chapter 10: Q87–95 (Algebraic Expressions) ───────────────────────────────

BATCH.append(q(10, 1,
    "Add: $3x^2 - 5xy + 7y^2$, $-2x^2 + 4xy - y^2$, and $5x^2 - 3xy + 2y^2$.",
    "$6x^2 - 4xy + 8y^2$",
    [
        {"rule": "$x^2$ terms", "why": "Combine coefficients.", "math": "(3-2+5)x^2 = 6x^2"},
        {"rule": "$xy$ terms", "why": "Combine.", "math": "(-5+4-3)xy = -4xy"},
        {"rule": "$y^2$ terms", "why": "Combine.", "math": "(7-1+2)y^2 = 8y^2"},
    ],
    "Sum: $6x^2 - 4xy + 8y^2$.",
))

BATCH.append(q(10, 2,
    "Subtract $(4a^2 - 3ab + 5b^2)$ from $(7a^2 + 2ab - 3b^2)$.",
    "$3a^2 + 5ab - 8b^2$",
    [
        {"rule": "Distribute minus", "why": "Change signs of subtrahend.", "math": "7a^2+2ab-3b^2-4a^2+3ab-5b^2"},
        {"rule": "Combine", "why": "Like terms.", "math": "3a^2+5ab-8b^2"},
    ],
    "$(7a^2+2ab-3b^2)-(4a^2-3ab+5b^2) = 3a^2+5ab-8b^2$.",
))

BATCH.append(q(10, 3,
    "Multiply: $(3x - 4y + 5)$ by $(2x + y - 3)$.",
    "$6x^2 - 5xy - 4y^2 + x + 17y - 15$",
    [
        {"rule": "Distribute", "why": "Multiply each term of first by each of second.", "math": "6x^2+3xy-9x-8xy-4y^2+12y+10x+5y-15"},
        {"rule": "Combine", "why": "Group like terms.", "math": "6x^2-5xy-4y^2+x+17y-15"},
    ],
    "Expanded and simplified to $6x^2 - 5xy - 4y^2 + x + 17y - 15$.",
))

BATCH.append(q(10, 4,
    "Divide: $12x^3 - 8x^2 + 6x$ by $2x$.",
    "$6x^2 - 4x + 3$",
    [
        {"rule": "Term-wise division", "why": "Divide each term by $2x$.", "math": "\\dfrac{12x^3}{2x}-\\dfrac{8x^2}{2x}+\\dfrac{6x}{2x}"},
        {"rule": "Simplify", "why": "Exponent rules.", "math": "6x^2-4x+3"},
    ],
    "$(12x^3-8x^2+6x) \\div 2x = 6x^2-4x+3$.",
))

BATCH.append(q(10, 5,
    "Simplify: $(3a + 2b)^2 - (3a - 2b)^2$.",
    "$24ab$",
    [
        {"rule": "Identity", "why": "$(x+y)^2-(x-y)^2 = 4xy$.", "math": "4(3a)(2b)"},
        {"rule": "Result", "why": "Multiply.", "math": "24ab"},
    ],
    "Identity → $24ab$.",
))

BATCH.append(q(10, 6,
    "If $x + y = 7$ and $xy = 12$, find $x^2 + y^2$ and $x^3 + y^3$.",
    "$x^2+y^2=25$; $x^3+y^3=91$",
    [
        {"rule": "$x^2+y^2$", "why": "$(x+y)^2-2xy$.", "math": "49-24=25"},
        {"rule": "$x^3+y^3$", "why": "$(x+y)(x^2+y^2-xy)$.", "math": "7(25-12)=91"},
    ],
    "$x^2+y^2=25$; $x^3+y^3=91$.",
))

BATCH.append(q(10, 7,
    "From the sum of $3a - 2b + 4c$ and $-5a + 6b - 2c$, subtract $2a - 3b + c$.",
    "$-4a + 7b + c$",
    [
        {"rule": "Sum first", "why": "Add the first two expressions.", "math": "-2a+4b+2c"},
        {"rule": "Subtract", "why": "Distribute minus sign.", "math": "-2a+4b+2c-2a+3b-c=-4a+7b+c"},
    ],
    "Result: $-4a+7b+c$.",
))

BATCH.append(q(10, 8,
    "Find the value of $2x^2 - 3xy + 5y^2$ when $x = -2$, $y = 3$.",
    "$71$",
    [
        {"rule": "Substitute", "why": "Replace $x$ and $y$.", "math": "2(-2)^2-3(-2)(3)+5(3)^2"},
        {"rule": "Evaluate", "why": "Order of operations.", "math": "8+18+45=71"},
    ],
    "Substitution gives 71.",
))

BATCH.append(q(10, 9,
    "Factor out common terms: $4x^2y - 8xy^2 + 12x^3y$.",
    "$4xy(x - 2y + 3x^2)$",
    [
        {"rule": "GCF", "why": "Coefficients GCD 4; lowest powers $x^1 y^1$.", "math": "4xy"},
        {"rule": "Factor", "why": "Divide each term by GCF.", "math": "4xy(x-2y+3x^2)"},
    ],
    "GCF $4xy$ → $4xy(x-2y+3x^2)$.",
))

# ── Chapter 10: Q96–104 (Algebraic Identities) ───────────────────────────────

BATCH.append(q(10, 10,
    "Using an identity, find $(98)^2$ without actual multiplication.",
    "$9604$",
    [
        {"rule": "Identity", "why": "$(a-b)^2 = a^2-2ab+b^2$ with $a=100$, $b=2$.", "math": "(100-2)^2"},
        {"rule": "Evaluate", "why": "Compute.", "math": "10000-400+4=9604"},
    ],
    "$(100-2)^2 = 9604$.",
))

BATCH.append(q(10, 11,
    "Expand using identities: $(2x + 3y + 4z)^2$.",
    "$4x^2 + 9y^2 + 16z^2 + 12xy + 24yz + 16zx$",
    [
        {"rule": "Identity", "why": "$(a+b+c)^2 = a^2+b^2+c^2+2ab+2bc+2ca$.", "math": "(2x)^2+(3y)^2+(4z)^2+2(2x)(3y)+2(3y)(4z)+2(4z)(2x)"},
        {"rule": "Result", "why": "Simplify.", "math": "4x^2+9y^2+16z^2+12xy+24yz+16zx"},
    ],
    "Expanded: $4x^2+9y^2+16z^2+12xy+24yz+16zx$.",
))

BATCH.append(q(10, 12,
    "If $a + b = 5$ and $ab = 6$, find $a^2 + b^2$ and $a^3 + b^3$.",
    "$a^2+b^2=13$; $a^3+b^3=35$",
    [
        {"rule": "$a^2+b^2$", "why": "$(a+b)^2-2ab$.", "math": "25-12=13"},
        {"rule": "$a^3+b^3$", "why": "$(a+b)(a^2+b^2-ab)$.", "math": "5(13-6)=35"},
    ],
    "$a^2+b^2=13$; $a^3+b^3=35$.",
))

BATCH.append(q(10, 13,
    "Factorise using identity: $x^2 + 10x + 25 - 9y^2$.",
    "$(x + 5 + 3y)(x + 5 - 3y)$",
    [
        {"rule": "Perfect square", "why": "Group first three terms.", "math": "(x+5)^2-(3y)^2"},
        {"rule": "Difference of squares", "why": "$A^2-B^2=(A-B)(A+B)$.", "math": "(x+5+3y)(x+5-3y)"},
    ],
    "$(x+5)^2-(3y)^2$ → $(x+5+3y)(x+5-3y)$.",
))

BATCH.append(q(10, 14,
    "Evaluate $(103)^3$ using the identity $(a+b)^3$.",
    "$1092727$",
    [
        {"rule": "Set $a=100$, $b=3$", "why": "$(a+b)^3 = a^3+3a^2b+3ab^2+b^3$.", "math": "1000000+30000+2700+27"},
        {"rule": "Add", "why": "Combine.", "math": "1092727"},
    ],
    "$(100+3)^3 = 1092727$.",
))

BATCH.append(q(10, 15,
    "Prove: $(a + b + c)^2 = a^2 + b^2 + c^2 + 2ab + 2bc + 2ca$ by expansion.",
    "Proved.",
    [
        {"rule": "Group", "why": "Let $X=a+b$, $Y=c$.", "math": "((a+b)+c)^2=(a+b)^2+2(a+b)c+c^2"},
        {"rule": "Expand", "why": "Expand $(a+b)^2$.", "math": "a^2+2ab+b^2+2ac+2bc+c^2"},
        {"rule": "Conclusion", "why": "Rearrange.", "math": "a^2+b^2+c^2+2ab+2bc+2ca\\; \\checkmark"},
    ],
    "Expand and rearrange → identity proved.",
))

BATCH.append(q(10, 16,
    "If $x - \\dfrac{1}{x} = 3$, find $x^2 + \\dfrac{1}{x^2}$ and $x^3 - \\dfrac{1}{x^3}$.",
    "$x^2+\\dfrac{1}{x^2}=11$; $x^3-\\dfrac{1}{x^3}=36$",
    [
        {"rule": "Square", "why": "$(x-1/x)^2 = x^2-2+1/x^2$.", "math": "x^2+1/x^2=11"},
        {"rule": "Cube", "why": "$(x-1/x)^3 = x^3-1/x^3-3(x-1/x)$.", "math": "27=x^3-1/x^3-9 \\Rightarrow x^3-1/x^3=36"},
    ],
    "$x^2+1/x^2=11$; $x^3-1/x^3=36$.",
))

BATCH.append(q(10, 17,
    "Using identity, simplify: $\\left(x + \\dfrac{1}{x}\\right)^2 - \\left(x - \\dfrac{1}{x}\\right)^2$.",
    "$4$",
    [
        {"rule": "Identity", "why": "$(A+B)^2-(A-B)^2=4AB$.", "math": "4(x)(1/x)=4"},
    ],
    "Identity → 4.",
))

BATCH.append(q(10, 18,
    "Find $(a + b)^3 - (a - b)^3$ and simplify.",
    "$2b(3a^2 + b^2)$",
    [
        {"rule": "Expand both", "why": "Use cube identities.", "math": "(a^3+3a^2b+3ab^2+b^3)-(a^3-3a^2b+3ab^2-b^3)"},
        {"rule": "Simplify", "why": "Cancel terms.", "math": "6a^2b+2b^3=2b(3a^2+b^2)"},
    ],
    "Difference = $2b(3a^2+b^2)$.",
))

# ── Chapter 11: Q105–113 (Factorisation) ─────────────────────────────────────

BATCH.append(q(11, 1,
    "Factorise completely: $12x^2y - 18xy^2 + 6xy$.",
    "$6xy(2x - 3y + 1)$",
    [
        {"rule": "GCF", "why": "GCD 6; shared $xy$.", "math": "6xy"},
        {"rule": "Factor", "why": "Divide each term.", "math": "6xy(2x-3y+1)"},
    ],
    "GCF $6xy$ → $6xy(2x-3y+1)$.",
))

BATCH.append(q(11, 2,
    "Factorise: $x^2 + 5x + 6$ and verify by expansion.",
    "$(x+2)(x+3)$",
    [
        {"rule": "Split middle term", "why": "Numbers multiplying to 6, adding to 5.", "math": "2,\\; 3"},
        {"rule": "Factor", "why": "Group.", "math": "(x+2)(x+3)"},
        {"rule": "Verify", "why": "Expand.", "math": "x^2+5x+6\\; \\checkmark"},
    ],
    "$(x+2)(x+3)$; verified.",
))

BATCH.append(q(11, 3,
    "Factorise by grouping: $ax + bx + ay + by$.",
    "$(a+b)(x+y)$",
    [
        {"rule": "Group", "why": "Pair terms.", "math": "(ax+bx)+(ay+by)"},
        {"rule": "Factor", "why": "Common binomial.", "math": "(a+b)(x+y)"},
    ],
    "$(a+b)(x+y)$.",
))

BATCH.append(q(11, 4,
    "Factorise: $4x^2 + 12xy + 9y^2 - 9$ (adjusted from likely typo $4x^2-9y^2+12xy-9$).",
    "$(2x+3y-3)(2x+3y+3)$",
    [
        {"rule": "Perfect square", "why": "Group as trinomial minus 9.", "math": "(2x+3y)^2-3^2"},
        {"rule": "Difference of squares", "why": "$A^2-B^2$.", "math": "(2x+3y-3)(2x+3y+3)"},
    ],
    "Assuming $4x^2+12xy+9y^2-9$ → $(2x+3y\\pm 3)$.",
))

BATCH.append(q(11, 5,
    "Factorise: $x^3 + 8$ (sum of cubes).",
    "$(x+2)(x^2-2x+4)$",
    [
        {"rule": "Identity", "why": "$a^3+b^3=(a+b)(a^2-ab+b^2)$.", "math": "x^3+2^3"},
        {"rule": "Apply", "why": "Substitute.", "math": "(x+2)(x^2-2x+4)"},
    ],
    "$x^3+8=(x+2)(x^2-2x+4)$.",
))

BATCH.append(q(11, 6,
    "Factorise the quadratic: $x^2 - 7x + 12$.",
    "$(x-3)(x-4)$",
    [
        {"rule": "Split", "why": "Product 12, sum $-7$.", "math": "-3,\\; -4"},
        {"rule": "Factor", "why": "Write binomials.", "math": "(x-3)(x-4)"},
    ],
    "$(x-3)(x-4)$.",
))

BATCH.append(q(11, 7,
    "Factorise: $2x^2 + 7x + 6$.",
    "$(x+2)(2x+3)$",
    [
        {"rule": "Split middle", "why": "$ac=12$, sum 7 → 3 and 4.", "math": "2x^2+4x+3x+6"},
        {"rule": "Group", "why": "Factor pairs.", "math": "(x+2)(2x+3)"},
    ],
    "$(x+2)(2x+3)$.",
))

BATCH.append(q(11, 8,
    "Resolve into factors: $a^3 - b^3 - a + b$.",
    "$(a-b)(a^2+ab+b^2-1)$",
    [
        {"rule": "Group", "why": "Cubes and linear terms.", "math": "(a^3-b^3)-(a-b)"},
        {"rule": "Factor", "why": "Common $(a-b)$.", "math": "(a-b)(a^2+ab+b^2-1)"},
    ],
    "$(a-b)(a^2+ab+b^2-1)$.",
))

BATCH.append(q(11, 9,
    "Factorise: (i) $(x^2-4x+3)(x^2-2x-3)$ (ii) $x^4-16$.",
    "(i) $(x-1)(x+1)(x-3)^2$ · (ii) $(x-2)(x+2)(x^2+4)$",
    [
        {"rule": "(i) First quadratic", "why": "$x^2-4x+3$.", "math": "(x-1)(x-3)"},
        {"rule": "(i) Second quadratic", "why": "$x^2-2x-3$.", "math": "(x-3)(x+1)"},
        {"rule": "(i) Combine", "why": "Collect factors.", "math": "(x-1)(x+1)(x-3)^2"},
        {"rule": "(ii) $x^4-16$", "why": "Difference of squares twice.", "math": "(x-2)(x+2)(x^2+4)"},
    ],
    "(i) $(x-1)(x+1)(x-3)^2$ · (ii) $(x-2)(x+2)(x^2+4)$.",
))

# ── Chapter 12: Q114–118 (Linear Equations) ──────────────────────────────────

BATCH.append(q(12, 1,
    "Solve: $3(2x - 1) - 2(3x + 4) = 5(x - 2) + 3$.",
    "$x = -\\dfrac{4}{5}$",
    [
        {"rule": "Expand", "why": "Remove brackets.", "math": "6x-3-6x-8=5x-10+3"},
        {"rule": "Simplify", "why": "Collect terms.", "math": "-11=5x-7"},
        {"rule": "Solve", "why": "Isolate $x$.", "math": "-4=5x \\Rightarrow x=-\\dfrac{4}{5}"},
    ],
    "$x = -\\frac{4}{5}$.",
))

BATCH.append(q(12, 2,
    "The sum of three consecutive even numbers is $48$. Find the numbers.",
    "$14$, $16$, $18$",
    [
        {"rule": "Let numbers", "why": "$x$, $x+2$, $x+4$.", "math": "x+(x+2)+(x+4)=48"},
        {"rule": "Solve", "why": "$3x+6=48$.", "math": "x=14"},
        {"rule": "Numbers", "why": "Add 2 each time.", "math": "14,\\; 16,\\; 18"},
    ],
    "Numbers: 14, 16, 18.",
))

BATCH.append(q(12, 3,
    "A number is $12$ more than the other. If their sum is $48$, find the numbers.",
    "$18$ and $30$",
    [
        {"rule": "Set up", "why": "Smaller $=x$, larger $=x+12$.", "math": "x+(x+12)=48"},
        {"rule": "Solve", "why": "$2x+12=48$.", "math": "x=18,\\; x+12=30"},
    ],
    "Numbers: 18 and 30.",
))

BATCH.append(q(12, 4,
    "Solve and verify: $\\dfrac{2x - 3}{5} + \\dfrac{x + 2}{3} = 4$.",
    "$x = \\dfrac{59}{11}$ (verified)",
    [
        {"rule": "Clear fractions", "why": "Multiply by LCM 15.", "math": "3(2x-3)+5(x+2)=60"},
        {"rule": "Expand", "why": "Simplify.", "math": "11x+1=60 \\Rightarrow x=\\dfrac{59}{11}"},
        {"rule": "Verify", "why": "Substitute into LHS.", "math": "LHS=\\dfrac{17}{11}+\\dfrac{27}{11}=4=RHS\\; \\checkmark"},
    ],
    "$x=\\frac{59}{11}$; verified.",
))

BATCH.append(q(12, 5,
    "A man's age is $4$ times his son's age. After $5$ years, his age will be $3$ times his son's age. Find their present ages.",
    "Son: $10$ years; Man: $40$ years",
    [
        {"rule": "Present ages", "why": "Son $=x$, man $=4x$.", "math": "x,\\; 4x"},
        {"rule": "After 5 years", "why": "Set up equation.", "math": "4x+5=3(x+5)"},
        {"rule": "Solve", "why": "$4x+5=3x+15$.", "math": "x=10,\\; 4x=40"},
    ],
    "Son 10, man 40.",
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
        title = data.get("title", META[ch][2])
        if "Batch 3" not in title:
            if "Batch" in title:
                title = title + " & 3" if " & 3" not in title else title
            else:
                title = f"{META[ch][2]} · Batch 3"
    else:
        questions = new_questions
        title = f"{META[ch][2]} · Batch 3"

    out = {
        "title": title,
        "chapter": ch,
        "count": len(questions),
        "questions": questions,
    }
    path.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
    return len(new_questions), len(questions)


def main():
    by_ch = {ch: [] for ch in META}
    for item in BATCH:
        by_ch[item["chapter"]].append(item)

    total_added = 0
    for ch in sorted(by_ch):
        if not by_ch[ch]:
            continue
        added, total = merge_chapter(ch, by_ch[ch])
        total_added += added
        print(f"Chapter {ch}: added {added} batch-3 questions (total {total})")
    print(f"Total added: {total_added}")


if __name__ == "__main__":
    main()
