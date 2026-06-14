#!/usr/bin/env python3
"""Add Batch 5 (final) detailed solutions Q157–200 to chapter practice session files."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "chapters"

META = {
    18: ("math-ch18", "CH18-sec-visualising-solid-shapes", "Visualising Solid Shapes"),
    19: ("math-ch19", "CH19-sec-mensuration", "Mensuration"),
    20: ("math-ch20", "CH20-sec-data-handling", "Data Handling"),
}

AREA_NOTE = "CH19-sec-area-and-perimeter-of-some-plane-figures"
VOL_NOTE = "CH19-sec-volume-and-capacity"
PROB_NOTE = "CH20-sec-likely"


def q(ch, num, question, answer, steps, explanation, note_id=None):
    topic, default_note, _ = META[ch]
    return {
        "id": f"Q-CH{ch:02d}-B05-{num:03d}",
        "chapter": ch,
        "topicId": topic,
        "type": "practice",
        "subtopic": "Batch 5 · Detailed Solutions",
        "question": question,
        "answer": answer,
        "options": [],
        "glassboxSteps": steps,
        "explanation": explanation,
        "linked_note_id": note_id or default_note,
        "source": "practice-session",
    }


BATCH = []

# ── Chapter 18: Q157–164 (Representing 3-D in 2-D) ───────────────────────────

BATCH.append(q(18, 1,
    "Draw the net of a cuboid with dimensions $5$ cm $\\times$ $4$ cm $\\times$ $3$ cm. Also describe its isometric view.",
    "Net: cross of six rectangles ($5\\times4$ centre, four side faces, one lid); isometric: 3-unit vertical, 5 left, 4 right on dot grid.",
    [
        {"rule": "Net", "why": "Six faces: central $5\\times4$; top/bottom $5\\times3$; left/right $3\\times4$; one extra $5\\times4$ lid.", "math": "\\text{Fold into cuboid } 5\\times4\\times3"},
        {"rule": "Isometric", "why": "120° axes; parallel edges equal.", "math": "3 \\text{ vertical},\\; 5 \\text{ down-left},\\; 4 \\text{ down-right}"},
    ],
    "Net = six rectangles; isometric on dot paper with 5, 4, 3 units.",
))

BATCH.append(q(18, 2,
    "Sketch the front view, side view and top view of a cylinder standing on its base.",
    "Top: circle; Front & Side: identical rectangles (height $\\times$ diameter).",
    [
        {"rule": "Top view", "why": "Looking down at circular base.", "math": "\\text{circle}"},
        {"rule": "Front & side", "why": "Orthographic elevation.", "math": "\\text{rectangle: height } \\times \\text{ diameter}"},
    ],
    "Plan = circle; elevations = rectangles.",
))

BATCH.append(q(18, 3,
    "Draw the isometric sketch of a cube of edge $4$ cm.",
    "Three rhombus faces meeting at a vertex; all edges 4 units on isometric dot paper.",
    [
        {"rule": "Start", "why": "Vertical edge 4 units.", "math": "4 \\text{ down}"},
        {"rule": "Complete", "why": "4 units down-left and down-right; close parallel faces.", "math": "\\text{all edges } 4"},
    ],
    "Isometric cube: all edges 4 units.",
))

BATCH.append(q(18, 4,
    "A cube is cut into $27$ smaller equal cubes ($3\\times3\\times3$). How many small cubes have 3, 2, 1, or 0 faces painted?",
    "3 faces: 8 · 2 faces: 12 · 1 face: 6 · 0 faces: 1",
    [
        {"rule": "3 faces", "why": "Corner cubes.", "math": "8"},
        {"rule": "2 faces", "why": "Middle of each edge.", "math": "12"},
        {"rule": "1 face", "why": "Centre of each face.", "math": "6"},
        {"rule": "0 faces", "why": "Interior core: $(n-2)^3$ with $n=3$.", "math": "1"},
    ],
    "8 + 12 + 6 + 1 = 27 painted-cube count.",
))

BATCH.append(q(18, 5,
    "Draw the front elevation, side elevation and plan of a triangular prism (on rectangular base).",
    "Front: triangle; Plan: rectangle with ridge line; Side: rectangle.",
    [
        {"rule": "Front", "why": "Triangular end face.", "math": "\\triangle"},
        {"rule": "Plan", "why": "Top view shows rectangular base + ridge.", "math": "\\text{rectangle with centre line}"},
        {"rule": "Side", "why": "Rectangular face.", "math": "\\text{rectangle}"},
    ],
    "Front = triangle; plan = rectangle; side = rectangle.",
))

BATCH.append(q(18, 6,
    "Represent a cone in 2D with dimensions and shade.",
    "Isosceles triangle with elliptical base; label height $h$ and radius $r$.",
    [
        {"rule": "Outline", "why": "Triangle with curved (elliptical) base.", "math": "\\text{apex to base}"},
        {"rule": "Labels", "why": "Dashed height $h$; radius $r$ on base.", "math": "h,\\; r"},
    ],
    "2D cone: triangle + elliptical base; mark $h$ and $r$.",
))

BATCH.append(q(18, 7,
    "A solid has 6 faces, 12 edges and 8 vertices. Identify it and verify Euler's formula $V-E+F=2$.",
    "Cube or cuboid; $8-12+6=2$ verified.",
    [
        {"rule": "Identify", "why": "6 faces, 12 edges, 8 vertices.", "math": "\\text{cube/cuboid}"},
        {"rule": "Euler", "why": "Substitute values.", "math": "8-12+6=2\\; \\checkmark"},
    ],
    "Cuboid/cube; Euler formula verified.",
))

BATCH.append(q(18, 8,
    "Draw an oblique sketch of a cuboid.",
    "True front face on square grid; depth lines at $45°$; dashed hidden edges.",
    [
        {"rule": "Front face", "why": "Draw true dimensions (e.g. $5\\times3$).", "math": "\\text{rectangle}"},
        {"rule": "Depth", "why": "$45°$ receding lines connect back face.", "math": "\\text{dash hidden edges}"},
    ],
    "Oblique: true front + 45° depth lines.",
))

# ── Chapter 19: Q165–173 (Area) ──────────────────────────────────────────────

BATCH.append(q(19, 1,
    "Find the area of a trapezium whose parallel sides are $25$ cm and $15$ cm and the distance between them is $12$ cm.",
    "$240$ cm²",
    [
        {"rule": "Formula", "why": "Area $= \\frac{1}{2}(a+b)h$.", "math": "\\frac{1}{2}(25+15)\\times12"},
        {"rule": "Calculate", "why": "Simplify.", "math": "20\\times12=240 \\text{ cm}^2"},
    ],
    "Area = 240 cm².",
    note_id=AREA_NOTE,
))

BATCH.append(q(19, 2,
    "The area of a trapezium is $480$ cm² and the distance between parallel sides is $15$ cm. If one parallel side is $20$ cm, find the other.",
    "$44$ cm",
    [
        {"rule": "Substitute", "why": "Use area formula.", "math": "480=\\frac{1}{2}(20+b)\\times15"},
        {"rule": "Solve", "why": "Multiply by 2, divide by 15.", "math": "960=15(20+b) \\Rightarrow 64=20+b \\Rightarrow b=44"},
    ],
    "Other parallel side = 44 cm.",
    note_id=AREA_NOTE,
))

BATCH.append(q(19, 3,
    "Find the area of a regular hexagon with side $6$ cm.",
    "$54\\sqrt{3}$ cm²",
    [
        {"rule": "Decompose", "why": "Hexagon = 6 equilateral triangles.", "math": "A_{\\triangle}=\\frac{\\sqrt{3}}{4}s^2"},
        {"rule": "Calculate", "why": "Side $=6$.", "math": "6\\times\\frac{\\sqrt{3}}{4}\\times36=54\\sqrt{3}"},
    ],
    "Area = $54\\sqrt{3}$ cm².",
    note_id=AREA_NOTE,
))

BATCH.append(q(19, 4,
    "A field is trapezium-shaped with parallel sides $25$ m and $10$ m, and non-parallel sides $14$ m and $13$ m. Find the area.",
    "$196$ m²",
    [
        {"rule": "Divide", "why": "Drop line parallel to 13 m side → parallelogram + triangle (sides 13, 14, 15).", "math": "s=21"},
        {"rule": "Heron", "why": "Triangle area.", "math": "\\sqrt{21\\times8\\times7\\times6}=84"},
        {"rule": "Height", "why": "$84=\\frac{1}{2}\\times15\\times h$.", "math": "h=11.2"},
        {"rule": "Trapezium", "why": "Apply formula.", "math": "\\frac{1}{2}(25+10)\\times11.2=196"},
    ],
    "Area = 196 m².",
    note_id=AREA_NOTE,
))

BATCH.append(q(19, 5,
    "Find the area of an irregular polygon by dividing it into triangles and trapeziums.",
    "Split polygon with diagonals/perpendiculars; sum areas of simpler parts.",
    [
        {"rule": "Strategy", "why": "Any polygon can be triangulated.", "math": "A_{\\text{total}}=\\sum A_i"},
        {"rule": "Example", "why": "Quadrilateral → two triangles by one diagonal.", "math": "A=\\frac{1}{2}d(h_1+h_2)"},
    ],
    "Divide into triangles/trapeziums; add their areas.",
    note_id=AREA_NOTE,
))

BATCH.append(q(19, 6,
    "The diagonals of a rhombus are $16$ cm and $12$ cm. Find its area.",
    "$96$ cm²",
    [
        {"rule": "Formula", "why": "Rhombus area from diagonals.", "math": "A=\\frac{1}{2}d_1d_2"},
        {"rule": "Calculate", "why": "Substitute.", "math": "\\frac{1}{2}\\times16\\times12=96"},
    ],
    "Area = 96 cm².",
    note_id=AREA_NOTE,
))

BATCH.append(q(19, 7,
    "A parallelogram and a triangle have the same base and lie between the same parallels. Compare their areas.",
    "Triangle area is half the parallelogram area (ratio 1:2).",
    [
        {"rule": "Parallelogram", "why": "Same base and height.", "math": "A_p=bh"},
        {"rule": "Triangle", "why": "Same base and height.", "math": "A_t=\\frac{1}{2}bh"},
    ],
    "Triangle = $\\frac{1}{2}$ parallelogram.",
    note_id=AREA_NOTE,
))

BATCH.append(q(19, 8,
    "Find the area of a regular pentagon with side $8$ cm.",
    "$\\approx 110.11$ cm²",
    [
        {"rule": "Central angle", "why": "$360°/5=72°$; half-angle $36°$, half-base $4$ cm.", "math": "a=\\frac{4}{\\tan36°}\\approx5.505"},
        {"rule": "One triangle", "why": "$\\frac{1}{2}\\times8\\times a$.", "math": "\\approx22.02"},
        {"rule": "Total", "why": "Five identical triangles.", "math": "5\\times22.02\\approx110.11"},
    ],
    "Area $\\approx 110.11$ cm².",
    note_id=AREA_NOTE,
))

BATCH.append(q(19, 9,
    "A square and an equilateral triangle have equal perimeters. Compare their areas.",
    "Square has larger area ($9x^2$ vs $4\\sqrt{3}x^2$).",
    [
        {"rule": "Let perimeter", "why": "Common perimeter $12x$.", "math": "s_{\\square}=3x,\\; s_{\\triangle}=4x"},
        {"rule": "Areas", "why": "Use standard formulas.", "math": "A_{\\square}=9x^2,\\; A_{\\triangle}=4\\sqrt{3}x^2"},
        {"rule": "Compare", "why": "$9>4\\sqrt{3}\\approx6.928$.", "math": "\\text{square larger}"},
    ],
    "Square encloses more area for equal perimeter.",
    note_id=AREA_NOTE,
))

# ── Chapter 19: Q174–182 (Surface Area, Volume, Capacity) ─────────────────────

BATCH.append(q(19, 10,
    "Find the total surface area and volume of a cuboid $15$ cm $\\times$ $10$ cm $\\times$ $8$ cm.",
    "TSA $=700$ cm²; Volume $=1200$ cm³",
    [
        {"rule": "TSA", "why": "$2(lb+bh+lh)$.", "math": "2(150+80+120)=700"},
        {"rule": "Volume", "why": "$l\\times b\\times h$.", "math": "15\\times10\\times8=1200"},
    ],
    "TSA 700 cm²; volume 1200 cm³.",
    note_id=VOL_NOTE,
))

BATCH.append(q(19, 11,
    "A cube has volume $729$ cm³. Find its total surface area and edge.",
    "Edge $=9$ cm; TSA $=486$ cm²",
    [
        {"rule": "Edge", "why": "$\\sqrt[3]{729}$.", "math": "9 \\text{ cm}"},
        {"rule": "TSA", "why": "$6a^2$.", "math": "6\\times81=486"},
    ],
    "Edge 9 cm; TSA 486 cm².",
    note_id=VOL_NOTE,
))

BATCH.append(q(19, 12,
    "The curved surface area of a cylinder is $440$ cm² and its height is $10$ cm. Find its volume ($\\pi=22/7$).",
    "$1540$ cm³",
    [
        {"rule": "Find $r$", "why": "$CSA=2\\pi rh$.", "math": "440=2\\times\\frac{22}{7}\\times r\\times10 \\Rightarrow r=7"},
        {"rule": "Volume", "why": "$\\pi r^2h$.", "math": "\\frac{22}{7}\\times49\\times10=1540"},
    ],
    "Radius 7 cm; volume 1540 cm³.",
    note_id=VOL_NOTE,
))

BATCH.append(q(19, 13,
    "A cylindrical tank has radius $7$ m and height $5$ m. Find the capacity in litres ($1$ m³ $=1000$ L).",
    "$770{,}000$ litres",
    [
        {"rule": "Volume", "why": "$\\pi r^2h$.", "math": "\\frac{22}{7}\\times49\\times5=770 \\text{ m}^3"},
        {"rule": "Convert", "why": "Multiply by 1000.", "math": "770\\times1000=770{,}000"},
    ],
    "Capacity = 770,000 L.",
    note_id=VOL_NOTE,
))

BATCH.append(q(19, 14,
    "Find the total surface area of a closed cylinder whose volume is $1540$ cm³ and height is $10$ cm.",
    "$748$ cm²",
    [
        {"rule": "Radius", "why": "From volume (same as Q174).", "math": "r=7"},
        {"rule": "TSA", "why": "$2\\pi r(r+h)$.", "math": "2\\times\\frac{22}{7}\\times7\\times17=748"},
    ],
    "TSA = 748 cm².",
    note_id=VOL_NOTE,
))

BATCH.append(q(19, 15,
    "A cuboid $8$ cm $\\times$ $6$ cm $\\times$ $4$ cm is melted and recast into a cube. Find the edge of the cube.",
    "$4\\sqrt[3]{3}$ cm",
    [
        {"rule": "Volume", "why": "Volume conserved.", "math": "8\\times6\\times4=192"},
        {"rule": "Edge", "why": "$a^3=192$.", "math": "a=\\sqrt[3]{192}=4\\sqrt[3]{3}"},
    ],
    "Edge = $4\\sqrt[3]{3}$ cm (≈ 5.85 cm).",
    note_id=VOL_NOTE,
))

BATCH.append(q(19, 16,
    "The ratio of radii of two cylinders is $2:3$ and their heights are in ratio $5:4$. Find the ratio of their volumes.",
    "$5:9$",
    [
        {"rule": "Volume ratio", "why": "$V\\propto r^2h$.", "math": "\\frac{V_1}{V_2}=\\left(\\frac{2}{3}\\right)^2\\times\\frac{5}{4}"},
        {"rule": "Simplify", "why": "Cancel common factors.", "math": "\\frac{4}{9}\\times\\frac{5}{4}=\\frac{5}{9}"},
    ],
    "Volume ratio = 5:9.",
    note_id=VOL_NOTE,
))

BATCH.append(q(19, 17,
    "A rectangular tank $2.5$ m long, $1.5$ m wide and $1$ m deep is full of water. Find the volume of water in litres.",
    "$3750$ litres",
    [
        {"rule": "Volume", "why": "$l\\times b\\times h$.", "math": "2.5\\times1.5\\times1=3.75 \\text{ m}^3"},
        {"rule": "Convert", "why": "$\\times1000$.", "math": "3750 \\text{ L}"},
    ],
    "3750 litres of water.",
    note_id=VOL_NOTE,
))

BATCH.append(q(19, 18,
    "An open cylindrical drum of radius $14$ cm and height $80$ cm is full of water. How many full cylindrical glasses of radius $3.5$ cm and height $10$ cm can be filled?",
    "$128$ glasses",
    [
        {"rule": "Ratio", "why": "Divide volumes; $\\pi$ cancels.", "math": "\\frac{14^2\\times80}{3.5^2\\times10}"},
        {"rule": "Calculate", "why": "Simplify.", "math": "\\frac{196\\times80}{12.25\\times10}=128"},
    ],
    "128 full glasses.",
    note_id=VOL_NOTE,
))

# ── Chapter 20: Q183–190 (Data Handling) ─────────────────────────────────────

BATCH.append(q(20, 1,
    "Marks of 30 students (out of 50) are given. Construct a frequency distribution with class intervals $0$–$10$, $10$–$20$, etc., and describe a histogram.",
    "Tally frequencies per class; histogram: touching bars, X = intervals, Y = frequency.",
    [
        {"rule": "Frequency table", "why": "Count data in each class interval.", "math": "0\\text{–}10,\\;10\\text{–}20,\\ldots"},
        {"rule": "Histogram", "why": "Bars touch (continuous data).", "math": "\\text{height}=\\text{frequency}"},
    ],
    "Group data; draw touching rectangular bars.",
))

BATCH.append(q(20, 2,
    "From a pie chart: Food $40\\%$, Rent $25\\%$, Education $15\\%$, Others $20\\%$. If total expenditure is ₹$8000$, find each amount.",
    "Food ₹3200 · Rent ₹2000 · Education ₹1200 · Others ₹1600",
    [
        {"rule": "Food", "why": "$40\\%$ of 8000.", "math": "3200"},
        {"rule": "Rent", "why": "$25\\%$.", "math": "2000"},
        {"rule": "Education", "why": "$15\\%$.", "math": "1200"},
        {"rule": "Others", "why": "$20\\%$.", "math": "1600"},
    ],
    "₹3200 + ₹2000 + ₹1200 + ₹1600 = ₹8000.",
))

BATCH.append(q(20, 3,
    "The following data shows number of books read by students. Describe how to draw a bar graph.",
    "Bars with gaps; height proportional to count; label axes.",
    [
        {"rule": "Axes", "why": "X = categories; Y = number of books.", "math": "\\text{scale on Y-axis}"},
        {"rule": "Bars", "why": "Discrete data → equal-width bars with spaces.", "math": "\\text{height} \\propto \\text{value}"},
    ],
    "Bar graph: spaced bars for discrete categories.",
))

BATCH.append(q(20, 4,
    "Construct a frequency polygon for given data on heights of students.",
    "Plot class marks vs frequency; join points; anchor ends to X-axis.",
    [
        {"rule": "Class marks", "why": "Midpoint of each interval.", "math": "\\frac{\\text{lower+upper}}{2}"},
        {"rule": "Plot & join", "why": "Connect points; extend to zero at ends.", "math": "\\text{line segments}"},
    ],
    "Frequency polygon uses class marks on X-axis.",
))

BATCH.append(q(20, 5,
    "In a survey of 60 people, use set notation to find only tea, only coffee, given totals for tea, coffee, and both.",
    "Only tea $= n(T)-n(T\\cap C)$; Only coffee $= n(C)-n(T\\cap C)$; sum with neither $=60$.",
    [
        {"rule": "Union formula", "why": "$n(T\\cup C)=n(T)+n(C)-n(T\\cap C)$.", "math": "60=n(T)+n(C)-x+\\text{neither}"},
        {"rule": "Only sets", "why": "Subtract overlap.", "math": "\\text{only T}=n(T)-x,\\;\\text{only C}=n(C)-x"},
    ],
    "Use Venn diagram or inclusion–exclusion.",
))

BATCH.append(q(20, 6,
    "Draw a pie chart for: Cricket $45\\%$, Football $30\\%$, Hockey $15\\%$, Others $10\\%$. Calculate central angles.",
    "Cricket $162°$ · Football $108°$ · Hockey $54°$ · Others $36°$",
    [
        {"rule": "Formula", "why": "Angle $=\\frac{\\%}{100}\\times360°$.", "math": "0.45\\times360=162"},
        {"rule": "All angles", "why": "Compute each sector.", "math": "108,\\;54,\\;36"},
    ],
    "Angles: 162°, 108°, 54°, 36° (sum 360°).",
))

BATCH.append(q(20, 7,
    "The mean of 5 numbers is $18$. If one number is excluded, the mean becomes $16$. Find the excluded number.",
    "$26$",
    [
        {"rule": "Sum of 5", "why": "Mean $\\times$ count.", "math": "5\\times18=90"},
        {"rule": "Sum of 4", "why": "After exclusion.", "math": "4\\times16=64"},
        {"rule": "Excluded", "why": "Difference.", "math": "90-64=26"},
    ],
    "Excluded number = 26.",
))

BATCH.append(q(20, 8,
    "From a cumulative frequency curve (ogive), describe how to find the median.",
    "Locate $N/2$ on Y-axis; horizontal to curve; vertical to X-axis = median.",
    [
        {"rule": "Find $N/2$", "why": "Half the total frequency.", "math": "\\frac{N}{2}"},
        {"rule": "Read median", "why": "Intersect ogive; drop to X-axis.", "math": "\\text{median class mark/value}"},
    ],
    "Median from ogive via $N/2$ method.",
))

# ── Chapter 20: Q191–200 (Probability) ───────────────────────────────────────

BATCH.append(q(20, 9,
    "A bag contains 5 red, 4 blue and 3 green balls. A ball is drawn at random. Find P(red) and P(not blue).",
    "P(red) $=\\frac{5}{12}$; P(not blue) $=\\frac{2}{3}$",
    [
        {"rule": "Total", "why": "Sum all balls.", "math": "12"},
        {"rule": "Red", "why": "Favourable/total.", "math": "\\frac{5}{12}"},
        {"rule": "Not blue", "why": "Red + green = 8.", "math": "\\frac{8}{12}=\\frac{2}{3}"},
    ],
    "P(red) = 5/12; P(not blue) = 2/3.",
    note_id=PROB_NOTE,
))

BATCH.append(q(20, 10,
    "A die is thrown once. Find P(prime), P(number $>4$), P(even).",
    "P(prime) $=\\frac{1}{2}$; P($>4$) $=\\frac{1}{3}$; P(even) $=\\frac{1}{2}$",
    [
        {"rule": "Sample space", "why": "6 outcomes.", "math": "\\{1,2,3,4,5,6\\}"},
        {"rule": "Prime", "why": "$\\{2,3,5\\}$.", "math": "\\frac{3}{6}=\\frac{1}{2}"},
        {"rule": "$>4$", "why": "$\\{5,6\\}$.", "math": "\\frac{1}{3}"},
        {"rule": "Even", "why": "$\\{2,4,6\\}$.", "math": "\\frac{1}{2}"},
    ],
    "1/2, 1/3, 1/2 respectively.",
    note_id=PROB_NOTE,
))

BATCH.append(q(20, 11,
    "Two coins are tossed simultaneously. Find P(two heads), P(at least one head), P(no tail).",
    "P(HH) $=\\frac{1}{4}$; P(at least one H) $=\\frac{3}{4}$; P(no tail) $=\\frac{1}{4}$",
    [
        {"rule": "Outcomes", "why": "Four equally likely.", "math": "\\{HH,HT,TH,TT\\}"},
        {"rule": "Two heads", "why": "One outcome.", "math": "\\frac{1}{4}"},
        {"rule": "At least one H", "why": "Three outcomes.", "math": "\\frac{3}{4}"},
    ],
    "HH: 1/4; at least one head: 3/4; no tail = all heads: 1/4.",
    note_id=PROB_NOTE,
))

BATCH.append(q(20, 12,
    "A card is drawn from a well-shuffled deck of 52 cards. Find P(king), P(red queen), P(face card).",
    "P(king) $=\\frac{1}{13}$; P(red queen) $=\\frac{1}{26}$; P(face) $=\\frac{3}{13}$",
    [
        {"rule": "King", "why": "4 kings.", "math": "\\frac{4}{52}=\\frac{1}{13}"},
        {"rule": "Red queen", "why": "Hearts or Diamonds queen.", "math": "\\frac{2}{52}=\\frac{1}{26}"},
        {"rule": "Face", "why": "12 face cards.", "math": "\\frac{12}{52}=\\frac{3}{13}"},
    ],
    "1/13, 1/26, 3/13.",
    note_id=PROB_NOTE,
))

BATCH.append(q(20, 13,
    "In a class of 40 students, 25 like cricket and 15 like football. Find P(likes cricket) and P(likes football) if one student is selected at random.",
    "P(cricket) $=\\frac{5}{8}$; P(football) $=\\frac{3}{8}$",
    [
        {"rule": "Cricket", "why": "25 of 40.", "math": "\\frac{25}{40}=\\frac{5}{8}"},
        {"rule": "Football", "why": "15 of 40.", "math": "\\frac{15}{40}=\\frac{3}{8}"},
    ],
    "5/8 and 3/8.",
    note_id=PROB_NOTE,
))

BATCH.append(q(20, 14,
    "A box contains 12 balls numbered 1 to 12. Find P(even), P(multiple of 3), P(prime).",
    "P(even) $=\\frac{1}{2}$; P(mult. of 3) $=\\frac{1}{3}$; P(prime) $=\\frac{5}{12}$",
    [
        {"rule": "Even", "why": "6 even numbers.", "math": "\\frac{6}{12}=\\frac{1}{2}"},
        {"rule": "Mult. of 3", "why": "$\\{3,6,9,12\\}$.", "math": "\\frac{1}{3}"},
        {"rule": "Prime", "why": "$\\{2,3,5,7,11\\}$.", "math": "\\frac{5}{12}"},
    ],
    "1/2, 1/3, 5/12.",
    note_id=PROB_NOTE,
))

BATCH.append(q(20, 15,
    "Two dice are thrown. Find the probability that the sum is 7 or 11.",
    "$\\frac{2}{9}$",
    [
        {"rule": "Total outcomes", "why": "$6\\times6$.", "math": "36"},
        {"rule": "Sum 7", "why": "6 ways.", "math": "6"},
        {"rule": "Sum 11", "why": "2 ways.", "math": "2"},
        {"rule": "Probability", "why": "Favourable/total.", "math": "\\frac{8}{36}=\\frac{2}{9}"},
    ],
    "P(7 or 11) = 2/9.",
    note_id=PROB_NOTE,
))

BATCH.append(q(20, 16,
    "A letter is chosen at random from \"MATHEMATICS\". Find P(vowel) and P(M or T).",
    "P(vowel) $=\\frac{4}{11}$; P(M or T) $=\\frac{4}{11}$",
    [
        {"rule": "Total letters", "why": "11 letters.", "math": "11"},
        {"rule": "Vowels", "why": "A, E, A, I.", "math": "\\frac{4}{11}"},
        {"rule": "M or T", "why": "M twice, T twice.", "math": "\\frac{4}{11}"},
    ],
    "Both probabilities = 4/11.",
    note_id=PROB_NOTE,
))

BATCH.append(q(20, 17,
    "If the probability of an event is $\\frac{3}{7}$, find the probability of its complement.",
    "$\\frac{4}{7}$",
    [
        {"rule": "Complement rule", "why": "$P(E')=1-P(E)$.", "math": "1-\\frac{3}{7}=\\frac{4}{7}"},
    ],
    "P(complement) = 4/7.",
    note_id=PROB_NOTE,
))

BATCH.append(q(20, 18,
    "A bag has 3 white, 4 black and 5 red balls. Three balls are drawn without replacement. Find P(all white).",
    "$\\frac{1}{220}$ (single white draw: $\\frac{1}{4}$)",
    [
        {"rule": "Draw 1", "why": "3 white of 12.", "math": "\\frac{3}{12}"},
        {"rule": "Draw 2", "why": "2 white of 11.", "math": "\\frac{2}{11}"},
        {"rule": "Draw 3", "why": "1 white of 10.", "math": "\\frac{1}{10}"},
        {"rule": "Multiply", "why": "Dependent events.", "math": "\\frac{3}{12}\\times\\frac{2}{11}\\times\\frac{1}{10}=\\frac{1}{220}"},
    ],
    "All three white (no replacement) = 1/220.",
    note_id=PROB_NOTE,
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
        if "Batch 5" not in title:
            title = (title + " & 5") if "Batch" in title else f"{META[ch][2]} · Batch 5"
    else:
        questions = new_questions
        title = f"{META[ch][2]} · Batch 5"

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
        print(f"Chapter {ch}: added {added} batch-5 questions (total {count})")
    print(f"Total added: {total}")


if __name__ == "__main__":
    main()
