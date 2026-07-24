# PrepFlow Phase D Completion — 2026-07-21

## Status

Phase D is complete.

Completed through:

```text
d96c847  refactor: extract browser display rules
b4b9d39  refactor: complete browser display rule integration
```

## What the continuity rebuild accomplished

This work did not replace the entire compiler/import pipeline. It established and enforced the architectural responsibility split for the active PrepFlow system.

The authoritative boundaries are now:

- source adapters and extraction retrieve source content without interpreting educational meaning;
- the cleaner removes contamination and extraction artifacts without casually rewriting admitted content;
- the detector measures source structure and exposes uncertainty;
- the parser converts cleaned source text into candidate questions;
- the normalizer converts supported parser output into one consistent compiler input shape;
- the validator decides structural eligibility using fatal, recoverable, and advisory findings;
- deduplication removes only genuine exact duplicates and preserves near-duplicates;
- the compiler preserves or assigns permanent question IDs and builds authoritative Packs;
- the Pack library is the durable product output of ingestion;
- browser quiz/session rules own grading, ordering, blocks, review, summaries, and save-state meaning;
- the browser GUI owns presentation, controls, layout, animation, and accessibility without inventing quiz rules.

Obsolete competing pathways were removed, while the working ingestion/compiler pipeline was preserved as PrepFlow's core.

## Permanent identity and browser stabilization

Completed during the continuity rebuild:

- all 3,721 official questions have unique permanent Pack-namespaced IDs;
- browser references now use `packPath + questionId` rather than fragile array positions;
- saved sessions use version 3 and reject incompatible older saves;
- quiz behavior was separated from direct DOM manipulation through focused tested rule modules;
- grading, response classification, session calculations, summary decisions, saved-session parsing, review queues, navigation, selection display, resume display, and quiz/summary display text now have independent browser tests;
- legacy desktop, PyInstaller, Windows-build, and obsolete DOCX prototype paths were removed;
- the browser remains the active compatibility target.

## Final Phase D milestone

Implemented:

- added `web/display-rules.js` with tested quiz-position, running-score, block-summary, and final-summary text helpers;
- added `web/display-rules.test.html` with 12 normal, review, score, completion, mastery, and singular/plural cases;
- integrated the tested helpers throughout the live quiz and summary paths;
- completed a final inspection and replaced the remaining inline running-score formatter after answer submission.

Verification completed:

- all 12 display-rule browser tests passed;
- all 72 Python tests passed after the batched integration and final cleanup;
- `git diff --check` passed;
- local, private, and public branch heads matched `b4b9d394266689126e0cc6e1f4284f70adbb3849` before this documentation update;
- working tree was clean.

## Phase D conclusion

The final inspection found no further pure behavior unit worth extracting from `web/app.js`. Remaining code is primarily DOM coordination, Pack loading, state transfer, and event wiring. Further extraction would add indirection without enough safety or testing value.

## Exact next milestone

Stage 4 — add a quiz setup choice between **Shuffle Questions** and **Keep Source Order**.

The milestone must:

1. add the two-option setup control;
2. add a small tested ordering rule;
3. preserve the full selected question pool in both modes;
4. shuffle only when Shuffle Questions is selected;
5. preserve the setting in saved sessions and restore it on resume;
6. test that source order remains unchanged when shuffle is off;
7. run browser tests, all 72 Python tests, `git diff --check`, and a live quiz smoke test in both modes.

The visible permanent question-reference item remains a separate small UI backlog change.
