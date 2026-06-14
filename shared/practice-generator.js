/* Random fraction MCQs for textbook practice (browser-only session). */
(function (root) {
  function gcd(a, b) {
    a = Math.abs(a); b = Math.abs(b);
    while (b) { const t = b; b = a % b; a = t; }
    return a || 1;
  }

  function frac(n, d) {
    return `$\\dfrac{${n}}{${d}}$`;
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

  function buildSameDenomAdd(chapterNum, linkedNoteId) {
    const d = pickDenom(5, 40);
    const n1 = 1 + Math.floor(Math.random() * (d - 2));
    const n2 = 1 + Math.floor(Math.random() * (d - 2));
    const sum = n1 + n2;
    const ans = frac(sum, d);
    const wrong = [
      frac(n1, d + 1),
      frac(Math.max(1, sum - 1), d),
      frac(sum + 1, d),
      frac(n1 + n2, d + 1),
    ].filter((w, i, a) => a.indexOf(w) === i && w !== ans);
    while (wrong.length < 3) wrong.push(frac(sum, d + wrong.length + 1));
    const options = shuffle([ans, ...wrong.slice(0, 3)]);
    const correctOption = options.indexOf(ans);
    const qText = `Simplify: ${frac(n1, d)} + ${frac(n2, d)}`;
    const expr = `$\\dfrac{${n1}}{${d}}+\\dfrac{${n2}}{${d}}$`;
    return {
      id: "Q-SESS-" + Date.now() + "-" + Math.random().toString(36).slice(2, 7),
      chapter: chapterNum,
      topicId: "math-ch" + chapterNum,
      type: "mcq",
      subtopic: "Generated · Same-denominator addition",
      question: qText,
      options,
      correctOption,
      answer: ans,
      glassboxSteps: [
        { rule: "Denominators match", why: `The denominators are already the same (${d}). Keep the denominator as is.`, math: expr },
        { rule: "Add numerators", why: `Combine the top numbers: ${n1} + ${n2} = ${sum}.`, math: `$\\dfrac{${sum}}{${d}}$` },
      ],
      linked_note_id: linkedNoteId || "",
      source: "session-generated",
    };
  }

  function buildSameDenomSub(chapterNum, linkedNoteId) {
    const d = pickDenom(6, 40);
    let n1 = 2 + Math.floor(Math.random() * (d - 2));
    let n2 = 1 + Math.floor(Math.random() * (n1 - 1));
    const diff = n1 - n2;
    const ans = frac(diff, d);
    const wrong = [
      frac(n1, d + 1),
      frac(diff + 1, d),
      frac(Math.max(1, diff - 1), d),
      frac(n1 + n2, d),
    ].filter((w, i, a) => a.indexOf(w) === i && w !== ans);
    while (wrong.length < 3) wrong.push(frac(diff, d + wrong.length + 2));
    const options = shuffle([ans, ...wrong.slice(0, 3)]);
    const correctOption = options.indexOf(ans);
    const qText = `Simplify: ${frac(n1, d)} - ${frac(n2, d)}`;
    const expr = `$\\dfrac{${n1}}{${d}}-\\dfrac{${n2}}{${d}}$`;
    return {
      id: "Q-SESS-" + Date.now() + "-" + Math.random().toString(36).slice(2, 7),
      chapter: chapterNum,
      topicId: "math-ch" + chapterNum,
      type: "mcq",
      subtopic: "Generated · Same-denominator subtraction",
      question: qText,
      options,
      correctOption,
      answer: ans,
      glassboxSteps: [
        { rule: "Denominators match", why: `The denominators are already the same (${d}). Keep the denominator as is.`, math: expr },
        { rule: "Subtract numerators", why: `Subtract the top numbers: ${n1} - ${n2} = ${diff}.`, math: `$\\dfrac{${diff}}{${d}}$` },
      ],
      linked_note_id: linkedNoteId || "",
      source: "session-generated",
    };
  }

  function buildDiffDenomAdd(chapterNum, linkedNoteId) {
    let d1 = pickDenom(3, 12);
    let d2 = pickDenom(3, 12);
    while (d1 === d2) d2 = pickDenom(3, 12);
    const lcm = (d1 * d2) / gcd(d1, d2);
    const n1 = 1 + Math.floor(Math.random() * (d1 - 1));
    const n2 = 1 + Math.floor(Math.random() * (d2 - 1));
    const sumN = n1 * (lcm / d1) + n2 * (lcm / d2);
    const g = gcd(sumN, lcm);
    const ans = frac(sumN / g, lcm / g);
    const raw = frac(sumN, lcm);
    const wrong = [
      frac(n1 + n2, d1 + d2),
      raw,
      frac(sumN + 1, lcm),
      frac(Math.max(1, sumN - 1), lcm),
    ].filter((w, i, a) => a.indexOf(w) === i && w !== ans);
    while (wrong.length < 3) wrong.push(frac(sumN, lcm + wrong.length + 1));
    const options = shuffle([ans, ...wrong.slice(0, 3)]);
    const correctOption = options.indexOf(ans);
    const qText = `Simplify: ${frac(n1, d1)} + ${frac(n2, d2)}`;
    return {
      id: "Q-SESS-" + Date.now() + "-" + Math.random().toString(36).slice(2, 7),
      chapter: chapterNum,
      topicId: "math-ch" + chapterNum,
      type: "mcq",
      subtopic: "Generated · Different denominators",
      question: qText,
      options,
      correctOption,
      answer: ans,
      glassboxSteps: [
        { rule: "LCM", why: `Common denominator is ${lcm}.`, math: `$\\dfrac{${n1}}{${d1}}+\\dfrac{${n2}}{${d2}}$` },
        { rule: "Convert & add", why: "Rewrite with the LCM, then add numerators.", math: `$\\dfrac{${sumN}}{${lcm}}$` },
        { rule: "Result", why: "Simplify if needed.", math: `$\\dfrac{${sumN / g}}{${lcm / g}}$` },
      ],
      linked_note_id: linkedNoteId || "",
      source: "session-generated",
    };
  }

  const BUILDERS = {
    same_add: buildSameDenomAdd,
    same_sub: buildSameDenomSub,
    diff_add: buildDiffDenomAdd,
    mixed: (ch, note) => {
      const keys = ["same_add", "same_sub", "diff_add"];
      const k = keys[Math.floor(Math.random() * keys.length)];
      return BUILDERS[k](ch, note);
    },
  };

  function generate(count, kind, chapterNum, linkedNoteId) {
    const build = BUILDERS[kind] || BUILDERS.same_add;
    const batch = Date.now();
    const out = [];
    for (let i = 0; i < count; i++) {
      const q = build(chapterNum, linkedNoteId);
      q.id = "Q-SESS-" + batch + "-" + i + "-" + Math.random().toString(36).slice(2, 6);
      out.push(q);
    }
    return out;
  }

  root.PracticeGenerator = { generate, BUILDERS };
})(typeof window !== "undefined" ? window : globalThis);
