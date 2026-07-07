# PROJECT_STATE.md

Project: PrepFlow

Version: 0.7.0

Status: Active Development

Current Sprint:

Sprint 7 — Canonical Compiler Architecture

---

# Current Milestone

Sprint 7 established the reusable compiler architecture and verified the complete compiler pipeline against a real production source.

The compiler is now capable of transforming supported source material into canonical PrepFlow domain objects and exporting lean Runtime Study Packs.

Current development remains focused on completing the end-to-end workflow before expanding functionality.

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

- Reader / Loader
- DOCX Tokenizer
- DOCX Parser
- Normalizer
- Validator
- Deduplicator
- Builder
- Canonical Domain Model
- Compiler Pipeline
- Typed Diagnostics
- Runtime Pack Exporter
- CLI Orchestration

Verified compiler flow:

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

Exporter

↓

Runtime Study Pack

The compiler pipeline has been verified by compiling a real production DOCX source into a Runtime Study Pack.

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

The Canonical Domain Model is the internal representation used throughout the compiler.

---

# Runtime Study Pack

The Runtime Study Pack is the exported format consumed by applications.

The exporter transforms Canonical Packs into lean Runtime Study Packs containing only the information required by the Study Engine.

The canonical representation remains the long-term source of truth.

---

# Current Compiler Status

Implemented:

- Typed compiler diagnostics
- Fatal diagnostics
- Recoverable diagnostics
- Advisory diagnostics
- Recoverable question skipping
- Duplicate reporting
- Canonical Question building
- Canonical Pack building
- Runtime Pack exporting

The compiler has been verified against a 220-question production document.

Results:

- Parsed Questions: 220
- Recoverable Questions Skipped: 1
- Duplicate Questions Removed: 22
- Runtime Questions Produced: 197

The compiler successfully exports a Runtime Study Pack.

---

# Known Source Data Issues

The remaining validation findings are confirmed source-data issues rather than compiler defects.

Known issues include:

- Duplicate question block (Questions 41–60)
- Missing correct answer and rationale (Question 80)
- Duplicate stems (Questions 117 and 156)

---

# Study Engine Status

Current implementation target:

Users can select questions by:

- Source
- Single Chapter
- Multiple Chapters
- Entire Source

Deferred until later:

- Topic filtering
- Body system filtering
- Mixed-topic generation
- Additional publishers

---

# Next Milestone

Implement the Pack Loader.

Objectives:

- Load Runtime Study Packs.
- Update the Study Engine to consume Runtime Study Packs.
- Complete the first end-to-end workflow from supported source material through study delivery.

Current development priorities:

1. Finish the complete workflow.
2. Maintain support for the validated Medical-Surgical and Pharmacy sources.
3. Delay additional publishers until the complete workflow is operational.
4. Prioritize proven functionality over architectural refinement.

---

# Repository Status

Branch:

master

Status:

Compiler milestone committed.

Documentation update in progress.

Remote:

Local branch is ahead of origin.

The compiler pipeline is operational for the currently supported sources.

The current objective is completing the functional workflow before revisiting architecture or optimization.