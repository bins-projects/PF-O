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

Sprint 6 – Pack Validation

Objective:

Continue improving compiler validation and reporting before resuming Study Engine feature development.

Current work includes:

- Validation improvements
- Better compiler output
- Pack integrity verification

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

Continue expanding the compiler validation system and improve validation reporting before beginning the next Study Engine sprint.

---

Last Updated

Sprint 6
Version 0.6.0