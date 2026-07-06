# ARCHITECTURE_BIBLE

## Purpose

This document defines the permanent architecture of PrepFlow.

Architectural decisions recorded here are considered stable unless explicitly revised.

---

# Design Philosophy

PrepFlow is a library-first study platform.

The compiler, study engine, and future applications are independent systems connected through a shared canonical data model.

All study content is supplied through interchangeable Packs.

Applications consume reusable compiler components rather than implementing compiler logic themselves.

The application contains no nursing-specific logic.

---

# System Architecture

PrepFlow consists of three major systems.

## 1. Import Layer

Purpose:

Convert supported source material into parsed question dictionaries.

Supported inputs:

- DOCX
- JSON

Future inputs:

- PDF
- CSV
- AI-assisted imports

The Import Layer performs extraction only.

It does not validate, repair, or build canonical objects.

---

## 2. Canonical Compiler

The compiler transforms parsed question dictionaries into canonical PrepFlow objects.

Compiler pipeline:

Reader / Loader

↓

Tokenizer (DOCX only)

↓

Parser (DOCX only)

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

Each compiler stage has exactly one responsibility.

---

## 3. Applications

Applications consume the compiler.

Current applications:

- Compiler CLI
- Study Engine

Future applications:

- Desktop GUI
- Web API
- Automated testing
- Additional exporters

Applications never duplicate compiler logic.

---

# Compiler Stages

## Reader / Loader

Loads source material.

DOCX uses the Reader.

JSON uses the Loader.

---

## Tokenizer

Converts raw document content into parser tokens.

DOCX only.

---

## Parser

Extracts question dictionaries from tokens.

Parser never validates.

Parser never repairs source data.

---

## Normalizer

Converts supported source formats into one compiler input schema.

Normalization handles source compatibility.

No later compiler stage performs schema translation.

---

## Validator

Reports structural problems.

Examples:

- Missing stem
- Missing answer choices
- Missing correct answer
- Missing rationale
- Missing question type
- Duplicate question numbers
- Duplicate stems

Validator reports problems only.

Validator never repairs data.

---

## Deduplicator

Removes duplicate records after validation.

Responsibilities:

- Keep first occurrence
- Remove duplicate question numbers
- Remove duplicate stems
- Report every removal

---

## Builder

Creates canonical PrepFlow objects.

Responsibilities:

- Build Question objects
- Build Pack objects

---

## Exporter

Writes canonical Packs into reusable formats.

Future exporters may include:

- JSON
- PrepFlow Pack
- Additional interchange formats

---

# Canonical Domain Model

The canonical model consists of:

Pack

↓

Question

↓

Answer

Additional supporting objects include:

- Origin
- Content
- Classification
- Metadata

Rules:

Pack owns Questions.

Question never owns Pack.

Stable Question IDs are publisher independent.

---

# Core Objects

## Pack

A complete collection of study material.

A Pack owns:

- Questions
- Metadata

Sections remain optional.

---

## Section

Optional organization inside a Pack.

Examples:

- Chapter
- Topic
- Body System

Not all Packs require Sections.

---

## Session

A temporary study instance.

Responsibilities:

- Shuffle questions
- Build Blocks
- Track scoring
- Track mastery
- Feed Review Queue

---

## Block

A balanced subset of questions.

Goals:

- Approximately 15 questions
- Sequential presentation
- Locked after creation

---

## Review Queue

Contains only missed questions.

Questions repeat until answered correctly.

First-attempt score never changes.

Mastery is tracked independently.

---

# Compiler Data Flow

PrepFlow recognizes three internal representations.

## Parsed Question

Raw parser output.

May vary depending on source format.

---

## Normalized Question

Compiler input.

Every supported source is converted into this representation before validation.

---

## Canonical Question

Immutable domain object used throughout PrepFlow.

Applications consume canonical objects rather than parser output.

---

# Guiding Principles

- Library first.
- Applications consume reusable compiler code.
- One responsibility per compiler stage.
- Never silently repair source data.
- Prefer diagnostics over hidden fixes.
- Normalize once.
- Build once.
- Reuse forever.
- Stable Question IDs.
- End users never require programming knowledge.

---

# Future Expansion

Architecture should support:

- Multiple Packs
- Multiple publishers
- Saved Sessions
- Statistics
- Desktop GUI
- Web API
- Mobile interface
- Community-created Packs
- Additional import formats
- Additional export formats

---

This document defines architecture only.

Project progress belongs in PROJECT_STATE.md.

Historical changes belong in CHANGELOG.md.

Session handoffs belong in RESTART_PACKET.md.