# PREPFLOW RESTART PACKET

## Purpose

This document is ChatGPT’s operational bootloader for resuming PrepFlow development.

It is the sole operational continuity handoff for the project. Before creating, replacing, or shortening this packet, always inspect and compare the currently committed `docs/RESTART_PACKET.md`. Preserve its permanent rules, workflow, architecture, privacy boundaries, verified milestones, and startup procedure. Update stale sections in place rather than substituting a shorter summary.

This document restores:

* the current verified repository state;
* permanent architectural and privacy rules;
* the completed compiler, Pack, desktop, packaging, and release milestones;
* the three locked starting study categories;
* established quiz and mastery behavior;
* the completed Version 1.0 desktop proof;
* the new Version 1.1 Progressive Web App direction;
* the later user-friendly PDF import goal;
* the exact startup procedure for the next session.

This is not the permanent architecture document.

Permanent technical truth belongs in:

```text
docs/ARCHITECTURE_BIBLE.md
```

The committed GitHub repository is the technical source of truth.

If this packet conflicts with the committed implementation:

1. inspect the committed repository;
2. trust the committed implementation;
3. correct this packet.

---

# Source of Truth

Primary repositories:

```text
Private repository:
https://github.com/bins-projects/prepflow-dev

Public mirror:
https://github.com/bins-projects/PF-O
```

Expected branch:

```text
master
```

Official Version 1 tag:

```text
v1.0.0
```

Before requesting terminal output, pasted code, local files, directory listings, or helper scripts, first ask:

> Can the committed GitHub repository answer this?

Use GitHub first whenever the required information is committed.

Request local inspection only when:

* work is uncommitted;
* runtime behavior must be observed;
* tests must run;
* dependencies must be inspected;
* private source material must be examined;
* generated import or release artifacts are intentionally untracked;
* GitHub genuinely cannot answer.

---

# Latest Verified Repository State


Latest confirmed implementation milestone:

eb78c29 — docs: finalize PWA multi-pack milestone

Current active development branch: master

Current verified state:

* The desktop custom quiz builder supports selecting chapters from Fundamentals, Pharm, and Medical-Surgical in one quiz.
* The hosted PWA supports persistent chapter selection across multiple study categories.
* Mixed-Pack sessions preserve question order, the current question, missed questions, and review queues during save and resume.
* Select All and Clear All affect only the currently displayed category.
* Multiple Response questions use checkboxes and exact-set grading in the PWA.
* Ordinary Multiple Choice behavior remains intact.
* Block transitions and the final first-pass results screen were manually exercised without observed errors.
* Save and resume during mastery review were manually verified.
* All 108 automated tests passed on merged master.
* The cross-category quiz-builder milestone was merged into master at eb78c29.
* Private origin/master and public/master were verified identical at full commit eb78c29f842d7e9faec91e3b3ceb3adff91f856d.

Before resuming, verify GitHub rather than assuming these values are still current.

---

# Working Discipline

PrepFlow development follows:

```text
Observe
   ↓
Inspect committed code
   ↓
Identify one real failure or next milestone
   ↓
Add or update a regression test when appropriate
   ↓
Make one focused generic change
   ↓
Run targeted tests
   ↓
Run the full test suite
   ↓
Build or run the real product
   ↓
Validate output
   ↓
Commit
   ↓
Push private remote
   ↓
Push public mirror
   ↓
Verify both remote hashes
   ↓
Repeat
```

Do not:

* make several speculative changes at once;
* redesign working architecture during debugging;
* create a separate importer for every book;
* reopen settled architecture without implementation evidence;
* collect endless diagnostics without making a decision;
* ask the user to paste code already available in GitHub;
* manually edit generated Packs instead of fixing the generic pipeline;
* rewrite the working desktop app while beginning the PWA;
* expose Pack filenames, Pack IDs, JSON, compiler, or repository terminology to users;
* begin hosting, service-worker work, or deployment before the local PWA shell exists;
* allow the future PDF-import milestone to interrupt the current PWA milestone.

When the user says:

> next

provide exactly the next executable step.

---

# Focus and Loop Prevention

Warning signs of a logic loop include:

* repeatedly inspecting the same files without a new decision;
* repeatedly asking for terminal output that GitHub can answer;
* proposing multiple competing frameworks before inspecting the committed implementation;
* discussing architecture after the product decision has already been made;
* trying to make the compiler theoretically perfect instead of responding to real source evidence;
* manually editing canonical output rather than fixing the reusable pipeline;
* expanding into hosting, accounts, cloud synchronization, or PDF import before the current local PWA milestone works.

When work becomes repetitive:

1. stop;
2. return to the active milestone;
3. inspect the committed implementation;
4. identify the smallest executable action;
5. test and verify before continuing.

---

# Permanent Product Goal

PrepFlow’s core purpose is:

> Give PrepFlow educational source material and make it study-able.

The product has two major user-facing workflows.

## Study Workflow

```text
Launch PrepFlow
   ↓
See PrepFlow branding
   ↓
Choose Fundamentals, Pharmacy, or Medical-Surgical
   ↓
Choose one or more chapters
   ↓
Begin studying
   ↓
Complete blocks
   ↓
Review missed questions
   ↓
Continue until mastery
```

## Future Import Workflow

```text
Import PDF
   ↓
Choose or drop source file
   ↓
Enter or confirm subject title
   ↓
PrepFlow extracts
   ↓
PrepFlow cleans
   ↓
PrepFlow detects structure
   ↓
PrepFlow parses
   ↓
PrepFlow normalizes
   ↓
PrepFlow validates
   ↓
PrepFlow reports warnings
   ↓
PrepFlow creates a study category
```

The import workflow remains a core product requirement, but it is not the immediate next milestone.

---

# Permanent Architecture

PrepFlow’s stable compiler architecture is:

```text
Private Source Material
        ↓
Source Adapter
        ↓
Extract
        ↓
Clean
        ↓
Detect Structure
        ↓
Parse
        ↓
Normalize
        ↓
Validate
        ↓
Recover usable questions
        ↓
Assign canonical IDs
        ↓
Build canonical Pack
        ↓
Export
        ↓
PrepFlow Study Engine
```

The importer is:

* format-aware;
* subject-agnostic.

Subjects such as Fundamentals, Pharmacy, Medical-Surgical, Maternity, Pediatrics, Mental Health, and non-nursing educational material are content.

They are not separate application architectures.

Do not create permanent book-specific importers.

The desktop GUI and the PWA are interface layers over the same settled study behavior and validated content model. Do not create a second educational architecture merely because the interface technology changes.

---

# Repository Boundaries

Permanent product areas include:

```text
compiler/
study/
packs/
tests/
docs/
README.md
requirements.txt
PrepFlow.spec
```

The Version 1.1 PWA should live in one clearly named web application area chosen after inspecting the repository. Do not scatter HTML, CSS, JavaScript, manifests, or service-worker files across unrelated directories.

Private source files must remain outside the repository.

Current source-storage convention:

```text
~/projects/prepflow-sources/
```

Working import artifacts may exist under:

```text
output/imports/<pack-id>/
```

These are generated diagnostic artifacts and should not automatically be committed.

The repository must not contain:

* copyrighted private source PDFs;
* private source DOCX files;
* scratch extraction text;
* personal identifying information;
* personal email addresses;
* personal local machine paths embedded in project files;
* PyInstaller `build/` output;
* PyInstaller `dist/` output;
* release archives;
* executable artifacts;
* obsolete temporary test Packs;
* one-time subject-specific importer scripts.

After a source has been successfully imported and validated into a canonical PrepFlow Pack, the original source material should not be retained inside the application or repository.

PrepFlow should preserve only:

* cleaned educational content needed for study;
* canonical PrepFlow identifiers;
* necessary subject, chapter, question, answer, rationale, and study metadata.

Source-specific publisher metadata and temporary implementation artifacts should be discarded after validation unless temporarily required for diagnostics.

---

# Privacy State

Repository history was previously rewritten to remove personal author and email information.

Reachable Git history uses:

```text
PrepFlow <bins-projects@users.noreply.github.com>
```

The private pre-anonymization recovery bundle remains outside the repository:

```text
~/projects/prepflow-before-anonymization.bundle
```

It must never be:

* uploaded;
* shared;
* included in a release;
* placed inside the repository;
* packaged with PrepFlow.


Before any public PWA deployment, repeat a privacy scan of committed web assets and generated output. Do not expose machine paths, personal names, local usernames, private source locations, internal IDs, or implementation details.

---

# Three Locked Starting Packs

PrepFlow has exactly three official starting study Packs:

```text
packs/fundamentals.prepflow.json
packs/pharmacy.prepflow.json
packs/medical_surgical.prepflow.json
```

Verified user-facing categories and counts:

```text
Fundamentals of Nursing — 1,040 questions
Pharmacy — 1,084 questions
Medical-Surgical — 1,443 questions
```

These three categories form the starting PrepFlow library.

The user-facing interface should display:

```text
Fundamentals
Pharmacy
Medical-Surgical
```

Where space is limited, `Med-Surg` is acceptable.

Do not display:

```text
fundamentals.prepflow.json
pharmacy.prepflow.json
medical_surgical.prepflow.json
pack_id
JSON
canonical Pack
compiler pipeline
repository folder
```

Those are implementation details.

---

# Fundamentals Milestone

Fundamentals was the first unseen source used to prove the generic importer.

The cold import began with the original PDF and successfully proved:

```text
PDF
→ Extract
→ Clean
→ Detect
→ Parse
→ Normalize
→ Validate
→ Build Pack
```

The final committed starting Pack contains:

```text
1,040 questions
```

Fundamentals established the first complete generic-import proof.

---

# Pharmacy Milestone

The official Pharmacy Pack is:

```text
packs/pharmacy.prepflow.json
```

Verified count:

```text
1,084 questions
```

Verified types:

```text
Multiple Choice: 963
Multiple Response: 73
Completion: 39
Ordering: 9
```

The official Pharmacy Pack is the retained validated Pack.

A later temporary file named:

```text
packs/pharmacy-test.prepflow.json
```

was inspected and identified as a stale, dirty intermediate artifact.

It had:

* only 1,073 questions;
* 271 Stuvia remnants;
* incomplete question-type support;
* a test Pack ID and title.

It was deleted and must not be restored or promoted.

Do not assume a `-test` file is newer or better than the official Pack.

---

# Medical-Surgical Milestone

The original private source was:

```text
~/projects/prepflow-sources/medsurg.pdf
```

The source was rerun through the improved universal pipeline.

Final official Pack:

```text
packs/medical_surgical.prepflow.json
```

Final verified results:

```text
Detected chapters: 63
Parsed questions: 1,443
Canonical questions: 1,443
Skipped questions: 0
```

Final question types:

```text
Multiple Choice: 1,187
Multiple Response: 133
Completion: 108
Ordered Response: 15
```

Final contamination scan:

```text
Stuvia remaining: 0
Marketplace remaining: 0
Linton remaining: 0
Medical-Surgical Nursing source-title fragments remaining: 0
Trailing standalone N/A artifacts remaining: 0
```

Final compiler diagnostics:

```text
3 advisory duplicate-text warnings
0 fatal diagnostics
0 recoverable diagnostics
0 skipped questions
```

The advisory duplicates were:

1. Chapter 3, Question 23 duplicated the text of Chapter 3, Question 2.
2. Chapter 25, Question 31 duplicated the text of Chapter 25, Question 12.
3. Chapter 42, Question 12 duplicated the text of Chapter 41, Question 9.

These diagnostics are advisory and did not block the Pack.

The validated Medical-Surgical Pack was committed in:

```text
30c41e8 Promote validated Medical-Surgical pack
```

---

# Important Compiler Improvements Proven by Medical-Surgical

Medical-Surgical exposed generic source patterns that were fixed in the universal pipeline.

## Wrapped Stem Beginning With a Time

A stem continuation such as:

```text
0700. The patient...
```

must not be mistaken for a new numbered question.

## Rationale Beginning With a Choice-Like Prefix

A rationale such as:

```text
C. albicans infection appears most often in skinfolds.
```

must remain rationale once the parser is already reading rationale text.

## Inline Source Branding

Branding appended to legitimate educational text is removed while preserving the educational content.

## Ordered-Response Recognition

Sequencing questions may appear under a Completion section and must be recognized through structural evidence such as:

* existing choices;
* `appropriate sequence`;
* `correct order`;
* `prioritize the steps`;
* `prioritize these`;
* `place the events`;
* `place the options`.

Ordered answers may appear on the same line or following line and are converted to ordered answer lists.

## Choice G Support

The parser and split-choice recovery accept answer choices through G.

## Wrapped Chapter Headings

Split chapter headings are joined when the first line clearly ends mid-title.

## Hard Chapter Boundaries

A new chapter line finalizes the previous question immediately so source headers cannot attach to the prior question.

## Wrapped Chapter Subtitle Preservation

Legitimate chapter subtitle prefixes are preserved while publisher metadata is removed.

## Source-Title Cleanup

Trailing source-title fragments are removed from chapter titles and educational fields.

## Standalone N/A Cleanup

A standalone `N/A` inside a metadata boundary is treated as an extraction artifact. Legitimate educational use of `N/A` in normal text must not be removed casually.

---

# Automated Test State

Latest verified full test run:

```text
108 passed
```

The suite covers at least:

* Pack building;
* chapter title export;
* Docsity cleanup;
* Stuvia cleanup;
* inline branding cleanup;
* source-title cleanup;
* standalone N/A cleanup;
* chapter-index removal;
* PDF adapter validation;
* importer request validation;
* raw artifact writing;
* clean artifact writing;
* detection report writing;
* question-type behavior;
* completion behavior;
* multiple-response answer handling;
* ordered-response answer order;
* source normalization;
* wrapped stems;
* wrapped choices;
* split choices;
* missing-A-choice recovery;
* time-like numbered stem continuations;
* rationale lines beginning with choice-like prefixes;
* ordered-response recognition inside Completion sections;
* multiline ordered answers;
* choice G support;
* wrapped chapter headings;
* chapter-boundary finalization;
* wrapped chapter subtitles;
* validation behavior;
* single-slot save overwrite;
* missing-save behavior;
* save deletion;
* invalid-save handling.

At startup, trust the current test output over the historical number recorded here.

---

# Study Engine Rules

Every interface must preserve the established Study Engine behavior.

## Source Fidelity

* Preserve questions word-for-word from the canonical Pack.
* Do not rewrite stems or choices.
* Do not introduce “hard mode” wording unless explicitly requested.
* Do not use publisher or source branding in user-facing content.

## Question Display

* One question at a time.
* No bolding or highlighting inside stems or choices.
* No hints before the learner answers.
* Do not expose internal question IDs unless needed for diagnostics.

## Feedback

After each answer, show:

* Correct or Incorrect;
* the correct answer;
* a concise rationale;
* running counters.

## Session Flow

* Default study blocks contain 15 questions.
* The final block may contain fewer than 15 questions.
* Shuffle once per session.
* Keep the shuffled set stable during the session.
* Combine multiple selected chapters into one shuffled session.
* Avoid repeating questions across initial blocks.
* After each block, review missed questions.
* Continue missed-question review until mastered.
* Preserve first-pass performance separately from eventual mastery.
* End with final mastery status.

## Supported Question Types

* Multiple Choice;
* Multiple Response;
* Completion;
* Ordered Response.

## Save and Resume

* Maintain one overwriteable local save slot.
* Autosave when a new question opens.
* Preserve subject, question order, current position, block state, score, missed questions, and review queue.
* Show a brief `Progress saved` notice.
* Show `Continue Saved Quiz` when a valid save exists.
* Delete the save after the session is completed.
* Do not require a manual Save button.

The PWA should reproduce these rules rather than invent a separate quiz system.

---

# Version 1.0 Desktop Milestone — Complete

PrepFlow Version 1.0 is a working Linux desktop application proof.

Completed desktop capabilities:

* Tkinter desktop home screen;
* dynamic discovery of the three official categories;
* clean user-facing category names;
* one or more chapter selections;
* Select All and Clear All;
* combined multi-chapter sessions;
* one shuffle per session;
* 15-question blocks;
* accurately shortened final blocks;
* Multiple Choice;
* Multiple Response;
* Completion;
* Ordered Response;
* drag-and-drop ordering;
* immediate feedback;
* correct answers and rationales;
* first-pass scoring;
* missed-question review until mastery;
* scrollable long content;
* fixed Submit and Continue controls;
* automatic single-slot save;
* Continue Saved Quiz;
* temporary Progress saved notice;
* save deletion after completion.

Do not rewrite or destabilize the working desktop application while beginning Version 1.1.

---

# Version 1.0 Packaging and Release State

The PyInstaller specification is:

```text
PrepFlow.spec
```

The Linux x86-64 desktop build was successfully created and tested.

The packaged application:

* launches without Python;
* does not require terminal interaction during normal use;
* bundles the three official starting categories;
* preserves autosave and resume;
* passed a fresh extracted-archive smoke test;
* passed a privacy scan for identifying information.

Generated packaging directories remain untracked:

```text
build/
dist/
```

Generated release archives must also remain untracked.

A clickable ChromeOS launcher was created under the local Linux desktop-app configuration and tested through the ChromeOS Linux Apps menu.

PyInstaller is not a cross-compiler:

* Windows builds must be produced and tested on Windows.
* macOS builds must be produced and tested on macOS.
* A macOS desktop build will not run on iPadOS.

Official Git release marker:

```text
v1.0.0
```

Do not move or rewrite the `v1.0.0` tag.

---

# Version 1.1 Direction — Progressive Web App

The next major platform milestone is a Progressive Web App developed entirely on the Chromebook.

The purpose is to let classmates use PrepFlow on iPads without:

* Xcode;
* a Mac;
* TestFlight;
* the App Store;
* Python;
* terminal commands;
* a native iPad application.

The intended iPad experience is:

```text
Open PrepFlow in Safari
   ↓
Add to Home Screen
   ↓
Launch PrepFlow like an app
   ↓
Study offline after required files are cached
```

The likely future GitHub Pages address is:

```text
https://bins-projects.github.io/PF-O/
```

That address is not the working PrepFlow site until the PWA exists and GitHub Pages is enabled.

## PWA Technical Direction

The first PWA should be static and use:

* HTML;
* CSS;
* JavaScript;
* the existing validated study content;
* browser-local save state;
* a web app manifest later;
* a service worker later.

No backend, login, account system, cloud database, instructor dashboard, or cloud synchronization is required for the first PWA milestone.

The browser interface replaces Tkinter for iPad use. It does not replace the compiler, validated Packs, canonical IDs, or established study rules.

## Public Deployment Gate

Before enabling GitHub Pages or publishing study content publicly:

* review whether the bundled educational question content may be publicly distributed;
* repeat privacy checks;
* confirm no internal implementation details are exposed;
* confirm only intended public assets are published.

Local PWA development may proceed before public deployment is approved.

---

# Exact First PWA Milestone

At the beginning of Version 1.1:

1. inspect the committed repository;
2. compare the current Restart Packet against implementation;
3. choose the cleanest single directory for the web application;
4. implement only the smallest visible local web milestone.

The first executable milestone is:

> Open a local PrepFlow web page that displays polished PrepFlow branding and three touch-friendly cards labeled Fundamentals, Pharmacy, and Medical-Surgical.

For this first milestone:

* run locally on the Chromebook;
* do not enable GitHub Pages;
* do not add service-worker caching;
* do not add quiz logic;
* do not add a backend;
* do not add accounts;
* do not redesign the Packs;
* do not modify the desktop app;
* load names and counts from existing validated content when practical rather than duplicating educational content manually.

---

# Recommended PWA Sequence

1. Inspect the repository and choose the web-app directory.
2. Create a local static web shell.
3. Add PrepFlow branding and the three category cards.
4. Load the existing Packs in the browser.
5. Add chapter multi-selection.
6. Add Multiple Choice.
7. Port block, score, and mastery behavior.
8. Add Multiple Response.
9. Add Completion.
10. Add touch-friendly Ordered Response.
11. Add browser-local automatic save and resume.
12. Add responsive iPad styling.
13. Add the web app manifest.
14. Add offline caching with a service worker.
15. Test locally.
16. Test on an iPad.
17. Complete the public-content distribution review.
18. Enable GitHub Pages.
19. Test Add to Home Screen and offline use.

Do not attempt this entire sequence in one speculative rewrite.

---

# Later PDF Import Interface

The PDF import interface remains a major future milestone, but it comes after the PWA study experience is stable.

Future user flow:

```text
Import and Create Study Category
   ↓
Choose or drop a PDF
   ↓
Enter or confirm category title
   ↓
PrepFlow extracts text
   ↓
PrepFlow cleans source artifacts
   ↓
PrepFlow detects chapters and question structures
   ↓
PrepFlow parses questions
   ↓
PrepFlow normalizes and validates
   ↓
PrepFlow reports warnings and skipped items
   ↓
PrepFlow creates the category
   ↓
Category appears on the home screen
```

Friendly progress wording may include:

```text
Reading PDF
Cleaning source
Finding chapters
Finding questions
Checking answers and rationales
Building study category
```

Do not expose:

```text
02_clean.txt
03_detection.json
04_questions.json
pack_id
canonical JSON
compiler diagnostic enum
```

The final import report may show:

* chapters found;
* questions created;
* question types;
* warnings;
* skipped questions;
* output category name;
* option to begin studying.

Do not build this workflow until the current PWA study milestone is stable.

---

# Documentation Rules

Permanent architecture belongs in:

```text
docs/ARCHITECTURE_BIBLE.md
```

Operational handoff and sole continuity bootloader belong in:

```text
docs/RESTART_PACKET.md
```

Completed milestones belong in:

```text
docs/CHANGELOG.md
```

Current unfinished work and active priorities belong in this Restart Packet.

Deferred feature ideas that remain relevant belong in the Deferred Feature Backlog section of this Restart Packet.

The README should describe only workflows users can actually perform.

Do not advertise GitHub Pages, offline PWA installation, or PDF import as completed until those workflows actually work.

Before writing a new Restart Packet:

1. inspect the currently committed Restart Packet;
2. compare proposed changes against it;
3. preserve permanent operating rules and continuity details;
4. update stale sections in place;
5. never replace it with a short summary that drops safeguards.

---

# Startup Procedure for the Next Session

At the beginning of the next PrepFlow session:

1. paste this Restart Packet into the fresh chat;
2. inspect the public GitHub mirror;
3. verify branch `master`;
4. verify the latest commit and `v1.0.0` tag;
5. compare this packet against the committed implementation;
6. confirm the three official Packs exist;
7. confirm no test Packs or release artifacts are tracked;
8. confirm the working tree is expected to be clean;
9. run the full test suite;
10. perform a focused top-down inspection for the web-app directory;
11. recommend exactly one first local PWA milestone;
12. implement one focused change;
13. test locally;
14. commit;
15. push `origin`;
16. push `public`;
17. verify both remote hashes match.

Do not begin with GitHub Pages.

Do not begin with a service worker.

Do not begin with PDF import.

Do not begin by rewriting the desktop app.

Do not begin by choosing multiple web frameworks without inspecting the committed repository.

---

# Current Exact Resume Statement

Resume PrepFlow from this statement:

> PrepFlow Version 1.0 is complete as a working Linux desktop application proof and is permanently marked by Git tag `v1.0.0`. The latest verified commit is `676f2b6`, both `origin/master` and `public/master` are synchronized, the working tree was clean, and all 53 automated tests passed. The official library contains Fundamentals with 1,040 questions, Pharmacy with 1,084 questions, and Medical-Surgical with 1,443 questions. The desktop app supports the three official categories, multi-chapter selection, one shuffled order per session, 15-question blocks, accurately shortened final blocks, Multiple Choice, Multiple Response, Completion, Ordered Response with drag-and-drop, first-pass scoring, missed-question review until mastery, automatic single-slot saving, Continue Saved Quiz, a Progress saved notice, standalone Linux packaging, a smoke-tested release archive, privacy validation, and a clickable ChromeOS launcher. Version 1.1 should begin as a Progressive Web App developed locally on the Chromebook so iPad users can eventually open PrepFlow in Safari, add it to the Home Screen, and study offline after installation. Do not begin with hosting, GitHub Pages, a backend, accounts, native SwiftUI, service-worker complexity, or PDF import. First inspect the committed repository, compare the current Restart Packet against implementation, choose one clean web-app directory, and build a local web shell showing polished PrepFlow branding and the three official study categories. Before public deployment, complete the public-content distribution and privacy review.

---

# Final Operating Reminder

One focused change at a time.

Use GitHub first.

Treat this Restart Packet as the sole operational continuity provider.

Always compare the committed Restart Packet before creating a replacement.

Preserve the working Version 1.0 desktop release.

Reuse established study behavior.

Let real runtime evidence drive changes.

Do not expose implementation details to users.

Do not build PDF import yet.

When the user says:

> next

provide the next executable step.

<!-- HOSTED_PWA_STATE_START -->
## Hosted Chromebook PWA — Verified Milestone

PrepFlow is hosted at:

`https://bins-projects.github.io/PF-O/web/`

Verified behavior:

- installs directly through Chrome;
- launches from the Chromebook Launcher;
- does not require Linux, Python, a terminal, or `localhost`;
- loads Fundamentals, Pharmacy, and Medical-Surgical;
- supports chapter multi-selection;
- supports configurable block sizes, with 15 as the default;
- presents Multiple Choice questions with feedback and rationales;
- pauses at block boundaries;
- reviews missed questions until mastered;
- automatically saves unfinished sessions;
- restores an unfinished session through Continue Session.

The hosted PWA and desktop application support Multiple Choice and Multiple
Response questions. Multiple Response questions in the PWA use checkboxes and
require the exact correct answer set. The desktop application additionally
supports Completion and Ordered Response questions.

The next active platform work is confirming the Windows Version 1.1.0 release
state and then beginning the macOS GitHub Actions packaging milestone.

For routine command sequences, obvious transitions such as stopping a local
server may be bundled with the following substantive command rather than
requiring a separate `next` response.
<!-- HOSTED_PWA_STATE_END -->

---

## Pharmacy Third-Edition Replacement — 2026-07-13

### Completed milestone

The official Pharmacy pack was rebuilt from the complete third-edition source and replaced locally and in the private `origin` repository.

Current official pack:

- File: `packs/pharmacy.prepflow.json`
- Questions: 1,202
- Source chapter range: 1–29
- Chapters represented: 28
- Question types:
  - Multiple choice: 1,140
  - Multiple response: 16
  - Completion: 45
  - Ordered response: 1
- Known source artifacts remaining: 0

The three genuine Chapter 3 questions were excluded because the source supplied correct answers but no rationales. Chapter 29 Question 11 was also excluded because the stable parser configuration did not safely associate its rationale. These four questions may be manually restored later with reviewed rationales.

### Compiler and cleaner work completed

Committed milestones:

- `4a58c15` — compiler support for additional Pharmacy source formats
- `5a79592` — removal of standalone source artifacts
- `3914f0f` — removal of the repeated Pharmacy Chapter 2 block
- `389af06` — replacement of the official Pharmacy pack

The parser now supports the additional inline-answer, labeled-question, split-choice, ordered-answer, and unnumbered-question formats encountered in this source.

The cleaner includes narrowly scoped rules for:

- obsolete embedded Pharmacy Chapter 32 removal
- condensed Chapter 3 duplicate-summary trimming
- repeated Chapter 2 multiple-response block removal
- exact standalone `extra per year?` artifact removal

### Validation status

- Full test suite: 72 passed
- Candidate parsed: 1,206
- Candidate exported: 1,202
- Candidate skipped: 4
- Duplicate-text advisories: 1 valid Chapter 12/13 look-alike pair
- Official pack contamination checks: all zero

### Repository synchronization status

Private repository `origin/master` contains the new official Pharmacy pack at:

`389af06155596f37a2780268bbabc4fd95dfd03d`



### Immediate next steps

1. Verify the desktop or local PrepFlow application loads the new 1,202-question Pharmacy pack.


---

# CURRENT STATE ADDENDUM — 2026-07-14

This addendum preserves the permanent rules and history already recorded above. Where older question counts, milestones, or resume instructions conflict with this section, this newest dated section is the current source of truth.

## Latest Verified Repository State

Latest completed and synchronized commit:

64897f6 feat: add desktop parity and update checks

After pushing, the following all matched commit 64897f6:

- local master
- origin/master
- public/master

Latest full automated test result:

81 passed

## Current Official Study Library

Current user-facing categories and question counts:

- Fundamentals — 1,040 questions
- Pharm — 1,238 questions
- Medical-Surgical — 1,443 questions

The user-facing Pharmacy category is now named Pharm.

The internal filename remains:

packs/pharmacy.prepflow.json

Do not expose Pack filenames, JSON terminology, Pack IDs, compiler details, or internal implementation language in the user-facing application.

## Pharm Pack Repair and Validation

The Pharmacy source was replaced with the validated third-edition source and rebuilt through the generic PrepFlow compiler.

The final Pharm Pack contains 1,238 questions.

Final validation showed:

- 0 Multiple Choice or Multiple Response questions with too few choices
- 0 answers referencing missing choices
- 0 merged-choice entries

Parser and validator improvements included support for:

- split choice markers;
- choice labels without periods;
- wrapped choices followed by label-only markers;
- inline metadata boundaries that previously swallowed the next question;
- recoverable validation when an answer references a missing source choice.

One malformed source question with a missing choice was safely quarantined rather than forcing a risky parser workaround.

For future imports, prefer quarantining a small number of malformed questions over spending hours building overly broad parser behavior. Clearly recoverable questions may be restored manually later.

## Hosted PWA State

Current hosted PWA:

https://bins-projects.github.io/PF-O/web/

Current PWA behavior includes:

- Fundamentals, Pharm, and Medical-Surgical;
- chapters selected across one or more study categories;
- configurable block size;
- Block X of Y display;
- one question at a time;
- Multiple Choice;
- Multiple Response;
- Completion;
- Ordered Response;
- automatic local save and resume;
- Save & Quit;
- Resume Saved Session;
- confirmed Start Over;
- answer choices removed after submission and replaced by feedback and rationale;
- missed-question mastery review until corrected;
- final Quiz Complete screen showing the first-pass percentage;
- network-first loading with offline cache fallback;
- inactive screens remaining properly hidden during a quiz.

Recent PWA quality-of-life work completed:

- total blocks are shown;
- routine refreshes retrieve current hosted files;
- the saved-session panel no longer appears over an active quiz;
- rationale replaces the answer area, reducing unnecessary scrolling;
- Continue remains visible in normal use;
- final first-pass percentage is displayed only after the quiz is complete;
- Exit Quiz was renamed Save & Quit;
- Start Over now requires confirmation.

## Desktop Application Parity

The shared Tkinter desktop application has been brought into practical parity with the PWA.

Current desktop behavior includes:

- Fundamentals, Pharm, and Medical-Surgical;
- the same current official Pack contents;
- block sizes of 5, 10, 15, or 20;
- Block X of Y display;
- one question at a time;
- Multiple Choice;
- Multiple Response;
- Completion;
- Ordered Response;
- automatic session saving;
- Save & Quit;
- Resume Saved Session;
- confirmed Start Over;
- choices removed after answer submission;
- correct or incorrect feedback;
- correct answer display when missed;
- rationale display;
- missed-question review until mastery;
- final Quiz Complete screen with first-pass percentage.

The desktop application currently displays:

Version 1.1.0

The application-version source is:

study/version.py

## Check for Updates Feature

The desktop application now has a non-blocking Check for Updates button.

Relevant files:

- study/version.py
- study/update_checker.py
- tests/test_update_checker.py

Current behavior:

- compares the installed APP_VERSION with the latest public GitHub release;
- reports when PrepFlow is up to date;
- reports when a newer release is available;
- offers to open the public release page;
- does not automatically download or install updates;
- performs the network request outside the GUI thread;
- safely ignores the callback if the application closes while checking.

Users who still have Version 1.0.0 must manually replace that copy once because Version 1.0.0 does not contain the update-check button.

After Version 1.1.0 is installed, later public releases can be detected from within PrepFlow.

## Cross-Platform Feature-Parity Rule

All supported PrepFlow clients must remain as close to feature parity as practical.

Supported or planned clients:

- hosted PWA;
- Windows desktop;
- macOS desktop.

Whenever a user-facing feature is added or changed in one supported client, review and update the other supported clients before release.

Do not allow the clients to drift into conflicting behavior for:

- category names;
- Pack contents;
- block sizes;
- scoring;
- save and resume behavior;
- mastery review;
- feedback and rationales;
- final results;
- update behavior.

macOS should use the same shared Tkinter desktop source and study engine as Windows. Do not create a separate macOS study engine.

## Windows Packaging State

Windows packaging currently uses:

- PrepFlow.spec
- .github/workflows/build-windows.yml

The GitHub Actions Windows workflow:

1. checks out the repository;
2. starts a Windows runner;
3. installs Python 3.13 and dependencies;
4. runs the full automated test suite;
5. builds the application with PyInstaller;
6. creates PrepFlow-Windows-x86_64.zip;
7. uploads the ZIP as a workflow artifact.

The Version 1.1.0 Windows build workflow was triggered after commit 64897f6 and is expected to complete successfully.

Still requiring confirmation:

- the workflow finished successfully;
- the artifact was downloaded;
- PrepFlow.exe launched on a real Windows computer;
- the current packs and desktop parity features work in the packaged build;
- Version 1.1.0 was published as the latest public release;
- the permanent Windows download link resolves to the new ZIP.

Correct this section if the workflow or Windows smoke test fails.

## Current Windows Distribution Method

The current Windows release is a portable ZIP, not a traditional installer.

There is currently no Windows uninstaller.

To replace an older portable copy:

1. close PrepFlow;
2. delete the entire old extracted PrepFlow folder;
3. remove any desktop shortcut pointing to the old executable;
4. download the new PrepFlow-Windows-x86_64.zip;
5. choose Extract All;
6. open the newly extracted PrepFlow folder;
7. launch PrepFlow.exe;
8. create a new shortcut if desired.

Do not run PrepFlow.exe from inside the ZIP.

Do not copy new files over an old extracted folder. Use a fresh extracted folder to avoid stale bundled files.

Desktop saved-session data is stored separately from the portable application folder.

On Windows, the save location is:

%USERPROFILE%\.prepflow\session.json

Deleting the extracted PrepFlow program folder does not delete saved quiz progress.

Delete the .prepflow folder only when the user intentionally wants to remove saved progress as well.

A proper Windows installer and uninstaller remain future packaging improvements.

## macOS Next Milestone

macOS packaging is the next active platform milestone after the Windows Version 1.1.0 build and release are confirmed.

The first macOS milestone is:

Add a GitHub Actions workflow that builds the current PrepFlow desktop application on a macOS runner and uploads a testable macOS artifact.

Use the existing:

- study/gui.py;
- shared study engine;
- PrepFlow Pack library;
- established parity behavior.

Do not redesign working quiz behavior during the initial macOS packaging milestone.

PyInstaller is not a cross-compiler. A macOS build must be produced on a macOS runner and later tested on a real Mac.

Expected initial macOS workflow:

1. run on a GitHub-hosted macOS runner;
2. install the supported Python version;
3. install project dependencies, pytest, and PyInstaller;
4. run the complete automated test suite;
5. build PrepFlow from the shared desktop source;
6. package the resulting macOS application;
7. upload it as a workflow artifact;
8. test the artifact on a real Mac before public release.

Code signing, notarization, installer packaging, and Gatekeeper improvements may follow after the first successful testable build.

## Deferred Feature Backlog

### Fundamentals Garbled Questions

Known garbled Fundamentals questions involving constipation and diarrhea remain deferred for focused source-level inspection and repair.

Do not apply speculative broad parser changes merely to repair a few isolated questions.

### Motivational Results Messages

Optional final score-band messages remain deferred.

Possible future bands include:

- 70–79 percent;
- 80–89 percent;
- 90–99 percent;
- 100 percent.

For now, the final results screen should prioritize the first-pass percentage without motivational scoring messages.

### Windows Installer and Uninstaller

A proper Windows installer and uninstaller remain deferred until the portable Version 1.1.0 build is confirmed stable.

## Exact Resume Point

Resume from this statement:

PrepFlow’s existing PWA multi-category quiz behavior remains merged in master, with all 108 automated tests passing at the last verified run.

A major arcade-style PWA redesign is now safely committed and pushed only to the private feature branch:

Branch: feat/arcade-home-screen
Commit: 8c6cf40
Commit message: feat: add arcade book-based multi-pack quiz builder

This feature branch is synchronized with origin/feat/arcade-home-screen. It has not been merged into master and has not been pushed to the public mirror.

Verified feature-branch behavior:

- the home screen uses the approved 16-bit PrepFlow artwork;
- Fundamentals, Pharm, and Med-Surg appear as reusable pixel-art textbook buttons;
- all three books open into the same two-page chapter-selection overlay;
- each entire chapter row is clickable;
- chapter selections persist while switching among books;
- selections from multiple books remain combined;
- each closed book displays its own selected-chapter count;
- the home screen displays the combined selection total;
- Questions per Block is configured globally on the home screen;
- Build Quiz enables only when chapters are selected;
- saved-session Continue Session and Start Over controls remain functional;
- the side control stacks remain visible in both full-screen and split-screen browser layouts;
- all 108 automated tests passed after the redesign;
- browser testing confirmed that all three books open and preserve selections.

The feature stylesheet currently contains many layered CSS overrides accumulated during visual iteration. A cleanup branch was created for inspection, but no cleanup changes were made because removing overrides without full visual regression testing could damage the approved design. Do not begin by rewriting or consolidating the stylesheet.

The next active milestone is redesigning the PWA quiz question, answer, feedback, and rationale experience to match the new arcade visual system. Preserve all established quiz logic, scoring, block behavior, mastery review, save/resume behavior, Multiple Choice behavior, and exact-set Multiple Response grading.

Do not merge the arcade feature branch into master until the question-and-rationale redesign is complete and the complete PWA workflow has been manually tested.

Before doing any work in the next session:

1. inspect the committed private GitHub branch feat/arcade-home-screen;
2. verify that its tip is still commit 8c6cf40;
3. inspect the current quiz-screen markup, styles, and behavior;
4. propose one focused first step for the question-and-rationale redesign;
5. do not alter the approved home screen unless a verified regression is found.

---

## Temporary New-Chat Handoff

Paste this into the first message of the next chat:

Read the repository’s current docs/RESTART_PACKET.md and inspect the private GitHub branch feat/arcade-home-screen before requesting local files or terminal output. The approved arcade home screen and reusable open-book multi-pack chapter selector are safely committed at 8c6cf40, with 108 tests passing. Do not merge yet. Continue with the next milestone: redesign the PWA question, answer, feedback, and rationale experience to match the arcade visual system while preserving all existing quiz behavior. Complete only the inspection-and-plan phase first, then give me one executable next step.
