# PREPFLOW RESTART PACKET

> **Continuity note:** This Restart Packet was rebuilt after the July 2026 forensic architecture review. Earlier versions are preserved in Git history and in the frozen tag `before-continuity-rebuild-2026-07-20`. If a decision or omitted pathway seems unclear, inspect that preserved baseline before assuming information was accidentally lost. Historical documents explain how PrepFlow arrived here; this packet records the approved operating state from this point forward.
>
> Do not restore legacy behavior merely because it appears in an older document. The current Architecture Bible and this Restart Packet are the active authorities unless Charlie deliberately changes a decision.

## Purpose

This is the operational handoff for resuming PrepFlow development.

Permanent architecture belongs in:

```text
docs/ARCHITECTURE_BIBLE.md
```

Detailed forensic findings and migration reasoning belong in:

```text
docs/CONTINUITY_REBUILD_PLAN.md
```

This packet must stay current and practical. It is not a chronological diary.

---

# 1. Source of Truth

Private development repository:

```text
bins-projects/prepflow-dev
```

Public repository:

```text
bins-projects/PrepFlow
```

Current development branch:

```text
docs/continuity-rebuild
```

Branch starting point:

```text
8987fdf
```

Frozen pre-rebuild reference:

```text
before-continuity-rebuild-2026-07-20
```

The frozen tag preserves the complete repository state before the continuity rebuild.

## Current verified branch state

Latest verified implementation cleanup commit:

```text
3839243  refactor: remove legacy desktop application
```

Immediately before the next documentation update:

- local `docs/continuity-rebuild` matched `origin/docs/continuity-rebuild`;
- working tree was clean;
- remaining Python suite passed 70 tests;
- the browser smoke test had passed;
- obsolete DOCX and desktop code had been removed as separate reversible commits.

## GitHub-first rule

Before asking Charlie to paste committed code, repository trees, documentation, branches, or file contents, inspect GitHub first.

Use local terminal output only for:

- uncommitted work;
- runtime behavior;
- local tests;
- ignored or generated artifacts;
- private source material;
- environment-specific behavior;
- exact local/remote synchronization checks.

---

# 2. Product Definition

PrepFlow takes deliberately selected educational material, cleans and structures it, turns it into an authoritative independent Pack, and provides study tools that use that Pack.

Core flow:

```text
Chosen source material
        ↓
Source adapter / extraction
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

The quiz, open-book interface, medication reference, characters, animations, and future coaching features are ways of using the library. They are not separate educational architectures.

---

# 3. Authority and Content Rules

A deliberately selected source becomes authoritative study material inside its own Pack after cleaning, structural validation, and review.

PrepFlow does not independently fact-check an entire nursing curriculum before allowing content into a Pack.

Each Pack is an independent authority boundary:

- sources are not silently blended into one universal truth database;
- one Pack can be removed or rebuilt without changing another;
- the original source is temporary import material;
- the finished Pack is the durable study product.

Required hierarchy:

```text
Pack
└── Chapter
    └── Question
```

Required question content:

- permanent PrepFlow question ID;
- chapter;
- chapter title when useful;
- question type;
- stem;
- choices when applicable;
- correct answer or ordered answers;
- rationale.

Publisher, edition, page, Bloom level, difficulty, and detailed source-provenance fields are not required merely because older models supported them.

Optional future tags may support concepts, medications, body systems, relationships, or coaching. They must not block ordinary imports.

Source fidelity rules:

- preserve admitted educational content faithfully;
- do not casually rewrite stems, choices, answers, or rationales;
- remove contamination and extraction artifacts through the cleaner;
- do not expose Pack filenames, IDs, JSON, compiler terms, or repository terminology in the user interface.

---

# 4. Responsibility Map

## Source adapters

Open supported file formats and return usable text or a neutral extraction structure.

Current authoritative adapter:

- text-based PDF.

Future adapters:

- DOCX;
- TXT;
- possible HTML;
- OCR only as a separate later project.

All adapters must feed the same shared pipeline.

## Extraction

Retrieves source content while preserving enough structure for later stages. It does not decide what is a question, answer, rationale, or contamination.

## Cleaner

Removes source noise and extraction artifacts while preserving educational meaning.

## Detector

Measures source structure and exposes uncertainty before parsing.

## Parser

Converts cleaned text into candidate question records and handles structures proven through real imports.

## Normalizer

Converts parser output into one consistent compiler input shape.

## Validator

Classifies problems as fatal, recoverable, or advisory. It checks structural safety, not medical truth.

## Deduplication

Automatically remove only genuine exact duplicates. Keep near-duplicates because they may test different judgments or provide useful context-specific repetition.

## Pack compiler

Preserves or assigns permanent question identities, builds the Pack, and exports only intentionally retained fields.

## Pack library

Stores approved study content and is the permanent output of ingestion.

## Browser quiz behavior layer

Owns:

- selected question pool;
- cross-Pack chapter selection;
- Shuffle or Keep Source Order;
- stable session order;
- block size;
- grading;
- first-pass tracking;
- missed-question review until mastered;
- block transitions;
- final first-pass result;
- save/resume state meaning.

## Browser GUI

Owns display, controls, layout, animation, responsive behavior, and accessibility presentation. It must not independently invent scoring or session rules.

## Offline layer

Defines the actual offline promise and caches the files required to satisfy it.

## Future downloadable clients

Future Windows or macOS downloads should package the browser-centered application. There is no requirement to preserve the removed Tkinter implementation.

---

# 5. Confirmed Active Implementation

## Compiler pipeline

Core files include:

```text
compiler/importer.py
compiler/pdf_reader.py
compiler/cleaner.py
compiler/detector.py
compiler/source_parser.py
compiler/normalizer.py
compiler/validator.py
compiler/builder.py
compiler/exporter.py
compiler/pipeline.py
compiler/models.py
compiler/ids.py
compiler/diagnostics.py
```

Authoritative flow:

```text
PDF
→ extraction
→ cleaner
→ detector
→ source parser
→ normalizer
→ validator
→ builder
→ exporter
→ Pack JSON
```

## Browser product

The active user-facing product is under:

```text
web/
```

Confirmed browser capabilities:

- Pack loading;
- chapter selection across Packs;
- full selected question pool;
- one-time shuffle;
- configurable blocks;
- one question at a time;
- Multiple Choice grading;
- Multiple Response exact-set grading;
- first-pass score tracking;
- missed-question review until mastered;
- final first-pass result;
- local save/resume;
- hosted/PWA use;
- layered arcade/open-book presentation;
- medication reference features.

Confirmed gaps from the audit:

- Completion and Ordered Response need active-path verification and repair where necessary;
- shuffle cannot be disabled;
- quiz rules and DOM manipulation are mixed in `web/app.js`;
- strong browser-level automated coverage is missing;
- complete first-install offline support is not clearly guaranteed.

## Official starting Packs

```text
packs/fundamentals.prepflow.json
packs/pharmacy.prepflow.json
packs/medical_surgical.prepflow.json
```

User-facing names:

```text
Fundamentals
Pharm
Medical-Surgical
```

Read exact counts directly from the Pack files. Do not rely on historical documentation.

## Medication reference

The current medication registry is derived primarily from Pharm appearances and gatekeeps which card records load.

Approved later direction:

- independent master medication records;
- source mappings to Pharm, Med-Surg, Fundamentals, and future Packs;
- a valid medication must not require presence in the Pharm Pack.

This is deferred unless a current defect makes it urgent.

## Visual identity

Preserve:

- dark navy foundation;
- bright blue, green, purple, pink, and gold accents;
- 16-bit/pixel styling;
- layered book presentation;
- category accents;
- reusable committed artwork;
- deliberate open-book quiz presentation.

Do not freeze creativity. New work should fit the established product and reuse approved assets where practical.

---

# 6. Permanent Question Identity

Current sequential IDs depend on export position and are not stable enough for the long-term library.

Approved requirement:

> A question's PrepFlow ID must not change merely because questions before it are deleted, inserted, or reordered.

The design must support:

- assigning an identity once;
- recognizing the same question during a rebuild;
- preserving identity through minor corrections;
- assigning a new identity only to genuinely new content;
- avoiding array-position dependence;
- detecting identity conflicts.

The exact algorithm remains an implementation decision.

Do not silently regenerate all IDs without a migration and verification plan.

---

# 7. Completed Legacy Removal

## Obsolete DOCX prototype

Removed at:

```text
0ed062f  refactor: remove obsolete docx prototype
```

Removed:

```text
compiler/docx_reader.py
compiler/tokenizer.py
compiler/parser.py
DOCX-specific route inside compiler/cli.py
tests/test_parser.py
tests/test_ids.py
```

Unused dependencies removed:

```text
python-docx
lxml
typing_extensions
```

The JSON compiler route remains. Future DOCX support should be rebuilt as a proper extraction adapter feeding the authoritative pipeline.

## Python desktop and terminal stack

Removed at:

```text
3839243  refactor: remove legacy desktop application
```

Removed:

```text
study/
PrepFlow.spec
.github/workflows/build-windows.yml
desktop-only tests
```

Reason:

- the browser is the active compatibility target;
- the browser did not consume the Python study stack;
- no released legacy installation requires compatibility;
- future desktop downloads can package the browser-centered application;
- useful capabilities are preserved as product requirements rather than obsolete implementations.

## Old visual experiment branch

```text
origin/feat/home-quiz-panel-clean
```

Do not merge this branch wholesale. Git history preserves its visual experiments for reference.

No other unmerged remote branch contained hidden compiler, quiz-engine, medication, or architectural work.

---

# 8. Test and Verification State

Before cleanup, the repository contained 108 Python tests, including desktop-only tests and two empty test files.

After deliberate legacy removal:

```text
70 passed
```

This reduction is expected because removed tests exercised implementations that are no longer active.

Verified after cleanup:

- remaining Python suite passed;
- `git diff --check` passed;
- no live imports or references remained outside intentional documentation history;
- working tree was clean;
- browser smoke test passed before cleanup;
- compiler and browser source were not changed by desktop removal.

## Current protection gap

The active browser still lacks a strong automated behavior suite.

Do not rebuild old Tkinter tests one-for-one. Add browser-centered tests when the browser behavior layer is separated and changed.

## Planned CI direction

Add automatic verification on pushes and pull requests.

Initial CI should:

- install the supported Python environment;
- run the remaining compiler tests;
- validate Pack files;
- fail on structural regressions.

Add browser checks as browser behavior becomes independently testable.

---

# 9. Approved Migration Sequence

## Phase A — Documentation foundation

Status: **Complete**

Completed:

- forensic audit;
- remote branch audit;
- continuity rebuild plan;
- rebuilt Architecture Bible;
- rebuilt Restart Packet;
- browser-centered README;
- redundant Question Lifecycle document removed;
- local test and browser smoke verification.

## Phase B — Initial cleanup

Status: **Complete**

Completed:

- obsolete DOCX prototype removed;
- unused DOCX dependencies removed;
- legacy Python desktop/terminal application removed;
- PyInstaller specification removed;
- old Windows build workflow removed;
- desktop-only tests retired;
- remaining suite verified at 70 passing tests;
- dangling-reference search completed;
- cleanup commits pushed to the private branch.

## Phase C — Permanent identity design

Status: **Next active phase**

1. inventory current question IDs across all official Packs;
2. inventory every code and data reference that depends on question IDs;
3. identify duplicate IDs or identity collisions;
4. choose the permanent identity strategy;
5. define rebuild matching and conflict behavior;
6. add focused identity tests;
7. migrate Packs only after the design is approved;
8. verify save/resume and medication/reference mappings affected by IDs.

Do not regenerate Pack IDs casually.

## Phase D — Browser behavior boundary

1. identify pure quiz/session rules inside `web/app.js`;
2. extract small testable behavior units without redesigning the GUI;
3. preserve the current browser flow after each change;
4. add Shuffle versus Keep Source Order;
5. preserve source order when shuffle is disabled.

## Phase E — Browser question-type verification and parity

1. verify active behavior for all Pack question types;
2. repair Completion support where needed;
3. repair Ordered Response support where needed;
4. preserve first-pass scoring, review, save/resume, and source fidelity;
5. add browser-centered tests.

## Phase F — Automatic verification

1. create a push/PR workflow for the remaining Python suite;
2. validate official Pack schemas and IDs;
3. add browser checks as the behavior boundary becomes testable.

## Phase G — Unified source adapters

1. preserve PDF as the authoritative current adapter;
2. rebuild DOCX as a proper extraction adapter;
3. add TXT through the same boundary;
4. route every format through the shared cleaner, detector, parser, normalizer, validator, and Pack compiler.

## Phase H — Offline and visual consolidation

1. define the offline promise;
2. inventory required shell, Pack, medication, visual, and data assets;
3. update service-worker coverage;
4. consolidate CSS only in visually safe increments;
5. preserve the approved identity and reusable artwork.

## Phase I — Deferred enrichment

After the foundation is stable:

- independent medication master library;
- optional topic and relationship tags;
- analytics and coaching;
- character animation and cut scenes;
- Windows/macOS browser wrappers;
- user-facing import interface.

---

# 10. Verification and Rollback Rules

Every implementation milestone must answer:

1. What exact behavior is changing?
2. What must remain unchanged?
3. Which tests protect it?
4. What manual browser check is required?
5. What commit is the rollback point?
6. Are intended remotes synchronized when the milestone is complete?

Standard loop:

```text
Observe
→ Inspect GitHub
→ Define one focused change
→ Add or update tests when appropriate
→ Implement
→ Run targeted tests
→ Run full tests
→ Run the real browser product
→ Inspect output
→ Commit
→ Push private remote
→ Push public remote when appropriate
→ Verify remote hashes
→ Repeat
```

Safe stopping point:

- coherent commit;
- applicable tests passing;
- browser status known;
- Restart Packet current focus updated when needed;
- no unexplained uncommitted files;
- exact next action recorded.

Rollback references:

```text
before-continuity-rebuild-2026-07-20
8987fdf
0ed062f
3839243
```

Prefer a normal revert or corrective commit over casual history rewriting.

---

# 11. Working Discipline

When Charlie says:

> next

provide the next executable step, not a menu.

Permanent rules:

- one focused change at a time;
- inspect committed code before speculating;
- do not ask for code already available through GitHub;
- do not manually repair generated Packs when the generic pipeline should be fixed;
- quarantine a small number of malformed questions rather than broadening the parser recklessly;
- do not preserve ghost code merely because it once worked;
- do not rebuild intentionally retired tests unless active behavior needs protection;
- use evidence from real imports and runtime behavior;
- protect privacy before public release or sharing;
- keep intended Git remotes synchronized at completed milestones;
- never claim a push, test, merge, or runtime result that was not verified.

Loop prevention:

1. stop;
2. return to the active phase;
3. identify the missing decision;
4. inspect the smallest relevant files;
5. choose one executable action;
6. test before expanding scope.

---

# 12. Deferred Ideas

Preserved but not active commitments:

- optional detailed topic tags;
- coaching based on missed concept clusters;
- independent medication master library and Pack mappings;
- animated character guidance;
- book-opening sequences and cut scenes;
- Windows and macOS packaged browser wrappers;
- user-facing PDF/DOCX/TXT import interface;
- OCR ingestion;
- additional Packs;
- deeper analytics and adaptive recommendations.

Deferred means do not interrupt the active architectural cleanup unless Charlie deliberately reprioritizes it.

---

# 13. Rejected or Superseded Directions

Not active requirements:

- preserving the Tkinter application for compatibility;
- rebuilding desktop parity before improving the browser;
- maintaining separate study engines for each platform;
- keeping the rigid old DOCX parser because it once existed;
- treating publisher/page provenance as required finished-Pack data;
- automatically deleting near-duplicate questions;
- making optional future tags mandatory for import;
- keeping stale files in active directories as historical reference;
- merging `feat/home-quiz-panel-clean` wholesale;
- using test count alone as proof of protection.

---

# 14. Current Rebuild Status

Completed on `docs/continuity-rebuild`:

- forensic architecture audit;
- remote branch audit;
- approved target architecture;
- continuity rebuild plan;
- rebuilt Architecture Bible;
- rebuilt Restart Packet;
- browser-centered README;
- redundant Question Lifecycle document removed;
- obsolete DOCX prototype removed;
- unused dependencies removed;
- legacy desktop/Tkinter/terminal stack removed;
- PyInstaller and old Windows workflow removed;
- remaining Python suite verified at 70 passing tests;
- browser smoke test passed;
- cleanup commits pushed to the private branch.

The active architectural work now moves to permanent question identity.

---

# 15. Exact Next Step

The next task is a read-only identity inventory.

Inspect:

- current ID format and generator;
- ID uniqueness across all official Packs;
- repeated IDs within and between Packs;
- code and data files that refer to question IDs;
- whether medication/reference mappings depend on those IDs;
- how a Pack rebuild currently changes IDs.

Do not change or regenerate IDs during the inventory.

The inventory must produce enough evidence to choose a permanent identity strategy before migration begins.

---

# 16. Startup Procedure for a New Session

1. inspect `docs/RESTART_PACKET.md` in the private GitHub repository;
2. inspect the current branch and latest commit;
3. inspect `docs/ARCHITECTURE_BIBLE.md` and `docs/CONTINUITY_REBUILD_PLAN.md` only as needed;
4. verify whether work remains on `docs/continuity-rebuild`;
5. inspect `git status` before giving modifying commands;
6. compare local, origin, and public hashes when relevant;
7. run the current test suite before destructive changes;
8. resume from the Exact Next Step;
9. make one focused change;
10. test and commit before expanding scope.

For historical reasoning, consult:

```text
before-continuity-rebuild-2026-07-20
```

Use that baseline for context, not as permission to restore superseded behavior.

---

# 17. Current Resume Statement

> PrepFlow's July 2026 forensic audit and documentation rebuild are complete. The browser is the only active compatibility target. The authoritative core is the shared ingestion/compiler pipeline, independent Pack library, and browser study application. The obsolete DOCX prototype was removed at `0ed062f`. The legacy Python desktop, terminal, PyInstaller, and Windows-build stack was removed at `3839243`. The remaining Python suite passes 70 tests, the browser smoke test passed, and the cleanup branch was synchronized with the private origin. The complete pre-rebuild state remains preserved by tag `before-continuity-rebuild-2026-07-20`. The next active phase is permanent question identity. Begin with a read-only inventory of existing IDs, collisions, references, and rebuild behavior. Do not regenerate IDs until the identity design and migration plan are approved.
