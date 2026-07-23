# PREPFLOW RESTART PACKET

## Purpose

This file is the single primary handoff for every new PrepFlow development session.

> **MANDATORY FIRST ACTION:** Read this entire file before inspecting GitHub, proposing a command, or changing any PrepFlow file. For the current visual milestone, then read `docs/VISUAL_REDESIGN_CONTINUITY_2026-07-23.md` in full.

A new chat must begin here. Supporting documents may contain detailed architecture, history, or visual decisions, but they do not replace this packet. This packet identifies which supporting documents apply to the current milestone and what authority each one has.

The local repository at `~/projects/prepflow` is the active working source during development. The private GitHub repository is the authority for the last committed state and later synchronization, but it must not be treated as the current working copy when local commits, uncommitted files, generated assets, or visual changes may exist. The rendered local application is also part of the source of truth for visual work.

---

# 1. Continuity Authority Hierarchy

Use this order:

1. `docs/RESTART_PACKET.md` — primary session handoff and authority index.
2. Local branch, working-tree status, local-only files, and the current local working copy — active development truth.
3. Current private-repository branch and latest commit — last committed implementation truth and synchronization target.
4. Supporting documents named by this packet for the active milestone.
5. The real rendered local application and baseline screenshots for visual work.
6. Charlie's explicit approval or correction of design intent.
7. Historical documents and tags for context only.

When sources conflict:

1. stop before modifying anything;
2. identify which source is newer and relevant to the active area;
3. compare the implementation and rendered result;
4. ask Charlie when approval history remains ambiguous;
5. update this packet so the same ambiguity cannot recur.

Do not reinterpret, remove, or restore work merely because an older document differs.

---

# 2. Repository and Work Locations

## Stable public version

```text
Repository: bins-projects/PrepFlow
Branch: master
Latest verified public commit: 8987fdf  feat: load the 15 missing Pharm drug cards
```

The public version is the stable fallback. Do not modify or publish it during unfinished redesign work unless Charlie explicitly approves a release or merge.

## Active private development work

```text
Repository: bins-projects/prepflow-dev
Branch: docs/continuity-rebuild
```

Protected redesign-canvas checkpoint:

```text
f393626  wip: checkpoint responsive home and sprite redesign
```

Latest completed responsive milestone:

```text
e5ed054  fix: stabilize half-width home composition
```

Latest visual-continuity update before this packet refresh:

```text
0624d32  docs: preserve Pharm sprite proof decisions
```

Frozen pre-rebuild reference:

```text
before-continuity-rebuild-2026-07-20
```

Use the frozen tag for historical context, not as permission to restore superseded behavior.

---

# 3. Supporting Documents and Their Roles

## Permanent architecture

```text
docs/ARCHITECTURE_BIBLE.md
```

Contains durable technical architecture and system boundaries.

## Continuity rebuild plan

```text
docs/CONTINUITY_REBUILD_PLAN.md
```

Contains the phased reconstruction plan and forensic reasoning. It is not the current session handoff.

## Historical detailed checkpoint

```text
docs/SESSION_CHECKPOINT_2026-07-20.md
```

Contains detailed completed work through the browser behavior extractions and later historical notes. Do not use an older “Exact next milestone” from that document when this packet names a newer active milestone.

## Current visual redesign authority

```text
docs/VISUAL_REDESIGN_CONTINUITY_2026-07-23.md
```

This document must be read in full before any visual, responsive, sprite, home-screen, book, button, background, or nurse-character work.

It now records:

- the completed half-width composition milestone;
- the approved three-book transparent PNG replacement completed locally on 2026-07-23;
- the proven local-snapshot collaboration workflow for multi-file work;
- the approved pixel-art background direction;
- the transparent-raster sprite production workflow;
- the PNG/WebP/SVG division of responsibility;
- the completed three-book sprite implementation and preserved JavaScript behavior;
- the decision to remove question totals from closed book covers;
- the warning that the older Pharm-only proof is superseded and must not be restored;
- the rule against generating or flattening the full PrepFlow scene when working on one isolated asset;
- the dedicated local-server workflow and command-flow preferences;
- the exact next visual milestone.

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

The legacy Tkinter desktop stack, PyInstaller configuration, old Windows workflow, and obsolete DOCX prototype were intentionally removed during the continuity rebuild. Do not restore them merely because they appear in history.

The browser behavior boundary work and permanent browser question-reference migration were completed on the private branch. The current active work is visual redesign, not another broad behavior extraction.

---

# 5. Current Visual Redesign State

The current home screen is an unfinished visual-development canvas. It is not a completed design and not technical debt to remove casually.

Approved and verified:

- preserve the pixel-art sunset-city background style;
- use the home terminal/launcher as the working canvas;
- the reduced-width launcher and reference panel no longer collide;
- the logo and tagline remain separated at reduced width;
- the environment reaches the bottom of the tested reduced-height viewport;
- full-width rendering was checked after the half-width change and was not regressed;
- use transparent raster sprites for principal illustrated books and characters;
- use PNG during design and iteration;
- optimized transparent WebP may be used after approval when fidelity is preserved;
- reserve SVG for clean vector-like symbols and interface icons;
- use CSS for placement, responsive behavior, movement, glow, and state—not for drawing the principal final book or character artwork;
- use Pharm as the first book-sprite prototype;
- apply the final approved pattern to Fundamentals and Med-Surg only afterward;
- keep changing application data as live HTML;
- do not display total question counts on closed home-screen books;
- show totals inside the opened book/chapter-selection experience instead;
- preserve live chapter-selection status, accessibility, data attributes, and click behavior;
- do not generate, redraw, or flatten the complete PrepFlow scene when working on one isolated asset.

Current approved reference asset:

```text
web/images/pixel-home-stage.webp
```

The background and two nurses are presently baked into that one static image. Do not crop, regenerate, substitute, or replace it casually.

The three closed home-screen books have now been replaced locally with Charlie-approved transparent PNG artwork:

```text
web/images/book-sprite-preview/prepflow-fundamentals-book.png
web/images/book-sprite-preview/prepflow-pharm-book.png
web/images/book-sprite-preview/prepflow-medsurg-book.png
```

The replacement preserves the existing `.subject-card` JavaScript hook, Pack data attributes, chapter-opening behavior, and live selection-badge behavior. The visual layer is isolated in:

```text
web/approved-book-buttons.css
```

Verified on 2026-07-23:

- all three approved books render in the live local application;
- the prior CSS-drawn books and inline cover emblems are no longer visible;
- Fundamentals, Pharm, and Med-Surg each open their chapter-selection screen;
- the local server must run from `~/projects/prepflow`, not from `~/projects/prepflow/web`, so the sibling `packs/` directory is served.

This work is currently local and uncommitted. Do not replace it with the older committed CSS-built placeholder state.

---

# 6. Required Startup Procedure

Before giving Charlie any modifying command in a new PrepFlow session:

1. Read this entire `docs/RESTART_PACKET.md` from the current local snapshot when available.
2. Read `docs/VISUAL_REDESIGN_CONTINUITY_2026-07-23.md` in full for the current milestone.
3. Treat `~/projects/prepflow` as the active working copy. Do not begin by editing GitHub or assuming GitHub contains the newest local work.
4. Inspect local `git status --short --branch` and determine whether local commits, uncommitted files, generated assets, backups, or archives exist.
5. Inspect the private GitHub branch only to establish the last committed baseline and eventual synchronization target.
6. When several related local files must be inspected and no direct local-filesystem tool is available, ask for one archive of the smallest relevant local folder or file set. Do not reconstruct a multi-file feature from repeated `grep`, `sed`, or copied snippets.
7. Inspect that uploaded local snapshot directly, prepare the complete focused change against it, and return only the modified files in an archive that preserves project-relative paths.
8. Apply the returned archive to the local repository, test the real local application, and review the actual rendered result before documenting, committing, or pushing.
9. For visual work, run the local application unchanged first and capture or inspect a fresh baseline screenshot.
10. Compare this packet, local Git state, the last committed state, the visual authority document, the rendered result, and Charlie's approval history.
11. State clearly before changing anything:
   - where the stable version lives;
   - where active local work lives;
   - the current branch;
   - what is approved;
   - what is unfinished;
   - the single next focused action.
12. Resolve contradictions before recommending a modifying command.

## Local-first collaboration rule

During active development, the local repository is the working source of truth. GitHub is not the editing target and must not be used as a substitute for uncommitted local files.

Use GitHub to:

- inspect the last committed baseline;
- review history when needed;
- commit and push only after the local change works;
- verify intended remotes after a milestone.

Use a packaged local snapshot when:

- the task spans several HTML, CSS, JavaScript, image, or documentation files;
- local uncommitted changes matter;
- the exact cascade, file relationships, or assets cannot be reliably reconstructed from snippets;
- direct local repository access is unavailable.

Do not ask Charlie to act as a repeated file viewer when one relevant local archive will provide the actual working copy.

---

# 7. Local Browser Preview Workflow

Use a dedicated terminal for the Python server:

```bash
cd ~/projects/prepflow && python3 -m http.server 8004
```

Leave that terminal running during previews.

Open:

```text
http://localhost:8004/web/
```

Use `Ctrl+Shift+R` for a hard refresh after visual changes.

The Python-server terminal printing request logs during refresh is normal.

Before blaming the service worker or CSS cascade, verify that port `8004` is actually running and serving the current `~/projects/prepflow` files. The current service worker uses a network-first fetch strategy.

---

# 8. Required Working Discipline

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
→ push the intended private branch
→ verify synchronization
→ repeat
```

Permanent rules:

- one focused change at a time;
- do not ask for code already available through GitHub;
- do not make broad cleanup changes during visual iteration;
- do not manually repair generated Packs when the generic pipeline should be fixed;
- quarantine a small number of malformed source questions rather than broadening parser behavior recklessly;
- never claim a test, push, merge, runtime result, preview, cleanup, server state, or visual approval that was not verified;
- protect privacy before public release or sharing;
- when Charlie says `next`, treat the previous paste command as completed and provide the next executable step;
- do not repeat the previous command after `next`;
- when output is required, say clearly: `Paste the output here before continuing.`;
- for ordinary Bash commands, say only `Paste this`;
- identify the Python-server terminal only when the command must run there;
- stop and reassess when troubleshooting becomes repetitive rather than stacking additional guesses;
- do not generate the complete scene when the task concerns one isolated sprite or graphic element.

When work becomes repetitive, uncertain, or context-heavy:

1. stop changing files;
2. return to this packet and the active supporting document;
3. identify the unresolved decision;
4. inspect the smallest relevant evidence;
5. update continuity before starting a new chat.

---

# 9. Required End-of-Session Procedure

Before ending a substantial PrepFlow session:

1. Inspect `git status` and identify every changed or untracked file.
2. Ensure intended work is committed, or explicitly document why it remains uncommitted.
3. Run applicable tests and real-browser checks.
4. Push the active private branch when the milestone or checkpoint should be backed up.
5. Verify local and private remote hashes match.
6. Update the detailed supporting document for the active milestone.
7. Update this Restart Packet with current branch, latest commit, completed work, unfinished work, exact next step, and required supporting documents.
8. Replace stale current-state wording rather than stacking contradictory temporary handoffs.
9. Confirm that a fresh chat can orient itself from this packet without relying on conversational memory.
10. Push the documentation update and verify the private remote hash.

---

# 10. Verification and Rollback Rules

Every milestone must answer:

1. What exact behavior or visual element is changing?
2. What must remain unchanged?
3. Which automated or manual checks protect it?
4. What real-browser check is required?
5. What commit is the rollback point?
6. Which remotes should be synchronized when complete?

Prefer normal corrective or revert commits over casual history rewriting.

Important rollback references:

```text
before-continuity-rebuild-2026-07-20
8987fdf
f393626
e5ed054
```

---

# 11. Current Exact Resume State

Stable public work remains on:

```text
bins-projects/PrepFlow
master
```

Active redesign work remains on the local branch:

```text
~/projects/prepflow
docs/continuity-rebuild
```

Required detailed supporting document:

```text
docs/VISUAL_REDESIGN_CONTINUITY_2026-07-23.md
```

Current verified local milestone:

> The three Charlie-approved transparent PNG book covers are installed and render correctly. Fundamentals, Pharm, and Med-Surg each open their chapter-selection screen. The implementation is local and uncommitted.

Do not restore the older CSS-built books, return to the superseded Pharm-only proof, rebuild the styling architecture, or treat GitHub as newer than the current local working copy.

---

# 12. Exact Next Step

The approved three-book PNG replacement is working locally but has not yet been committed.

Required sequence:

1. keep the Python server rooted at `~/projects/prepflow`;
2. verify the home screen at full width and at the reduced-width layout normally used during development;
3. verify chapter-selection badges still appear after selecting chapters from each book;
4. run the existing automated test suite;
5. inspect the focused local diff for `web/index.html`, `web/approved-book-buttons.css`, and the three PNG assets;
6. remove or relocate temporary transfer archives and the temporary `web/index.html.before-book-repair` backup so they are not accidentally committed;
7. update this packet only if testing changes the verified state;
8. commit the approved book replacement locally;
9. push and verify the intended private remote;
10. do not publish or merge to the stable public version until Charlie explicitly approves that release step.

Do not restart the book design, restore the older CSS-drawn books, rebuild the styling architecture, or treat GitHub as newer than the current local working copy.

## What Charlie should say in a fresh chat

Use this exact instruction:

> Continue PrepFlow from my local repository at `~/projects/prepflow` on branch `docs/continuity-rebuild`. Read the current local `docs/RESTART_PACKET.md` first, then read `docs/VISUAL_REDESIGN_CONTINUITY_2026-07-23.md` in full. Treat local uncommitted work as newer than GitHub, inspect `git status` before giving me any command, and follow the exact resume state in the packet.

## Final restart authority

Read `docs/FINAL_HANDOFF_2026-07-23.md` before starting another PrepFlow session.
The authoritative development branch is `docs/continuity-rebuild`.
Production `master` remains intentionally unchanged at `8987fdf`.

