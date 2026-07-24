# PREPFLOW ARCHITECTURE BIBLE

> **Continuity note:** This document was rebuilt after the July 2026 forensic review of PrepFlow. Earlier versions are preserved in Git history and in the frozen tag `before-continuity-rebuild-2026-07-20`. If a removed pathway or decision seems unclear, inspect that baseline for historical context. Older documents explain how PrepFlow arrived here; this document is the active architectural authority.

## Purpose

This document defines PrepFlow's durable technical architecture.

It contains:

- what PrepFlow is;
- the permanent responsibility of each major part;
- the boundaries between ingestion, Packs, quiz behavior, and presentation;
- architectural rules that should survive individual milestones.

It does not contain current tasks, temporary milestones, session notes, or implementation status. Those belong in `docs/RESTART_PACKET.md`.

---

# 1. Product Definition

PrepFlow is primarily a document-ingestion, sanitization, structuring, and study-library system.

Its defining purpose is:

> Take deliberately chosen educational material, clean and organize it, turn it into an authoritative independent PrepFlow Pack, and provide study tools that use that Pack.

The visible quiz, open-book interface, characters, medication reference, and future coaching features are ways of using the structured library. They are important experiences, but they are not the underlying core.

The permanent flow is:

```text
Chosen educational source
        ↓
Source extraction
        ↓
Cleaning and sanitization
        ↓
Structure detection and parsing
        ↓
Normalization and validation
        ↓
Permanent PrepFlow question identity
        ↓
Independent authoritative Pack
        ↓
Browser study application
```

---

# 2. Authority Model

PrepFlow does not independently fact-check an entire nursing curriculum before admitting content.

The authority rule is:

> Material deliberately selected for import becomes authoritative study material inside its own Pack after it passes PrepFlow's cleaning, structural validation, and review process.

Each Pack remains a separate authority boundary.

This means:

- sources are not silently blended into one universal truth database;
- chapter organization may follow the selected source because it matches the intended course structure;
- a contaminated, poisoned, obsolete, or unwanted Pack can be deleted or rebuilt as a unit;
- one Pack does not depend on detailed publisher or page-level provenance stored inside every question.

The finished Pack is the study authority. The original source is temporary import material.

---

# 3. Core Data Model

## 3.1 Pack

A finished Pack requires:

- permanent Pack ID;
- user-facing title;
- format/schema version as needed for compatibility;
- questions.

## 3.2 Question

A finished question requires:

- permanent PrepFlow question ID;
- chapter;
- chapter title when useful for display;
- question type;
- stem;
- choices where applicable;
- correct answer or ordered answers;
- rationale.

Optional future enrichment may include concepts, medication classes, body systems, clinical relationships, or study tags. These fields are optional unless a future product decision makes them necessary.

Publisher, edition, page, Bloom level, difficulty, and detailed source provenance are not required in the finished study record.

---

# 4. Permanent Question Identity

Question identity must not depend on array position, display order, or neighboring questions.

Approved rule:

> A question receives a permanent PrepFlow identity that does not change merely because its position, chapter order, or surrounding questions change.

The source question number and chapter are organizational fields, not the true identity.

Permanent identity must support:

- Pack rebuilds;
- saved sessions;
- corrections;
- duplicate detection;
- future analytics;
- medication or concept relationships;
- stable references across versions.

The exact ID algorithm may evolve, but it must preserve existing identity whenever the same question is rebuilt and create a new identity only for genuinely new content.

---

# 5. Ingestion Architecture

## 5.1 Source Adapters

A source adapter opens one file format and returns usable text or a simple neutral extraction structure.

Examples include:

- PDF;
- future DOCX;
- future TXT;
- possible future HTML;
- OCR only as a separate later project.

Adapters may understand file-format structure such as pages, paragraphs, headings, or tables. They must not contain a separate question-processing architecture for each format.

Approved rule:

> Different source formats feed one shared cleaning, detection, parsing, normalization, validation, and Pack-building pipeline.

## 5.2 Extraction

Extraction retrieves source content while preserving enough structure for later processing.

It does not decide whether text is a question, answer, rationale, or contamination.

## 5.3 Cleaning

Cleaning removes non-educational noise while preserving the selected educational material.

Typical responsibilities include:

- download-site contamination;
- branding and repeated source fragments;
- page headers and footers;
- broken extraction artifacts;
- repeated indexes or proven duplicated source blocks;
- narrowly evidenced source-specific contamination rules.

Cleaning must not casually rewrite stems, choices, answers, or rationales.

## 5.4 Detection

Detection measures and reports source structure before parsing.

It identifies evidence such as:

- chapters;
- section headings;
- answer markers;
- question-like blocks;
- unknown or unsupported patterns.

Detection exposes uncertainty rather than hiding it.

## 5.5 Parsing

The parser turns cleaned source text into candidate question records.

It owns recognition and recovery of:

- chapter and chapter title;
- source question number;
- question type;
- wrapped stems;
- split or wrapped choices;
- inline and multiline answers;
- rationales;
- Multiple Choice;
- Multiple Response;
- Completion;
- Ordered Response;
- source structures proven through real imports.

The parser does not create final permanent identity and does not decide user-interface behavior.

## 5.6 Normalization

Normalization converts supported parser output into one consistent compiler input shape.

It may resolve compatible field names and safe structural differences. It must not become a second parser or silently invent educational content.

## 5.7 Validation

Validation decides whether candidate records are structurally safe to admit.

Severity model:

- **Fatal:** the Pack cannot safely be built.
- **Recoverable:** the affected question is quarantined or skipped while valid questions may proceed.
- **Advisory:** a concern is recorded but the question remains eligible.

Validation may check:

- missing stem;
- missing answer;
- missing rationale;
- required choices missing;
- answer references missing choice;
- unsupported type;
- remaining contamination;
- genuine exact duplicates;
- identity conflicts.

Validation does not independently certify medical truth.

## 5.8 Deduplication

Only genuine exact duplicates should be removed automatically.

Near-duplicates remain because similar questions may test different judgments, appear in different chapters, or provide valuable repetition in different contexts.

Safe duplicate decisions should consider more than the stem, including choices, answer, rationale, and Pack/chapter context.

Every automatic removal should be explainable and reportable.

## 5.9 Pack Compilation

The compiler:

- receives normalized validated candidate records;
- preserves or assigns permanent PrepFlow IDs;
- builds the finished Pack;
- exports only fields PrepFlow intentionally needs.

The permanent output of ingestion is the Pack, not the original source or temporary extraction artifacts.

---

# 6. Pack Library

The library hierarchy is:

```text
Pack
└── Chapter
    └── Question
```

Each Pack is independently removable and rebuildable.

The browser consumes finished Packs only. It does not parse private source files or repair malformed Pack content during a quiz.

Original source material, temporary extraction output, diagnostics, and publisher-specific clutter remain outside the finished library unless temporarily needed during import review.

---

# 7. Browser Study Architecture

The browser is the only active client that currently matters for compatibility decisions.

The browser application should contain two distinct responsibilities.

## 7.1 Quiz Behavior Layer

The quiz behavior layer owns rules that must remain stable regardless of visual redesign:

- collect the full selected question pool;
- support selected chapters across Packs;
- allow **Shuffle Questions** or **Keep Source Order**;
- keep order stable after a session begins;
- configurable block size;
- one question at a time;
- grading by question type;
- first-pass correct and missed tracking;
- missed-question review until mastered;
- block transitions;
- final first-pass result;
- save/resume state meaning.

Quiz behavior should be testable without depending on the screen layout or DOM structure.

## 7.2 Browser GUI

The GUI displays state and collects user input.

It owns:

- home screen;
- book interface;
- buttons;
- chapter controls;
- answer controls;
- progress display;
- rationale presentation;
- results screens;
- visual themes;
- characters and animation;
- responsive layout;
- accessibility presentation.

The GUI should not independently invent scoring, review, or session rules.

## 7.3 Question-Type Rule

The active browser study system is intended to support:

- Multiple Choice;
- Multiple Response;
- Completion;
- Ordered Response.

A question type present in an approved Pack should not require a separate legacy desktop client merely to remain usable.

## 7.4 Save and Resume

Saved state belongs to the active browser study system.

It should preserve the meaning of:

- selected question set;
- established question order;
- current position;
- block state;
- first-pass score;
- missed questions;
- review queue;
- active screen/state.

The storage mechanism may evolve, but the behavioral meaning should remain stable.

---

# 8. Offline Architecture

The service worker defines the browser application's offline promise.

The offline contract must be explicit:

- either the complete installed product is available on first offline use;
- or a narrower promise is documented and tested.

Shell, Packs, visual assets, medication-reference assets, scripts, and styles should not be assumed available offline merely because some were loaded previously.

---

# 9. Medication Reference

Medication reference content is a separate library feature that may use Pack relationships but should not be permanently gated by the Pharm Pack.

Long-term direction:

- stable independent medication records;
- source mappings to Pharm, Med-Surg, Fundamentals, and future Packs;
- optional relationships used for study and coaching;
- no requirement that a valid medication exist in Pharm before it can exist in the reference library.

Medication architecture is secondary to the core ingestion, Pack, identity, and browser-study boundaries.

---

# 10. Visual System

PrepFlow's visual identity is intentional and must remain structurally separate from changing application state.

The detailed authority for artwork, rendering, formats, asset folders, and approved visual decisions is:

```text
docs/ART_SYSTEM.md
```

## 10.1 Visual ownership boundaries

The home experience is composed from separate layers with separate owners.

### Background plate

The background plate owns static scene artwork such as:

- environment;
- skyline;
- sunset;
- architecture;
- environmental lighting;
- noninteractive scenery.

It must not permanently own characters, books, controls, counts, progress, or changing application data.

### Nurse sprites

Nurses are reusable transparent raster assets.

They own character appearance, clothing, pose, expression, and character-specific rendering.

They must remain separate from the rebuilt background plate so the same characters can support additional screens and poses.

### Book assets

The three subject books are separate transparent clickable assets.

They own permanent subject identity, cover artwork, icons, pages, spine, tabs, and permanent PrepFlow branding.

They must not contain changing totals, selected-chapter state, accessibility text, Pack paths, or interaction behavior.

### HTML and JavaScript

HTML and JavaScript own:

- subject-button structure;
- Pack paths;
- accessibility labels;
- chapter-selection counts and state;
- saved-session state;
- click behavior;
- enabled and disabled behavior;
- quiz and progress data.

### CSS

CSS owns:

- placement;
- display size;
- equal spacing;
- responsive composition;
- hover, pressed, disabled, and focus presentation;
- glow and drop-shadow treatment;
- live badge placement.

CSS must not redraw the principal final books, nurses, or background artwork.

## 10.2 Permanent artwork versus live data

Permanent identity may be baked into approved artwork.

Changing application information must remain live HTML and JavaScript.

Do not bake question totals, selection counts, progress, or status into closed-book artwork or static scene files.

## 10.3 Asset reuse

Approved committed artwork must be reused rather than recreated unnecessarily.

Visual consolidation must be staged, visually conservative, and verified in the real browser application before commitment.

---

# 11. Testing and Verification

Tests protect active PrepFlow behavior, not obsolete implementations.

Required direction:

- keep strong ingestion/compiler tests;
- add browser-centered tests for quiz behavior;
- validate Pack structure and identity rules;
- verify the hosted browser experience manually where automation is not yet practical;
- replace the old desktop-build workflow with automatic verification on pushes and pull requests.

Deleting old tests is safe only after equivalent active-product behavior is protected or deliberately rejected.

---

# 12. Legacy Code Policy

Unreleased desktop and terminal compatibility has no architectural authority.

Approved rule:

> Preserve valuable capabilities and behavior, not obsolete implementations.

A legacy pathway may be removed when:

- the active browser does not use it;
- it contains no unique ingestion or library capability;
- any still-wanted behavior is already implemented or protected elsewhere;
- Git history and the frozen baseline preserve recovery options.

The old Tkinter desktop application, terminal client, PyInstaller packaging, desktop update system, and rigid DOCX prototype are not strategic assets merely because they exist.

Proper future DOCX support should be a source adapter feeding the main ingestion pipeline.

---

# 13. Future Downloadable Applications

There is no obligation to preserve unreleased desktop compatibility.

A future Windows or macOS application should most likely package the cleaned browser-centered product rather than revive the Tkinter client by default.

Platform packaging may differ, but the following must not be redefined separately for each platform:

- Pack meaning;
- question identity;
- quiz rules;
- grading;
- scoring;
- review behavior;
- save-state meaning.

---

# 14. Repository Boundaries

Permanent product areas include:

- active compiler/ingestion code;
- finished Packs;
- browser application code and assets;
- tests protecting active behavior;
- durable documentation.

The repository must not contain:

- private source books;
- personal identifying information;
- scratch extraction files;
- generated build output;
- release archives;
- obsolete temporary Packs;
- one-time source-specific scripts that should have been absorbed into the shared pipeline.

Generated artifacts may exist locally under ignored working directories.

---

# 15. Architectural Principles

1. PrepFlow is a cleaning, structuring, and Pack-building system first.
2. Packs are independent study-authority boundaries.
3. The finished Pack, not the original source, is the permanent study product.
4. Question identity remains stable across reorder, deletion, and rebuild.
5. Source formats share one ingestion pipeline after extraction.
6. Cleaning preserves educational meaning.
7. Detection exposes uncertainty.
8. Parsing recovers source structure but does not control the GUI.
9. Validation protects structural usability, not universal medical truth.
10. Only genuine exact duplicates are removed automatically.
11. Near-duplicates remain unless deliberately reviewed.
12. The browser is the active compatibility target.
13. Quiz behavior and GUI presentation have separate responsibilities.
14. Optional tags and analytics must not block ordinary import.
15. Legacy implementations may be removed when active value is absent.
16. Future downloads should reuse the cleaned browser-centered product.
17. One focused change, test, verify, commit, and repeat.

---

# 16. Change Control

Update this document only when durable architecture changes.

Do not place temporary milestones, current branch state, dated addenda, or the next executable task here.

Those belong in `docs/RESTART_PACKET.md`.

For the detailed reasoning and migration classification behind the July 2026 rebuild, consult `docs/CONTINUITY_REBUILD_PLAN.md` and the frozen tag `before-continuity-rebuild-2026-07-20`.
