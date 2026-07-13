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
https://github.com/bins-projects/prepflow

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

Latest confirmed committed milestone:

```text
676f2b6 docs: update README for desktop Version 1
```

Official release tag:

```text
v1.0.0
```

Important preceding milestones:

```text
7b3ee0a docs: record desktop Version 1 milestone
81160bd build: package PrepFlow desktop application
9fc8fdb feat: add desktop study flow and session resume
30c41e8 Promote validated Medical-Surgical pack
87a0e81 Harden Med-Surg source cleanup and chapter boundaries
```

At the stopping point:

* local `master` was clean;
* private `origin/master` was pushed;
* public `public/master` was pushed;
* both remotes pointed to `676f2b6`;
* tag `v1.0.0` was pushed to both remotes;
* all 53 automated tests passed;
* there were no untracked release files left in the repository root;
* the Linux release archive had been built and smoke-tested from a fresh extraction;
* the packaged app had been launched successfully;
* a ChromeOS Linux Apps launcher had been created and tested;
* the working tree reported:

```text
nothing to commit, working tree clean
```

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
* ask Charlie to paste code already available in GitHub;
* manually edit generated Packs instead of fixing the generic pipeline;
* rewrite the working desktop app while beginning the PWA;
* expose Pack filenames, Pack IDs, JSON, compiler, or repository terminology to users;
* begin hosting, service-worker work, or deployment before the local PWA shell exists;
* allow the future PDF-import milestone to interrupt the current PWA milestone.

When Charlie says:

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

Repository history was previously rewritten to remove Charlie’s personal author and email information.

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

The local terminal prompt:

```text
charliekeila@penguin
```

is only the Linux username and host name.

It is not the Git identity.

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
53 passed
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
* passed a privacy scan for Charlie’s identifying information.

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

Unfinished Version 1 work belongs in:

```text
docs/V1_RELEASE_CHECKLIST.md
```

Future ideas belong in:

```text
docs/IDEAS.md
```

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

When Charlie says:

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

The desktop application still supports Multiple Choice, Multiple Response,
Completion, and Ordered Response questions.

The next focused PWA milestone is adding Multiple Response questions while
preserving the existing block, mastery-review, and autosave behavior.

For routine command sequences, obvious transitions such as stopping a local
server may be bundled with the following substantive command rather than
requiring a separate `next` response.
<!-- HOSTED_PWA_STATE_END -->
