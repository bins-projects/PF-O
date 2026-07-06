# PrepFlow Pack Specification

Version: 0.1  
Project Version: 0.6.2  
Sprint: 7 — Pack Standardization  

## Purpose

The Pack Specification defines the official internal data format for PrepFlow.

Every importer, compiler, validator, study engine, GUI, and future feature must treat this document as the contract for what a valid PrepFlow pack and question look like.

---

## Core Vocabulary

### Question

A single standardized assessment item.

### Pack

A collection of standardized Questions plus metadata.

### Importer

Reads a source file and extracts raw content.

### Parser

Interprets imported content into structured question data.

### Compiler

Converts parsed data into canonical PrepFlow Question objects and assembles Packs.

### Validator

Verifies that a Pack conforms to this specification.

### Study Engine

Delivers Questions to learners and records results.

### Pack Specification

The formal contract defining Question and Pack structure.

---

## Design Principles

1. A question is not its textbook.
2. PrepFlow owns the identity of every question.
3. Source information is preserved as origin data.
4. Production packs should not contain raw source text.
5. The study engine should not care where a question came from.
6. All packs must use the same internal structure.

---

## Question Object

Every question must use this structure:

```json
{
  "identity": {
    "id": "PFQ-000000001",
    "pack_id": "pharm_workman_ch15_20_v1",
    "version": 1
  },
  "origin": {
    "publisher": "",
    "book": "",
    "edition": "",
    "chapter": "",
    "section": "",
    "page": null,
    "source_id": ""
  },
  "content": {
    "stem": "",
    "choices": [],
    "rationale": ""
  },
  "answer": {
    "type": "",
    "value": null
  },
  "classification": {
    "concepts": [],
    "tags": [],
    "body_system": null,
    "difficulty": null,
    "bloom_level": null
  },
  "metadata": {
    "created": "",
    "compiler_version": "",
    "validated": false,
    "notes": []
  }
}