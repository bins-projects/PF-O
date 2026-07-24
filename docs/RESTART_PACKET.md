# PREPFLOW RESTART PACKET

## Purpose

This file is the primary handoff for every new PrepFlow development session.

> **MANDATORY FIRST ACTION:** Read this entire file before proposing a command or changing a PrepFlow file.

For visual work, also read:

```text
docs/ART_SYSTEM.md
docs/VISUAL_REDESIGN_CONTINUITY_2026-07-23.md
docs/RELEASE_2026-07-24_BOOK_MILESTONE.md
```

The local repository at `~/projects/prepflow` is the active working copy during development. The rendered local application is part of the source of truth for visual work.

---

# 1. Current Release and Development Topology

## Public production

```text
Repository: bins-projects/PrepFlow
Branch: master
Public deployment commit: 8e8e85b1e9b9604d257b6db52e9bb802fcb91fce
Public site: https://bins-projects.github.io/PrepFlow/web/
Release PR: bins-projects/PrepFlow#2
```

Charlie opened the deployed site after release and confirmed that the new three-book homepage looked great.

## Frozen release source snapshot

```text
Source snapshot: 648bcfbf218b11b7786bdb4cd42f5a596e7b4f58
Release branch: release/2026-07-24-book-milestone
```

The release branch exists in both:

```text
bins-projects/prepflow-dev
bins-projects/PrepFlow
```

Both release branches point to `648bcfb`.

Public `master` has merge commit `8e8e85b` because GitHub merged the fixed release branch through pull request #2. The deployed source tree is the tree from `648bcfb`.

Do not move, reuse, or continue ordinary development on the release branch.

## Active development

```text
Local repository: ~/projects/prepflow
Active branch: docs/continuity-rebuild
Private development repository: bins-projects/prepflow-dev
Public mirror repository: bins-projects/PrepFlow
Public mirror development branch: docs/continuity-rebuild
```

Daily work continues on `docs/continuity-rebuild`, not on public `master` and not on the frozen release branch.

The development branch is expected to move ahead of public production while the next milestone is being built.

---

# 2. Authority Order

Use this order:

1. Charlie's explicit approval or correction.
2. The rendered local application for visual and interaction truth.
3. The local repository, active branch, working tree, and local-only files.
4. `docs/RESTART_PACKET.md` for current topology and resume procedure.
5. `docs/ART_SYSTEM.md` for durable visual rules and asset ownership.
6. `docs/VISUAL_REDESIGN_CONTINUITY_2026-07-23.md` for the active visual milestone.
7. `docs/RELEASE_2026-07-24_BOOK_MILESTONE.md` for the current public release boundary.
8. The private development branch for the last committed development state.
9. The public mirror development branch for synchronization and release preparation.
10. Public `master` for the currently deployed production state.
11. Older dated handoffs, tags, and historical documents for context only.

When sources conflict:

1. stop before modifying anything;
2. inspect `git status --short --branch` locally;
3. identify the newest relevant source;
4. inspect the real rendered result;
5. ask Charlie when approval remains ambiguous;
6. update continuity after the conflict is resolved.

Do not overwrite newer local work merely because GitHub has an older committed copy.

---

# 3. Local-First Development Rule

The local repository is where PrepFlow is actively built and tested:

```text
~/projects/prepflow
```

Use the local working copy to:

- inspect and edit application files;
- run automated tests;
- run the local browser server;
- check real layout and behavior;
- preserve local visual experiments before committing;
- review the exact diff before a checkpoint or release.

Use GitHub to:

- inspect committed baselines and history;
- create durable documentation changes without long terminal heredocs;
- preserve verified checkpoints;
- synchronize the intended remotes;
- create fixed release branches and pull requests;
- verify branch and release hashes.

For large documentation rewrites, use the GitHub connector and then give Charlie one short `git pull --ff-only` command.

For implementation work, do not reconstruct the project from repeated snippets when the real local files are available.

---

# 4. Public Release Policy

PrepFlow should now be released publicly in coherent, tested chunks rather than waiting for every planned improvement.

Required release sequence:

1. complete one coherent milestone on `docs/continuity-rebuild`;
2. run applicable automated tests;
3. inspect the real local browser result;
4. verify core interactions affected by the milestone;
5. inspect the focused diff;
6. commit and push the development branch to both intended remotes;
7. verify local, private, and public-mirror development hashes;
8. create a fixed release branch from the approved commit;
9. open a pull request from that release branch into public `master`;
10. review the exact release scope and removals;
11. merge the release pull request;
12. verify the public GitHub Pages site;
13. record the release boundary in documentation.

Public `master` must not be used as the daily working branch.

Unfinished nurse, background, animation, or experimental work remains on the development branch until it forms an approved release chunk.

---

# 5. Current Product State

PrepFlow is a browser-centered nursing study application built around validated question Packs.

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

Read exact question counts from the current Pack files rather than relying on old documentation.

The browser-centered application is the active product. The removed legacy Tkinter, PyInstaller, and separate desktop-study stack must not be restored merely because it exists in history.

---

# 6. Released Three-Book Milestone

The public site now includes the approved transparent subject books:

```text
web/images/book-sprite-preview/prepflow-fundamentals-book.png
web/images/book-sprite-preview/prepflow-pharm-book.png
web/images/book-sprite-preview/prepflow-medsurg-book.png
```

They use:

- locked v21 hardcover construction;
- transparent 1024 × 1024 PNG masters;
- smooth alpha and browser image smoothing;
- correct page-grain direction;
- clean-border language;
- approved subject colors and icons;
- 256 CSS-pixel desktop display in the current composition;
- equal three-column spacing;
- transparent clickable button structure.

Authoritative presentation layer:

```text
web/approved-book-buttons.css
```

Live state owner:

```text
web/app.js
```

The complete book is the clickable button. A zero-selection badge is empty and hidden. A selected-count badge appears only when chapters are actually selected.

Do not restore:

- CSS-drawn principal books;
- inline replacement cover emblems;
- the Pharm-only prototype;
- native-256 hard-edge exports;
- braided multi-color borders;
- crosswise cover-to-cover page bands;
- baked closed-book question totals;
- always-visible `OPEN BOOK` ovals.

Release verification included all 72 automated tests passing and real-browser approval.

---

# 7. Current Background and Nurse State

Current combined visual reference:

```text
web/images/pixel-home-stage.webp
```

It still contains the sunset-city environment and both nurses baked into one static image.

It is the approved visual reference but not the final ownership structure.

The next milestone must separate:

1. a background-only static environment plate;
2. the female nurse as a transparent sprite;
3. the male nurse as a transparent sprite.

The separated assets must preserve:

- recognizable character identity;
- proportions;
- clothing and stethoscopes;
- palette;
- upper-left lighting direction;
- apparent scale;
- approved composition;
- PrepFlow Illustrated Pixel rendering language.

Preserve the combined reference. Do not overwrite it while building the separate layers.

Use separate pose files initially. Do not create a sprite sheet unless later animation or runtime reuse justifies it.

Do not regenerate or flatten the complete scene when changing one isolated asset.

---

# 8. Local Browser Workflow

Start the canonical local server from the repository root:

```bash
cd ~/projects/prepflow && python3 -m http.server 8004
```

Open:

```text
http://localhost:8004/web/
```

The server must run from `~/projects/prepflow`, not from `~/projects/prepflow/web`, because the sibling `packs/` directory must also be served.

Hard refresh:

```text
Ctrl+Shift+R
```

Clean diagnostic origin:

```bash
cd ~/projects/prepflow && python3 -m http.server 8005
```

```text
http://localhost:8005/web/
```

Port 8005 is only a troubleshooting origin.

Troubleshooting order:

1. verify the Python server is running;
2. verify its working directory;
3. open the target asset directly by URL;
4. compare the direct asset with the homepage;
5. inspect the live DOM element and its children;
6. inspect pseudo-elements;
7. only then diagnose CSS, cache, or service-worker behavior.

The old `OPEN BOOK` ovals came from `.book-selected-count`, not `.card-action` and not the background image.

---

# 9. Working Discipline

Standard loop:

```text
Read continuity
→ inspect local status
→ observe the real local application
→ identify one focused change
→ implement locally
→ test
→ inspect the output and diff
→ document durable decisions
→ commit
→ push intended remotes
→ verify hashes
→ repeat
```

Permanent rules:

- one focused change at a time;
- when Charlie says `next`, provide the next executable step rather than repeating the previous command;
- do not ask for code already available through GitHub or the local project;
- do not perform speculative redesigns;
- do not claim tests, pushes, merges, previews, or approvals that were not verified;
- keep backup assets, screenshots, transfer archives, and temporary proofs out of production commits;
- protect privacy before public sharing or release;
- preserve exact approved source art;
- update continuity whenever a durable rule, release boundary, or active milestone changes;
- push every remote intended to remain synchronized and explicitly compare hashes.

Do not assume a plain `git push` updates both remotes.

---

# 10. End-of-Session Procedure

Before ending a substantial PrepFlow session:

1. inspect `git status --short --branch`;
2. classify every changed and untracked file;
3. remove or relocate temporary backups from the repository;
4. run applicable automated tests;
5. perform real-browser checks for affected behavior;
6. inspect the focused diff;
7. update supporting documentation;
8. update this restart packet when topology or milestones changed;
9. commit one coherent milestone;
10. push both development remotes when both should match;
11. verify local, private, and public-mirror hashes;
12. create a release branch only for an approved public chunk;
13. confirm a fresh chat can resume without relying on conversational memory.

---

# 11. Exact Current Resume State

Public production is the released book milestone:

```text
Public master: 8e8e85b1e9b9604d257b6db52e9bb802fcb91fce
Release source snapshot: 648bcfbf218b11b7786bdb4cd42f5a596e7b4f58
Release branch: release/2026-07-24-book-milestone
Public site: https://bins-projects.github.io/PrepFlow/web/
```

Active development remains:

```text
~/projects/prepflow
docs/continuity-rebuild
```

The next focused milestone is the background-only plate plus two separate nurse sprites.

Do not redesign the books during that milestone.

Do not merge unfinished nurse/background work directly into public `master`.

---

# 12. Fresh-Chat Opening Instruction

Use this exact instruction:

> Continue PrepFlow from my local repository at `~/projects/prepflow` on branch `docs/continuity-rebuild`. Read the current local `docs/RESTART_PACKET.md`, `docs/ART_SYSTEM.md`, `docs/VISUAL_REDESIGN_CONTINUITY_2026-07-23.md`, and `docs/RELEASE_2026-07-24_BOOK_MILESTONE.md` before giving me a command. Inspect `git status --short --branch` first. The tested book-milestone source snapshot is frozen at `648bcfb`, and the public site is deployed from public `master` merge commit `8e8e85b`. Daily work remains local-first on `docs/continuity-rebuild`; public updates are promoted in tested milestone chunks through fixed release branches. Begin with the background-only plate and separate female and male nurse sprites while preserving the approved combined scene and book composition. Give me one executable step at a time and use the GitHub plugin for large documentation rewrites instead of long terminal heredocs.
