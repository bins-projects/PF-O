# PREPFLOW RESTART PACKET

## Purpose

This file is the primary handoff for every new PrepFlow development session.

> **MANDATORY FIRST ACTION:** Read this entire file before proposing a command or changing a PrepFlow file.

For the current visual milestone, also read:

```text
docs/ART_SYSTEM.md
docs/VISUAL_REDESIGN_CONTINUITY_2026-07-23.md
```

The local repository at `~/projects/prepflow` is the active working copy during development. The rendered local application is part of the source of truth for visual work.

---

# 1. Authority Order

Use this order:

1. `docs/RESTART_PACKET.md` — current branch state, exact resume point, and next step.
2. Local branch, working-tree state, local-only files, and rendered application.
3. Current private development branch — last committed development state.
4. `docs/ART_SYSTEM.md` — durable art, rendering, file-format, and visual-ownership rules.
5. `docs/VISUAL_REDESIGN_CONTINUITY_2026-07-23.md` — detailed visual history and active milestone guidance.
6. `docs/ARCHITECTURE_BIBLE.md` — durable technical architecture.
7. Charlie's explicit approval or correction.
8. Historical documents and tags for context only.

When sources conflict:

1. stop before modifying anything;
2. determine which source is newer and relevant;
3. inspect the real local implementation and browser output;
4. ask Charlie when approval remains ambiguous;
5. update continuity so the conflict cannot recur.

---

# 2. Repository and Branch State

## Production

```text
Repository: bins-projects/PrepFlow
Branch: master
Latest verified production commit: 8987fdf
```

Production `master` remains intentionally unchanged during the redesign.

Do not merge or publish the redesign to production `master` without Charlie's explicit approval.

## Active development

```text
Local repository: ~/projects/prepflow
Private repository: bins-projects/prepflow-dev
Public mirror repository: bins-projects/PrepFlow
Active branch: docs/continuity-rebuild
```

## Completed book milestone

```text
61851cd  checkpoint: preserve approved homepage book artwork
ca1b5d0  chore: finalize approved book UI cleanup
```

On 2026-07-24, local, `origin/docs/continuity-rebuild`, and `public/docs/continuity-rebuild` were explicitly verified at:

```text
ca1b5d0e1e5d8e598b7a202890234e43348dc4fb
```

The implementation milestone is complete and synchronized.

Documentation-only commits may be newer than `ca1b5d0`; that does not mean the book implementation is unfinished.

Frozen historical reference:

```text
before-continuity-rebuild-2026-07-20
```

---

# 3. Supporting Documents

## Architecture

```text
docs/ARCHITECTURE_BIBLE.md
```

Defines durable technical boundaries, including separation of artwork, live state, and browser behavior.

## Art system

```text
docs/ART_SYSTEM.md
```

Defines:

- PrepFlow Illustrated Pixel;
- background, nurse, book, HTML/JavaScript, and CSS ownership;
- runtime and source asset roles;
- approved book geometry and rendering;
- file-format rules;
- implemented, approved-but-not-implemented, experimental, and superseded status language.

## Visual continuity

```text
docs/VISUAL_REDESIGN_CONTINUITY_2026-07-23.md
```

Defines the completed book result, troubleshooting discoveries, and the next background/nurse milestone.

## Historical rebuild reasoning

```text
docs/CONTINUITY_REBUILD_PLAN.md
```

Use for forensic context only. It is not the current resume authority.

---

# 4. Current Product State

PrepFlow converts deliberately chosen educational material into independent validated Packs used by a browser-centered study application.

```text
Chosen educational source
→ extraction adapter
→ cleaner
→ detector
→ parser
→ normalizer
→ validator
→ permanent question identity
→ authoritative Pack
→ browser study application
```

Active browser product:

```text
web/
```

Official starting Packs:

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

Read exact question counts from the Pack files rather than old documentation.

The old Tkinter desktop stack, PyInstaller workflow, terminal client, and obsolete DOCX prototype were intentionally removed during the continuity rebuild. Do not restore them merely because they exist in Git history.

---

# 5. Completed and Approved Book State

Approved runtime assets:

```text
web/images/book-sprite-preview/prepflow-fundamentals-book.png
web/images/book-sprite-preview/prepflow-pharm-book.png
web/images/book-sprite-preview/prepflow-medsurg-book.png
```

Approved implementation:

```text
web/approved-book-buttons.css
web/app.js
web/index.html
web/pixel-home.css
```

Verified result:

- three transparent 1024 × 1024 subject-book PNG masters;
- locked v21 hardcover construction;
- smooth alpha and normal browser image smoothing;
- corrected page-grain direction;
- approved clean-border language;
- 256 CSS-pixel desktop display;
- equal three-column spacing;
- complete book artwork remains clickable;
- all three books open the correct chapter-selection screen;
- zero-selection badges are empty and hidden;
- selected-chapter badges remain live HTML/JavaScript state;
- question totals remain off closed-book artwork;
- always-visible `OPEN BOOK` ovals are removed.

Do not restore:

- CSS-drawn principal books;
- inline replacement cover emblems;
- the Pharm-only prototype;
- hard-edge native-256 exports;
- braided multi-color borders;
- crosswise page bands;
- baked question totals;
- always-visible `OPEN BOOK` labels.

Automated verification completed before commit `ca1b5d0`:

```text
72 passed
```

The cleanup commit contains only the four intended web files. Timestamped backups and proof assets were moved outside the repository to:

```text
~/prepflow-local-backups/2026-07-24-book-cleanup
```

---

# 6. Current Background and Nurse State

Current combined reference:

```text
web/images/pixel-home-stage.webp
```

It currently contains:

- the sunset-city environment;
- the female nurse;
- the male nurse.

This image is the approved visual reference, but it is not the final ownership structure.

Do not casually crop, regenerate, substitute, or overwrite it.

## Approved but not implemented

- a background-only static plate;
- a separate transparent female-nurse sprite;
- a separate transparent male-nurse sprite;
- reusable nurse pose variants after the base sprites are approved.

Separate pose files should be used first. Do not create a sprite sheet until runtime animation or repeated reuse justifies one.

---

# 7. Exact Next Visual Milestone

> Rebuild the current home scene as a background-only plate plus two separate transparent nurse sprites while preserving the approved character designs, sunset-city environment, proportions, palette, lighting, apparent scale, pixel density, and current book composition.

Start by documenting and inspecting the target layer boundaries before changing an asset.

Required order:

1. inspect the current combined reference at actual browser size;
2. identify the background-only plate boundary;
3. identify the female-nurse sprite boundary;
4. identify the male-nurse sprite boundary;
5. preserve the existing combined WebP as the rollback reference;
6. establish one representative nurse sprite before producing pose variants;
7. compose separate layers in the real application;
8. verify desktop, reduced-width, reduced-height, and narrow layouts;
9. leave the approved books unchanged during this milestone.

---

# 8. Local Browser Workflow

Canonical server command:

```bash
cd ~/projects/prepflow && python3 -m http.server 8004
```

Canonical URL:

```text
http://localhost:8004/web/
```

The server must run from:

```text
~/projects/prepflow
```

It must not run from `~/projects/prepflow/web`, because the sibling `packs/` directory must also be served.

Use:

```text
Ctrl+Shift+R
```

for a hard refresh.

A clean troubleshooting origin may use:

```bash
cd ~/projects/prepflow && python3 -m http.server 8005
```

```text
http://localhost:8005/web/
```

Port 8005 is diagnostic only; port 8004 remains canonical.

## Troubleshooting order

Before changing CSS or artwork because something looks stale:

1. verify a Python server is running;
2. verify its working directory;
3. open the exact asset directly by URL;
4. compare that asset with the homepage;
5. inspect the actual live DOM element;
6. inspect dynamically inserted children and pseudo-elements;
7. only then diagnose caching or the service worker.

The old visible ovals were produced by `.book-selected-count`, not by `.card-action` or the background image. Inspect live DOM before stacking suppression rules.

---

# 9. Working Discipline

Standard loop:

```text
Read restart authority
→ inspect local status
→ observe the real application
→ identify one focused change
→ implement locally
→ test
→ inspect the real output
→ document verified state
→ commit
→ push every intended remote
→ verify hashes
→ repeat
```

Permanent rules:

- one executable step at a time;
- local-first for active implementation;
- GitHub plugin for large documentation rewrites rather than long terminal heredocs;
- do not ask Charlie to paste hundreds of lines into the terminal;
- do not reconstruct multi-file local work from repeated snippets when a compact archive can expose the actual files;
- no speculative redesigns;
- do not claim tests, pushes, previews, or approvals that were not verified;
- preserve approved source artwork and exact SVG paths;
- do not flatten the complete scene when changing one isolated asset;
- keep temporary proofs, screenshots, transfer archives, and timestamped backups out of production commits;
- after every milestone, push both intended remotes and explicitly compare hashes.

When Charlie says `next`, continue to the next executable step rather than repeating the previous command.

---

# 10. Startup Procedure for the Next Chat

Before giving Charlie a modifying command:

1. read this packet;
2. read `docs/ART_SYSTEM.md`;
3. read `docs/VISUAL_REDESIGN_CONTINUITY_2026-07-23.md`;
4. inspect `git status --short --branch`;
5. confirm the branch is `docs/continuity-rebuild`;
6. confirm the book milestone is already complete;
7. run the existing home screen unchanged;
8. inspect the combined background/nurse reference;
9. state the one focused first action for the layer-separation milestone.

Do not restart book design or repeat the completed cleanup.

---

# 11. End-of-Session Procedure

Before ending substantial PrepFlow work:

1. inspect all tracked and untracked files;
2. classify production files, docs, proofs, backups, screenshots, and archives;
3. run applicable tests and browser checks;
4. update the relevant continuity documents;
5. commit the focused milestone;
6. push both `origin` and `public` when both should remain synchronized;
7. compare local, origin, and public hashes explicitly;
8. confirm a fresh chat can resume without conversational memory.

Do not assume a plain `git push` updates both remotes.

---

# 12. Fresh-Chat Opening Instruction

Use this exact instruction:

> Continue PrepFlow from my local repository at `~/projects/prepflow` on branch `docs/continuity-rebuild`. Read the current local `docs/RESTART_PACKET.md`, `docs/ART_SYSTEM.md`, and `docs/VISUAL_REDESIGN_CONTINUITY_2026-07-23.md` before giving me a command. Inspect `git status` first. The approved three-book milestone is complete and synchronized; begin with the background-only plate and separate nurse-sprite milestone. Give me one executable step at a time and use the GitHub plugin for large documentation rewrites instead of long terminal heredocs.

The authoritative development branch is `docs/continuity-rebuild`.

Production `master` remains intentionally unchanged at `8987fdf`.
