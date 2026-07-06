# PrepFlow Restart Packet

## Read First (Repository Source of Truth)

Read these project documents first, in this order:

1. docs/PROJECT_STATE.md
2. docs/CHANGELOG.md
3. docs/VISION.md
4. docs/ARCHITECTURE_BIBLE.md
5. docs/DOMAIN_MODEL.md
6. docs/PACK_SPEC.md
7. docs/QUESTION_LIFECYCLE.md
8. docs/RESTART_PACKET.md

The repository documentation is the source of truth.

---

# Project Status

Project: PrepFlow

Version: 0.7.0

Current Sprint:

Sprint 7 — Canonical Compiler Architecture

Status:

Sprint 7 has established the reusable compiler pipeline.

The compiler architecture is now library-first.

Current focus is completing the compiler by implementing the Exporter stage.

---

# Current Compiler Architecture

PrepFlow now consists of three major systems.

## 1. Import Layer

Responsibilities:

- Read supported source material
- Tokenize DOCX
- Parse source content

Supported inputs:

- DOCX
- JSON

Future:

- PDF
- CSV
- AI-assisted imports

---

## 2. Canonical Compiler

Current pipeline:

Reader / Loader

↓

Tokenizer (DOCX)

↓

Parser (DOCX)

↓

Normalizer

↓

Validator

↓

Deduplicator

↓

Builder

↓

Canonical Pack

↓

Exporter (next)

Each stage has exactly one responsibility.

---

## 3. Applications

Applications consume compiler functionality.

Current:

- Compiler CLI
- Study Engine

Future:

- GUI
- API
- Automated testing
- Additional exporters

Applications never duplicate compiler logic.

---

# Canonical Domain Model

Implemented:

- Pack
- Question
- Answer
- Origin
- Content
- Classification
- Metadata

Rules:

- Pack owns Questions.
- Question never owns Pack.
- Stable Question IDs are publisher independent.

---

# Compiler Status

Implemented:

- Validator
- Deduplicator
- Builder
- Pipeline
- Normalizer

The CLI has been refactored into a thin orchestration layer.

Validation, deduplication, and canonical object creation now occur exclusively inside the compiler pipeline.

---

# Compiler Data Flow

PrepFlow recognizes three internal representations.

1. Parsed Question

Raw parser output.

2. Normalized Question

Compiler input after schema normalization.

3. Canonical Question

Immutable domain object used throughout PrepFlow.

---

# Known Source Data Issues

Confirmed source-data issues:

- Duplicate question block (Questions 41–60)
- Missing correct answer and rationale (Question 80)
- Duplicate stems (Questions 117 and 156)

These are source issues, not compiler defects.

---

# Immediate Next Task

Implement the Exporter stage.

Goals:

- Export canonical Packs.
- Establish the official PrepFlow Pack format.
- Separate exported packs from parser output.
- Allow future applications to consume canonical packs directly.

---

# Study Engine Scope

Current functional goal:

Support selecting questions by:

Source:

- Pharmacy
- Medical-Surgical

Selection:

- Single chapter
- Multiple chapters
- Entire source

Deferred until later:

- Topic filtering
- Body system filtering
- Mixed-topic generation
- Additional publishers

No additional source banks should be added until this workflow is complete.

---

# Repository Status

Branch:

master

Remote:

GitHub synchronized.

Working tree:

Clean.

Latest commit:

Sprint 7: add compiler normalization stage

---

# Permanent Architecture Rules

Parser parses.

Normalizer normalizes.

Validator validates.

Deduplicator deduplicates.

Builder builds.

Exporter exports.

Pack owns Questions.

Question never owns Pack.

Never silently repair source data.

Prefer diagnostics over hidden fixes.

Each compiler stage has one responsibility.

PrepFlow is library-first.

Applications consume reusable compiler code.

---

# Permanent Development Workflow

When modifying code:

1. Locate the exact code.
2. Replace the exact code.
3. Save.
4. Compile.
5. Wait for confirmation before continuing.

Prefer replacing entire files during significant refactors.

Avoid vague instructions.

---

# VS Code Rule

When creating new files:

Never enter:

compiler/example.py

into the New File dialog.

Instead:

1. Select the destination folder.
2. Choose New File.
3. Enter only:

example.py

---

# End-of-Session Workflow

1. Compile modified Python files.
2. Review git status.
3. Commit.
4. Push.
5. Rewrite this restart packet completely.
6. Verify repository state.
7. End session.