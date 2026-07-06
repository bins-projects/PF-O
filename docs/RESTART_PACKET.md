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

Sprint 7 is actively restructuring PrepFlow into a reusable, library-first architecture.

Production importers are complete.

Current work is focused on separating importing, compilation, and study functionality into independent layers.

---

# Architecture Overview

PrepFlow is organized into three major systems.

## 1. Import Layer

Purpose:

Convert source material into parsed question dictionaries.

Current supported inputs:

- DOCX
- Existing JSON question banks

Future inputs:

- PDF
- CSV
- AI-assisted imports

Current production data includes:

- output/medsurg_questions.json
- output/pharm_questions.json
- output/pharm_ch13_17_questions.json
- output/pharm_ch15_20_questions.json

Importers are considered production ready.

---

## 2. Canonical Compiler Pipeline

Current pipeline:

Reader / JSON Loader

↓

Tokenizer (DOCX only)

↓

Parser (DOCX only)

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

Current philosophy:

Each stage has exactly one responsibility.

---

## 3. Applications

Applications consume the canonical compiler.

Current applications:

- Compiler CLI
- Study Engine

Future applications:

- GUI
- API
- Automated testing
- Additional export tools

Applications should never duplicate compiler logic.

---

# Canonical Domain Model

Implemented:

compiler/models.py

Canonical dataclasses:

- Answer
- Origin
- Content
- Classification
- Metadata
- Question
- Pack

Design rules:

Pack owns Questions.

Question never owns Pack.

Stable question IDs are publisher independent.

---

# Compiler Components

## Validator

File:

compiler/validator.py

Responsibilities:

- detect duplicate question numbers
- detect duplicate stems
- detect missing stems
- detect missing answer choices
- detect missing correct answers
- detect missing rationales
- detect missing question type

Validator reports problems only.

Validator never repairs source data.

Current duplicate diagnostics include:

- duplicate question
- original matching question
- stem preview

---

## Deduplicator

File:

compiler/deduplicator.py

Added during this session.

Responsibilities:

- keep first occurrence
- remove duplicate question numbers
- remove duplicate stems
- report every removal

Returns:

DeduplicationResult

---

## Builder

File:

compiler/builder.py

Responsibilities:

Convert validated dictionaries into canonical objects.

Current functions:

- build_question()
- build_questions()
- build_pack()

---

## Pipeline

File:

compiler/pipeline.py

Added during this session.

Introduced:

CompilationResult dataclass

compile_questions()

Purpose:

Reusable compiler pipeline independent of:

- CLI
- DOCX
- JSON loading
- printing
- sys.exit()

Current flow:

questions

↓

validate_questions()

↓

deduplicate_questions()

↓

build_questions()

↓

build_pack()

↓

CompilationResult

---

# CLI Status

File:

compiler/cli.py

Current state:

Supports:

- DOCX input
- JSON input

Validation now occurs before canonical building.

Deduplication stage exists.

Current limitation:

CLI still duplicates compiler pipeline logic.

---

# Immediate Next Task

Refactor:

compiler/cli.py

Goal:

CLI should become an orchestrator only.

Desired flow:

DOCX

↓

Reader

↓

Tokenizer

↓

Parser

↓

compile_questions()

↓

Print results

JSON

↓

Load JSON

↓

compile_questions()

↓

Print results

Validation, deduplication, and building should only exist inside compiler/pipeline.py.

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
- All chapters

Deferred until later:

- topic filtering
- body system filtering
- mixed-topic packs
- additional publishers

No new source banks should be added until this workflow is complete.

---

# Known Source Data Issues

Question 80

Missing:

- correct answer
- rationale

Confirmed source issue.

Not a parser or validator bug.

---

Duplicate Block

Questions:

41–60

Duplicate question numbers and duplicate stems.

Investigate original source document before implementing aggressive deduplication.

---

Duplicate Stems

Questions:

117

156

Require investigation.

---

# Repository Status

Current repository state has been committed and pushed.

Current Git baseline:

Sprint 7: establish canonical compiler pipeline

Repository is synchronized with GitHub.

Generated export JSON files remain intentionally untracked until exporter policy is finalized.

---

# Permanent Architecture Rules

Parser parses.

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

Use exact code landmarks.

---

# VS Code Rule

When creating new files:

Never enter:

compiler/example.py

into the New File dialog.

Instead:

1. Select the existing destination folder.
2. Choose New File.
3. Enter only:

example.py

This prevents accidental nested folders.

---

# End-of-Session Workflow (Permanent)

Every coding session ends in this order:

1. Compile modified Python files.
2. Review git status.
3. Commit.
4. Push.
5. Completely rewrite docs/RESTART_PACKET.md.
6. Verify repository state.
7. End session.

The restart packet is never appended to.

It is rewritten completely every session.

Its purpose is to allow a brand-new ChatGPT conversation to resume development immediately.

---

# Documentation Responsibilities

VISION.md

Project purpose.

Rarely changes.

ARCHITECTURE_BIBLE.md

System architecture.

Changes occasionally.

PROJECT_STATE.md

Current milestone status.

Updated at major milestones.

CHANGELOG.md

Historical log.

Append only.

Never rewritten.

RESTART_PACKET.md

Current engineering handoff.

Completely rewritten every coding session.

Primary bootstrap document for all future development sessions.