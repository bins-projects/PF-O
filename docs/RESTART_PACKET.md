# PREPFLOW RESTART PACKET

## Purpose

This file is the single primary handoff for every new PrepFlow development session.

A new chat must begin here. Supporting documents may contain detailed architecture, history, or visual decisions, but they do not replace this packet. This packet must identify which supporting documents apply to the current milestone and what authority each one has.

The committed private repository is the technical source of truth. Local Git state and the rendered application must also be checked whenever work may be uncommitted, environment-specific, or visual.

---

# 1. Continuity Authority Hierarchy

Use this order:

1. `docs/RESTART_PACKET.md` — primary session handoff and authority index.
2. Current private-repository branch and latest commit — committed implementation truth.
3. Local branch, working-tree status, and local-only files — required when work may be uncommitted.
4. Supporting documents named by this packet for the active milestone.
5. The real rendered application and baseline screenshots for visual work.
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

Repository:

```text
bins-projects/PrepFlow
```

Branch:

```text
master
```

Latest verified public commit when this packet was updated:

```text
8987fdf  feat: load the 15 missing Pharm drug cards
```

The public version is the stable fallback. Do not modify or publish it during unfinished redesign work unless Charlie explicitly approves a release or merge.

## Active private development work

Repository:

```text
bins-projects/prepflow-dev
```

Branch:

```text
docs/continuity-rebuild
```

Protected redesign-canvas checkpoint:

```text
f393626  wip: checkpoint responsive home and sprite redesign
```

The current private branch also contains the dedicated visual continuity document added after that checkpoint.

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

Contains detailed completed work through the browser behavior extractions and later local notes. Treat it as a historical work log. Do not use an older “Exact next milestone” from that document when this packet names a newer active milestone.

## Current visual redesign authority

```text
docs/VISUAL_REDESIGN_CONTINUITY_2026-07-23.md
```

Must be read in full before any visual, responsive, sprite, home-screen, book, button, background, or nurse-character work.

It records:

- the unfinished home terminal/launcher canvas;
- responsive scaling and dead-space work still in progress;
- the pixel-art background direction;
- the Pharm-first reusable book-sprite plan;
- reusable pixel-art button direction;
- the current combined nurse/background reference asset;
- the future separation of background and reusable nurse sprites;
- change-control rules for overlapping visual CSS.

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

Protected canvas commit:

```text
f393626
```

Current approved direction:

- preserve the pixel-art sunset-city background style;
- extend the environment to the bottom of normal viewports to eliminate dead space;
- finish responsive scaling without distorting live text;
- use the home terminal/launcher as the working canvas;
- rebuild books and buttons into a coherent reusable pixel-art sprite system;
- use Pharm as the first book-sprite prototype;
- apply the approved pattern to Fundamentals and Med-Surg only after Pharm is approved;
- keep changing titles, counts, selection status, and button labels as live HTML where practical;
- preserve the current combined two-nurse sunset asset as the approved visual reference;
- later separate the environment and nurses into reusable assets;
- create consistent nurse pose variants for different screens only after the home composition and asset system are stable.

Current approved reference asset:

```text
web/images/pixel-home-stage.webp
```

The background and two nurses are presently baked into that one static image. Do not crop, regenerate, substitute, or replace it casually.

The current layered CSS files are unfinished visual iterations. Do not disable, delete, consolidate, or reinterpret a layer solely because rules overlap. First determine which visual decision it represents and compare the real rendered page.

---

# 6. Required Startup Procedure

Before giving Charlie any modifying command in a new PrepFlow session:

1. Read this entire `docs/RESTART_PACKET.md` from the private repository.
2. Identify the stable public repository and the active private repository named here.
3. Inspect the active private branch and latest commit.
4. Inspect local `git status --short --branch` before assuming the local branch matches GitHub.
5. Determine whether local commits or uncommitted files exist.
6. Read every supporting document this packet names for the current milestone.
7. For visual work, run the actual local application unchanged and inspect a fresh baseline screenshot.
8. Compare the packet, current Git state, supporting documents, rendered result, and Charlie's recalled approvals.
9. State clearly before changing anything:
   - where the stable version lives;
   - where active work lives;
   - the current branch;
   - the protected rollback/checkpoint commit;
   - what is approved;
   - what is unfinished;
   - the single next focused action.
10. Resolve contradictions before recommending a modifying command.

GitHub-first rule:

Before asking Charlie to paste committed files, inspect the connected private repository. Request terminal output only for local state, runtime behavior, tests, ignored/generated artifacts, environment-specific behavior, or exact synchronization checks.

For visual work, GitHub inspection is necessary but not sufficient. The real browser rendering and baseline screenshot are part of the source of truth.

---

# 7. Required Working Discipline

Standard loop:

```text
Observe
→ inspect committed code
→ inspect local status
→ run the real product unchanged when relevant
→ identify one focused change
→ preserve or add tests where appropriate
→ implement
→ run targeted verification
→ run full applicable verification
→ inspect the real output
→ commit
→ push the intended private branch
→ verify hashes
→ update continuity documents
→ repeat
```

Permanent rules:

- one focused change at a time;
- do not ask for code already available through GitHub;
- do not make broad cleanup changes during visual iteration;
- do not manually repair generated Packs when the generic pipeline should be fixed;
- quarantine a small number of malformed source questions rather than broadening parser behavior recklessly;
- never claim a test, push, merge, runtime result, or visual approval that was not verified;
- protect privacy before public release or sharing;
- when Charlie says `next`, provide the next executable step rather than a menu;
- for ordinary Bash commands, say only “paste this”; identify the terminal only when the command must run in the Python-server terminal.

When work becomes repetitive, uncertain, or context-heavy:

1. stop changing files;
2. return to this packet and the active supporting document;
3. identify the unresolved decision;
4. inspect the smallest relevant evidence;
5. update continuity before starting a new chat.

---

# 8. Required End-of-Session Procedure

Before ending a substantial PrepFlow work session:

1. Inspect `git status` and identify every changed or untracked file.
2. Ensure intended work is committed, or explicitly document why it remains uncommitted.
3. Run applicable tests and real-browser checks.
4. Push the active private branch when the milestone or checkpoint should be backed up.
5. Verify local and private remote hashes match.
6. Update the detailed supporting document for the active milestone.
7. Update this Restart Packet with:
   - current branch;
   - latest verified commit or protected checkpoint;
   - stable-versus-active work locations;
   - completed work;
   - unfinished work;
   - exact next step;
   - supporting documents the next chat must read.
8. Replace stale current-state wording rather than stacking contradictory temporary handoffs.
9. Confirm that a fresh chat can orient itself from this packet without relying on conversational memory.
10. Push the documentation update and verify the private remote hash.

A temporary checkpoint is allowed only when work is unfinished and detailed context will not fit cleanly here. This packet must point to it and explain its authority. A checkpoint never silently becomes an alternate primary handoff.

---

# 9. Verification and Rollback Rules

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
```

---

# 10. Current Exact Resume State

Stable public work remains on:

```text
bins-projects/PrepFlow
master
```

Active redesign work remains on:

```text
bins-projects/prepflow-dev
docs/continuity-rebuild
```

Protected working-canvas checkpoint:

```text
f393626  wip: checkpoint responsive home and sprite redesign
```

Required supporting document:

```text
docs/VISUAL_REDESIGN_CONTINUITY_2026-07-23.md
```

Current unfinished milestone:

> Establish the real home terminal as a dependable visual canvas, finish the reduced-window scaling and bottom dead-space investigation without redesigning unrelated elements, then establish the background-extension strategy before finalizing Pharm as the first reusable book sprite.

Do not begin by removing layered CSS, disabling the emblem preview, redesigning all three books at once, regenerating the approved home scene, or merging the unfinished redesign into public `master`.

---

# 11. Exact Next Step

1. Synchronize the local `docs/continuity-rebuild` branch with the latest private remote documentation commits.
2. Verify local and remote hashes and confirm the working tree is clean.
3. Read this packet and `docs/VISUAL_REDESIGN_CONTINUITY_2026-07-23.md` locally.
4. Run the current home page unchanged.
5. Capture and inspect a baseline at full width and reduced width/height.
6. Identify one scaling or dead-space failure without changing the book design.
7. Make one isolated responsive-composition change and verify both baselines before continuing.
