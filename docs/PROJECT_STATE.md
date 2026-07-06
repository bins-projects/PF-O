# PROJECT_STATE.md

Project: PrepFlow

Version: 0.7.0

Status: Active Development

Current Sprint:

Sprint 7 — Canonical Compiler Architecture

---

# Current Milestone

Sprint 7 is restructuring PrepFlow into a reusable, library-first compiler architecture.

The production importers are complete.

Current development is focused on separating importing, compilation, and study functionality into independent layers.

---

# Completed Milestones

## Medical-Surgical Importer

Status:

Production Ready

Output:

- output/medsurg_questions.json

Validated production question bank.

---

## Pharmacy Importer

Status:

Production Ready

Output:

- output/pharm_questions.json

Validation:

- Chapters: 24
- Total Questions: 1076

Question Types:

- Multiple Choice
- SATA
- Completion
- Ordered Response

Importer development is considered complete.

---

# Canonical Compiler

Implemented:

- Canonical domain model
- Validator
- Deduplicator
- Builder
- Compiler pipeline
- Normalizer
- CLI orchestration

Current compiler flow:

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

# Current Compiler Status

Validation, deduplication, and canonical object creation now occur inside the reusable compiler pipeline.

Applications consume compiler functionality rather than implementing compiler logic directly.

The CLI has been refactored into a thin orchestration layer.

---

# Known Source Data Issues

The remaining validation failures are confirmed source issues rather than compiler defects.

Known issues include:

- Duplicate question block (Questions 41–60)
- Missing correct answer and rationale (Question 80)
- Duplicate stems (Questions 117 and 156)

---

# Study Engine Status

Current implementation target:

Users can select questions by:

- Source
- Chapter
- Multiple Chapters
- Entire Source

Deferred until later:

- Topic filtering
- Body system filtering
- Mixed-topic generation
- Additional publishers

---

# Next Milestone

Implement the Exporter stage.

Goals:

- Export canonical Packs.
- Establish the official PrepFlow Pack format.
- Separate exported packs from parser output.
- Allow future applications to consume canonical packs directly.

---

# Repository Status

Branch:

master

Status:

Clean

Remote:

Synchronized with GitHub

Compiler architecture is now the primary focus of development.