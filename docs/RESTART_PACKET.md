# PREPFLOW RESTART PACKET

## Purpose

This file is the single primary handoff for every new PrepFlow development session.

> **MANDATORY FIRST ACTION:** Read this entire file before inspecting GitHub, proposing a command, or changing any PrepFlow file.

For the current visual milestone, also read:

```text
docs/ART_SYSTEM.md
docs/VISUAL_REDESIGN_CONTINUITY_2026-07-23.md
```

The local repository at `~/projects/prepflow` is the active working source during development. The private GitHub branch is the authority for the last committed state and later synchronization, but it must not be treated as newer than local uncommitted work. The rendered local application is part of the source of truth for visual work.

---

# 1. Continuity Authority Hierarchy

Use this order:

1. `docs/RESTART_PACKET.md` — primary session handoff and authority index.
2. Local branch, working-tree status, local-only files, and current local working copy — active development truth.
3. Current private-repository branch and latest commit — last committed implementation truth.
4. `docs/ART_SYSTEM.md` — durable artwork, asset-ownership, rendering, format, and folder authority.
5. `docs/VISUAL_REDESIGN_CONTINUITY_2026-07-23.md` — detailed current visual milestone history and continuation rules.
6. `docs/ARCHITECTURE_BIBLE.md` — durable technical architecture and system boundaries.
7. The real rendered local application and approved screenshots.
8. Charlie's explicit approval or correction.
9. Historical documents and tags for context only.

When sources conflict:

1. stop before modifying anything;
2. identify which source is newer and relevant;
3. inspect the local implementation and rendered result;
4. ask Charlie when approval history remains ambiguous;
5. update continuity so the ambiguity cannot recur.

Do not reinterpret, remove, or restore work merely because an older document differs.

---

# 2. Repository and Work Locations

## Stable production version

```text
Repository: bins-projects/PrepFlow
Branch: master
Latest verified production commit: 8987fdf
```

Production `master` remains intentionally unchanged during the redesign.

Do not merge or publish the redesign to production `master` until Charlie explicitly approves that release step.

## Active development work

```text
Local repository: ~/projects/prepflow
Private repository: bins-projects/prepflow-dev
Public mirror repository: bins-projects/PrepFlow
Active branch: docs/continuity-rebuild
```

Important commits:

```text
6fa291c  docs: finalize continuity restart handoff
61851cd  checkpoint: preserve approved homepage book artwork
8960ccf  docs: add permanent PrepFlow art system
41e3b03  docs: define visual ownership boundaries
292b8e2  docs: refresh visual redesign handoff
```

At the time of this packet refresh:

- the approved book artwork checkpoint `61851cd` exists on both `origin/docs/continuity-rebuild` and `public/docs/continuity-rebuild`;
- later documentation commits exist on the private branch and local branch;
- the final production cleanup of the book implementation remains uncommitted locally;
- the public mirror branch must be brought fully current after that cleanup is committed and verified.

Frozen historical reference:

```text
before-continuity-rebuild-2026-07-20
```

Use the frozen tag for context, not as permission to restore superseded behavior.

---

# 3. Supporting Documents and Their Roles

## Permanent architecture

```text
docs/ARCHITECTURE_BIBLE.md
```

Defines durable technical architecture and visual ownership boundaries.

## Permanent art system

```text
docs/ART_SYSTEM.md
```

Defines:

- PrepFlow Illustrated Pixel;
- background, nurse, book, HTML/JavaScript, and CSS ownership;
- production formats;
- source/review/runtime folder roles;
- locked v21 book construction;
- smooth 1024-pixel book rendering;
- correct page-grain direction;
- approved subject locks;
- localhost visual-verification workflow;
- implemented, experimental, approved-but-not-implemented, and superseded status language.

## Current visual redesign authority

```text
docs/VISUAL_REDESIGN_CONTINUITY_2026-07-23.md
```

Defines the current visual milestone history, approved book result, troubleshooting discoveries, and next background/nurse milestone.

## Continuity rebuild plan

```text
docs/CONTINUITY_REBUILD_PLAN.md
```

Contains forensic reasoning and phased reconstruction history. It is not the current session handoff.

## Historical documents

Older dated handoffs and checkpoints are historical context only when this packet names a newer state.

---

# 4. Current Product and Architecture State

PrepFlow converts deliberately selected educational material into independent validated Packs and provides a browser-centered study application that uses those Packs.

Authoritative product flow:

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

Read exact question counts from the Pack files rather than relying on old documentation.

The legacy Tkinter desktop stack, PyInstaller workflow, old Windows pathway, and obsolete DOCX prototype were intentionally removed during the continuity rebuild. Do not restore them merely because they exist in history.

---

# 5. Current Visual State

The current home screen remains a visual-development canvas. It is approved through the subject-book milestone, but the background and nurses have not yet been separated.

## Implemented and approved

The three home-screen books are separate transparent 1024 × 1024 PNG assets:

```text
web/images/book-sprite-preview/prepflow-fundamentals-book.png
web/images/book-sprite-preview/prepflow-pharm-book.png
web/images/book-sprite-preview/prepflow-medsurg-book.png
```

They use:

- locked v21 hardcover construction;
- smooth alpha;
- correct page-grain direction;
- clean-border language;
- approved subject colors and icons;
- 256 CSS-pixel desktop display;
- equal spacing;
- transparent clickable button structure.

The authoritative book presentation layer is:

```text
web/approved-book-buttons.css
```

The complete transparent book is the clickable button.

Do not restore:

- CSS-drawn principal books;
- inline replacement cover emblems;
- the Pharm-only prototype;
- hard-edge native-256 exports;
- braided multi-color borders;
- crosswise cover-to-cover page bands;
- baked closed-book question totals;
- always-visible `OPEN BOOK` ovals.

## Live application state

HTML and JavaScript retain:

- `.subject-card` buttons;
- Pack paths;
- accessibility labels;
- click behavior;
- chapter-opening behavior;
- selected-chapter state;
- selected-chapter badges.

A zero-selection badge must be empty and hidden.

A selected-chapter badge may appear only when one or more chapters are selected.

## Current background reference

```text
web/images/pixel-home-stage.webp
```

This current reference still contains both nurses baked into the static image.

Do not casually crop, regenerate, substitute, or overwrite it. It is the visual reference for the next milestone.

## Approved but not implemented

- a background-only static plate;
- the two nurses as separate transparent sprites;
- reusable nurse pose variants;
- permanent source/review/export art folders if they do not yet exist.

---

# 6. Current Local Uncommitted Cleanup

The approved book artwork is already backed up in checkpoint commit `61851cd`.

After that checkpoint, the local working copy was cleaned and verified visually. These later changes are saved on the Chromebook but are not yet committed:

```text
web/approved-book-buttons.css
web/app.js
web/pixel-home.css
web/index.html
```

The cleanup does the following:

- replaces accumulated proof CSS with one authoritative book layer;
- retains 256-pixel desktop books and equal spacing;
- removes duplicate proof sizing blocks;
- removes temporary `.card-action` hiding attempts;
- removes the temporary DOM-removal experiment;
- retains the correct zero-selection badge behavior;
- normalizes cache-version references.

The cleaned result was inspected in the real browser and Charlie confirmed it looked clean.

Do not discard or overwrite these local changes before they are committed.

---

# 7. Required Startup Procedure

Before giving Charlie a modifying command in a new PrepFlow session:

1. Read this entire packet.
2. Read `docs/ART_SYSTEM.md`.
3. Read `docs/VISUAL_REDESIGN_CONTINUITY_2026-07-23.md`.
4. Treat `~/projects/prepflow` as the active working copy.
5. Inspect `git status --short --branch` before proposing a command.
6. Identify local uncommitted files, backups, generated files, and archives.
7. Inspect GitHub only to establish the last committed baseline and synchronization target.
8. Run the local application unchanged first for visual work.
9. State clearly:
   - stable production location;
   - active branch;
   - current local changes;
   - what is approved;
   - what remains unfinished;
   - the single next focused action.
10. Resolve contradictions before changing anything.

## Local-first rule

During active implementation, the local repository is the working source of truth.

Use GitHub to:

- inspect committed baselines;
- review history;
- perform large documentation rewrites when that is safer than a long terminal heredoc;
- back up verified milestones;
- synchronize intended remotes.

For large documentation rewrites:

- prefer the GitHub plugin;
- commit the documentation change to the active private branch;
- give Charlie one short `git pull --ff-only` command;
- do not make Charlie paste hundreds of lines into an interactive heredoc.

For multi-file local implementation work:

- do not reconstruct the working copy from repeated snippets when a compact local archive can expose the actual files;
- preserve project-relative paths;
- test the real local application before committing.

---

# 8. Local Browser Preview Workflow

Canonical server command:

```bash
cd ~/projects/prepflow && python3 -m http.server 8004
```

Canonical preview:

```text
http://localhost:8004/web/
```

The server must run from:

```text
~/projects/prepflow
```

It must not run from `~/projects/prepflow/web`, because the sibling `packs/` directory must also be served.

Use `Ctrl+Shift+R` for a hard refresh.

The Python server printing request logs is normal.

## Troubleshooting order

Before blaming CSS, the browser cache, or the service worker:

1. verify a Python server is actually running;
2. verify the server process working directory;
3. open the exact image asset directly by URL;
4. compare the direct asset with the homepage;
5. inspect the actual live DOM element;
6. inspect its children and pseudo-elements;
7. only then diagnose caching or service-worker behavior.

A clean diagnostic origin may use:

```bash
cd ~/projects/prepflow && python3 -m http.server 8005
```

```text
http://localhost:8005/web/
```

Port 8005 is a troubleshooting origin, not the canonical project URL.

Important lesson from the `OPEN BOOK` investigation:

- do not infer the source from a CSS class name alone;
- inspect the live DOM and use `$0.outerHTML` when necessary;
- the visible ovals came from `.book-selected-count`, not `.card-action` or the background plate.

---

# 9. Required Working Discipline

Standard loop:

```text
Read restart authority
→ inspect local working copy and status
→ inspect committed baseline only as needed
→ observe the rendered local application
→ identify one focused change
→ implement against the local working copy
→ run targeted verification
→ inspect the real output
→ document the verified state
→ commit
→ push every intended remote
→ verify branch hashes match
→ repeat
```

Permanent rules:

- one focused change at a time;
- do not ask for code already available through GitHub;
- do not perform speculative redesigns;
- do not claim tests, pushes, merges, previews, server states, cleanups, or approvals that were not verified;
- protect privacy before public release or sharing;
- when Charlie says `next`, treat the previous command as completed and provide the next executable step;
- do not repeat the previous command after `next`;
- clearly say when terminal output must be pasted before continuing;
- stop and reassess when troubleshooting becomes repetitive rather than stacking guesses;
- do not generate or flatten the complete scene when changing one isolated asset;
- update continuity when a durable decision changes.

---

# 10. Required End-of-Session Procedure

Before ending a substantial PrepFlow session:

1. inspect `git status` and identify every changed or untracked file;
2. classify production work, documentation, generated backups, screenshots, archives, and temporary proofs;
3. ensure intended work is committed or explicitly document why it remains uncommitted;
4. run applicable automated tests and browser checks;
5. inspect the focused diff;
6. keep timestamped backups, transfer ZIPs, screenshots, and superseded proofs out of the commit;
7. update the active supporting documentation;
8. update this Restart Packet;
9. commit one focused milestone;
10. push both `origin` and `public` when both are intended to stay synchronized;
11. fetch both remotes and explicitly compare local, origin, and public branch hashes;
12. confirm that a fresh chat can resume without conversational memory.

Do not assume a plain `git push` updates both remotes.

---

# 11. Current Exact Resume State

Active local work:

```text
~/projects/prepflow
docs/continuity-rebuild
```

Production remains:

```text
bins-projects/PrepFlow
master
8987fdf
```

Current committed private-branch documentation head before this packet update:

```text
292b8e2
```

Current verified milestone:

> The three approved transparent subject books render correctly, are evenly spaced, use the approved smooth 1024-pixel system, and no longer display always-visible `OPEN BOOK` ovals. The artwork checkpoint is backed up on both remotes. The later code cleanup is verified locally but remains uncommitted.

Current temporary local backups and proof files must be reviewed and excluded from the final commit unless deliberately retained under an ignored working location.

---

# 12. Exact Next Step

Finish and publish the approved book milestone before starting the background/nurse rebuild.

Required sequence:

1. inspect current `git status --short`;
2. run the applicable automated tests;
3. verify the home screen at full width and the reduced-width development layout;
4. verify all three books still open their chapter-selection screens;
5. select chapters and verify a real selected-count badge appears;
6. confirm zero-selection badges remain hidden;
7. inspect the final focused diff;
8. exclude or remove timestamped backups and transfer artifacts from the commit;
9. commit the local cleanup and final documentation state;
10. push `docs/continuity-rebuild` to both `origin` and `public`;
11. fetch both remotes and verify local, origin, and public hashes match;
12. begin the next session with the background-only plate and separate nurse-sprite milestone.

Do not merge to production `master` during this sequence.

---

# 13. Next Visual Milestone

After the book milestone is fully synchronized:

1. preserve `web/images/pixel-home-stage.webp` as the approved combined reference;
2. create a background-only plate without nurses;
3. create the female nurse as a separate transparent sprite;
4. create the male nurse as a separate transparent sprite;
5. preserve their approved designs, proportions, palette, lighting, and apparent scale;
6. compose the three layers in the real application;
7. verify desktop, reduced-width, reduced-height, and narrow layouts;
8. create pose variants only after the base reusable sprites are approved.

Use separate pose files initially. Do not create a sprite sheet until animation or runtime reuse justifies it.

---

# 14. Fresh-Chat Opening Instruction

Use this exact instruction:

> Continue PrepFlow from my local repository at `~/projects/prepflow` on branch `docs/continuity-rebuild`. Read the current local `docs/RESTART_PACKET.md`, `docs/ART_SYSTEM.md`, and `docs/VISUAL_REDESIGN_CONTINUITY_2026-07-23.md` before giving me a command. Inspect `git status` first. The approved three-book milestone should be fully synchronized before beginning the background-only plate and separate nurse-sprite rebuild. Give me one executable step at a time and use the GitHub plugin for large documentation rewrites instead of long terminal heredocs.

The authoritative development branch is `docs/continuity-rebuild`.

Production `master` remains intentionally unchanged at `8987fdf`.
