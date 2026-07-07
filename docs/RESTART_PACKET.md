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

The canonical compiler pipeline is operational.

The compiler has been successfully verified against a production DOCX source and produces Runtime Study Packs.

Current development is focused on completing the end-to-end workflow before adding new functionality.

The long-term objective remains fully supporting the existing Medical-Surgical and Pharmacy sources before introducing additional publishers.

---

# Current Architecture

PrepFlow consists of three major systems.

## 1. Import Layer

Responsibilities:

- Read supported source material.
- Tokenize DOCX.
- Parse source content.

Supported inputs:

- DOCX
- JSON

Future:

- PDF
- CSV
- AI-assisted imports

---

## 2. Canonical Compiler

Verified compiler pipeline:

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

Each stage has exactly one responsibility.

---

## 3. Applications

Applications consume compiler functionality.

Current:

- Compiler CLI
- Study Engine (next major integration)

Future:

- Desktop GUI
- API
- Automated testing

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

The Canonical Pack is the internal source of truth.

---

# Runtime Study Pack

Implemented.

The Exporter converts Canonical Packs into lean Runtime Study Packs.

Runtime Packs intentionally contain only the information required by the Study Engine.

Current Runtime Question fields:

- id
- chapter
- type
- stem
- choices
- correct_answers
- rationale

The Runtime Pack intentionally excludes publisher artifacts, parser history, watermark text, importer metadata, and unnecessary compiler information.

---

# Compiler Status

Implemented:

- Reader
- Tokenizer
- Parser
- Normalizer
- Validator
- Deduplicator
- Builder
- Exporter
- Compiler Pipeline
- Typed Diagnostics
- CLI orchestration

Compilation Policy:

Implemented.

Diagnostic levels:

- Fatal
- Recoverable
- Advisory

Behavior:

- Fatal diagnostics abort compilation.
- Recoverable diagnostics skip affected questions.
- Advisory diagnostics are reported without preventing export.

Verified against a production source:

- Parsed Questions: 220
- Recoverable Questions Skipped: 1
- Duplicate Questions Removed: 22
- Runtime Questions Produced: 197

---

# Compiler Data Flow

PrepFlow uses three internal representations.

1. Parsed Question

Raw parser output.

2. Normalized Question

Validated compiler input.

3. Canonical Question

Immutable PrepFlow domain object.

Applications consume Runtime Study Packs rather than parser output.

---

# Known Source Data Issues

Confirmed source-data issues:

- Duplicate question block (Questions 41–60)
- Missing correct answer and rationale (Question 80)
- Duplicate stems (Questions 117 and 156)

These are source defects rather than compiler defects.

---

# Immediate Next Task

Implement the Pack Loader.

Objectives:

- Load Runtime Study Packs.
- Update the Study Engine to consume Runtime Study Packs.
- Complete the first fully functional end-to-end workflow.

Do not begin adding new publishers until this workflow is complete.

---

# Study Engine Scope

Current functional goal:

Support selecting questions by:

Source:

- Pharmacy
- Medical-Surgical

Selection:

- Single Chapter
- Multiple Chapters
- Entire Source

Deferred:

- Topic filtering
- Body system filtering
- Mixed-topic generation
- Additional publishers

---

# Repository Status

Branch:

master

Status:

One compiler milestone committed.

Documentation update in progress.

Remote:

Local branch is ahead of origin.

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

Canonical Pack is the internal source of truth.

Runtime Study Pack is the application format.

Never silently repair source data.

Prefer diagnostics over hidden fixes.

Each compiler stage has exactly one responsibility.

PrepFlow is library-first.

Applications consume reusable compiler functionality.

---

# Permanent Development Workflow

Primary objective:

Build a reliable compiler that transforms supported source material into clean Runtime Study Packs.

Functionality takes priority over elegance.

Complete the workflow before optimizing or redesigning.

When implementing or debugging:

1. Observe actual behavior.
2. Inspect the relevant code.
3. Make one focused change.
4. Save.
5. Compile.
6. Test.
7. Repeat.

Avoid speculative redesign during debugging.

Avoid multiple simultaneous fixes.

Verify every milestone against real source documents before expanding the architecture.

For documentation:

Prefer replacing complete documentation files so they accurately reflect the current project state.

---

# VS Code Rule

When creating new files:

Never type:

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
2. Verify functionality.
3. Review git status.
4. Commit code.
5. Update documentation.
6. Commit documentation.
7. Push.
8. Verify repository state.
9. Rewrite this restart packet completely.
10. End session.