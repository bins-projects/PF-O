# PrepFlow Changelog

This document records major project milestones. Minor edits and intermediate work are preserved in Git history.
## Sprint 6 — Pack Validation

- Fixed validator crash caused by duplicate stem tracking.
- Improved compiler validation output with grouped problem reporting.
- Added clearer duplicate question number reporting.
- - Validation reports now group multiple issues under each affected question.
---

# Version 0.6.0 — Sprint 6 Documentation Refresh

## Repository

- Reorganized all project documentation into the `docs/` directory.
- Established `PROJECT_STATE.md` as the primary source of truth.
- Added `RESTART_PACKET.md` for starting new ChatGPT sessions.
- Added `SESSION_CHECKLIST.md` for standardized end-of-session workflow.
- Simplified project documentation structure.
- Removed duplicate documentation files.
- Standardized repository organization.

---

## Compiler

Completed features:

- DOCX document loader
- Tokenizer
- Question parser
- JSON artifact generation
- Validation framework
- Duplicate question number detection
- Duplicate question text detection
- Missing question stem detection
- Missing answer choice detection
- Missing correct answer detection
- Missing rationale detection
- Missing question type detection
- Graceful compiler failure when validation errors are found
- Human-readable validation reporting

---

## Study Engine

Completed features:

- Interactive terminal quiz
- Block mode
- Session manager
- Running score
- Review queue
- Progress tracking
- Rationales
- Question randomization

---

## Documentation

Current documentation system:

- PROJECT_STATE.md
- CHANGELOG.md
- VISION.md
- RESTART_PACKET.md
- SESSION_CHECKLIST.md
- ARCHITECTURE.md
- PACK_SPEC.md
- IDEAS.md

---

Future releases should be added above this line.