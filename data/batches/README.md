# Gemini question batches (500 total)

Upload **10 batches × 50 questions** here. Existing textbook questions are **never deleted** — batches merge at load time.

## Files

| File | Global Q# | Chapters |
|------|-----------|----------|
| `batch_01.json` | 1–50 | Ch 1–3 |
| `batch_02.json` | 51–100 | Ch 3 (8), Ch 4 (15), Ch 5 (15), Ch 6 (12) |
| `batch_03.json` | 101–150 | Ch 6 (3), Ch 7 (36), Ch 8 (11) |
| `batch_04.json` | 151–200 | Ch 8 (9), Ch 9 (15), Ch 10 (26) |
| `batch_05.json` | 201–250 | Ch 10 (12), Ch 11 (18), Ch 12 (20) |
| `batch_06.json` | 251–300 | Ch 13 (30), Ch 14 (12), Ch 18 (8) |
| `batch_07.json` | 301–350 | Ch 18 (4), Ch 19 (40), Ch 20 (6) |
| `batch_10.json` | 451–500 | (TBD) |

## Add a new batch

1. Extend `scripts/build_gemini_batch.py` with a `batch_NN()` function (or paste structured JSON).
2. Run: `python3 scripts/build_gemini_batch.py N`
3. Commit `data/batches/batch_NN.json` and push — the app loads it automatically.

## Question format

Each entry uses `type: "practice"` with full `glassboxSteps`. Optional `"diagram"` id renders an inline SVG (see `shared/practice-diagrams.js`). IDs: `Q-GEM-B01-001` … `Q-GEM-B10-050`.
