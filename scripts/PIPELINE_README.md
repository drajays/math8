# ICSE Class 8 Mathematics — Glassbox Pipeline Output

Source: `maths.pdf_by_PaddleOCR-VL-1.6.md` + `.json` (M.L. Aggarwal — Understanding Mathematics)  
Architecture: aligned with [StudyHub FEATURES.md](/Users/dr.ajayshukla/class_8_sci/FEATURES.md) (`math-ch{n}` topic IDs, note/question schema, bi-directional links)

## Regenerate

```bash
cd /Users/dr.ajayshukla/Downloads/math
python3 pipeline_glassbox.py
```

## Per-chapter deliverables (×20 chapters)

| Step | File | Description |
|------|------|-------------|
| 1 | `chapter_XX_source.json` / `.md` | Segregated chapter source + section index |
| 2 | `chapter_XX_facts.json` | Facts with IDs `FACT-CHXX-NNN` |
| 3 | `chapter_XX_questions.json` | **100 questions** (70 MCQ / 20 fill / 10 T-F) with `glassboxSteps` |
| 4 | `chapter_XX_notes.md` | Textbook notes with **Tests concepts in: Q-CHXX-…** links |
| 5 | `chapter_XX_assets.json` + `assets/chapter_XX/` | Image manifest + URL stubs |
| 6 | `chapter_XX_mindmap.md`, `_cheatsheet.md`, `_oneword.json` | Cognitive toolkits (30 one-word cards) |

## Scale

- **2,000** glass-box questions (`Q-CH01-001` … `Q-CH20-100`)
- **600** one-word recall cards (`OW-CHxx-001` … `030`)
- **20** chapter note sets with bi-directional question links
- Question fields map to StudyHub: `topicId`, `type`, `linksTo` / `linked_note_id`, `glassboxSteps`

## Question schema (excerpt)

```json
{
  "id": "Q-CH01-001",
  "topicId": "math-ch1",
  "type": "mcq",
  "question": "…",
  "options": ["…", "…", "…", "…"],
  "correctOption": 2,
  "glassboxSteps": [
    { "rule": "Given", "why": "…", "math": "$…$" }
  ],
  "linked_note_id": "CH01-sec-rational-numbers"
}
```
