/* Rich notes renderer for ICSE textbook markdown (sections, tables, math). */
(function (root) {
  const SECTION_THEMES = [
    { accent: "#6366f1", soft: "#eef2ff", icon: "🔢" },
    { accent: "#0d9488", soft: "#ccfbf1", icon: "📐" },
    { accent: "#d97706", soft: "#fef3c7", icon: "⚡" },
    { accent: "#e11d48", soft: "#ffe4e6", icon: "🎯" },
    { accent: "#7c3aed", soft: "#ede9fe", icon: "🧮" },
    { accent: "#0284c7", soft: "#e0f2fe", icon: "📊" },
    { accent: "#059669", soft: "#d1fae5", icon: "✨" },
    { accent: "#db2777", soft: "#fce7f3", icon: "💡" },
  ];

  function esc(s) {
    return String(s).replace(/[&<>]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;" }[c]));
  }

  function inlineFmt(text, escFn) {
    return escFn(text)
      .replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>")
      .replace(/\*([^*]+)\*/g, "<em>$1</em>")
      .replace(/`([^`]+)`/g, "<code>$1</code>");
  }

  function splitRenderTex(text, deps) {
    const re = /\$\$([^$]+)\$\$|\$([^$]+)\$/g;
    let out = "", last = 0, m;
    const s = String(text ?? "");
    while ((m = re.exec(s)) !== null) {
      out += inlineFmt(s.slice(last, m.index), deps.esc);
      out += `<span class="mathline">${deps.texHtml(m[1] ?? m[2])}</span>`;
      last = m.index + m[0].length;
    }
    out += inlineFmt(s.slice(last), deps.esc);
    return out;
  }

  function tryParseOcrTable(line, deps) {
    const re = /(\d+)\$\s*([^$]+?)\s*\$/g;
    const rows = [];
    let m;
    while ((m = re.exec(line)) !== null) {
      if (m[2].trim()) rows.push({ n: m[1], expr: m[2].trim() });
    }
    if (rows.length < 2) return null;
    if (!/cube|number|\d+\$/i.test(line) && rows.length < 3) return null;

    const dual = /Natural numberCubeNatural numberCube/i.test(line);
    if (dual) {
      const half = Math.ceil(rows.length / 2);
      const left = rows.slice(0, half);
      const right = rows.slice(half);
      const max = Math.max(left.length, right.length);
      let html = `<div class="note-table-wrap"><table class="note-table note-table--dual"><thead><tr>
        <th>Number</th><th>Cube</th><th>Number</th><th>Cube</th></tr></thead><tbody>`;
      for (let i = 0; i < max; i++) {
        const L = left[i], R = right[i];
        html += `<tr>
          <td class="note-td-num">${L ? esc(L.n) : ""}</td>
          <td>${L ? `<span class="mathline">${deps.texHtml(L.expr)}</span>` : ""}</td>
          <td class="note-td-num">${R ? esc(R.n) : ""}</td>
          <td>${R ? `<span class="mathline">${deps.texHtml(R.expr)}</span>` : ""}</td>
        </tr>`;
      }
      return html + "</tbody></table></div>";
    }

    let html = `<div class="note-table-wrap"><table class="note-table"><thead><tr>
      <th>Natural number</th><th>Cube</th></tr></thead><tbody>`;
    rows.forEach(r => {
      html += `<tr><td class="note-td-num">${esc(r.n)}</td><td><span class="mathline">${deps.texHtml(r.expr)}</span></td></tr>`;
    });
    return html + "</tbody></table></div>";
  }

  function isSpecialLine(line) {
    const t = line.trim();
    if (!t) return false;
    if (/^\$\$/.test(t)) return true;
    if (/^#{4,5} /.test(t)) return true;
    if (/^Property \d+\./i.test(t)) return true;
    if (/^(Example|For example)/i.test(t)) return true;
    if (/^Table \d+/i.test(t)) return true;
    if (/^\([ivx]+\)/i.test(t)) return true;
    if (/^\d+\.\s/.test(t)) return true;
    if (/^\*\*Note ID:\*\*/.test(t)) return true;
    if (/^\*\*Tests concepts in:\*\*/.test(t)) return true;
    if (/^Hence, we can say that:/i.test(t)) return true;
    if (/^Look at the following table:/i.test(t)) return true;
    return /(\d+\$\s*[^$]+\$){2,}/.test(t);
  }

  function renderNoteBody(body, deps) {
    const lines = body.split("\n");
    let html = "";
    let i = 0;
    while (i < lines.length) {
      const line = lines[i];
      const t = line.trim();
      if (!t) { i++; continue; }

      const table = tryParseOcrTable(t, deps);
      if (table) { html += table; i++; continue; }

      if (/^\$\$/.test(t)) {
        const math = t.replace(/^\$\$\s*/, "").replace(/\s*\$\$$/, "");
        html += `<div class="note-math-block"><span class="mathline">${deps.texHtml(math)}</span></div>`;
        i++; continue;
      }

      const h4 = t.match(/^#{4,5} (.+)$/);
      if (h4) {
        html += `<h4 class="note-h4">${splitRenderTex(h4[1], deps)}</h4>`;
        i++; continue;
      }

      if (/^\*\*Note ID:\*\*/.test(t)) { i++; continue; }

      if (/^\*\*Tests concepts in:\*\*/.test(t)) {
        html += `<div class="note-linked"><span class="note-linked-icon">🔗</span>${splitRenderTex(t.replace(/\*\*/g, ""), deps)}</div>`;
        i++; continue;
      }

      if (/^Property \d+\./i.test(t)) {
        const label = t.match(/^(Property \d+\.)/i)[1];
        const rest = t.slice(label.length).trim();
        html += `<div class="note-callout note-callout--property">
          <div class="note-callout-badge">${esc(label)}</div>
          <div class="note-callout-body">${rest ? splitRenderTex(rest, deps) : ""}</div></div>`;
        i++; continue;
      }

      if (/^(Example \d+|For example)/i.test(t)) {
        html += `<div class="note-callout note-callout--example">
          <div class="note-callout-badge">Example</div>
          <div class="note-callout-body">${splitRenderTex(t, deps)}</div></div>`;
        i++; continue;
      }

      if (/^Table \d+/i.test(t)) {
        html += `<div class="note-table-caption">${splitRenderTex(t, deps)}</div>`;
        i++; continue;
      }

      if (/^Look at the following table:/i.test(t)) {
        html += `<p class="note-lead">${splitRenderTex(t, deps)}</p>`;
        i++; continue;
      }

      if (/^Hence, we can say that:/i.test(t)) {
        html += `<div class="note-highlight"><p>${splitRenderTex(t, deps)}</p></div>`;
        i++; continue;
      }

      if (/^\([ivx]+\)/i.test(t)) {
        const label = t.match(/^\([ivx]+\)/i)[0];
        let rest = t.slice(label.length).trim();
        i++;
        if (!rest && i < lines.length && /^\$\$/.test(lines[i].trim())) {
          const math = lines[i].trim().replace(/^\$\$\s*/, "").replace(/\s*\$\$$/, "");
          html += `<div class="note-rule"><span class="note-rule-label">${esc(label)}</span>
            <div class="note-math-block note-math-block--inline"><span class="mathline">${deps.texHtml(math)}</span></div></div>`;
          i++; continue;
        }
        html += `<div class="note-rule"><span class="note-rule-label">${esc(label)}</span><span>${splitRenderTex(rest, deps)}</span></div>`;
        continue;
      }

      if (/^\d+\.\s/.test(t)) {
        const num = t.match(/^(\d+)\./)[1];
        html += `<div class="note-numbered"><span class="note-num">${esc(num)}</span><span>${splitRenderTex(t.replace(/^\d+\.\s*/, ""), deps)}</span></div>`;
        i++; continue;
      }

      if (/^\([a-z]\)/i.test(t)) {
        const label = t.match(/^\([a-z]\)/i)[0];
        html += `<div class="note-rule note-rule--alpha"><span class="note-rule-label">${esc(label)}</span><span>${splitRenderTex(t.replace(/^\([a-z]\)\s*/i, ""), deps)}</span></div>`;
        i++; continue;
      }

      let para = t;
      i++;
      while (i < lines.length && lines[i].trim() && !isSpecialLine(lines[i])) {
        para += " " + lines[i].trim();
        i++;
      }
      html += `<p class="note-p">${splitRenderTex(para, deps)}</p>`;
    }
    return html;
  }

  function parseSection(block, idx) {
    const lines = block.split("\n");
    const title = (lines[0] || "").replace(/^##\s*/, "").trim();
    let noteId = "";
    const bodyLines = [];
    for (let j = 1; j < lines.length; j++) {
      const line = lines[j];
      const nid = line.match(/^\*\*Note ID:\*\*\s*`([^`]+)`/);
      if (nid) { noteId = nid[1]; continue; }
      bodyLines.push(line);
    }
    return { title, noteId, body: bodyLines.join("\n"), idx };
  }

  function slugify(s, idx) {
    return "note-sec-" + idx;
  }

  function notesToHtml(md, deps) {
    const full = String(md ?? "").replace(/\r\n/g, "\n");
    const splitAt = full.search(/\n## /);
    const heroBlock = splitAt >= 0 ? full.slice(0, splitAt).trim() : full.trim();
    const sectionsBlock = splitAt >= 0 ? full.slice(splitAt + 1) : "";
    const sectionParts = sectionsBlock ? sectionsBlock.split(/\n(?=## )/) : [];

    const heroLines = heroBlock.split("\n");
    let chapterTitle = "";
    let summary = "";
    for (const line of heroLines) {
      const h1 = line.match(/^# (.+)$/);
      if (h1) { chapterTitle = h1[1]; continue; }
      const sum = line.match(/^\*\*Executive summary:\*\*\s*(.+)$/);
      if (sum) { summary = sum[1]; continue; }
    }

    const sections = sectionParts.map((p, i) => parseSection(p.trim(), i));
    const chMatch = chapterTitle.match(/Chapter\s+(\d+)/i);

    let html = `<div class="notes-doc">`;

    html += `<header class="notes-hero">
      <div class="notes-hero-badge">${chMatch ? "Chapter " + chMatch[1] : "ICSE Class 8"}</div>
      <h1 class="notes-title">${splitRenderTex(chapterTitle, deps)}</h1>`;
    if (summary) {
      html += `<div class="notes-summary"><span class="notes-summary-label">Executive summary</span>
        <p>${splitRenderTex(summary, deps)}</p></div>`;
    }
    html += `</header>`;

    if (sections.length > 1) {
      html += `<nav class="notes-toc" aria-label="Section navigation"><span class="notes-toc-label">Jump to</span><div class="notes-toc-links">`;
      sections.forEach((sec, i) => {
        const short = sec.title.length > 42 ? sec.title.slice(0, 40) + "…" : sec.title;
        html += `<a href="#${slugify(sec.title, i)}" class="notes-toc-link">${esc(short)}</a>`;
      });
      html += `</div></nav>`;
    }

    sections.forEach((sec, i) => {
      const theme = SECTION_THEMES[i % SECTION_THEMES.length];
      html += `<article class="note-section" id="${slugify(sec.title, i)}" style="--sec-accent:${theme.accent};--sec-soft:${theme.soft}">
        <div class="note-section-head">
          <span class="note-section-icon" aria-hidden="true">${theme.icon}</span>
          <div class="note-section-titles">
            <h2 class="note-section-title">${splitRenderTex(sec.title, deps)}</h2>`;
      if (sec.noteId) {
        html += `<span class="note-id-pill" title="Linked practice note">${esc(sec.noteId)}</span>`;
      }
      html += `</div></div>
        <div class="note-section-body">${renderNoteBody(sec.body, deps)}</div>
      </article>`;
    });

    html += `</div>`;
    return html;
  }

  function chapterTheme(chNum) {
    return SECTION_THEMES[(Math.max(1, chNum) - 1) % SECTION_THEMES.length];
  }

  function panelHeroHtml(kind, badge, title, subtitle, deps) {
    const icons = { practice: "❓", mindmap: "🧠", cheat: "⚡", oneword: "🔤" };
    const subs = {
      practice: "Full solution shown · toggle step-by-step reveal if you want",
      mindmap: "Concept tree linked to facts & practice",
      cheat: "Quick facts, formulas & exam traps",
      oneword: "Tap a card to flip and reveal",
    };
    return `<header class="panel-hero panel-hero--${kind}">
      <div class="panel-hero-inner">
        <span class="panel-hero-icon" aria-hidden="true">${icons[kind] || "📖"}</span>
        <div class="panel-hero-text">
          <span class="panel-hero-badge">${esc(badge)}</span>
          <h2 class="panel-hero-title">${splitRenderTex(title, deps)}</h2>
          <p class="panel-hero-sub">${esc(subtitle || subs[kind] || "")}</p>
        </div>
      </div>
    </header>`;
  }

  function cheatSheetHtml(md, deps) {
    const lines = String(md ?? "").split("\n");
    let title = "Cheat Sheet";
    const facts = [];
    for (const line of lines) {
      const h = line.match(/^# (.+)$/);
      if (h) { title = h[1]; continue; }
      if (!line.trim().startsWith("|") || /^\|[-\s|]+\|$/.test(line.trim())) continue;
      const cells = line.split("|").map(c => c.trim()).filter(Boolean);
      if (cells.length >= 3 && cells[0] !== "#" && !/^[-]+$/.test(cells[0])) {
        facts.push({ num: cells[0], fact: cells[1], noteId: cells[2].replace(/`/g, "").trim() });
      }
    }
    let html = `<div class="rich-doc cheat-doc">${panelHeroHtml("cheat", facts.length + " facts", title, null, deps)}<div class="cheat-grid">`;
    facts.forEach((f, i) => {
      const theme = SECTION_THEMES[i % SECTION_THEMES.length];
      html += `<article class="cheat-card" style="--sec-accent:${theme.accent};--sec-soft:${theme.soft}">
        <span class="cheat-num">${esc(f.num)}</span>
        <div class="cheat-body">${splitRenderTex(f.fact, deps)}</div>
        <span class="note-id-pill">${esc(f.noteId)}</span>
      </article>`;
    });
    return html + `</div></div>`;
  }

  function renderMindBranch(items, start, depth, deps) {
    let html = `<ul class="mind-branch mind-branch--${depth}">`;
    let i = start;
    while (i < items.length) {
      const d = Math.floor(items[i].depth / 2);
      if (d < depth) break;
      if (d > depth) { i++; continue; }
      const theme = SECTION_THEMES[d % SECTION_THEMES.length];
      html += `<li class="mind-node${d === 0 ? " mind-node--root" : ""}" style="--sec-accent:${theme.accent};--sec-soft:${theme.soft}">
        <div class="mind-node-card">${splitRenderTex(items[i].text, deps)}</div>`;
      i++;
      if (i < items.length && Math.floor(items[i].depth / 2) > depth) {
        const sub = renderMindBranch(items, i, depth + 1, deps);
        html += sub.html;
        i = sub.index;
      }
      html += `</li>`;
    }
    html += `</ul>`;
    return { html, index: i };
  }

  function mindMapHtml(md, deps) {
    const lines = String(md ?? "").split("\n");
    let title = "Mind Map";
    const items = [];
    for (const line of lines) {
      const h = line.match(/^# (.+)$/);
      if (h) { title = h[1]; continue; }
      const m = line.match(/^(\s*)- (.+)$/);
      if (m) items.push({ depth: m[1].length, text: m[2] });
    }
    let html = `<div class="rich-doc mind-doc">${panelHeroHtml("mindmap", items.length + " nodes", title, null, deps)}<div class="mind-tree">`;
    if (items.length) html += renderMindBranch(items, 0, 0, deps).html;
    else html += `<p class="empty-state">No mind map nodes for this chapter.</p>`;
    return html + `</div></div>`;
  }

  root.NotesRender = { notesToHtml, splitRenderTex, inlineFmt, SECTION_THEMES, chapterTheme, panelHeroHtml, cheatSheetHtml, mindMapHtml };
})(typeof window !== "undefined" ? window : this);
