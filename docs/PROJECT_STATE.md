# PrepFlow — Project State

## Project Information

**Project:** PrepFlow

**Version:** 0.6.0

**Current Sprint:** Sprint 6 – Pack Validation

**Status:** Active Development

**Branch:** master

---

# Project Overview

PrepFlow is a modular Python application that converts educational source material into validated study packs and delivers those packs through an interactive study engine.

The project consists of two primary systems:

- Compiler
- Study Engine

The compiler is responsible for producing reliable study packs.

The Study Engine is responsible for presenting those packs to the user.

---

# Current Progress

## Compiler

Completed:

- Document loading
- Tokenization
- Question parsing
- JSON export
- Validation framework
- Missing stem validation
- Missing answer validation
- Missing rationale validation
- Missing question type validation
- Duplicate question number detection
- Duplicate question text detection
- Validation failure handling
- Duplicate detection utility

---

## Study Engine

Completed:

- Block mode
- Question loader
- Session manager
- Review queue
- Running score
- Rationales
- Progress tracking
- Randomized question ordering

---

# Current Sprint

# Current Sprint

Sprint 6 — Pack Validation

Status:
Active development

Objective:

Complete the Pack Validation system and improve compiler diagnostics before resuming Study Engine feature development.

Completed this sprint:

- Fixed validator crash caused by duplicate stem tracking (`set()` instead of `{}`).
- Improved validation output formatting.
- Grouped validation problems by question.
- Duplicate question numbers now identify the original conflicting question.
- Validation improvements committed and pushed to GitHub.

Current focus:

- Continue improving compiler robustness.
- Expand validation checks.
- Improve compiler success summary.
- Prepare for resuming Study Engine development.
---

# Documentation

Repository documentation lives in:

docs/

Primary files:

- PROJECT_STATE.md
- CHANGELOG.md
- VISION.md
- RESTART_PACKET.md
- SESSION_CHECKLIST.md

---

# Development Workflow

Standard workflow:

1. Build feature
2. Test feature
3. Review changes
4. git add
5. git commit
6. git push
7. Verify working tree clean
8. Update documentation

---

# Next Development Target

# Next Development Target

Priority:

Continue Pack Validation improvements.

Immediate tasks:

1. Add compiler success summary.
2. Add validation totals.
3. Improve parser robustness.
4. Continue pack integrity verification.
5. Resume Study Engine development after Pack Validation reaches MVP.

---

Last Updated

Sprint 6
Version 0.6.0