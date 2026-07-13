# PrepFlow

PrepFlow is a desktop study application built around mastery-based review.

It loads validated PrepFlow study categories, lets the learner choose one or more chapters, presents questions in shuffled study blocks, tracks first-pass performance, and repeats missed questions until they are mastered.

PrepFlow currently includes:

- Fundamentals
- Pharmacy
- Medical-Surgical

---

# Current Desktop Experience

Launch PrepFlow and:

1. Choose a study category.
2. Select one or more chapters.
3. Start studying.
4. Complete questions in blocks of 15.
5. Review missed questions until mastered.
6. Resume an unfinished quiz later through automatic session saving.

Selected chapters are combined and shuffled once at the beginning of each session.

The final block is shortened automatically when fewer than 15 questions remain.

---

# Supported Question Types

PrepFlow supports:

- Multiple Choice
- Multiple Response
- Completion
- Ordered Response

Ordered Response questions use drag-and-drop controls.

Long questions and rationales scroll while the navigation controls remain visible.

---

# Study Behavior

During a study session, PrepFlow:

- presents one question at a time;
- gives immediate Correct or Incorrect feedback;
- displays the correct answer;
- displays the rationale;
- tracks first-pass correct and missed answers;
- places missed questions into a review queue;
- repeats missed review questions until answered correctly;
- shows final first-pass and mastery results.

---

# Automatic Save and Resume

PrepFlow maintains one overwriteable local save slot.

Whenever a new question opens, the current session state is saved automatically. The saved state includes:

- subject and question set;
- shuffled question order;
- current position;
- block progress;
- first-pass score;
- missed questions;
- mastery-review queue.

When a saved session exists, the home screen displays:

```text
Continue Saved Quiz
```

The save is removed automatically after the session is completed.

---

# Standalone Application

A standalone Linux x86-64 build has been produced and tested with PyInstaller.

The packaged application:

- opens without requiring Python;
- does not require terminal interaction during normal use;
- bundles the three official starting study categories;
- supports automatic save and resume.

Separate builds must be created and tested on Windows and macOS.

A normal macOS desktop build will not run on iPadOS. An iPad-compatible PrepFlow frontend is a later platform milestone.

---

# Architecture

PrepFlow keeps source compilation separate from study delivery.

```text
Private Source Material
        ↓
Compiler
        ↓
Validated PrepFlow Packs
        ↓
Desktop Study Application
```

Private source material remains outside the repository.

---

# Repository Layout

```text
compiler/    Reusable source compilation pipeline

study/       Study logic, desktop interface, scoring, review, and save state

packs/       Validated PrepFlow study categories

tests/       Automated regression tests

docs/        Architecture, milestones, release planning, and handoff documents
```

Generated PyInstaller `build/` and `dist/` directories are not committed.

---

# Running From Source

Create and activate a Python virtual environment, install the project requirements, and launch:

```bash
python3 -m study.gui
```

Tkinter must be available in the Python environment.

On Debian-based Linux systems:

```bash
sudo apt install python3-tk
```

---

# Building the Linux Desktop Application

With PyInstaller installed, run:

```bash
python3 -m PyInstaller --clean --noconfirm PrepFlow.spec
```

The application is created under:

```text
dist/PrepFlow/
```

Launch it with:

```bash
./dist/PrepFlow/PrepFlow
```

PyInstaller is not a cross-compiler. Windows and macOS releases must be built and tested on their respective operating systems.

---

# Testing

Run the full automated test suite with:

```bash
python3 -m pytest -q
```

The latest verified suite contains 53 passing tests.

---

# Documentation

Authoritative project documents include:

- `docs/ARCHITECTURE_BIBLE.md` — permanent technical architecture
- `docs/RESTART_PACKET.md` — operational development handoff
- `docs/V1_RELEASE_CHECKLIST.md` — remaining Version 1 release work
- `docs/CHANGELOG.md` — completed milestones
- `docs/IDEAS.md` — future enhancements

---

# Current Status

PrepFlow has reached a working Version 1 desktop application proof on Linux.

Completed capabilities include:

- three validated starting study categories;
- desktop subject and chapter selection;
- all supported question types;
- block study and mastery review;
- automatic save and resume;
- standalone Linux packaging;
- repository and release privacy validation.

The remaining Version 1 work is focused on final release validation, documentation, archive testing, and tagging.

<!-- CHROMEBOOK_PWA_START -->
## Chromebook App

[Open PrepFlow for Chromebook](https://bins-projects.github.io/PF-O/web/)

PrepFlow can be installed directly from Chrome and launched from the Chromebook
Launcher. It does not require Linux, Python, a terminal, or `localhost`.

### Install

1. Open the PrepFlow link above in Chrome.
2. Click **Install PrepFlow** in the address bar.
3. Confirm the installation.
4. Open PrepFlow from the Chromebook Launcher.

### Chromebook Features

- Fundamentals, Pharmacy, and Medical-Surgical
- Multi-chapter selection
- Configurable questions per block
- Immediate feedback and rationales
- End-of-block summaries
- Review missed questions until mastered
- Automatic session saving
- Continue an unfinished session after reopening
<!-- CHROMEBOOK_PWA_END -->
