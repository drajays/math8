/* Self-contained LaTeX renderer (fractions, roots, super/subscripts) — no external deps. */
(function (root) {
  const SYM = {
    times: "×", div: "÷", cdot: "·", pm: "±", mp: "∓", approx: "≈",
    le: "≤", ge: "≥", leq: "≤", geq: "≥", neq: "≠", ne: "≠",
    angle: "∠", checkmark: "✓", varnothing: "∅", emptyset: "∅",
    cup: "∪", cap: "∩", in: "∈", notin: "∉", subset: "⊂", subseteq: "⊆",
    pi: "π", Rightarrow: "⇒", rightarrow: "→", to: "→", implies: "⇒",
    longrightarrow: "⟶", longleftarrow: "⟵", leftarrow: "←", mapsto: "↦", gets: "←",
    ldots: "…", dots: "…", cdots: "⋯", sum: "∑", prod: "∏",
    triangle: "△", bigcirc: "◯", circ: "∘", times2: "×",
    alpha: "α", beta: "β", theta: "θ", lambda: "λ", Delta: "Δ",
    gcd: "gcd", lcm: "lcm", min: "min", max: "max", mod: "mod",
    infty: "∞", sqrt: "√", quad: "\u2003", qquad: "\u2003\u2003",
  };
  const SPACE = { ";": "\u2005", ",": "\u2009", ":": "\u2005", "!": "", " ": "\u2002" };

  function esc(s) { return s.replace(/[&<>]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;" }[c])); }

  function readGroup(s, i) {
    while (s[i] === " ") i++;
    if (s[i] === "{") {
      let depth = 1, j = i + 1, start = j;
      while (j < s.length && depth > 0) { if (s[j] === "{") depth++; else if (s[j] === "}") depth--; if (depth === 0) break; j++; }
      return { body: s.slice(start, j), next: j + 1 };
    }
    if (s[i] === "\\") {
      let j = i + 1; if (/[a-zA-Z]/.test(s[j])) { while (j < s.length && /[a-zA-Z]/.test(s[j])) j++; }
      else j = i + 2;
      return { body: s.slice(i, j), next: j };
    }
    return { body: s[i] || "", next: i + 1 };
  }

  function render(tex) {
    if (tex == null) return "";
    let s = String(tex);
    s = s.replace(/\^\\circ/g, "°").replace(/\^\{\\circ\}/g, "°").replace(/\^circ/g, "°");
    let out = "", i = 0;
    while (i < s.length) {
      const c = s[i];
      if (c === "\\") {
        let j = i + 1, name = "";
        if (/[a-zA-Z]/.test(s[j])) { while (j < s.length && /[a-zA-Z]/.test(s[j])) { name += s[j]; j++; } }
        else {
          const ch = s[j];
          if (SPACE[ch] !== undefined) { out += SPACE[ch]; i = j + 1; continue; }
          out += esc(ch || ""); i = j + 1; continue;
        }
        i = j;
        if (name === "dfrac" || name === "frac" || name === "tfrac") {
          const a = readGroup(s, i); const b = readGroup(s, a.next);
          out += `<span class="mfrac"><span class="mnum">${render(a.body)}</span><span class="mden">${render(b.body)}</span></span>`;
          i = b.next; continue;
        }
        if (name === "sqrt") {
          let idx = "";
          if (s[i] === "[") { const k = s.indexOf("]", i); idx = s.slice(i + 1, k); i = k + 1; }
          const a = readGroup(s, i);
          out += `<span class="msqrt">${idx ? `<span class="mroot">${esc(idx)}</span>` : ""}<span class="mradsign">√</span><span class="mrad">${render(a.body)}</span></span>`;
          i = a.next; continue;
        }
        if (name === "text" || name === "mathrm" || name === "operatorname") {
          const a = readGroup(s, i);
          out += `<span class="mtext">${esc(a.body)}</span>`; i = a.next; continue;
        }
        if (name === "underline") { const a = readGroup(s, i); out += `<span style="text-decoration:underline">${render(a.body)}</span>`; i = a.next; continue; }
        if (name === "overline") { const a = readGroup(s, i); out += `<span style="border-top:1.4px solid currentColor;padding-top:1px">${render(a.body)}</span>`; i = a.next; continue; }
        if (name === "left" || name === "right" || name === "displaystyle") { continue; }
        if (SYM[name] !== undefined) { out += SYM[name]; continue; }
        out += "\\" + name; continue;
      }
      if (c === "^" || c === "_") {
        const a = readGroup(s, i + 1);
        out += `<${c === "^" ? "sup" : "sub"} class="m${c === "^" ? "sup" : "sub"}">${render(a.body)}</${c === "^" ? "sup" : "sub"}>`;
        i = a.next; continue;
      }
      if (c === "{" || c === "}") { i++; continue; }
      if (c === "$") { i++; continue; }
      if (/[a-zA-Z]/.test(c)) { out += `<i class="mvar">${c}</i>`; i++; continue; }
      out += esc(c); i++;
    }
    return out;
  }

  root.MathRender = { render };
  if (typeof module !== "undefined") module.exports = { render };
})(typeof window !== "undefined" ? window : this);
