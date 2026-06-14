#!/usr/bin/env python3
"""Add Batch 4 detailed solutions (Q119–156) to chapter practice session files."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "chapters"

META = {
    12: ("math-ch12", "CH12-sec-linear-equations-and-inequalities-in-one-variabl", "Linear Equations and Inequalities"),
    13: ("math-ch13", "CH13-sec-understanding-shapes", "Understanding Shapes"),
    14: ("math-ch14", "CH14-sec-construction-of-quadrilaterals", "Construction of Quadrilaterals"),
}


def q(ch, num, question, answer, steps, explanation, note_id=None):
    topic, default_note, _ = META[ch]
    return {
        "id": f"Q-CH{ch:02d}-B04-{num:03d}",
        "chapter": ch,
        "topicId": topic,
        "type": "practice",
        "subtopic": "Batch 4 · Detailed Solutions",
        "question": question,
        "answer": answer,
        "options": [],
        "glassboxSteps": steps,
        "explanation": explanation,
        "linked_note_id": note_id or default_note,
        "source": "practice-session",
    }


BATCH = []

# ── Chapter 12: Q119–122 (Linear Equations continued) ────────────────────────

BATCH.append(q(12, 1,
    "The perimeter of a rectangle is $40$ cm. If its length is $4$ cm more than its breadth, find the dimensions.",
    "Breadth $= 8$ cm; Length $= 12$ cm",
    [
        {"rule": "Let breadth", "why": "$B = x$, length $L = x + 4$.", "math": "P = 2(L+B)"},
        {"rule": "Equation", "why": "Substitute into perimeter formula.", "math": "2(x+x+4)=40 \\Rightarrow 4x+8=40"},
        {"rule": "Solve", "why": "$4x=32$.", "math": "x=8;\\; L=12"},
    ],
    "Breadth 8 cm, length 12 cm.",
))

BATCH.append(q(12, 2,
    "Solve: $\\dfrac{5x}{3} - \\dfrac{x-3}{2} = \\dfrac{2x+1}{4}$.",
    "$x = -\\dfrac{15}{8}$",
    [
        {"rule": "Clear fractions", "why": "LCM of 3, 2, 4 is 12.", "math": "20x-6(x-3)=3(2x+1)"},
        {"rule": "Expand", "why": "Remove brackets.", "math": "20x-6x+18=6x+3"},
        {"rule": "Solve", "why": "Collect $x$ terms.", "math": "14x+18=6x+3 \\Rightarrow 8x=-15 \\Rightarrow x=-\\dfrac{15}{8}"},
    ],
    "$x = -\\frac{15}{8}$.",
))

BATCH.append(q(12, 3,
    "A sum of ₹$500$ is in denominations of ₹$5$ and ₹$10$. If the number of ₹$10$ notes is twice the number of ₹$5$ notes, find the number of each.",
    "₹$5$ notes: $20$; ₹$10$ notes: $40$",
    [
        {"rule": "Let ₹5 notes", "why": "$x$ notes of ₹5; ₹10 notes $= 2x$.", "math": "5x+10(2x)=500"},
        {"rule": "Solve", "why": "$25x=500$.", "math": "x=20;\\; 2x=40"},
    ],
    "20 notes of ₹5, 40 notes of ₹10.",
))

BATCH.append(q(12, 4,
    "The denominator of a fraction is $3$ more than the numerator. If $2$ is added to both, the fraction becomes $\\dfrac{4}{5}$. Find the fraction.",
    "$\\dfrac{10}{13}$",
    [
        {"rule": "Set up", "why": "Fraction $\\frac{x}{x+3}$; after adding 2: $\\frac{x+2}{x+5}$.", "math": "\\dfrac{x+2}{x+5}=\\dfrac{4}{5}"},
        {"rule": "Cross-multiply", "why": "Clear fractions.", "math": "5(x+2)=4(x+5) \\Rightarrow 5x+10=4x+20"},
        {"rule": "Solve", "why": "$x=10$.", "math": "\\dfrac{10}{13}"},
    ],
    "Numerator 10, denominator 13 → $\\frac{10}{13}$.",
))

# ── Chapter 12: Q123–130 (Linear Inequations) ────────────────────────────────

BATCH.append(q(12, 5,
    "Solve and represent on number line: $3x + 5 > 2x - 7$, $x \\in \\mathbb{N}$.",
    "$x > -12$; solution set $\\{1,2,3,\\ldots\\}$",
    [
        {"rule": "Isolate $x$", "why": "Subtract $2x$, subtract 5.", "math": "x > -12"},
        {"rule": "Natural numbers", "why": "$\\mathbb{N}=\\{1,2,3,\\ldots\\}$.", "math": "\\{1,2,3,4,\\ldots\\}"},
    ],
    "$x>12$ → all natural numbers 1, 2, 3, …",
))

BATCH.append(q(12, 6,
    "Solve: $2(x - 3) \\le 5x + 9$ and represent the solution set on the number line.",
    "$x \\ge -5$",
    [
        {"rule": "Expand", "why": "Remove brackets.", "math": "2x-6 \\le 5x+9"},
        {"rule": "Isolate", "why": "Collect $x$ on one side.", "math": "-15 \\le 3x \\Rightarrow x \\ge -5"},
    ],
    "Solution: $x \\ge -5$ (solid dot at $-5$, ray rightward).",
))

BATCH.append(q(12, 7,
    "Solve: $5 - 2x \\ge 3$ where $x$ is an integer. Represent on the number line.",
    "$x \\le 1$; integers $\\{\\ldots,-3,-2,-1,0,1\\}$",
    [
        {"rule": "Rearrange", "why": "$-2x \\ge -2$.", "math": "-2x \\ge -2"},
        {"rule": "Divide by $-2$", "why": "Flip inequality sign.", "math": "x \\le 1"},
    ],
    "$x \\le 1$; integer dots at …, −1, 0, 1.",
))

BATCH.append(q(12, 8,
    "Find the solution set: $\\dfrac{3x+4}{5} < \\dfrac{2x+7}{3}$, $x \\in \\mathbb{R}$.",
    "$x > -23$; solution $(-23, \\infty)$",
    [
        {"rule": "Clear fractions", "why": "Multiply by LCM 15.", "math": "3(3x+4) < 5(2x+7)"},
        {"rule": "Simplify", "why": "Expand and isolate.", "math": "9x+12 < 10x+35 \\Rightarrow -23 < x"},
    ],
    "$x > -23$.",
))

BATCH.append(q(12, 9,
    "Solve and graph: $4x - 7 > 5$ and $3x + 2 < 14$ (find intersection).",
    "$3 < x < 4$",
    [
        {"rule": "First inequation", "why": "$4x > 12$.", "math": "x > 3"},
        {"rule": "Second inequation", "why": "$3x < 12$.", "math": "x < 4"},
        {"rule": "Intersection", "why": "Both must hold.", "math": "3 < x < 4"},
    ],
    "Open segment between 3 and 4.",
))

BATCH.append(q(12, 10,
    "A number is such that when multiplied by $3$ and then $5$ is subtracted, the result is greater than $10$. Find the smallest integer satisfying it.",
    "$6$",
    [
        {"rule": "Inequation", "why": "Let number be $x$.", "math": "3x-5 > 10"},
        {"rule": "Solve", "why": "$3x > 15$.", "math": "x > 5"},
        {"rule": "Smallest integer", "why": "Strictly greater than 5.", "math": "6"},
    ],
    "$x>5$ → smallest integer 6.",
))

BATCH.append(q(12, 11,
    "Solve: $-3 \\le 2x + 1 < 7$ and represent on the number line ($x$ integer).",
    "$-2 \\le x < 3$; integers $\\{-2,-1,0,1,2\\}$",
    [
        {"rule": "Subtract 1", "why": "All three parts.", "math": "-4 \\le 2x < 6"},
        {"rule": "Divide by 2", "why": "Isolate $x$.", "math": "-2 \\le x < 3"},
    ],
    "Integers: −2, −1, 0, 1, 2.",
))

BATCH.append(q(12, 12,
    "The sum of two numbers is at most $25$. If one is at least $10$, find possible values for the other.",
    "$y \\le 15$",
    [
        {"rule": "Inequations", "why": "$x+y \\le 25$, $x \\ge 10$.", "math": "x+y \\le 25"},
        {"rule": "Maximum $y$", "why": "When $x=10$: $10+y \\le 25$.", "math": "y \\le 15"},
    ],
    "Other number $y \\le 15$.",
))

# ── Chapter 13: Q131–139 (Polygons & angles) ─────────────────────────────────

BATCH.append(q(13, 1,
    "Find the sum of interior angles of a polygon with $9$ sides. Also find each interior angle if regular.",
    "Sum $= 1260°$; each regular interior angle $= 140°$",
    [
        {"rule": "Sum formula", "why": "$(n-2)\\times 180°$.", "math": "(9-2)\\times 180°=1260°"},
        {"rule": "Regular polygon", "why": "Divide by $n$.", "math": "1260°/9=140°"},
    ],
    "Sum 1260°; each angle 140°.",
))

BATCH.append(q(13, 2,
    "An exterior angle of a regular polygon is $24°$. Find the number of sides.",
    "$15$ sides",
    [
        {"rule": "Exterior angles sum", "why": "Always $360°$ for convex polygon.", "math": "n=360°/24°=15"},
    ],
    "$360° ÷ 24° = 15$ sides.",
))

BATCH.append(q(13, 3,
    "Prove that the sum of exterior angles of any polygon is $360°$ (one at each vertex).",
    "Proved.",
    [
        {"rule": "Linear pairs", "why": "At each vertex: $i_k+e_k=180°$.", "math": "\\sum(i_k+e_k)=180°\\cdot n"},
        {"rule": "Interior sum", "why": "$\\sum i_k=(n-2)\\cdot 180°$.", "math": "(n-2)180°+\\sum e=180°n"},
        {"rule": "Conclusion", "why": "Simplify.", "math": "\\sum e=360°\\; \\checkmark"},
    ],
    "Interior + exterior argument → 360°. Proved.",
))

BATCH.append(q(13, 4,
    "The interior angles of a hexagon are in the ratio $2:3:4:5:6:7$. Find all the angles.",
    "$\\dfrac{160}{3}°$, $80°$, $\\dfrac{320}{3}°$, $\\dfrac{400}{3}°$, $160°$, $\\dfrac{560}{3}°$",
    [
        {"rule": "Hexagon sum", "why": "$(6-2)\\times 180°=720°$.", "math": "720°"},
        {"rule": "Ratio", "why": "$2x+3x+4x+5x+6x+7x=720°$.", "math": "27x=720° \\Rightarrow x=\\dfrac{80}{3}°"},
        {"rule": "Angles", "why": "Multiply ratio parts.", "math": "\\dfrac{160}{3}°,\\; 80°,\\; \\dfrac{320}{3}°,\\; \\dfrac{400}{3}°,\\; 160°,\\; \\dfrac{560}{3}°"},
    ],
    "$x=\\frac{80}{3}°$; six angles as above.",
))

BATCH.append(q(13, 5,
    "In a quadrilateral, three angles are equal and the fourth is $120°$. Find each equal angle.",
    "$80°$ each",
    [
        {"rule": "Quadrilateral sum", "why": "$360°$ total.", "math": "3x+120°=360°"},
        {"rule": "Solve", "why": "$3x=240°$.", "math": "x=80°"},
    ],
    "Each equal angle = 80°.",
))

BATCH.append(q(13, 6,
    "Find the measure of each angle of a regular octagon.",
    "$135°$",
    [
        {"rule": "Exterior angle", "why": "$360°/8$.", "math": "45°"},
        {"rule": "Interior", "why": "$180°-45°$.", "math": "135°"},
    ],
    "Interior angle = 135°.",
))

BATCH.append(q(13, 7,
    "If one angle of a triangle is $90°$ and the other two are in ratio $2:3$, find the angles.",
    "$36°$ and $54°$",
    [
        {"rule": "Triangle sum", "why": "$180°$ total.", "math": "90°+2x+3x=180°"},
        {"rule": "Solve", "why": "$5x=90°$.", "math": "x=18°;\\; 36°,\\; 54°"},
    ],
    "Other angles: 36° and 54°.",
))

BATCH.append(q(13, 8,
    "Prove that in any triangle, the sum of angles is $180°$.",
    "Proved.",
    [
        {"rule": "Construction", "why": "Through $A$, draw line parallel to $BC$.", "math": "XY \\parallel BC"},
        {"rule": "Alternate angles", "why": "$\\angle XAB=\\angle B$, $\\angle YAC=\\angle C$.", "math": "\\angle XAB+\\angle A+\\angle YAC=180°"},
        {"rule": "Conclusion", "why": "Substitute.", "math": "\\angle A+\\angle B+\\angle C=180°\\; \\checkmark"},
    ],
    "Parallel line + alternate angles → 180°. Proved.",
))

BATCH.append(q(13, 9,
    "The angles of a quadrilateral are in ratio $1:2:3:4$. Find the angles.",
    "$36°$, $72°$, $108°$, $144°$",
    [
        {"rule": "Sum", "why": "$x+2x+3x+4x=360°$.", "math": "10x=360°"},
        {"rule": "Solve", "why": "$x=36°$.", "math": "36°,\\; 72°,\\; 108°,\\; 144°"},
    ],
    "Angles: 36°, 72°, 108°, 144°.",
))

# ── Chapter 13: Q140–148 (Quadrilaterals) ────────────────────────────────────

BATCH.append(q(13, 10,
    "Prove that the diagonals of a parallelogram bisect each other.",
    "Proved: $AO=OC$, $BO=OD$ by ASA congruence of $\\triangle AOB$ and $\\triangle COD$.",
    [
        {"rule": "Congruence setup", "why": "In $\\parallelogram$ $ABCD$, diagonals meet at $O$.", "math": "AB=CD,\\; \\angle OAB=\\angle OCD,\\; \\angle OBA=\\angle ODC"},
        {"rule": "ASA", "why": "$\\triangle AOB \\cong \\triangle COD$.", "math": "AO=OC,\\; BO=OD"},
    ],
    "ASA on $\\triangle AOB$, $\\triangle COD$ → diagonals bisect. Proved.",
    note_id="CH13-sec-quadrilateral",
))

BATCH.append(q(13, 11,
    "In parallelogram $ABCD$, if $\\angle A = 65°$, find all other angles and prove opposite sides equal.",
    "Angles: $65°$, $115°$, $65°$, $115°$; $AB=CD$, $AD=BC$",
    [
        {"rule": "Angles", "why": "Opposite equal; adjacent supplementary.", "math": "65°,\\; 115°,\\; 65°,\\; 115°"},
        {"rule": "Sides", "why": "$\\triangle ABC \\cong \\triangle CDA$ (ASA).", "math": "AB=CD,\\; AD=BC"},
    ],
    "Angles as above; opposite sides equal by ASA.",
    note_id="CH13-sec-quadrilateral",
))

BATCH.append(q(13, 12,
    "Prove that the diagonals of a rhombus bisect each other at right angles.",
    "Proved: $\\angle AOB = 90°$ via SSS congruence.",
    [
        {"rule": "Bisection", "why": "Rhombus is a parallelogram → diagonals bisect.", "math": "AO=OC,\\; BO=OD"},
        {"rule": "SSS", "why": "$\\triangle AOB \\cong \\triangle AOD$ ($AB=AD$, common $AO$, $BO=OD$).", "math": "\\angle AOB=\\angle AOD=90°"},
    ],
    "SSS → right angles at intersection. Proved.",
    note_id="CH13-sec-quadrilateral",
))

BATCH.append(q(13, 13,
    "In rectangle $ABCD$, diagonals $AC$ and $BD$ intersect at $O$. Prove $AO=OC$ and the triangles are congruent.",
    "$AO=OC$ (parallelogram); $AC=BD$ by SAS on $\\triangle ADC$ and $\\triangle BCD$.",
    [
        {"rule": "Bisection", "why": "Rectangle is a parallelogram.", "math": "AO=OC"},
        {"rule": "Equal diagonals", "why": "$\\triangle ADC \\cong \\triangle BCD$ (SAS).", "math": "AC=BD"},
    ],
    "Diagonals bisect and are equal.",
    note_id="CH13-sec-quadrilateral",
))

BATCH.append(q(13, 14,
    "The diagonals of a rhombus are $16$ cm and $12$ cm. Find its side and area.",
    "Side $= 10$ cm; Area $= 96$ cm²",
    [
        {"rule": "Half-diagonals", "why": "Right triangle legs 8 cm and 6 cm.", "math": "8,\\; 6"},
        {"rule": "Side", "why": "Pythagoras.", "math": "\\sqrt{8^2+6^2}=10 \\text{ cm}"},
        {"rule": "Area", "why": "$\\frac{1}{2}d_1 d_2$.", "math": "\\frac{1}{2}\\times 16\\times 12=96 \\text{ cm}^2"},
    ],
    "Side 10 cm; area 96 cm².",
    note_id="CH13-sec-quadrilateral",
))

BATCH.append(q(13, 15,
    "Prove that each pair of opposite angles of a parallelogram are equal.",
    "Proved: $\\angle A=\\angle C$, $\\angle B=\\angle D$.",
    [
        {"rule": "Supplementary pairs", "why": "Consecutive interior angles with parallel sides.", "math": "\\angle A+\\angle B=180°,\\; \\angle B+\\angle C=180°"},
        {"rule": "Conclusion", "why": "Equate expressions.", "math": "\\angle A=\\angle C;\\; \\angle B=\\angle D"},
    ],
    "Consecutive interior angle argument. Proved.",
    note_id="CH13-sec-quadrilateral",
))

BATCH.append(q(13, 16,
    "In a square, prove all sides equal, all angles $90°$, diagonals equal and bisect at $90°$.",
    "Proved (combines parallelogram, rectangle, rhombus properties).",
    [
        {"rule": "Sides & angles", "why": "Parallelogram with one right angle and adjacent sides equal.", "math": "AB=BC=CD=DA;\\; \\text{all } 90°"},
        {"rule": "Diagonals", "why": "Equal (rectangle) and perpendicular (rhombus).", "math": "AC=BD;\\; \\angle AOB=90°"},
    ],
    "Square inherits rectangle + rhombus diagonal properties. Proved.",
    note_id="CH13-sec-quadrilateral",
))

BATCH.append(q(13, 17,
    "A parallelogram has one angle $75°$. Find the other angles and prove adjacent angles supplementary.",
    "$75°$, $105°$, $75°$, $105°$; adjacent angles sum to $180°$.",
    [
        {"rule": "Angles", "why": "Opposite equal; adjacent supplementary.", "math": "75°,\\; 105°,\\; 75°,\\; 105°"},
        {"rule": "Proof", "why": "Parallel lines + transversal → consecutive interior angles sum $180°$.", "math": "\\angle A+\\angle B=180°"},
    ],
    "Angles 75°, 105°, …; adjacent supplementary by parallel lines.",
    note_id="CH13-sec-quadrilateral",
))

BATCH.append(q(13, 18,
    "If $ABCD$ is a trapezium with $AB \\parallel DC$, prove angles on the same side of a transversal are supplementary.",
    "$\\angle A+\\angle D=180°$ and $\\angle B+\\angle C=180°$",
    [
        {"rule": "Parallel sides", "why": "$AB \\parallel DC$.", "math": "AB \\parallel DC"},
        {"rule": "Transversals", "why": "$AD$ and $BC$ cross parallel lines.", "math": "\\angle A+\\angle D=180°,\\; \\angle B+\\angle C=180°"},
    ],
    "Consecutive interior angles on parallel lines. Proved.",
    note_id="CH13-sec-quadrilateral",
))

# ── Chapter 14: Q149–156 (Constructions) ───────────────────────────────────

BATCH.append(q(14, 1,
    "Construct quadrilateral $ABCD$ where $AB=5$ cm, $BC=4.5$ cm, $CD=6$ cm, $DA=5.5$ cm and diagonal $AC=7$ cm.",
    "Steps: draw $AC=7$ cm; arcs from $A$ (5 cm) and $C$ (4.5 cm) give $B$; arcs from $A$ (5.5 cm) and $C$ (6 cm) give $D$; join sides.",
    [
        {"rule": "Step 1", "why": "Draw diagonal first.", "math": "AC=7 \\text{ cm}"},
        {"rule": "Step 2", "why": "Locate $B$.", "math": "AB=5,\\; BC=4.5"},
        {"rule": "Step 3", "why": "Locate $D$.", "math": "AD=5.5,\\; CD=6"},
        {"rule": "Step 4", "why": "Complete quadrilateral.", "math": "Join AB, BC, CD, DA"},
    ],
    "Diagonal-first arc method.",
))

BATCH.append(q(14, 2,
    "Construct a rhombus whose diagonals are $6$ cm and $8$ cm.",
    "Steps: draw $AC=8$ cm; perpendicular bisector at $O$; mark $B,D$ at 3 cm from $O$; join.",
    [
        {"rule": "Diagonal 1", "why": "Draw $AC=8$ cm; bisect at $O$.", "math": "AO=OC=4"},
        {"rule": "Diagonal 2", "why": "Perpendicular at $O$; $BO=OD=3$.", "math": "BD=6"},
        {"rule": "Join", "why": "Connect vertices.", "math": "ABCD \\text{ rhombus}"},
    ],
    "Diagonals 8 cm and 6 cm via perpendicular bisector.",
))

BATCH.append(q(14, 3,
    "Construct parallelogram $ABCD$ with $AB=5$ cm, $AD=4$ cm and $\\angle A=60°$.",
    "Steps: draw $AB=5$; $60°$ at $A$; cut $AD=4$; arcs locate $C$; join.",
    [
        {"rule": "Base & angle", "why": "$AB=5$; construct $60°$ at $A$.", "math": "AB=5,\\; \\angle A=60°"},
        {"rule": "Side $AD$", "why": "Mark 4 cm on angle arm.", "math": "AD=4"},
        {"rule": "Vertex $C$", "why": "Arcs: 5 cm from $D$, 4 cm from $B$.", "math": "Join BC, DC"},
    ],
    "Base-angle-arc method for parallelogram.",
))

BATCH.append(q(14, 4,
    "Construct an isosceles triangle with base $6$ cm and equal sides $5$ cm each.",
    "Steps: draw $BC=6$; intersect arcs of radius 5 cm from $B$ and $C$ at $A$; join.",
    [
        {"rule": "Base", "why": "Draw $BC=6$ cm.", "math": "BC=6"},
        {"rule": "Apex", "why": "Arcs radius 5 from $B$ and $C$.", "math": "AB=AC=5"},
    ],
    "SSS arc intersection at apex.",
))

BATCH.append(q(14, 5,
    "Construct a square with side $4.5$ cm and verify diagonals.",
    "Steps: draw $AB=4.5$; $90°$ at $A,B$; cut 4.5 cm to $D,C$; join. Diagonal $\\approx 6.36$ cm.",
    [
        {"rule": "Base", "why": "AB=4.5 cm.", "math": "AB=4.5"},
        {"rule": "Right angles", "why": "Construct $90°$ at $A$ and $B$.", "math": "AD=BC=4.5"},
        {"rule": "Verify diagonal", "why": "$\\sqrt{4.5^2+4.5^2}$.", "math": "\\approx 6.36 \\text{ cm}"},
    ],
    "Square side 4.5 cm; diagonal ≈ 6.36 cm.",
))

BATCH.append(q(14, 6,
    "Construct a rectangle with length $7$ cm and breadth $5$ cm. Construct and measure diagonals.",
    "Steps: $AB=7$; $90°$ at $A,B$; cut 5 cm to $D,C$; join. Diagonal $\\approx 8.6$ cm.",
    [
        {"rule": "Base", "why": "$AB=7$ cm.", "math": "AB=7"},
        {"rule": "Breadth", "why": "$90°$ arms; $AD=BC=5$.", "math": "5 \\text{ cm}"},
        {"rule": "Diagonal", "why": "$\\sqrt{7^2+5^2}=\\sqrt{74}$.", "math": "\\approx 8.6 \\text{ cm}"},
    ],
    "Rectangle 7×5 cm; diagonal ≈ 8.6 cm.",
))

BATCH.append(q(14, 7,
    "Construct a triangle with sides $5$ cm, $6$ cm, $7$ cm and then construct its circumcircle.",
    "Steps: SSS triangle; perpendicular bisectors of two sides meet at circumcenter $O$; draw circle through $A$.",
    [
        {"rule": "Triangle", "why": "Base 7 cm; arcs 5 and 6 cm.", "math": "BC=7,\\; AB=5,\\; AC=6"},
        {"rule": "Circumcenter", "why": "Intersection of perpendicular bisectors.", "math": "O"},
        {"rule": "Circumcircle", "why": "Radius $OA$.", "math": "Circle through A, B, C"},
    ],
    "SSS triangle + perpendicular bisectors → circumcircle.",
))

BATCH.append(q(14, 8,
    "Using ruler and compass only, construct a $75°$ angle and bisect it.",
    "Steps: build $60°+15°=75°$; bisect to get two $37.5°$ angles.",
    [
        {"rule": "$75°$ angle", "why": "$60°$ + bisected gap to $90°$ gives $15°$ more.", "math": "60°+15°=75°"},
        {"rule": "Bisect", "why": "Standard angle bisector construction.", "math": "37.5° \\text{ each}"},
    ],
    "75° via 60°+15°; bisect → 37.5° each.",
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
        if "Batch 4" not in title:
            title = (title + " & 4") if "Batch" in title else f"{META[ch][2]} · Batch 4"
    else:
        questions = new_questions
        title = f"{META[ch][2]} · Batch 4"

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

    total = 0
    for ch in sorted(by_ch):
        if not by_ch[ch]:
            continue
        added, count = merge_chapter(ch, by_ch[ch])
        total += added
        print(f"Chapter {ch}: added {added} batch-4 questions (total {count})")
    print(f"Total added: {total}")


if __name__ == "__main__":
    main()
