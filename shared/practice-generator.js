/* Random rational-number MCQs for textbook practice (browser-only session). */
(function (root) {
  function gcd(a, b) {
    a = Math.abs(a); b = Math.abs(b);
    while (b) { const t = b; b = a % b; a = t; }
    return a || 1;
  }

  function lcm(a, b) {
    return Math.abs(a * b) / gcd(a, b);
  }

  function simplify(n, d) {
    if (d < 0) { n = -n; d = -d; }
    const g = gcd(n, d);
    return { n: n / g, d: d / g };
  }

  function frac(n, d) {
    const s = simplify(n, d);
    if (s.d === 1) return `$${s.n}$`;
    return `$\\dfrac{${s.n}}{${s.d}}$`;
  }

  function shuffle(arr) {
    const a = arr.slice();
    for (let i = a.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [a[i], a[j]] = [a[j], a[i]];
    }
    return a;
  }

  function pickDenom(min, max) {
    return min + Math.floor(Math.random() * (max - min + 1));
  }

  function pickNum(d) {
    const sign = Math.random() < 0.35 ? -1 : 1;
    return sign * (1 + Math.floor(Math.random() * (d - 1)));
  }

  function makeMcq(question, answer, wrongPool, steps, subtopic, chapterNum, linkedNoteId) {
    const wrong = wrongPool.filter((w, i, a) => w !== answer && a.indexOf(w) === i);
    while (wrong.length < 3) wrong.push(wrong.length ? wrong[0] : "none of these");
    const options = shuffle([answer, ...wrong.slice(0, 3)]);
    return {
      chapter: chapterNum,
      topicId: "math-ch" + chapterNum,
      type: "mcq",
      subtopic: subtopic,
      question,
      options,
      correctOption: options.indexOf(answer),
      answer,
      glassboxSteps: steps,
      linked_note_id: linkedNoteId || "",
      source: "session-generated",
    };
  }

  function buildSameDenomAdd(chapterNum, linkedNoteId) {
    const d = pickDenom(5, 40);
    const n1 = 1 + Math.floor(Math.random() * (d - 2));
    const n2 = 1 + Math.floor(Math.random() * (d - 2));
    const sum = n1 + n2;
    const ans = frac(sum, d);
    return makeMcq(
      `Simplify: ${frac(n1, d)} + ${frac(n2, d)}`,
      ans,
      [frac(n1, d + 1), frac(Math.max(1, sum - 1), d), frac(sum + 1, d), frac(n1 + n2, d + 1)],
      [
        { rule: "Denominators match", why: `The denominators are already the same (${d}). Keep the denominator as is.`, math: `$\\dfrac{${n1}}{${d}}+\\dfrac{${n2}}{${d}}$` },
        { rule: "Add numerators", why: `Combine the top numbers: ${n1} + ${n2} = ${sum}.`, math: `$\\dfrac{${sum}}{${d}}$` },
      ],
      "Generated · Addition (same denominator)",
      chapterNum, linkedNoteId
    );
  }

  function buildSameDenomSub(chapterNum, linkedNoteId) {
    const d = pickDenom(6, 40);
    const n1 = 2 + Math.floor(Math.random() * (d - 2));
    const n2 = 1 + Math.floor(Math.random() * (n1 - 1));
    const diff = n1 - n2;
    const ans = frac(diff, d);
    return makeMcq(
      `Simplify: ${frac(n1, d)} - ${frac(n2, d)}`,
      ans,
      [frac(n1, d + 1), frac(diff + 1, d), frac(Math.max(1, diff - 1), d), frac(n1 + n2, d)],
      [
        { rule: "Denominators match", why: `The denominators are already the same (${d}). Keep the denominator as is.`, math: `$\\dfrac{${n1}}{${d}}-\\dfrac{${n2}}{${d}}$` },
        { rule: "Subtract numerators", why: `Subtract the top numbers: ${n1} - ${n2} = ${diff}.`, math: `$\\dfrac{${diff}}{${d}}$` },
      ],
      "Generated · Subtraction (same denominator)",
      chapterNum, linkedNoteId
    );
  }

  function buildDiffDenomAdd(chapterNum, linkedNoteId) {
    let d1 = pickDenom(3, 12);
    let d2 = pickDenom(3, 12);
    while (d1 === d2) d2 = pickDenom(3, 12);
    const n1 = pickNum(d1);
    const n2 = pickNum(d2);
    const L = lcm(d1, d2);
    const sumN = n1 * (L / d1) + n2 * (L / d2);
    const s = simplify(sumN, L);
    const ans = frac(s.n, s.d);
    return makeMcq(
      `Simplify: ${frac(n1, d1)} + ${frac(n2, d2)}`,
      ans,
      [frac(n1 + n2, d1 + d2), frac(sumN, L), frac(sumN + 1, L), frac(Math.max(1, sumN - 1), L)],
      [
        { rule: "LCM", why: `Common denominator is ${L}.`, math: `$\\dfrac{${n1}}{${d1}}+\\dfrac{${n2}}{${d2}}$` },
        { rule: "Convert & add", why: "Rewrite with the LCM, then add numerators.", math: `$\\dfrac{${sumN}}{${L}}$` },
        { rule: "Result", why: "Simplify if needed.", math: `$\\dfrac{${s.n}}{${s.d}}$` },
      ],
      "Generated · Addition (different denominators)",
      chapterNum, linkedNoteId
    );
  }

  function buildDiffDenomSub(chapterNum, linkedNoteId) {
    let d1 = pickDenom(4, 12);
    let d2 = pickDenom(3, 10);
    while (d1 === d2) d2 = pickDenom(3, 10);
    let n1 = pickNum(d1);
    let n2 = pickNum(d2);
    if (Math.abs(n1) * d2 <= Math.abs(n2) * d1) n1 = Math.abs(n1) + d1;
    const L = lcm(d1, d2);
    const diffN = n1 * (L / d1) - n2 * (L / d2);
    const s = simplify(diffN, L);
    const ans = frac(s.n, s.d);
    return makeMcq(
      `Simplify: ${frac(n1, d1)} - ${frac(n2, d2)}`,
      ans,
      [frac(n1 - n2, d1 + d2), frac(diffN, L), frac(diffN + 1, L), frac(n1 + n2, L)],
      [
        { rule: "LCM", why: `Common denominator is ${L}.`, math: `$\\dfrac{${n1}}{${d1}}-\\dfrac{${n2}}{${d2}}$` },
        { rule: "Convert & subtract", why: "Rewrite with the LCM, then subtract numerators.", math: `$\\dfrac{${diffN}}{${L}}$` },
        { rule: "Result", why: "Simplify if needed.", math: `$\\dfrac{${s.n}}{${s.d}}$` },
      ],
      "Generated · Subtraction (different denominators)",
      chapterNum, linkedNoteId
    );
  }

  function buildMultiply(chapterNum, linkedNoteId) {
    const d1 = pickDenom(2, 9);
    const d2 = pickDenom(2, 9);
    const n1 = pickNum(d1);
    const n2 = pickNum(d2);
    const prod = n1 * n2;
    const den = d1 * d2;
    const s = simplify(prod, den);
    const ans = frac(s.n, s.d);
    return makeMcq(
      `Simplify: ${frac(n1, d1)} \\times ${frac(n2, d2)}`,
      ans,
      [frac(n1 + n2, d1 + d2), frac(prod, den), frac(prod + 1, den), frac(n1 * n2, d1 + d2)],
      [
        { rule: "Multiply", why: "Multiply numerators and denominators.", math: `$\\dfrac{${n1}}{${d1}} \\times \\dfrac{${n2}}{${d2}} = \\dfrac{${prod}}{${den}}$` },
        { rule: "Result", why: "Simplify if needed.", math: `$\\dfrac{${s.n}}{${s.d}}$` },
      ],
      "Generated · Multiplication",
      chapterNum, linkedNoteId
    );
  }

  function buildDivide(chapterNum, linkedNoteId) {
    const d1 = pickDenom(2, 9);
    const d2 = pickDenom(2, 9);
    const n1 = pickNum(d1);
    let n2 = pickNum(d2);
    if (n2 === 0) n2 = 1;
    const prod = n1 * d2;
    const den = d1 * n2;
    const s = simplify(prod, den);
    const ans = frac(s.n, s.d);
    return makeMcq(
      `Simplify: ${frac(n1, d1)} \\div ${frac(n2, d2)}`,
      ans,
      [frac(n1 * n2, d1 * d2), frac(prod, den), frac(n1, d1), frac(d2, n2)],
      [
        { rule: "Reciprocal", why: "Division is multiplication by the reciprocal.", math: `$\\dfrac{${n1}}{${d1}} \\div \\dfrac{${n2}}{${d2}} = \\dfrac{${n1}}{${d1}} \\times \\dfrac{${d2}}{${n2}}$` },
        { rule: "Multiply", why: "Multiply numerators and denominators.", math: `$\\dfrac{${prod}}{${den}}$` },
        { rule: "Result", why: "Simplify if needed.", math: `$\\dfrac{${s.n}}{${s.d}}$` },
      ],
      "Generated · Division",
      chapterNum, linkedNoteId
    );
  }

  function buildAdditiveInverse(chapterNum, linkedNoteId) {
    const d = pickDenom(3, 15);
    const n = pickNum(d);
    const ans = frac(-n, d);
    return makeMcq(
      `Additive inverse of ${frac(n, d)} is`,
      ans,
      [frac(n, d), frac(d, n), frac(-d, n), frac(n, -d)],
      [
        { rule: "Definition", why: "The additive inverse of $a$ is $-a$, so that $a + (-a) = 0$.", math: `-(${n}/${d})` },
        { rule: "Result", why: "Change the sign.", math: `$\\dfrac{${-n}}{${d}}$` },
      ],
      "Generated · Additive inverse",
      chapterNum, linkedNoteId
    );
  }

  function buildMultiplicativeInverse(chapterNum, linkedNoteId) {
    const d = pickDenom(3, 15);
    let n = pickNum(d);
    if (n === 0) n = 1;
    const ans = frac(d, n);
    const wrongN = frac(-d, n);
    return makeMcq(
      `Multiplicative inverse of ${frac(n, d)} is`,
      ans,
      [frac(n, d), wrongN, frac(-n, d), frac(d, -n)],
      [
        { rule: "Definition", why: "The reciprocal of $\\dfrac{a}{b}$ is $\\dfrac{b}{a}$ (for $a \\neq 0$).", math: `$\\dfrac{${n}}{${d}} \\times \\dfrac{${d}}{${n}} = 1$` },
        { rule: "Result", why: "Flip the fraction.", math: `$\\dfrac{${d}}{${n}}$` },
      ],
      "Generated · Multiplicative inverse",
      chapterNum, linkedNoteId
    );
  }

  function buildProductWithReciprocal(chapterNum, linkedNoteId) {
    const d = pickDenom(3, 12);
    const n = pickNum(d);
    return makeMcq(
      `Product of ${frac(n, d)} and its reciprocal is`,
      "1",
      ["0", "-1", frac(n, d), "none of these"],
      [
        { rule: "Definition", why: "A number times its reciprocal equals 1.", math: `$\\dfrac{${n}}{${d}} \\times \\dfrac{${d}}{${n}} = 1$` },
        { rule: "Result", why: "The product is always 1.", math: "1" },
      ],
      "Generated · Product with reciprocal",
      chapterNum, linkedNoteId
    );
  }

  function buildSumWithAdditiveInverse(chapterNum, linkedNoteId) {
    const d = pickDenom(3, 12);
    const n = pickNum(d);
    return makeMcq(
      `Sum of ${frac(n, d)} and its additive inverse is`,
      "0",
      ["1", "-1", frac(n, d), "none of these"],
      [
        { rule: "Definition", why: "A number plus its additive inverse equals 0.", math: `$\\dfrac{${n}}{${d}} + \\left(-\\dfrac{${n}}{${d}}\\right) = 0$` },
        { rule: "Result", why: "The sum is always 0.", math: "0" },
      ],
      "Generated · Sum with additive inverse",
      chapterNum, linkedNoteId
    );
  }

  function buildCompare(chapterNum, linkedNoteId) {
    const d1 = pickDenom(3, 10);
    let d2 = pickDenom(3, 10);
    while (d1 === d2) d2 = pickDenom(3, 10);
    const n1 = pickNum(d1);
    const n2 = pickNum(d2);
    const v1 = n1 / d1;
    const v2 = n2 / d2;
    const bigger = v1 > v2 ? frac(n1, d1) : frac(n2, d2);
    const smaller = v1 > v2 ? frac(n2, d2) : frac(n1, d1);
    return makeMcq(
      `Which is greater: ${frac(n1, d1)} or ${frac(n2, d2)}?`,
      bigger,
      [smaller, frac(n1 + n2, d1 + d2), "Both are equal", "Cannot compare"],
      [
        { rule: "Compare", why: "Convert to common denominator or compare cross-products.", math: `$\\dfrac{${n1}}{${d1}} ${v1 > v2 ? ">" : v1 < v2 ? "<" : "="} \\dfrac{${n2}}{${d2}}$` },
        { rule: "Result", why: "The greater rational number.", math: bigger.replace(/\$/g, "") },
      ],
      "Generated · Comparison",
      chapterNum, linkedNoteId
    );
  }

  const ALL_KINDS = [
    "same_add", "same_sub", "diff_add", "diff_sub",
    "multiply", "divide",
    "additive_inverse", "multiplicative_inverse",
    "product_reciprocal", "sum_additive_inverse",
    "compare",
  ];

  const BUILDERS = {
    same_add: buildSameDenomAdd,
    same_sub: buildSameDenomSub,
    diff_add: buildDiffDenomAdd,
    diff_sub: buildDiffDenomSub,
    multiply: buildMultiply,
    divide: buildDivide,
    additive_inverse: buildAdditiveInverse,
    multiplicative_inverse: buildMultiplicativeInverse,
    product_reciprocal: buildProductWithReciprocal,
    sum_additive_inverse: buildSumWithAdditiveInverse,
    compare: buildCompare,
    mixed: (ch, note) => {
      const k = ALL_KINDS[Math.floor(Math.random() * ALL_KINDS.length)];
      return BUILDERS[k](ch, note);
    },
    mixed_all: (ch, note) => BUILDERS.mixed(ch, note),
  };

  function generate(count, kind, chapterNum, linkedNoteId) {
    const build = BUILDERS[kind] || BUILDERS.mixed_all;
    const batch = Date.now();
    const out = [];
    for (let i = 0; i < count; i++) {
      const q = build(chapterNum, linkedNoteId);
      q.id = "Q-SESS-" + batch + "-" + i + "-" + Math.random().toString(36).slice(2, 6);
      out.push(q);
    }
    return out;
  }

  root.PracticeGenerator = { generate, BUILDERS, ALL_KINDS };
})(typeof window !== "undefined" ? window : globalThis);
