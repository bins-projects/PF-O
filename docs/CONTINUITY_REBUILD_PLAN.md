# PREPFLOW CONTINUITY REBUILD DECISION MAP

> **Continuity note:** This document was created after the July 2026 forensic review of PrepFlow. Earlier documentation, implementation history, and abandoned pathways are preserved in Git history and in the frozen tag `before-continuity-rebuild-2026-07-20`. If a decision below seems unclear, inspect that baseline before assuming information was accidentally lost. Historical material explains how PrepFlow arrived here; this document records the approved direction from this point forward.

## Purpose

This document connects three things:

1. what the repository actually contains;
2. what Charlie has decided PrepFlow is;
3. how to move from the current implementation to the approved architecture without losing working behavior.

It is intentionally detailed. It is not the long-term Architecture Bible and it is not the everyday Restart Packet. It is the migration decision map used to rebuild both documents and then guide the cleanup.

No implementation should be deleted or substantially reorganized until the relevant behavior and verification gate in this plan are understood.

---

# 1. Product Definition

PrepFlow is primarily a document-ingestion, sanitization, structuring, and library-building system.

Its defining purpose is:

> Take deliberately chosen educational material, clean and organize it, turn it into an authoritative independent PrepFlow Pack, and provide study tools that use that Pack.

The visible quiz, open-book interface, characters, medication reference, and future coaching features are ways of using the structured library. They are important product experiences, but they are not the underlying core.

The core flow is:

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

PrepFlow does not independently fact-check an entire nursing curriculum before allowing content into a Pack.

The authority rule is:

> Material deliberately selected for import becomes authoritative study material inside its own Pack after it passes PrepFlow's cleaning, structural validation, and review process.

This is appropriate because the material is generally selected to match the class, instructor, course resources, or testing environment being studied.

PrepFlow accepts the practical risk that a chosen source may contain inaccurate or outdated material. The Pack boundary limits that risk:

- each source collection remains its own book/Pack;
- sources are not silently blended into one universal truth database;
- a contaminated, poisoned, or unwanted Pack can be deleted or rebuilt as a unit;
- the validity of one Pack does not depend on preserving publisher or page-level provenance for every question.

The finished Pack is the study authority. The original source is temporary import material.

---

# 3. Minimum Canonical Study Record

The finished library does not need speculative publisher, edition, page, Bloom level, difficulty, or detailed source-provenance fields merely because an earlier model allowed them.

The required Pack-level fields are:

- permanent Pack ID;
- user-facing Pack title;
- format/schema version as needed for compatibility;
- questions.

The required question-level fields are:

- permanent PrepFlow question ID;
- chapter;
- chapter title when useful for display;
- question type;
- stem;
- choices where applicable;
- correct answer or ordered answers;
- rationale.

Optional future enrichment may include:

- concepts;
- medication classes;
- body systems;
- clinical relationships;
- study tags used for coaching or cross-reference features.

Optional enrichment must not become a requirement for ordinary import unless a future product decision changes this rule.

---

# 4. Permanent Question Identity

The current ID generator assigns IDs by export position. That means deleting or inserting an earlier question can renumber later questions.

That is not acceptable as the long-term identity model.

Approved requirement:

> A question receives a permanent PrepFlow identity that does not change merely because its display order, chapter position, or neighboring questions change.

A permanent identity supports:

- saved sessions;
- corrections;
- duplicate detection;
- future analytics;
- medication or concept relationships;
- Pack rebuilds;
- consistent references across versions.

The source question number and chapter remain organizational fields, not the true identity.

The exact ID algorithm is not yet selected. The implementation design must address:

- assigning an ID once;
- recognizing the same question during a rebuild;
- preserving an existing ID through minor corrections;
- creating a new ID only for genuinely new content;
- avoiding dependence on array position.

This is a core library requirement, not optional metadata.

---

# 5. Approved Responsibility Map

## 5.1 Source Adapters

Source adapters open a particular file format and return usable source text or a simple neutral extraction structure.

Examples:

- PDF adapter;
- future DOCX adapter;
- future TXT adapter;
- possible future HTML adapter;
- OCR only as a separate later project.

Adapters may understand file-format structure such as pages, paragraphs, headings, or tables. They must not contain a separate question engine for each format.

Approved rule:

> Different source formats feed one shared cleaning, detection, parsing, normalization, validation, and Pack-building pipeline.

## 5.2 Extraction

Extraction retrieves content while preserving enough structure for later processing.

It does not decide whether text is a question, answer, rationale, or contamination.

## 5.3 Cleaner

The cleaner removes non-educational noise while preserving the selected educational material.

Typical responsibilities:

- download-site contamination;
- branding and repeated source fragments;
- page headers and footers;
- broken extraction artifacts;
- repeated indexes or known duplicated source blocks;
- narrowly evidenced source-specific contamination rules.

The cleaner should not casually rewrite stems, choices, answers, or rationales.

## 5.4 Detector

Detection measures and reports source structure before parsing.

It identifies evidence such as:

- chapters;
- section headings;
- answer markers;
- question-like blocks;
- unknown or unsupported patterns.

Detection exposes uncertainty rather than hiding it.

## 5.5 Parser

The parser turns cleaned source text into candidate question records.

It owns recognition and recovery of:

- chapter and chapter title;
- source question number;
- question type;
- wrapped stems;
- split or wrapped choices;
- inline and multiline answers;
- rationales;
- Completion questions;
- Multiple Response questions;
- Ordered Response questions;
- source structures proven through real imports.

The parser does not create final permanent identity or decide user-interface behavior.

## 5.6 Normalizer

The normalizer converts supported parser output into one consistent compiler input shape.

It may resolve compatible field names and safe structural differences. It should not become a second parser or silently invent educational content.

## 5.7 Validator

The validator decides whether candidate records are structurally safe to admit.

Approved severity model:

- **Fatal:** the Pack cannot safely be built.
- **Recoverable:** the affected question is quarantined/skipped while valid questions may proceed.
- **Advisory:** a concern is recorded but the question remains eligible.

Validation concerns include:

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

Near-duplicates stay because similar questions may test different judgments, appear in different chapters, or provide valuable repetition in different contexts.

Safe duplicate decisions should compare more than the raw stem. At minimum consider:

- stem;
- choices;
- correct answer;
- rationale;
- Pack/chapter context.

Every automatic removal should be explainable and reportable.

## 5.9 Pack Compiler

The compiler:

- receives normalized validated candidate records;
- preserves or assigns permanent PrepFlow IDs;
- builds the finished Pack;
- exports only the fields PrepFlow intentionally needs.

Publisher and page-level provenance are not required in the finished Pack.

## 5.10 Pack Library

The Pack library is the permanent product output of ingestion.

The organizational hierarchy is:

```text
Pack
└── Chapter
    └── Question
```

Each Pack is an independent authority boundary and can be removed or rebuilt independently.

## 5.11 Browser Quiz Behavior Layer

The browser is the only active client that matters for compatibility decisions today.

The quiz behavior layer should own rules that must remain consistent regardless of visual redesign:

- collect the full selected question pool;
- support selected chapters across Packs;
- optional Shuffle or Keep Source Order setting;
- stable question order after session start;
- configurable block size;
- one question at a time;
- answer grading by question type;
- first-pass correct and missed tracking;
- missed-question review until mastered;
- block transitions;
- final first-pass result;
- save/resume state meaning.

The current browser implements much of this directly inside `web/app.js`. The approved future direction is to separate quiz/session rules from DOM manipulation enough that behavior can be tested without depending on screen layout.

This does not require a grand rewrite or a server. It requires a clearer internal boundary inside the browser code.

## 5.12 Browser GUI

The GUI displays state and collects user input.

It owns:

- home screen;
- book interface;
- buttons;
- chapter checkboxes;
- answer controls;
- progress display;
- rationale presentation;
- result screens;
- visual themes;
- characters and animation;
- responsive layout;
- accessibility presentation.

The GUI should not independently invent scoring, review, or session rules.

## 5.13 Optional Analytics and Enrichment

Future analytics may interpret results using optional tags.

Example:

```text
Missed questions tagged with:
- ARBs
- diuretics
- calcium monitoring

Future result:
- recommend reviewing those topics
```

This is deferred enrichment. It should not block the current cleanup.

## 5.14 Offline Layer

The service worker controls the browser application's offline promise.

The current worker explicitly precaches the shell and three Packs, while many layered visual and medication-reference assets depend on having been loaded before going offline.

The future offline contract must be explicit:

- either complete first-install offline support;
- or a narrower documented promise.

## 5.15 Future Downloadable Applications

There is no obligation to preserve unreleased desktop compatibility.

A future Windows or macOS download should most likely package the cleaned browser-centered application rather than revive the Tkinter application merely because it exists.

Platform packaging may differ, but question meaning, Pack structure, quiz rules, scoring, and saves should not be redefined separately for each platform.

---

# 6. Confirmed Current Implementation

## 6.1 Active Core

The active and valuable Python side is the ingestion/compiler pipeline:

- `compiler/importer.py`
- `compiler/pdf_reader.py`
- `compiler/cleaner.py`
- `compiler/detector.py`
- `compiler/source_parser.py`
- `compiler/normalizer.py`
- `compiler/validator.py`
- `compiler/builder.py`
- `compiler/exporter.py`
- `compiler/pipeline.py`
- `compiler/models.py`
- `compiler/ids.py`
- `compiler/diagnostics.py`

These files are core PrepFlow, although identity, validation references, and model simplicity need redesign.

## 6.2 Active Browser Product

The active user-facing product is under `web/`.

The browser currently provides:

- Pack loading;
- multi-Pack chapter selection;
- full-pool question aggregation for supported types;
- one-time shuffle;
- block sessions;
- Multiple Choice and Multiple Response grading;
- first-pass tracking;
- review-until-mastered behavior;
- final first-pass score;
- local save/resume;
- hosted/PWA experience;
- layered arcade/open-book visual system;
- medication reference features.

Confirmed current browser gaps:

- Completion excluded from quiz selection;
- Ordered Response excluded from quiz selection;
- shuffle cannot be disabled;
- quiz rules and GUI/DOM control are mixed together;
- no strong browser-level automated test suite;
- offline precache does not clearly cover the complete product.

## 6.3 Pack Library

The permanent tracked library contains three official Packs:

- Fundamentals;
- Pharm;
- Medical-Surgical.

Exact current counts must be read from the Packs rather than copied from stale documentation.

## 6.4 Medication Reference

The medication reference currently uses a Pharm-derived registry as the gatekeeper for loaded cards.

This works for the existing feature but is not the ideal long-term master-library architecture.

Future direction:

- independent stable medication records;
- source mappings to Pharm, Med-Surg, Fundamentals, and future Packs;
- no requirement that a valid medication exist in the Pharm Pack before it can exist in the reference library.

This is deferred until after the architectural cleanup unless a current defect requires earlier work.

## 6.5 Visual System

The current visual identity is intentional and should be preserved:

- dark navy background/panels;
- bright blue, green, purple, pink, and gold accents;
- 16-bit/pixel visual language;
- layered book presentation;
- scan lines and stepped animations;
- category-specific accents;
- reusable committed artwork.

The goal is not to freeze creativity. The goal is to prevent future controls from looking unrelated to PrepFlow and to reuse approved assets rather than redrawing them unnecessarily.

The visual system is currently spread across layered CSS files with overrides and duplication. Consolidation must be staged and visually conservative.

---

# 7. Verified Legacy and Ghost Pathways

Git history and the frozen tag preserve all removed work. The following code has no compatibility authority merely because it once supported a desktop or terminal client.

## 7.1 Old DOCX Prototype Route

Verified removal candidates:

- `compiler/docx_reader.py`
- `compiler/tokenizer.py`
- `compiler/parser.py`
- DOCX-specific route inside `compiler/cli.py`
- empty `tests/test_parser.py`
- empty `tests/test_ids.py`

Reason:

- rigid Markdown-like source expectations;
- no shared cleaner/detector;
- only MC/SATA inference;
- no robust varied-source handling;
- trivial useful capability to recreate;
- proper future DOCX support should be a source adapter feeding the main pipeline.

Preserved future requirement:

> Add DOCX as a first-class extraction adapter through the authoritative pipeline when effort and use justify it.

## 7.2 Old Python Study/Desktop Stack

Verified removal candidates after browser behavior protections are in place:

- `study/cli.py`
- `study/gui.py`
- `study/loader.py`
- `study/question.py`
- `study/review.py`
- `study/save_state.py`
- `study/scoring.py`
- `study/selection.py`
- `study/session.py`
- `study/update_checker.py`
- `study/version.py`
- `PrepFlow.spec`
- `.github/workflows/build-windows.yml`
- desktop-only tests after equivalent active-product coverage exists.

Reason:

- browser does not import these modules;
- browser independently performs the meaningful quiz work;
- old implementations are small and reproducible;
- unreleased desktop compatibility has no value in current decisions;
- future downloads can be built from the cleaned browser-centered application.

The old Python tests may still be useful as temporary behavioral references. Passing fewer tests after deleting test files is not proof that behavior remained correct. Equivalent browser-centered protection should exist before the bulk removal commit.

## 7.3 Old Visual Branch

`origin/feat/home-quiz-panel-clean` is the only unmerged remote branch.

Classification:

- preserve as historical visual reference;
- do not merge wholesale;
- selectively reuse an asset only if later visual review proves it valuable.

No hidden unfinished compiler or quiz-engine work exists on other remote branches.

---

# 8. Repository and Artifact Boundaries

Tracked permanent areas are currently clean:

- compiler code;
- Packs;
- browser application;
- tests;
- documentation;
- build configuration still retained from the legacy desktop route.

Ignored temporary areas:

- `.venv/`
- caches;
- `build/`
- `dist/`
- `output/`
- `scratch/`

Approved boundary:

```text
Private chosen sources      → outside repository
Temporary import artifacts  → output/
Experiments                  → scratch/
Finished authoritative data → packs/
Product code and assets      → tracked
```

---

# 9. Testing and Verification Strategy

## 9.1 Existing Tests

The repository contains over one hundred Python tests, with strongest coverage around:

- cleaner;
- source parser;
- importer;
- compiler pipeline;
- validator;
- desktop selection/custom builder.

Weak or missing coverage includes:

- complete browser quiz flow;
- browser save/resume behavior;
- browser question-type parity;
- medication reference behavior;
- service-worker/offline behavior;
- visual regressions.

## 9.2 Automated Execution

The existing GitHub workflow runs Python tests only as part of a manually triggered Windows desktop build.

Approved replacement requirement:

> Add automatic verification on pushes and pull requests, independent of desktop packaging.

The future workflow should eventually:

- install declared compiler/test dependencies;
- run Python compiler tests;
- validate Pack structure;
- run browser behavior tests;
- report failures from a clean environment.

Local tests remain part of the workflow before commit and push.

## 9.3 Migration Gates

Every structural cleanup step must define:

- behavior being protected;
- targeted tests;
- full test-suite result;
- browser smoke checks;
- Pack validation checks;
- rollback commit/tag;
- remote synchronization status.

A smaller test count after deletion is not success unless deleted coverage has been intentionally replaced or declared obsolete.

---

# 10. Approved First User-Facing Tweak After Stabilization

Add a quiz setup choice:

- **Shuffle Questions**
- **Keep Source Order**

Responsibility split:

- GUI presents the setting;
- quiz behavior layer applies it;
- save state preserves it;
- tests prove source order remains unchanged when shuffle is off;
- default behavior should be explicitly chosen during implementation.

This is the first intended user-facing tweak after the architecture and continuity foundation is stable.

---

# 11. Proposed Migration Sequence

The exact implementation commits may be adjusted as evidence appears, but the sequence should preserve a working browser product throughout.

## Stage 0 — Documentation Baseline

- create this decision map;
- rewrite Architecture Bible;
- replace Restart Packet;
- correct README to describe only active browser behavior;
- identify redundant documentation;
- commit and push the documentation baseline before code cleanup.

## Stage 1 — Protect Active Browser Behavior

- define a testable browser quiz/session contract;
- add focused tests for existing MC/MR behavior;
- add tests for full-pool selection;
- add tests for block boundaries;
- add tests for first-pass counting;
- add tests for review requeue-until-mastered;
- add tests for save/resume state;
- add automatic push/PR test workflow.

## Stage 2 — Permanent Question Identity Design

- choose ID preservation/matching strategy;
- add tests proving reorder/delete/insert does not renumber unchanged questions;
- migrate Packs safely;
- verify browser saves and references use stable IDs rather than fragile indexes where practical.

## Stage 3 — Separate Browser Quiz Rules From GUI

- extract session/order/scoring/review behavior from direct DOM operations;
- keep user-visible behavior unchanged;
- verify existing PWA manually and automatically;
- avoid framework migration unless a concrete need proves it worthwhile.

## Stage 4 — Shuffle Toggle

- add Shuffle/Source Order setting;
- preserve setting in saves;
- test both modes;
- verify full selected pool remains included.

## Stage 5 — Browser Question-Type Completion

- add Completion;
- add Ordered Response;
- verify exact grading rules;
- confirm Pack types display and save correctly.

## Stage 6 — Remove Verified Legacy Study/Desktop Code

- delete old Python study stack;
- delete PyInstaller spec;
- delete desktop update/version logic;
- delete old Windows-build workflow;
- remove obsolete desktop-only tests only after active coverage exists;
- clean imports and dependencies;
- run all gates.

## Stage 7 — Remove Old DOCX Prototype

- delete tokenizer/parser/docx prototype route;
- simplify compiler entry point around the authoritative pipeline;
- remove unused dependencies;
- retain DOCX adapter as a documented future feature, not ghost code.

## Stage 8 — Compiler Reliability Improvements

- implement permanent identity;
- use internal candidate identity instead of human-readable labels for skip decisions;
- implement conservative exact-duplicate handling;
- improve quarantine reporting;
- keep near-duplicates.

## Stage 9 — Offline Contract

- define what must work on first offline launch;
- explicitly cache required CSS, JS, data, medication assets, images, and Packs;
- add service-worker tests or deterministic verification.

## Stage 10 — Visual-System Consolidation

- inventory approved assets;
- document core palette and reusable patterns;
- centralize low-risk variables/components;
- preserve current appearance;
- do not perform a broad aesthetic redesign during structural cleanup.

## Stage 11 — Source Adapter Expansion

- add DOCX through shared pipeline when needed;
- add TXT if useful;
- add other formats only from real use cases;
- treat OCR as a separate high-risk feature.

## Stage 12 — Medication and Analytics Enrichment

- decouple medication master records from the Pharm-derived registry;
- add source mappings;
- preserve optional concepts/tags for coaching;
- avoid forcing deep classification on every imported question.

## Stage 13 — Optional Downloadable Distribution

- evaluate a desktop wrapper around the browser-centered application;
- build separately for Windows/macOS as required;
- preserve one product behavior contract;
- do not restore old Tkinter merely because it is available in history.

---

# 12. File Classification Summary

## Keep and evolve

- active compiler pipeline files;
- official Packs;
- browser application;
- medication data/cards/assets;
- core compiler tests;
- approved visual assets;
- README and docs after replacement.

## Keep temporarily as behavioral reference, then remove

- old Python study modules;
- desktop-related tests that describe still-approved behavior;
- old desktop packaging configuration;
- old Windows workflow.

## Verified removal candidates

- empty tests;
- old DOCX tokenizer/parser route;
- abandoned terminal/Tkinter client after browser protections exist;
- desktop updater/version code;
- PyInstaller build spec;
- Windows build workflow.

## Historical reference only

- `origin/feat/home-quiz-panel-clean`;
- frozen tag `before-continuity-rebuild-2026-07-20`;
- prior Architecture Bible and Restart Packet versions in Git history.

---

# 13. Deferred Feature Backlog

These are not current implementation commitments:

- DOCX/TXT source adapters;
- richer topic and medication tags;
- character-led result coaching;
- animated home characters;
- cut scenes or clipboard result screens;
- multi-frame book-opening animation;
- independent medication master library;
- complete first-install offline support;
- downloadable Windows/macOS wrappers;
- OCR ingestion;
- broader analytics and adaptive study recommendations.

Deferred does not mean rejected. It means not allowed to interrupt the current stabilization sequence.

---

# 14. Rejected or Superseded Directions

## Preserve old desktop compatibility

Rejected. There are no meaningful installed legacy users whose compatibility should shape the architecture.

## Maintain separate desktop and browser quiz engines indefinitely

Rejected as the preferred direction. The browser is active; future downloads should reuse browser-centered behavior.

## Keep old code because it might be useful someday

Rejected. Git history preserves it. Active code must justify its current role.

## Preserve publisher, edition, page, and detailed source provenance in final Packs

Rejected as a general requirement. The Pack is the authority boundary. Temporary import diagnostics may retain source context while needed.

## Remove near-duplicate questions automatically

Rejected. Only genuine exact duplicates are candidates for automatic removal.

## Build a new parser for every book

Rejected. Real source-specific evidence may justify narrowly scoped cleaning/recovery rules, but all sources feed the same architecture.

## Start with a broad rewrite

Rejected. Migration proceeds through protected, testable stages.

---

# 15. Current Priority Order

1. Complete documentation and continuity baseline.
2. Protect active browser behavior with automated tests.
3. Design and implement permanent question identity.
4. Separate browser quiz behavior from GUI enough to test and evolve safely.
5. Add Shuffle/Keep Source Order.
6. Add browser Completion and Ordered Response support.
7. Remove verified legacy desktop/study and old DOCX pathways.
8. Implement conservative exact deduplication and stronger quarantine identity.
9. Define reliable offline behavior.
10. Consolidate visual system without changing its identity.
11. Revisit medication architecture and optional enrichment.
12. Add source formats and downloadable wrappers only when justified.

---

# 16. Documentation Outputs From This Plan

## Architecture Bible

Should contain durable technical truth:

- product definition;
- authority model;
- approved responsibility map;
- Pack and identity model;
- browser-centered architecture;
- repository boundaries;
- permanent architectural principles.

It should not contain temporary branch state, exact next commands, or dated session history.

## Restart Packet

Should contain current operational truth:

- continuity note and frozen baseline;
- current branch and remotes;
- current documentation milestone;
- approved migration sequence;
- completed/active/deferred status;
- exact next safe step;
- verification, commit, push, and stopping procedures;
- permanent user workflow preferences relevant to development.

It must replace stale state rather than append dated addenda.

## README

Should be concise and user-facing:

- what PrepFlow does;
- how to open the active browser version;
- how study sessions work today;
- current subjects;
- current limitations accurately stated.

It should not advertise abandoned desktop downloads or unsupported question types.

## Question Lifecycle Document

Its useful content is redundant with the Architecture Bible. Absorb the permanent question-lifecycle material into the Architecture Bible, then delete `docs/QUESTION_LIFECYCLE.md` in a later documentation cleanup commit.

---

# 17. Safe Stop Rule

Do not begin invasive code cleanup in the same session unless:

- this decision map is committed;
- the new Architecture Bible is committed;
- the new Restart Packet is committed;
- the README no longer misstates current behavior;
- the exact next implementation stage is recorded;
- the working tree and remote state are known.

The project may safely stop after any committed documentation stage. It should not stop halfway through a bulk deletion or identity migration without a recorded rollback point and next action.

---

# 18. Change Control

This document records the July 2026 continuity-rebuild decisions.

Update it only when:

- Charlie changes an approved product decision;
- implementation evidence disproves a finding;
- the migration sequence materially changes;
- a deferred item becomes active;
- a stage is completed and its outcome affects later stages.

Do not append a dated diary. Replace stale status in the relevant section.
