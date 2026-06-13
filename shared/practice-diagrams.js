/** Inline SVG diagrams for Gemini practice questions (keyed by diagram id). */
const PRACTICE_DIAGRAMS = {
  "cone-net": `<svg viewBox="0 0 320 200" width="320" height="200" aria-label="Net of a cone">
    <circle cx="70" cy="100" r="36" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
    <text x="70" y="104" text-anchor="middle" font-size="11" fill="#1e40af">r=3</text>
    <path d="M160 30 A80 80 0 0 1 160 170 L160 100 Z" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
    <line x1="160" y1="30" x2="160" y2="100" stroke="#b45309" stroke-width="1.5" stroke-dasharray="4"/>
    <text x="175" y="55" font-size="11" fill="#92400e">slant=5</text>
    <text x="120" y="190" font-size="12" fill="#334155">Circle base + sector (party-hat net)</text>
  </svg>`,

  "hex-pyramid": `<svg viewBox="0 0 260 200" width="260" height="200" aria-label="Hexagonal pyramid">
    <polygon points="130,25 210,65 210,135 130,175 50,135 50,65" fill="#e0e7ff" stroke="#4338ca" stroke-width="2"/>
    <polygon points="130,25 210,65 130,100" fill="#c7d2fe" stroke="#4338ca" stroke-width="1.5"/>
    <polygon points="130,25 50,65 130,100" fill="#a5b4fc" stroke="#4338ca" stroke-width="1.5"/>
    <circle cx="130" cy="25" r="4" fill="#dc2626"/>
    <text x="138" y="20" font-size="10" fill="#334155">apex</text>
    <text x="20" y="195" font-size="11" fill="#334155">F=7, V=7, E=12</text>
  </svg>`,

  "isometric-cuboid-4x3x2": `<svg viewBox="0 0 280 200" width="280" height="200" aria-label="Isometric cuboid 4 by 3 by 2">
    <polygon points="80,140 180,90 180,150 80,200" fill="#bfdbfe" stroke="#2563eb" stroke-width="2"/>
    <polygon points="80,140 120,120 220,70 180,90" fill="#93c5fd" stroke="#2563eb" stroke-width="2"/>
    <polygon points="180,90 220,70 220,130 180,150" fill="#60a5fa" stroke="#2563eb" stroke-width="2"/>
    <text x="125" y="210" font-size="11" fill="#334155">4 × 3 × 2 units (isometric)</text>
  </svg>`,

  "square-pyramid": `<svg viewBox="0 0 240 200" width="240" height="200" aria-label="Square pyramid">
    <polygon points="60,150 180,150 120,40" fill="#fde68a" stroke="#b45309" stroke-width="2"/>
    <polygon points="60,150 180,150 180,170 60,170" fill="#fcd34d" stroke="#b45309" stroke-width="2"/>
    <text x="50" y="190" font-size="11" fill="#334155">F=5, V=5, E=8 → Euler verified</text>
  </svg>`,

  "trapezium-area": `<svg viewBox="0 0 300 160" width="300" height="160" aria-label="Trapezium with parallel sides and height">
    <polygon points="60,120 240,120 200,40 100,40" fill="#ecfccb" stroke="#65a30d" stroke-width="2"/>
    <line x1="100" y1="40" x2="100" y2="120" stroke="#dc2626" stroke-width="1.5" stroke-dasharray="5"/>
    <text x="88" y="85" font-size="11" fill="#dc2626">h</text>
    <text x="115" y="135" font-size="11" fill="#334155">a</text>
    <text x="205" y="135" font-size="11" fill="#334155">b</text>
    <text x="70" y="30" font-size="11" fill="#334155">Area = ½(a+b)×h</text>
  </svg>`,

  "polygon-house-coords": `<svg viewBox="0 0 220 200" width="220" height="200" aria-label="Polygon house shape on coordinate grid">
    <line x1="20" y1="170" x2="200" y2="170" stroke="#94a3b8"/><line x1="20" y1="170" x2="20" y2="20" stroke="#94a3b8"/>
    <polygon points="20,170 100,170 100,110 60,50 20,110" fill="#fef9c3" stroke="#ca8a04" stroke-width="2"/>
    <circle cx="20" cy="170" r="3" fill="#dc2626"/><text x="8" y="185" font-size="10">(0,0)</text>
    <circle cx="100" cy="170" r="3" fill="#dc2626"/><text x="92" y="185" font-size="10">(4,0)</text>
    <circle cx="100" cy="110" r="3" fill="#dc2626"/><text x="92" y="105" font-size="10">(4,3)</text>
    <circle cx="60" cy="50" r="3" fill="#dc2626"/><text x="52" y="45" font-size="10">(2,5)</text>
    <circle cx="20" cy="110" r="3" fill="#dc2626"/><text x="4" y="105" font-size="10">(0,3)</text>
  </svg>`,

  "regular-hexagon": `<svg viewBox="0 0 200 200" width="200" height="200" aria-label="Regular hexagon split into triangles">
    <polygon points="100,20 170,60 170,140 100,180 30,140 30,60" fill="#ddd6fe" stroke="#7c3aed" stroke-width="2"/>
    <line x1="100" y1="20" x2="100" y2="180" stroke="#7c3aed" stroke-dasharray="4"/>
    <line x1="30" y1="60" x2="170" y2="140" stroke="#7c3aed" stroke-dasharray="4"/>
    <line x1="170" y1="60" x2="30" y2="140" stroke="#7c3aed" stroke-dasharray="4"/>
    <text x="55" y="195" font-size="11" fill="#334155">6 equilateral triangles</text>
  </svg>`,

  "rhombus-diagonals": `<svg viewBox="0 0 220 180" width="220" height="180" aria-label="Rhombus with diagonals">
    <polygon points="110,20 200,90 110,160 20,90" fill="#fce7f3" stroke="#db2777" stroke-width="2"/>
    <line x1="110" y1="20" x2="110" y2="160" stroke="#dc2626" stroke-width="1.5"/>
    <line x1="20" y1="90" x2="200" y2="90" stroke="#2563eb" stroke-width="1.5"/>
    <text x="112" y="95" font-size="10" fill="#dc2626">d₁</text>
    <text x="185" y="88" font-size="10" fill="#2563eb">d₂</text>
    <text x="45" y="175" font-size="11" fill="#334155">Area = ½ d₁ d₂</text>
  </svg>`,

  "polygon-pentagon-coords": `<svg viewBox="0 0 240 200" width="240" height="200" aria-label="Irregular pentagon on grid">
    <polygon points="30,160 120,160 180,100 140,40 30,100" fill="#e0f2fe" stroke="#0284c7" stroke-width="2"/>
    <text x="20" y="175" font-size="9">A(1,1)</text><text x="110" y="175" font-size="9">B(4,1)</text>
    <text x="170" y="95" font-size="9">C(6,4)</text><text x="130" y="35" font-size="9">D(4,7)</text><text x="15" y="95" font-size="9">E(1,4)</text>
  </svg>`,

  "polygon-split-coords": `<svg viewBox="0 0 260 200" width="260" height="200" aria-label="Polygon split into trapezium and triangle">
    <polygon points="20,170 140,170 200,110 120,50 20,110" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
    <line x1="20" y1="110" x2="200" y2="110" stroke="#dc2626" stroke-dasharray="5"/>
    <text x="60" y="145" font-size="10" fill="#334155">trapezium</text>
    <text x="130" y="85" font-size="10" fill="#334155">triangle</text>
  </svg>`,

  "cuboid-dims": `<svg viewBox="0 0 280 200" width="280" height="200" aria-label="Cuboid dimensions">
    <polygon points="70,150 190,90 190,130 70,190" fill="#bbf7d0" stroke="#16a34a" stroke-width="2"/>
    <polygon points="70,150 100,135 220,75 190,90" fill="#86efac" stroke="#16a34a" stroke-width="2"/>
    <polygon points="190,90 220,75 220,115 190,130" fill="#4ade80" stroke="#16a34a" stroke-width="2"/>
    <text x="120" y="205" font-size="11" fill="#334155">L × B × H</text>
  </svg>`,

  "cylinder-tank": `<svg viewBox="0 0 200 220" width="200" height="220" aria-label="Cylinder tank">
    <ellipse cx="100" cy="40" rx="55" ry="15" fill="#bae6fd" stroke="#0284c7" stroke-width="2"/>
    <rect x="45" y="40" width="110" height="140" fill="#e0f2fe" stroke="#0284c7" stroke-width="2"/>
    <ellipse cx="100" cy="180" rx="55" ry="15" fill="#7dd3fc" stroke="#0284c7" stroke-width="2"/>
    <text x="60" y="115" font-size="11" fill="#0369a1">h</text>
    <text x="115" y="35" font-size="11" fill="#0369a1">r</text>
    <text x="45" y="210" font-size="11" fill="#334155">V = πr²h</text>
  </svg>`,

  "bar-graph-classes": `<svg viewBox="0 0 320 200" width="320" height="200" aria-label="Bar graph of students by class">
    <line x1="40" y1="170" x2="300" y2="170" stroke="#64748b" stroke-width="2"/>
    <line x1="40" y1="30" x2="40" y2="170" stroke="#64748b" stroke-width="2"/>
    <rect x="55" y="70" width="35" height="100" fill="#6366f1"/><text x="62" y="185" font-size="10">6</text>
    <rect x="105" y="80" width="35" height="90" fill="#8b5cf6"/><text x="112" y="185" font-size="10">7</text>
    <rect x="155" y="90" width="35" height="80" fill="#a855f7"/><text x="162" y="185" font-size="10">8</text>
    <rect x="205" y="105" width="35" height="65" fill="#d946ef"/><text x="212" y="185" font-size="10">9</text>
    <rect x="255" y="120" width="35" height="50" fill="#ec4899"/><text x="262" y="185" font-size="10">10</text>
    <text x="120" y="20" font-size="12" fill="#334155">Students per class</text>
  </svg>`,

  "pie-chart-books": `<svg viewBox="0 0 220 220" width="220" height="220" aria-label="Pie chart of books read">
    <circle cx="110" cy="110" r="80" fill="#f8fafc" stroke="#cbd5e1"/>
    <path d="M110 110 L110 30 A80 80 0 0 1 186 74 Z" fill="#fca5a5"/>
    <path d="M110 110 L186 74 A80 80 0 0 1 170 170 Z" fill="#fdba74"/>
    <path d="M110 110 L170 170 A80 80 0 0 1 34 170 Z" fill="#86efac"/>
    <path d="M110 110 L34 170 A80 80 0 0 1 110 30 Z" fill="#93c5fd"/>
    <text x="55" y="210" font-size="10" fill="#334155">0 / 1-2 / 3-5 / 5+ books</text>
  </svg>`,

  "histogram-frequency": `<svg viewBox="0 0 320 200" width="320" height="200" aria-label="Histogram with touching bars">
    <line x1="40" y1="170" x2="300" y2="170" stroke="#64748b" stroke-width="2"/>
    <line x1="40" y1="30" x2="40" y2="170" stroke="#64748b" stroke-width="2"/>
    <rect x="40" y="120" width="50" height="50" fill="#38bdf8" stroke="#0284c7"/>
    <rect x="90" y="90" width="50" height="80" fill="#38bdf8" stroke="#0284c7"/>
    <rect x="140" y="60" width="50" height="110" fill="#38bdf8" stroke="#0284c7"/>
    <rect x="190" y="45" width="50" height="125" fill="#38bdf8" stroke="#0284c7"/>
    <rect x="240" y="70" width="50" height="100" fill="#38bdf8" stroke="#0284c7"/>
    <text x="55" y="185" font-size="9">0-10</text><text x="105" y="185" font-size="9">10-20</text>
    <text x="120" y="20" font-size="12" fill="#334155">Histogram (bars touch)</text>
  </svg>`,

  "trapezium-field": `<svg viewBox="0 0 300 150" width="300" height="150" aria-label="Trapezium field">
    <polygon points="40,120 260,120 220,40 80,40" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
    <text x="100" y="135" font-size="11">25 m</text><text x="200" y="135" font-size="11">10 m</text>
    <text x="120" y="30" font-size="11" fill="#334155">Field trapezium</text>
  </svg>`,

  "venn-two-sets": `<svg viewBox="0 0 280 180" width="280" height="180" aria-label="Venn diagram two sets">
    <circle cx="105" cy="90" r="55" fill="#dbeafe" fill-opacity="0.6" stroke="#2563eb" stroke-width="2"/>
    <circle cx="175" cy="90" r="55" fill="#fecaca" fill-opacity="0.6" stroke="#dc2626" stroke-width="2"/>
    <text x="75" y="95" font-size="11">Only A</text>
    <text x="148" y="95" font-size="11">Both</text>
    <text x="195" y="95" font-size="11">Only B</text>
    <text x="90" y="170" font-size="10" fill="#64748b">Neither outside circles</text>
  </svg>`,

  "double-bar-students": `<svg viewBox="0 0 320 200" width="320" height="200" aria-label="Double bar graph">
    <line x1="40" y1="170" x2="300" y2="170" stroke="#64748b"/><line x1="40" y1="30" x2="40" y2="170" stroke="#64748b"/>
    <rect x="55" y="80" width="12" height="90" fill="#6366f1"/><rect x="69" y="95" width="12" height="75" fill="#f472b6"/>
    <rect x="105" y="70" width="12" height="100" fill="#6366f1"/><rect x="119" y="85" width="12" height="85" fill="#f472b6"/>
    <rect x="155" y="90" width="12" height="80" fill="#6366f1"/><rect x="169" y="100" width="12" height="70" fill="#f472b6"/>
    <text x="55" y="185" font-size="9">Math</text><text x="105" y="185" font-size="9">Sci</text><text x="155" y="185" font-size="9">Eng</text>
    <text x="120" y="20" font-size="11">Student A (blue) vs B (pink)</text>
  </svg>`,

  "frequency-polygon": `<svg viewBox="0 0 320 200" width="320" height="200" aria-label="Frequency polygon">
    <line x1="40" y1="170" x2="300" y2="170" stroke="#64748b"/><line x1="40" y1="30" x2="40" y2="170" stroke="#64748b"/>
    <polyline points="70,170 110,130 150,95 190,115 230,140 270,170" fill="none" stroke="#2563eb" stroke-width="2"/>
    <circle cx="110" cy="130" r="4" fill="#2563eb"/><circle cx="150" cy="95" r="4" fill="#2563eb"/>
    <circle cx="190" cy="115" r="4" fill="#2563eb"/><circle cx="230" cy="140" r="4" fill="#2563eb"/>
    <text x="100" y="195" font-size="10">Midpoints of class intervals</text>
  </svg>`,

  "pie-expenditure": `<svg viewBox="0 0 220 220" width="220" height="220" aria-label="Pie chart expenditure">
    <circle cx="110" cy="110" r="80" fill="#f8fafc" stroke="#cbd5e1"/>
    <path d="M110 110 L110 30 A80 80 0 1 1 86 186 Z" fill="#fca5a5"/>
    <path d="M110 110 L86 186 A80 80 0 0 1 30 110 Z" fill="#fdba74"/>
    <path d="M110 110 L30 110 A80 80 0 0 1 70 40 Z" fill="#86efac"/>
    <text x="45" y="210" font-size="9">Transport/Food/Educ/Rent/Others</text>
  </svg>`,

  "bar-rainfall": `<svg viewBox="0 0 300 200" width="300" height="200" aria-label="Bar graph rainfall">
    <line x1="40" y1="170" x2="280" y2="170" stroke="#64748b"/><line x1="40" y1="20" x2="40" y2="170" stroke="#64748b"/>
    <rect x="55" y="130" width="30" height="40" fill="#38bdf8"/><rect x="100" y="115" width="30" height="55" fill="#38bdf8"/>
    <rect x="145" y="95" width="30" height="75" fill="#38bdf8"/><rect x="190" y="70" width="30" height="100" fill="#38bdf8"/>
    <rect x="235" y="30" width="30" height="140" fill="#38bdf8"/>
    <text x="58" y="185" font-size="9">Jan</text><text x="103" y="185" font-size="9">Feb</text>
    <text x="148" y="185" font-size="9">Mar</text><text x="193" y="185" font-size="9">Apr</text><text x="238" y="185" font-size="9">May</text>
  </svg>`,

  "coord-rectangle": `<svg viewBox="0 0 220 220" width="220" height="220" aria-label="Coordinate rectangle">
    <line x1="110" y1="20" x2="110" y2="200" stroke="#94a3b8"/><line x1="20" y1="110" x2="200" y2="110" stroke="#94a3b8"/>
    <polygon points="150,70 70,70 70,150 150,150" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
    <circle cx="150" cy="70" r="4" fill="#dc2626"/><circle cx="70" cy="70" r="4" fill="#dc2626"/>
    <circle cx="70" cy="150" r="4" fill="#dc2626"/><circle cx="150" cy="150" r="4" fill="#dc2626"/>
    <text x="30" y="215" font-size="10">Rectangle on grid</text>
  </svg>`,

  "line-graph-linear": `<svg viewBox="0 0 260 200" width="260" height="200" aria-label="Linear graph">
    <line x1="30" y1="170" x2="240" y2="170" stroke="#64748b"/><line x1="30" y1="20" x2="30" y2="170" stroke="#64748b"/>
    <line x1="30" y1="150" x2="210" y2="30" stroke="#2563eb" stroke-width="2"/>
    <circle cx="30" cy="150" r="4" fill="#2563eb"/><circle cx="90" cy="110" r="4" fill="#2563eb"/>
    <circle cx="150" cy="70" r="4" fill="#2563eb"/>
    <text x="80" y="195" font-size="10">y = 2x + 1 (example)</text>
  </svg>`,

  "line-graph-negative-slope": `<svg viewBox="0 0 260 200" width="260" height="200" aria-label="Line with negative slope">
    <line x1="30" y1="170" x2="240" y2="170" stroke="#64748b"/><line x1="30" y1="20" x2="30" y2="170" stroke="#64748b"/>
    <line x1="30" y1="50" x2="190" y2="170" stroke="#dc2626" stroke-width="2"/>
    <circle cx="30" cy="50" r="4" fill="#dc2626"/><circle cx="190" cy="170" r="4" fill="#dc2626"/>
    <text x="70" y="195" font-size="10">y = −x + 4</text>
  </svg>`,

  "parabola-yx2": `<svg viewBox="0 0 260 200" width="260" height="200" aria-label="Parabola y equals x squared">
    <line x1="130" y1="20" x2="130" y2="180" stroke="#94a3b8"/><line x1="30" y1="170" x2="230" y2="170" stroke="#94a3b8"/>
    <path d="M50 170 Q130 20 210 170" fill="none" stroke="#7c3aed" stroke-width="2"/>
    <circle cx="130" cy="170" r="4" fill="#7c3aed"/>
    <text x="85" y="195" font-size="10">U-shaped parabola y = x²</text>
  </svg>`,

  "square-lines-symmetry": `<svg viewBox="0 0 180 180" width="180" height="180" aria-label="Square lines of symmetry">
    <rect x="40" y="40" width="100" height="100" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
    <line x1="90" y1="40" x2="90" y2="140" stroke="#dc2626" stroke-dasharray="4"/>
    <line x1="40" y1="90" x2="140" y2="90" stroke="#dc2626" stroke-dasharray="4"/>
    <line x1="40" y1="40" x2="140" y2="140" stroke="#2563eb" stroke-dasharray="4"/>
    <line x1="140" y1="40" x2="40" y2="140" stroke="#2563eb" stroke-dasharray="4"/>
    <text x="35" y="175" font-size="10">4 lines of symmetry</text>
  </svg>`,

  "triangle-lines-symmetry": `<svg viewBox="0 0 180 180" width="180" height="180" aria-label="Equilateral triangle symmetry">
    <polygon points="90,30 150,150 30,150" fill="#ddd6fe" stroke="#7c3aed" stroke-width="2"/>
    <line x1="90" y1="30" x2="90" y2="150" stroke="#dc2626" stroke-dasharray="4"/>
    <line x1="30" y1="150" x2="120" y2="90" stroke="#2563eb" stroke-dasharray="4"/>
    <line x1="150" y1="150" x2="60" y2="90" stroke="#16a34a" stroke-dasharray="4"/>
    <text x="25" y="175" font-size="10">3 lines of symmetry</text>
  </svg>`,

  "hexagon-lines-symmetry": `<svg viewBox="0 0 200 200" width="200" height="200" aria-label="Regular hexagon symmetry">
    <polygon points="100,25 165,62 165,138 100,175 35,138 35,62" fill="#ecfccb" stroke="#65a30d" stroke-width="2"/>
    <line x1="100" y1="25" x2="100" y2="175" stroke="#dc2626" stroke-dasharray="4"/>
    <line x1="35" y1="62" x2="165" y2="138" stroke="#2563eb" stroke-dasharray="4"/>
    <line x1="165" y1="62" x2="35" y2="138" stroke="#2563eb" stroke-dasharray="4"/>
    <text x="30" y="195" font-size="10">6 lines of symmetry</text>
  </svg>`,

  "reflect-letter-a": `<svg viewBox="0 0 200 160" width="200" height="160" aria-label="Letter A reflection">
    <line x1="100" y1="20" x2="100" y2="140" stroke="#64748b" stroke-dasharray="5"/>
    <text x="72" y="100" font-size="48" font-family="serif" fill="#2563eb">A</text>
    <text x="108" y="100" font-size="48" font-family="serif" fill="#2563eb" opacity="0.5">A</text>
    <text x="55" y="155" font-size="10">Vertical mirror line</text>
  </svg>`,
};

function renderPracticeDiagram(id) {
  if (!id) return "";
  const svg = PRACTICE_DIAGRAMS[id];
  if (!svg) return `<div class="practice-diagram-missing">Diagram: ${String(id)}</div>`;
  return `<figure class="practice-diagram" role="img">${svg}</figure>`;
}

if (typeof window !== "undefined") {
  window.PRACTICE_DIAGRAMS = PRACTICE_DIAGRAMS;
  window.renderPracticeDiagram = renderPracticeDiagram;
}
