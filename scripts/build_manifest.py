#!/usr/bin/env python3
"""Regenerate textbook/manifest.json after pipeline run."""
import json
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
chapters_dir = REPO / "data" / "chapters"
manifest = []
for ch in range(1, 21):
    tag = f"{ch:02d}"
    src = json.loads((chapters_dir / f"chapter_{tag}_source.json").read_text())
    manifest.append({
        "num": ch, "tag": tag, "title": src["title"], "topicId": src["topicId"], "questions": 100,
        "files": {
            "questions": f"data/chapters/chapter_{tag}_questions.json",
            "facts": f"data/chapters/chapter_{tag}_facts.json",
            "notes": f"data/chapters/chapter_{tag}_notes.md",
            "mindmap": f"data/chapters/chapter_{tag}_mindmap.md",
            "cheatsheet": f"data/chapters/chapter_{tag}_cheatsheet.md",
            "oneword": f"data/chapters/chapter_{tag}_oneword.json",
        },
    })
(REPO / "textbook" / "manifest.json").write_text(
    json.dumps({"chapters": manifest, "totalQuestions": 2000}, indent=2), encoding="utf-8"
)
print("Updated textbook/manifest.json")
