from pathlib import Path

checkpoint_path = Path("docs/SESSION_CHECKPOINT_2026-07-20.md")
checkpoint = checkpoint_path.read_text()

old = '''### Exact next milestone

Continue Phase D with another read-only inspection of `web/app.js`. Extract only the next smallest pure behavior unit that can be tested without changing visible browser flow. Prefer a narrowly scoped score-text, feedback-text, or other remaining display helper. Do not begin a broad rewrite. The visible question-reference item remains a separate small UI backlog change.
'''

new = '''### Tenth Phase D extraction completed

Completed through:

```text
d96c847  refactor: extract browser display rules
b4b9d39  refactor: complete browser display rule integration
```

Implemented:

- added `web/display-rules.js` with tested quiz-position, running-score, block-summary, and final-summary text helpers;
- added `web/display-rules.test.html` with 12 normal, review, score, completion, mastery, and singular/plural cases;
- integrated the tested helpers throughout the live quiz and summary paths;
- completed a final inspection and replaced the one remaining inline running-score formatter after answer submission.

Verification completed:

- all 12 display-rule browser tests passed;
- all 72 Python tests passed after the batched integration and after the final cleanup;
- `git diff --check` passed;
- local, private, and public branch heads all matched `b4b9d394266689126e0cc6e1f4284f70adbb3849`;
- working tree was clean.

### Phase D complete

The final inspection found no further pure behavior unit worth extracting from `web/app.js`. Remaining code is primarily DOM coordination, Pack loading, state transfer, and event wiring. Further extraction would add indirection without enough safety or testing value.

### Exact next milestone

Move to the next continuity-rebuild phase by inspecting `docs/CONTINUITY_REBUILD_PLAN.md`, `docs/ARCHITECTURE_BIBLE.md`, and the current browser structure. Select one coherent next milestone from the documented plan. Keep the visible permanent question-reference item as a separate small UI backlog change unless the next phase explicitly calls for it.
'''

if old not in checkpoint:
    raise SystemExit("Expected Exact next milestone block not found")

checkpoint_path.write_text(checkpoint.replace(old, new, 1))
print("Phase D completion checkpoint update applied.")
