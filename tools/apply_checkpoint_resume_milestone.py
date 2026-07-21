from pathlib import Path

checkpoint = Path("docs/SESSION_CHECKPOINT_2026-07-20.md")
text = checkpoint.read_text(encoding="utf-8")
marker = "\n### Backlog addition\n"
entry = """

### Ninth Phase D extraction completed

Completed at:

```text
c756a2b  refactor: extract browser resume rules
```

Implemented:

- added `web/resume-rules.js` with pure saved-session description and accessibility-label formatting;
- added `web/resume-rules.test.html` covering named quizzes, review mode, the Custom Quiz fallback, and the resume accessibility label;
- loaded the resume rules before `web/app.js`;
- updated the live resume panel to use the tested description and accessibility helpers;
- removed the temporary integration helper after use.

Verification completed:

- all four resume-rule browser tests passed;
- all 72 Python tests passed;
- `git diff --check` passed;
- a live resume-panel click-through was not performed for this extraction;
- local, private, and public branch heads all matched `c756a2ba0099e2b41e716963ac01a8c17830c62c`;
- working tree was clean.
"""

if "### Ninth Phase D extraction completed" in text:
    raise SystemExit("Resume milestone is already recorded.")
if marker not in text:
    raise SystemExit("Checkpoint insertion marker was not found.")

text = text.replace(marker, entry + marker, 1)
text = text.replace(
    "Continue Phase D with another read-only inspection of `web/app.js`. Extract only the next smallest pure behavior unit that can be tested without changing visible browser flow. Prefer a narrowly scoped resume-description, score-text, or other display helper. Do not begin a broad rewrite. The visible question-reference item remains a separate small UI backlog change.",
    "Continue Phase D with another read-only inspection of `web/app.js`. Extract only the next smallest pure behavior unit that can be tested without changing visible browser flow. Prefer a narrowly scoped score-text, feedback-text, or other remaining display helper. Do not begin a broad rewrite. The visible question-reference item remains a separate small UI backlog change.",
)
checkpoint.write_text(text, encoding="utf-8")
Path(__file__).unlink()
print("Resume milestone checkpoint update applied.")
