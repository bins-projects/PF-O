# PREPFLOW RESTART PACKET

## Purpose

This document is ChatGPT’s operational bootloader for resuming PrepFlow development.

It restores:

* the current verified repository state;
* permanent architectural and privacy rules;
* completed compiler and Pack milestones;
* the three locked starting study categories;
* established quiz behavior;
* the next desktop-application milestone;
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

Before requesting terminal output, pasted code, local files, or helper scripts, first ask:

> Can the committed GitHub repository answer this?

Use GitHub first whenever the required information is committed.

Request local inspection only when:

* work is uncommitted;
* runtime behavior must be observed;
* tests must run;
* dependencies must be inspected;
* private source material must be examined;
* generated import artifacts are intentionally untracked;
* GitHub genuinely cannot answer.

---

# Latest Verified Repository State

Latest confirmed committed milestone:

```text
30c41e8 Promote validated Medical-Surgical pack
```

Immediately preceding compiler milestone:

```text
87a0e81 Harden Med-Surg source cleanup and chapter boundaries
```

At the stopping point:

* local `master` was clean;
* private `origin/master` was pushed;
* public `public/master` was pushed;
* both remotes were synchronized;
* there were no remaining untracked test Packs;
* the working tree reported:

```text
nothing to commit, working tree clean
```

Before resuming, verify GitHub rather than assuming these commits are still current.

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
Add or update a regression test
   ↓
Make one focused generic change
   ↓
Run targeted tests
   ↓
Run the full test suite
   ↓
Rebuild the real source
   ↓
Validate output
   ↓
Commit
   ↓
Push private remote
   ↓
Push public mirror
   ↓
Repeat
```

Do not:

* make several speculative changes at once;
* redesign working architecture during debugging;
* create a separate importer for every book;
* reopen settled architecture without implementation evidence;
* collect endless diagnostics without making a decision;
* rewrite the Study Engine while building the interface;
* expose Pack filenames, Pack IDs, JSON, or compiler terminology to users;
* allow later PDF-import ideas to interrupt the desktop-shell milestone.

When Charlie says:

> next

provide exactly the next executable step.

---

# Focus and Loop Prevention

Warning signs of a logic loop include:

* repeatedly inspecting the same files without a new decision;
* asking Charlie to paste code already available in GitHub;
* proposing multiple competing interface frameworks before inspecting the existing Study Engine;
* trying to make the compiler theoretically perfect instead of responding to real source evidence;
* manually editing generated Packs instead of fixing the generic pipeline;
* treating an older Pack as automatically correct when the new source-derived Pack differs;
* expanding into PDF import before the desktop study interface works.

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

The import workflow is a core product requirement, but it is not the immediate next milestone.

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
```

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
* PyInstaller build output;
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

---

# Three Locked Starting Packs

PrepFlow now has exactly three official starting study Packs:

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

The three advisory duplicates were:

1. Chapter 3, Question 23 duplicated the text of Chapter 3, Question 2.
2. Chapter 25, Question 31 duplicated the text of Chapter 25, Question 12.
3. Chapter 42, Question 12 duplicated the text of Chapter 41, Question 9.

These diagnostics are advisory and did not block the Pack.

The new official Medical-Surgical Pack replaced the historical Pack and was committed in:

```text
30c41e8 Promote validated Medical-Surgical pack
```

---

# Important Compiler Improvements Proven by Medical-Surgical

Medical-Surgical exposed several generic source patterns that were fixed in the universal pipeline.

## Wrapped Stem Beginning With a Time

A stem continuation such as:

```text
0700. The patient...
```

must not be mistaken for a new numbered question.

The parser now preserves it as part of the current stem.

## Rationale Beginning With a Choice-Like Prefix

A rationale such as:

```text
C. albicans infection appears most often in skinfolds.
```

must not be mistaken for answer choice C.

Once the parser is reading rationale text, choice-like prefixes remain rationale.

## Inline Stuvia Branding

Branding appended to legitimate text is removed while preserving the educational content.

Example:

```text
Where should the nurse assess...? Stuvia.com - The Marketplace...
```

becomes:

```text
Where should the nurse assess...?
```

## Ordered-Response Recognition

Some sequencing questions are stored by the source under:

```text
COMPLETION
```

rather than an explicit `ORDERING` section.

The parser now recognizes ordered-response items through generic structural evidence such as:

* existing choices;
* instructions containing `appropriate sequence`;
* instructions containing `correct order`;
* `prioritize the steps`;
* `prioritize these`;
* `place the events`;
* `place the options`.

Ordered answers may appear:

```text
ANS: CBDA
```

or:

```text
ANS:
CBDA
```

The parser converts the answer to an ordered list:

```text
C, B, D, A
```

## Choice G Support

The parser and split-choice recovery now accept choices through:

```text
G
```

This fixed cases where:

```text
g. Evaluate the plan over time.
```

had previously merged into choice F.

## Wrapped Chapter Headings

Chapter headings split across PDF lines are joined when the first line clearly ends mid-title.

Example:

```text
Chapter 03: Medical-Surgical Patients: Individuals, Families, and
Communities Linton: Medical-Surgical Nursing, 8th Edition
```

becomes the clean chapter title:

```text
Medical-Surgical Patients: Individuals, Families, and Communities
```

## Hard Chapter Boundaries

A new `Chapter...` line now finalizes the previous question immediately.

This prevents publisher/source header lines from being appended to the prior question’s stem or rationale.

## Wrapped Chapter Subtitle Preservation

When a real chapter subtitle appears before publisher metadata, the legitimate prefix is preserved.

Example:

```text
Chapter 33: Cardiovascular System
Introduction Linton: Medical-Surgical Nursing,
8th Edition
```

becomes:

```text
Cardiovascular System Introduction
```

Publisher text is discarded.

## Source-Title Cleanup

Trailing source-title fragments are removed from chapter titles and educational fields, including:

```text
Linton:
Linton: Medical-
Linton: Medical-Surgical
Linton: Medical-Surgical Nursing, 8th Edition
Medical-Surgical Nursing, 8th Edition
Surgical Nursing, 8th Edition
```

## Standalone N/A Cleanup

A line containing only:

```text
N/A
```

inside a metadata boundary is treated as an extraction artifact and removed.

Legitimate educational uses of `N/A` inside normal text should not be removed casually.

---

# Automated Test State

Latest verified full test run:

```text
49 passed
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
* validation behavior.

At startup, trust the current test output over the historical number recorded here.

---

# Study Engine Rules

The desktop interface must preserve the established Study Engine behavior.

## Source Fidelity

* Preserve questions word-for-word from the canonical Pack.
* Do not rewrite stems or choices.
* Do not introduce “hard mode” wording unless explicitly requested.
* Do not use publisher/source branding in user-facing content.

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
* Shuffle once per session.
* Keep the shuffled set stable during the session.
* Avoid repeating questions across initial blocks.
* After each block, review missed questions.
* Continue missed-question review until mastered.
* Preserve first-pass performance separately from eventual mastery.
* Allow the established full-block redo option where already implemented.
* End with final mastery status.

## Supported Question Types

* Multiple Choice;
* Multiple Response;
* Completion;
* Ordered Response.

The desktop shell should reuse this behavior rather than creating a separate quiz system.

---

# Next Major Milestone

The next milestone is:

> Build a user-friendly standalone desktop application shell around the existing Study Engine.

The interface should launch like a normal application on Windows or macOS.

The initial user experience should be:

```text
Launch PrepFlow
   ↓
PrepFlow banner/home screen
   ↓
Choose Fundamentals, Pharmacy, or Medical-Surgical
   ↓
Choose one or more chapters
   ↓
Start quiz
   ↓
Use the established quiz and mastery flow
```

The user should not need:

* a terminal;
* Python;
* command-line arguments;
* knowledge of Pack files;
* knowledge of JSON;
* knowledge of compiler stages;
* knowledge of repository folders.

---

# Desktop Interface Requirements

## Home Screen

Show:

```text
PrepFlow
```

with a polished banner or branding element.

Then display three clear subject choices:

```text
Fundamentals
Pharmacy
Medical-Surgical
```

The interface should feel like a real study application, not a developer utility.

## Chapter Selection

After choosing a subject:

* display clean chapter titles;
* allow selecting one chapter;
* allow selecting multiple chapters;
* provide Select All and Clear All;
* show the number of available questions when useful;
* provide a clear Start Studying button.

## Quiz Screen

The quiz screen should provide:

* one question at a time;
* readable choices;
* support for Multiple Choice;
* support for Multiple Response;
* a text field for Completion;
* ordering controls for Ordered Response;
* Submit Answer;
* feedback;
* rationale;
* question position;
* block progress;
* first-pass score;
* mastery-review status.

## Navigation

Provide clear controls for:

* Home;
* Back to subjects;
* Back to chapters;
* Exit session;
* Continue;
* Review missed questions.

Avoid overwhelming the learner with settings during the first desktop milestone.

## Visual Direction

The first version should prioritize:

* clear typography;
* large readable controls;
* straightforward navigation;
* accessibility;
* clean spacing;
* minimal clutter;
* consistent PrepFlow branding.

Do not spend the first milestone on elaborate animation or cosmetic overengineering.

---

# Packaging Goal

PrepFlow should ultimately be distributed as a standalone desktop application.

Desired experience:

```text
Double-click PrepFlow
→ application opens
→ choose subject
→ choose chapters
→ study
```

The user should not install Python or open a terminal.

Linux standalone packaging was previously proven with PyInstaller.

Important:

* PyInstaller is not a cross-compiler.
* Windows builds should be produced and tested in a Windows environment.
* macOS builds should be produced and tested in a macOS environment.
* A Linux machine should not be expected to create fully trustworthy Windows and macOS release binaries directly.

The desktop interface can be developed first in the current Linux environment, then packaged and tested separately on the target operating systems.

---

# Desktop Implementation Strategy

Do not attempt the entire interface in one speculative rewrite.

Recommended sequence:

1. inspect the committed Study Engine;
2. identify reusable session and answer-checking functions;
3. separate any remaining terminal-only input/output from study logic;
4. create the smallest window that launches;
5. add the PrepFlow banner;
6. add the three subject cards;
7. load the three official Packs dynamically;
8. add chapter multi-selection;
9. connect Start Studying to the existing session logic;
10. add one working Multiple Choice screen;
11. add feedback and rationale;
12. preserve block and mastery behavior;
13. add Multiple Response;
14. add Completion;
15. add Ordered Response;
16. test a complete session;
17. package a Linux proof build;
18. prepare Windows packaging;
19. prepare macOS packaging.

The interface is a thin layer around the proven Study Engine.

Do not rewrite the engine merely because the terminal display must be replaced.

---

# Exact Next Top-Down Assessment

At the beginning of the next session, perform a focused top-down inspection of the committed repository.

The assessment should answer:

1. What files currently implement Pack discovery?
2. What files implement subject selection?
3. What files implement chapter selection?
4. What functions implement question presentation?
5. What functions check each answer type?
6. What functions implement blocks, missed-question review, and mastery?
7. Which parts are tightly coupled to terminal `input()` and `print()`?
8. What is the smallest desktop UI layer that can reuse the current logic?
9. What existing packaging configuration can be reused?
10. What is the single best first desktop milestone?

Do not perform another broad architecture debate.

The intended first executable milestone is likely:

> Open a PrepFlow desktop window that displays the PrepFlow banner and the three official subject categories loaded from the committed Packs.

The top-down assessment must inspect the committed GitHub mirror before requesting local files or terminal output.

---

# Later PDF Import Interface

The PDF import interface is a major future milestone, but it comes after the study desktop shell works.

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

The interface should show friendly progress wording such as:

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

Do not build this workflow until the desktop study experience is stable.

---

# Documentation Rules

Permanent architecture belongs in:

```text
docs/ARCHITECTURE_BIBLE.md
```

Operational handoff belongs in:

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

Avoid duplicating the same information across all documents.

The README should describe only workflows users can actually perform.

Do not advertise the future PDF import button until it works.

---

# Startup Procedure for the Next Session

At the beginning of the next PrepFlow session:

1. paste this Restart Packet into the fresh chat;
2. inspect the public GitHub mirror;
3. verify branch `master`;
4. verify the latest commit;
5. confirm the three official Packs exist;
6. confirm there are no test Packs;
7. confirm the working tree is expected to be clean;
8. run the full test suite;
9. perform the focused Study Engine top-down assessment;
10. recommend exactly one first desktop-shell milestone;
11. implement one focused change;
12. test;
13. commit;
14. push both remotes.

Do not begin with PDF import.

Do not begin by rewriting quiz logic.

Do not begin by choosing several UI frameworks without inspecting the existing code.

---

# Current Exact Resume Statement

Resume PrepFlow from this statement:

> PrepFlow’s generic compiler has now been proven across three starting sources. The official library contains Fundamentals with 1,040 questions, Pharmacy with 1,084 questions, and Medical-Surgical with 1,443 questions. Medical-Surgical was rebuilt from the original private PDF through the improved universal pipeline with 63 chapters, 1,187 Multiple Choice questions, 133 Multiple Response questions, 108 Completion questions, 15 Ordered Response questions, zero skipped questions, zero source-branding remnants, and only three advisory duplicate-text diagnostics. The full automated suite passed 49 tests. The latest verified commit is `30c41e8`, both remotes were synchronized, and the working tree was clean. The next major milestone is a user-friendly standalone desktop PrepFlow application for Windows and macOS that launches with PrepFlow branding, displays Fundamentals, Pharmacy, and Medical-Surgical as normal study categories, allows one or more chapters to be selected, and runs the existing quiz, block, missed-question review, and mastery rules without exposing JSON, Pack IDs, filenames, terminal commands, or compiler internals. The later in-app PDF drop/import workflow remains required but must not begin until the desktop study shell is stable.

---

# Final Operating Reminder

One focused change at a time.

Use GitHub first.

Reuse the existing Study Engine.

Let real runtime evidence drive interface changes.

Do not expose implementation details to users.

Do not build PDF import yet.

When Charlie says:

> next

provide the next executable step.
