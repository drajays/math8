#!/usr/bin/env python3
"""Add Batch 2 detailed solutions (Q41–78) to chapter practice session files."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "chapters"

META = {
    5: ("math-ch5", "CH05-sec-playing-with-numbers", "Playing with Numbers"),
    6: ("math-ch6", "CH06-sec-operations-on-sets", "Operations on Sets"),
    7: ("math-ch7", "CH07-sec-percentage-and-its-applications", "Percentage and its Applications"),
    8: ("math-ch8", "CH08-sec-simple-and-compound-interest", "Simple and Compound Interest"),
}


def q(ch, num, question, answer, steps, explanation, note_id=None, diagram=None):
    topic, default_note, _ = META[ch]
    out = {
        "id": f"Q-CH{ch:02d}-B02-{num:03d}",
        "chapter": ch,
        "topicId": topic,
        "type": "practice",
        "subtopic": "Batch 2 · Detailed Solutions",
        "question": question,
        "answer": answer,
        "options": [],
        "glassboxSteps": steps,
        "explanation": explanation,
        "linked_note_id": note_id or default_note,
        "source": "practice-session",
    }
    if diagram:
        out["diagram"] = diagram
    return out


BATCH = []

# ── Chapter 5: Q41–43 ────────────────────────────────────────────────────────

BATCH.append(q(5, 1,
    "Express $98765$ in the generalised form and check divisibility by $11$.",
    "$98765$ is not divisible by $11$ (alternating difference $= 7$).",
    [
        {"rule": "Generalised form", "why": "Expand by place value.", "math": "9 \\times 10000 + 8 \\times 1000 + 7 \\times 100 + 6 \\times 10 + 5"},
        {"rule": "Rule for 11", "why": "Alternating sum (from right): odd positions minus even positions must be 0 or a multiple of 11.", "math": "(5+7+9) - (6+8) = 21 - 14 = 7"},
        {"rule": "Conclusion", "why": "$7$ is not 0 or a multiple of 11.", "math": "98765 \\text{ is not divisible by } 11"},
    ],
    "Alternating sum: $(5+7+9)-(6+8)=7$ → not divisible by 11.",
))

BATCH.append(q(5, 2,
    "Find the smallest positive number which leaves remainder $3$ when divided by $5$ and remainder $4$ when divided by $7$.",
    "$18$",
    [
        {"rule": "Condition 1", "why": "Numbers of form $5k+3$.", "math": "3,\\; 8,\\; 13,\\; 18,\\; 23,\\; 28,\\; 33,\\; \\ldots"},
        {"rule": "Condition 2", "why": "Numbers of form $7m+4$.", "math": "4,\\; 11,\\; 18,\\; 25,\\; 32,\\; \\ldots"},
        {"rule": "Answer", "why": "First common value.", "math": "18"},
    ],
    "Lists intersect at 18 — smallest such number.",
))

BATCH.append(q(5, 3,
    "If $2A3 + 3B4 = 5C7$ and $A + B + C = 12$, find $A$, $B$, $C$ (letter puzzle; assume standard typo $3B4$ not $B4$).",
    "$C = 6$; $A + B = 6$ (e.g. $A=2$, $B=4$).",
    [
        {"rule": "Units column", "why": "$3+4=7$ — no carry.", "math": "3 + 4 = 7"},
        {"rule": "Hundreds column", "why": "$2+3=5$ — matches.", "math": "2 + 3 = 5"},
        {"rule": "Tens column", "why": "No carry in or out → $A+B=C$.", "math": "A + B = C"},
        {"rule": "Use sum condition", "why": "$A+B+C=12$ and $C=A+B$.", "math": "C + C = 12 \\Rightarrow C = 6;\\quad A + B = 6"},
    ],
    "With $2A3+3B4=5C7$: $C=6$, $A+B=6$. Note: original $B4$ form is impossible.",
))

# ── Chapter 6: Q44–52 ────────────────────────────────────────────────────────

BATCH.append(q(6, 1,
    "If $U = \\{1,2,3,4,5,6,7,8,9,10\\}$, $A = \\{2,4,6,8,10\\}$, $B = \\{1,3,5,7,9\\}$, find $A' \\cup B'$ and $(A \\cap B)'$.",
    "$A' \\cup B' = U$; $(A \\cap B)' = U$",
    [
        {"rule": "Identify sets", "why": "$A$ = evens in $U$; $B$ = odds in $U$.", "math": "A = \\{2,4,6,8,10\\},\\; B = \\{1,3,5,7,9\\}"},
        {"rule": "Partition of $U$", "why": "$A$ and $B$ are mutually exclusive ($A \\cap B = \\emptyset$) and collectively exhaustive ($A \\cup B = U$): every element of $U$ is in exactly one of them.", "math": "A \\cap B = \\emptyset,\\; A \\cup B = U"},
        {"rule": "Complements", "why": "Since $B$ is exactly the non-evens in $U$, $A' = B$; similarly $B' = A$.", "math": "A' = B,\\; B' = A"},
        {"rule": "$A' \\cup B'$", "why": "Union of complements equals $B \\cup A = U$.", "math": "A' \\cup B' = U"},
        {"rule": "$(A \\cap B)'$", "why": "Because $A \\cap B = \\emptyset$, its complement is the entire universal set: $\\emptyset' = U$.", "math": "(A \\cap B)' = U"},
        {"rule": "De Morgan check", "why": "$(A \\cup B)' = A' \\cap B' = \\emptyset$ and $(A \\cap B)' = A' \\cup B' = U$ — consistent with the partition.", "math": "(A \\cap B)' = A' \\cup B' = U"},
    ],
    "$A$ (evens) and $B$ (odds) partition $U$, so $A \\cap B = \\emptyset$ and $(A \\cap B)' = U$; also $A' \\cup B' = U$.",
))

BATCH.append(q(6, 2,
    "Given $n(U)=50$, $n(A)=20$, $n(B)=25$, $n(A \\cap B)=8$, find $n(A \\cup B)$ and $n(A' \\cap B')$.",
    "$n(A \\cup B)=37$; $n(A' \\cap B')=13$",
    [
        {"rule": "Union formula", "why": "$n(A \\cup B)=n(A)+n(B)-n(A \\cap B)$.", "math": "20 + 25 - 8 = 37"},
        {"rule": "Outside both sets", "why": "By De Morgan: $n(A' \\cap B')=n(U)-n(A \\cup B)$.", "math": "50 - 37 = 13"},
    ],
    "$n(A\\cup B)=37$; $n(A'\\cap B')=13$.",
))

BATCH.append(q(6, 3,
    "Draw a Venn diagram to represent: students who play cricket or football but not both in a class of $40$ (with numbers).",
    "Shade $C \\oplus F = (C \\cup F) - (C \\cap F)$: only-cricket and only-football regions (15 + 15, with 5 in both and 5 in neither).",
    [
        {"rule": "Symmetric difference", "why": "Cricket or football but not both = elements in exactly one of $C$ or $F$.", "math": "C \\oplus F = (C \\cup F) - (C \\cap F)"},
        {"rule": "Diagram", "why": "Two overlapping circles in rectangle $U$; shade the left and right crescents only — leave the intersection unshaded.", "math": "\\text{Shade } C \\setminus F \\text{ and } F \\setminus C"},
        {"rule": "Example numbers", "why": "Sample partition of 40: $15 + 15 + 5 + 5 = 40$.", "math": "15 \\text{ only C},\\; 15 \\text{ only F},\\; 5 \\text{ both},\\; 5 \\text{ neither}"},
    ],
    "Shade only-cricket and only-football crescents ($C \\oplus F$); exclude the intersection. See diagram.",
    diagram="venn-symmetric-difference",
))

BATCH.append(q(6, 4,
    "If $A = \\{x : x \\text{ is a prime number less than } 20\\}$ and $B = \\{x : x \\text{ is a multiple of } 3 \\text{ less than } 20\\}$, find $A \\cap B$ and $A - B$.",
    "$A \\cap B = \\{3\\}$; $A - B = \\{2,5,7,11,13,17,19\\}$",
    [
        {"rule": "Roster form", "why": "List elements explicitly.", "math": "A = \\{2,3,5,7,11,13,17,19\\},\\; B = \\{3,6,9,12,15,18\\}"},
        {"rule": "$A \\cap B$", "why": "Common elements.", "math": "\\{3\\}"},
        {"rule": "$A - B$", "why": "In $A$ but not in $B$.", "math": "\\{2,5,7,11,13,17,19\\}"},
    ],
    "$A\\cap B=\\{3\\}$; $A-B=\\{2,5,7,11,13,17,19\\}$.",
))

BATCH.append(q(6, 5,
    "Prove that $A \\cup B = B \\cup A$ using sets from $U = \\{1,\\ldots,10\\}$.",
    "Proved with example: $\\{1,2,3\\}\\cup\\{3,4,5\\}=\\{1,2,3,4,5\\}$ both ways.",
    [
        {"rule": "Choose sets", "why": "Example from $U$.", "math": "A = \\{1,2,3\\},\\; B = \\{3,4,5\\}"},
        {"rule": "LHS", "why": "Union of $A$ and $B$.", "math": "A \\cup B = \\{1,2,3,4,5\\}"},
        {"rule": "RHS", "why": "Union of $B$ and $A$.", "math": "B \\cup A = \\{1,2,3,4,5\\}"},
        {"rule": "Conclusion", "why": "Commutative property of union.", "math": "A \\cup B = B \\cup A\\; \\checkmark"},
    ],
    "Example shows $A\\cup B = B\\cup A$. Proved.",
))

BATCH.append(q(6, 6,
    "Find the number of elements in the power set of $A = \\{a,b,c,d\\}$.",
    "$16$",
    [
        {"rule": "Formula", "why": "Power set has $2^n$ subsets.", "math": "2^n"},
        {"rule": "Apply", "why": "$n=4$.", "math": "2^4 = 16"},
    ],
    "$n(A)=4$ → power set has $2^4=16$ elements.",
))

BATCH.append(q(6, 7,
    "If $n(A)=12$, $n(B)=15$, $n(A \\cup B)=23$, find $n(A \\cap B)$ and discuss $n(A' \\cap B')$.",
    "$n(A \\cap B)=4$; $n(A' \\cap B')$ needs $n(U)$ (would be 0 if $A \\cup B = U$).",
    [
        {"rule": "Intersection", "why": "Rearrange union formula.", "math": "n(A \\cap B) = 12 + 15 - 23 = 4"},
        {"rule": "$n(A' \\cap B')$", "why": "$= n(U) - n(A \\cup B)$; $n(U)$ not given.", "math": "n(A' \\cap B') = n(U) - 23"},
    ],
    "$n(A\\cap B)=4$; $n(A'\\cap B')$ requires $n(U)$.",
))

BATCH.append(q(6, 8,
    "Represent in roster and set-builder form: (i) set of even prime numbers (ii) set of vowels in \"MATHEMATICS\".",
    "(i) Roster $\\{2\\}$ · (ii) Roster $\\{A,E,I\\}$",
    [
        {"rule": "(i) Even primes", "why": "Only 2 is even and prime.", "math": "\\{2\\},\\; \\{x : x \\text{ is an even prime}\\}"},
        {"rule": "(ii) Vowels", "why": "No repeats in a set.", "math": "\\{A,E,I\\},\\; \\{x : x \\text{ is a vowel in MATHEMATICS}\\}"},
    ],
    "(i) $\\{2\\}$ · (ii) $\\{A,E,I\\}$.",
))

BATCH.append(q(6, 9,
    "If $A \\subset B$ and $B \\subset C$, prove $A \\subset C$ with an example.",
    "Proved: e.g. $A=\\{1\\}$, $B=\\{1,2\\}$, $C=\\{1,2,3\\}$.",
    [
        {"rule": "Example", "why": "Construct nested subsets.", "math": "A=\\{1\\},\\; B=\\{1,2\\},\\; C=\\{1,2,3\\}"},
        {"rule": "Check", "why": "Every element of $A$ lies in $C$.", "math": "1 \\in C \\Rightarrow A \\subset C"},
    ],
    "Transitivity: $A\\subset B\\subset C$ → $A\\subset C$. Proved.",
))

# ── Chapter 7: Q53–61 (Percent) ───────────────────────────────────────────────

BATCH.append(q(7, 1,
    "Convert: (i) $\\dfrac{3}{8}$ into percent (ii) $0.075$ into percent (iii) $125\\%$ into fraction.",
    "(i) $37.5\\%$ · (ii) $7.5\\%$ · (iii) $\\dfrac{5}{4}$",
    [
        {"rule": "(i)", "why": "Multiply by $100\\%$.", "math": "\\dfrac{3}{8} \\times 100\\% = 37.5\\%"},
        {"rule": "(ii)", "why": "Multiply by $100\\%$.", "math": "0.075 \\times 100\\% = 7.5\\%"},
        {"rule": "(iii)", "why": "Divide by 100 and simplify.", "math": "125\\% = \\dfrac{125}{100} = \\dfrac{5}{4}"},
    ],
    "(i) 37.5% · (ii) 7.5% · (iii) $\\frac{5}{4}$.",
    note_id="CH07-sec-percentage",
))

BATCH.append(q(7, 2,
    "A number is increased by $20\\%$ and then decreased by $20\\%$. Find the net percentage change.",
    "$4\\%$ decrease",
    [
        {"rule": "Assume 100", "why": "Convenient base.", "math": "100 \\xrightarrow{+20\\%} 120 \\xrightarrow{-20\\%} 96"},
        {"rule": "Net change", "why": "$100-96=4$.", "math": "4\\% \\text{ decrease}"},
        {"rule": "Shortcut", "why": "Equal $\\pm x\\%$ gives loss $x^2/100$.", "math": "20^2/100 = 4\\%"},
    ],
    "100 → 120 → 96: net 4% decrease.",
))

BATCH.append(q(7, 3,
    "If $15\\%$ of a number is $45$, find $35\\%$ of the number.",
    "$105$",
    [
        {"rule": "Find number", "why": "$0.15x=45$.", "math": "x = 45/0.15 = 300"},
        {"rule": "35% of 300", "why": "Multiply.", "math": "0.35 \\times 300 = 105"},
    ],
    "$x=300$ → 35% of 300 = 105.",
))

BATCH.append(q(7, 4,
    "In a class of $50$ students, $60\\%$ are girls. If $10\\%$ of girls and $20\\%$ of boys failed, find the number who passed.",
    "$43$ students passed",
    [
        {"rule": "Girls and boys", "why": "60% of 50.", "math": "30 \\text{ girls},\\; 20 \\text{ boys}"},
        {"rule": "Passed", "why": "Subtract failures.", "math": "27 \\text{ girls passed} + 16 \\text{ boys passed} = 43"},
    ],
    "30 girls (27 pass) + 20 boys (16 pass) = 43 passed.",
))

BATCH.append(q(7, 5,
    "The price of sugar is increased by $25\\%$. By what percent must consumption be reduced so expenditure stays the same?",
    "$20\\%$",
    [
        {"rule": "Formula", "why": "Required reduction $= \\frac{R}{100+R}\\times 100\\%$.", "math": "\\dfrac{25}{125} \\times 100\\% = 20\\%"},
    ],
    "$\\frac{25}{125}\\times 100\\% = 20\\%$ reduction needed.",
))

BATCH.append(q(7, 6,
    "A man's salary is first increased by $10\\%$ and then decreased by $10\\%$. Find net % change and final salary if original was ₹$25000$.",
    "₹$24750$; $1\\%$ decrease",
    [
        {"rule": "After +10%", "why": "Multiply by 1.10.", "math": "25000 \\times 1.10 = 27500"},
        {"rule": "After −10%", "why": "Multiply by 0.90.", "math": "27500 \\times 0.90 = 24750"},
        {"rule": "Net %", "why": "Shortcut: $10^2/100=1\\%$ loss.", "math": "1\\% \\text{ decrease}"},
    ],
    "Final ₹24750; net 1% decrease.",
))

BATCH.append(q(7, 7,
    "Express $2.5$ as percent of $12.5$. Also find what percent $12.5$ is of $2.5$.",
    "$2.5$ is $20\\%$ of $12.5$; $12.5$ is $500\\%$ of $2.5$",
    [
        {"rule": "First part", "why": "$(A/B)\\times 100$.", "math": "\\dfrac{2.5}{12.5} \\times 100 = 20\\%"},
        {"rule": "Second part", "why": "Reverse ratio.", "math": "\\dfrac{12.5}{2.5} \\times 100 = 500\\%"},
    ],
    "2.5 is 20% of 12.5; 12.5 is 500% of 2.5.",
))

BATCH.append(q(7, 8,
    "In an examination, $30\\%$ failed in English, $25\\%$ in Maths. If $15\\%$ failed in both, find $\\%$ who passed in both subjects.",
    "$60\\%$",
    [
        {"rule": "Failed in at least one", "why": "Set formula on percentages.", "math": "30 + 25 - 15 = 40\\%"},
        {"rule": "Passed both", "why": "Complement.", "math": "100\\% - 40\\% = 60\\%"},
    ],
    "40% fail at least one → 60% pass both.",
))

BATCH.append(q(7, 9,
    "A mixture contains $40\\%$ milk and $60\\%$ water. How much water must be added to make it $25\\%$ milk?",
    "Add water equal to $60\\%$ of the initial mixture volume",
    [
        {"rule": "Milk constant", "why": "Let initial volume $= V$.", "math": "0.4V \\text{ milk unchanged}"},
        {"rule": "Equation", "why": "Milk is 25% of new total.", "math": "0.4V = 0.25(V+w)"},
        {"rule": "Solve", "why": "Isolate $w$.", "math": "w = 0.6V"},
    ],
    "$0.4V=0.25(V+w)$ → add $0.6V$ water.",
))

# ── Chapter 7: Q62–69 (Profit, Loss & Discount — user's Ch8) ─────────────────

BATCH.append(q(7, 10,
    "A shopkeeper buys $80$ articles for ₹$2400$ and sells them at a profit of $16\\%$. Find the selling price of one article.",
    "₹$34.80$ per article",
    [
        {"rule": "CP per article", "why": "Divide total cost.", "math": "2400/80 = 30"},
        {"rule": "SP", "why": "Add 16% profit.", "math": "30 + 0.16 \\times 30 = 34.80"},
    ],
    "CP ₹30 → SP ₹34.80.",
    note_id="CH07-sec-profit-and-loss",
))

BATCH.append(q(7, 11,
    "A man buys a TV for ₹$18500$ and sells it at a loss of $8\\%$. Find the selling price.",
    "₹$17020$",
    [
        {"rule": "Formula", "why": "SP = CP × (1 − loss%).", "math": "18500 \\times 0.92 = 17020"},
    ],
    "SP = 18500 × 0.92 = ₹17020.",
    note_id="CH07-sec-profit-and-loss",
))

BATCH.append(q(7, 12,
    "The marked price of a shirt is ₹$850$. A shopkeeper allows $8\\%$ discount and still makes $15\\%$ profit. Find the cost price.",
    "₹$680$",
    [
        {"rule": "SP after discount", "why": "850 × 0.92.", "math": "782"},
        {"rule": "CP", "why": "SP = CP × 1.15.", "math": "782/1.15 = 680"},
    ],
    "SP ₹782 → CP ₹680.",
    note_id="CH07-sec-discount",
))

BATCH.append(q(7, 13,
    "A trader sells an article at $12.5\\%$ profit. If he had sold it for ₹$90$ more, he would have gained $25\\%$. Find the cost price.",
    "₹$720$",
    [
        {"rule": "Profit difference", "why": "25% − 12.5% = 12.5% of CP = ₹90.", "math": "0.125 \\times CP = 90"},
        {"rule": "Solve", "why": "Divide.", "math": "CP = 720"},
    ],
    "12.5% of CP = 90 → CP = ₹720.",
    note_id="CH07-sec-profit-and-loss",
))

BATCH.append(q(7, 14,
    "A dealer buys an article for ₹$380$. At what price must he mark it so that after $5\\%$ discount he makes $25\\%$ profit?",
    "₹$500$",
    [
        {"rule": "Required SP", "why": "380 × 1.25.", "math": "475"},
        {"rule": "Marked price", "why": "M × 0.95 = 475.", "math": "M = 500"},
    ],
    "Need SP ₹475 → MP ₹500.",
    note_id="CH07-sec-discount",
))

BATCH.append(q(7, 15,
    "By selling $90$ ball pens for ₹$160$, a shopkeeper loses $20\\%$. How many ball pens should he sell for ₹$96$ to gain $20\\%$?",
    "$36$ pens",
    [
        {"rule": "CP per pen", "why": "SP ₹160/90 at 80% of CP.", "math": "CP = \\dfrac{16/9}{0.8} = \\dfrac{20}{9}"},
        {"rule": "Target SP per pen", "why": "CP × 1.20.", "math": "8/3"},
        {"rule": "Count", "why": "96 ÷ (8/3).", "math": "36 \\text{ pens}"},
    ],
    "CP ₹20/9 → sell 36 pens for ₹96 at 20% gain.",
    note_id="CH07-sec-profit-and-loss",
))

BATCH.append(q(7, 16,
    "The cost price of $12$ pens is equal to the selling price of $15$ pens. Find the gain or loss percent.",
    "$20\\%$ loss",
    [
        {"rule": "Assume ₹60", "why": "LCM of 12 and 15.", "math": "CP_{12}=SP_{15}=60"},
        {"rule": "Per pen", "why": "CP = 5, SP = 4.", "math": "Loss = 1"},
        {"rule": "Loss %", "why": "$(1/5)\\times 100$.", "math": "20\\% \\text{ loss}"},
    ],
    "CP ₹5, SP ₹4 per pen → 20% loss.",
    note_id="CH07-sec-profit-and-loss",
))

BATCH.append(q(7, 17,
    "A man sold two horses for ₹$4000$ each. On one he gains $25\\%$ and on the other loses $25\\%$. Find his overall gain or loss percent.",
    "$6.25\\%$ overall loss",
    [
        {"rule": "Shortcut", "why": "Equal ±x% at same SP → loss $x^2/100$.", "math": "25^2/100 = 6.25\\%"},
        {"rule": "Verify", "why": "Total CP > total SP.", "math": "CP_1=3200,\\; CP_2=5333.33;\\; \\text{loss } 6.25\\%"},
    ],
    "Equal ±25% at same SP → 6.25% net loss.",
    note_id="CH07-sec-profit-and-loss",
))

# ── Chapter 8: Q70–78 (Interest — user's Ch9) ────────────────────────────────

BATCH.append(q(8, 1,
    "Find the simple interest on ₹$6500$ for $3$ years $6$ months at $8\\%$ per annum.",
    "₹$1820$",
    [
        {"rule": "Time in years", "why": "6 months = 0.5 year.", "math": "T = 3.5"},
        {"rule": "SI formula", "why": "$SI = PRT/100$.", "math": "\\dfrac{6500 \\times 8 \\times 3.5}{100} = 1820"},
    ],
    "SI = (6500×8×3.5)/100 = ₹1820.",
))

BATCH.append(q(8, 2,
    "The simple interest on a certain sum for $2.5$ years at $12\\%$ p.a. is ₹$3750$. Find the sum.",
    "₹$12500$",
    [
        {"rule": "Rearrange", "why": "$P = SI\\times 100/(RT)$.", "math": "P = \\dfrac{3750 \\times 100}{12 \\times 2.5} = 12500"},
    ],
    "P = 375000/30 = ₹12500.",
))

BATCH.append(q(8, 3,
    "Find the compound interest on ₹$8000$ for $2$ years at $10\\%$ p.a. compounded annually.",
    "₹$1680$",
    [
        {"rule": "Amount", "why": "$A = P(1+R/100)^T$.", "math": "8000 \\times 1.1^2 = 9680"},
        {"rule": "CI", "why": "$A - P$.", "math": "9680 - 8000 = 1680"},
    ],
    "A = ₹9680 → CI = ₹1680.",
))

BATCH.append(q(8, 4,
    "A sum amounts to ₹$9800$ after $5$ years and ₹$12005$ after $8$ years at the same rate of simple interest. Find the rate and the sum.",
    "Principal ₹$6125$; rate $12\\%$ p.a.",
    [
        {"rule": "SI for 3 years", "why": "Difference in amounts.", "math": "12005 - 9800 = 2205"},
        {"rule": "SI per year", "why": "Divide by 3.", "math": "735"},
        {"rule": "Principal", "why": "9800 − SI for 5 years.", "math": "9800 - 3675 = 6125"},
        {"rule": "Rate", "why": "$R = SI\\times 100/(PT)$.", "math": "12\\%"},
    ],
    "P = ₹6125; R = 12% p.a.",
))

BATCH.append(q(8, 5,
    "Calculate the difference between compound interest and simple interest on ₹$16000$ for $2$ years at $10\\%$ p.a.",
    "₹$160$",
    [
        {"rule": "2-year formula", "why": "$Diff = P(R/100)^2$.", "math": "16000 \\times (0.1)^2 = 160"},
    ],
    "CI − SI = 16000 × 0.01 = ₹160.",
))

BATCH.append(q(8, 6,
    "At what rate per cent per annum will ₹$6400$ amount to ₹$7744$ in $2$ years when interest is compounded annually?",
    "$10\\%$ p.a.",
    [
        {"rule": "Set up", "why": "7744/6400 = (1+R/100)².", "math": "\\dfrac{121}{100} = \\left(1+\\dfrac{R}{100}\\right)^2"},
        {"rule": "Solve", "why": "Square root.", "math": "R = 10\\%"},
    ],
    "121/100 = (1+R/100)² → R = 10%.",
))

BATCH.append(q(8, 7,
    "A man invests ₹$5000$ at $8\\%$ p.a. compound interest for $3$ years. Find the amount and interest. Also find the difference from simple interest.",
    "Amount ₹$6298.56$; CI ₹$1298.56$; CI − SI = ₹$98.56$",
    [
        {"rule": "Amount", "why": "$5000 \\times 1.08^3$.", "math": "6298.56"},
        {"rule": "CI", "why": "$A - P$.", "math": "1298.56"},
        {"rule": "SI", "why": "$PRT/100$.", "math": "1200"},
        {"rule": "Difference", "why": "CI − SI.", "math": "98.56"},
    ],
    "A = ₹6298.56; CI − SI = ₹98.56.",
))

BATCH.append(q(8, 8,
    "The compound interest on a certain sum for $2$ years at $10\\%$ p.a. is ₹$630$. Find the sum.",
    "₹$3000$",
    [
        {"rule": "CI formula", "why": "$630 = P[(1.1)^2 - 1]$.", "math": "630 = P \\times 0.21"},
        {"rule": "Solve", "why": "Divide.", "math": "P = 3000"},
    ],
    "630 = 0.21P → P = ₹3000.",
))

BATCH.append(q(8, 9,
    "Find the time in which ₹$12500$ will amount to ₹$14641$ at $8\\%$ p.a. compound interest.",
    "No exact integer $T$ ($\\approx 2.05$ years); likely typo in source (e.g. $10\\%$ gives $T=4$ years for $\\frac{14641}{10000}$).",
    [
        {"rule": "Set up", "why": "14641/12500 = 1.08^T.", "math": "1.17128 = 1.08^T"},
        {"rule": "Analyse", "why": "No integer power of 1.08 matches exactly.", "math": "T \\approx 2.05 \\text{ years}"},
        {"rule": "Note", "why": "If rate were 10%: $(1.1)^4 = 14641/10000$.", "math": "T = 4 \\text{ years at 10\\%}"},
    ],
    "As written: T ≈ 2.05 yr. Likely source typo (10% → T=4 yr).",
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
        if "Batch 2" not in title:
            title = title.replace(" · Batch 1", "") + " · Batch 1 & 2"
            if "Batch" not in title:
                title = f"{META[ch][2]} · Batch 1 & 2"
    else:
        questions = new_questions
        title = f"{META[ch][2]} · Batch 2"

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
        print(f"Chapter {ch}: added {added} batch-2 questions (total {total})")
    print(f"Total added: {total_added}")


if __name__ == "__main__":
    main()
