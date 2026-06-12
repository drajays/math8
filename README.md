# math8

Two **separate** ICSE Class 8 mathematics apps in one repository — both offline-first with glass-box step-by-step solutions.

**Hub (pick an app):** https://drajays.github.io/math8/

| App | URL | Description |
|-----|-----|-------------|
| **Glass-Box Math** | [/glass-box/](https://drajays.github.io/math8/glass-box/) | MathDerive engine — 49 modules, mental math, KV question bank (1,700+ problems) |
| **Understanding Mathematics** | [/textbook/](https://drajays.github.io/math8/textbook/) | M.L. Aggarwal textbook — 20 chapters, 2,000 glass-box questions, notes & revision toolkits |

Repository: [github.com/drajays/math8](https://github.com/drajays/math8)

## Structure

```
math8/
├── index.html              ← App launcher (GitHub Pages root)
├── glass-box/              ← App 1: MathDerive + KV bank
├── textbook/               ← App 2: Aggarwal ICSE textbook
├── data/chapters/          ← Textbook chapter JSON & notes (20 × 100 Q)
├── assets/                 ← Diagram URL manifests per chapter
└── scripts/                ← pipeline_glassbox.py (regenerate textbook data)
```

## Offline use

- **Hub:** open `index.html`
- **Glass-Box Math:** open `glass-box/index.html`
- **Textbook:** open `textbook/index.html` (requires `data/chapters/` folder)

## Regenerate textbook data

```bash
python3 scripts/pipeline_glassbox.py   # reads OCR from configured path
```

See `scripts/PIPELINE_README.md` for the 6-step glass-box pipeline schema.
