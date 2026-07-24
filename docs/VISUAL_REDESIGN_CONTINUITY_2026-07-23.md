# PrepFlow Visual Redesign Continuity — 2026-07-23

> **Updated 2026-07-24:** The approved three-book artwork and runtime cleanup are complete, tested, committed, pushed to both development remotes, and explicitly verified at matching commit `ca1b5d0e1e5d8e598b7a202890234e43348dc4fb`. The active visual milestone is now separation of the background and nurses.

This document is the detailed handoff for the active visual redesign.

Durable art rules:

```text
docs/ART_SYSTEM.md
```

Durable technical ownership boundaries:

```text
docs/ARCHITECTURE_BIBLE.md
```

Current branch state and exact resume procedure:

```text
docs/RESTART_PACKET.md
```

---

## 1. Active branch and protected milestones

Continue redesign work on:

```text
docs/continuity-rebuild
```

Production `master` remains separate until Charlie intentionally approves promotion.

Important preserved commits:

```text
61851cd  checkpoint: preserve approved homepage book artwork
8960ccf  docs: add permanent PrepFlow art system
41e3b03  docs: define visual ownership boundaries
ca1b5d0  chore: finalize approved book UI cleanup
```

On 2026-07-24, these three branch locations were verified at the same implementation commit:

```text
LOCAL:  ca1b5d0e1e5d8e598b7a202890234e43348dc4fb
ORIGIN: ca1b5d0e1e5d8e598b7a202890234e43348dc4fb
PUBLIC: ca1b5d0e1e5d8e598b7a202890234e43348dc4fb
```

Documentation-only commits may be newer than this implementation commit.

---

## 2. Completed and approved three-book milestone

Approved runtime assets:

```text
web/images/book-sprite-preview/prepflow-fundamentals-book.png
web/images/book-sprite-preview/prepflow-pharm-book.png
web/images/book-sprite-preview/prepflow-medsurg-book.png
```

Approved result:

- all three books use the locked v21 hardcover construction;
- all three are transparent 1024 × 1024 PNG masters;
- all three use smooth alpha and normal browser image smoothing;
- all three use corrected page-grain direction;
- all three use the approved clean-border language;
- all three display at 256 CSS pixels in the current desktop composition;
- all three remain real `<button class="subject-card">` elements;
- the complete transparent book is clickable;
- all three open the correct chapter-selection screen;
- zero-selection badges are empty and hidden;
- selected-chapter state remains live HTML and JavaScript;
- selected-chapter badges appear only for actual selections;
- question totals remain off closed-book artwork;
- always-visible `OPEN BOOK` ovals are gone.

The visible set was explicitly approved by Charlie.

Do not restore:

- CSS-drawn principal books;
- inline replacement cover emblems;
- the Pharm-only prototype;
- native 256 hard-edge exports;
- hard alpha thresholds;
- tiny-palette quantization;
- braided multi-color borders;
- crosswise cover-to-cover page bands;
- baked question totals;
- always-visible `OPEN BOOK` labels.

---

## 3. Completed runtime cleanup

Authoritative book presentation layer:

```text
web/approved-book-buttons.css
```

Live selection-state owner:

```text
web/app.js
```

The final cleanup committed in `ca1b5d0`:

- replaced accumulated proof CSS with one authoritative production layer;
- retained 256-pixel desktop sizing and equal spacing;
- retained normal image smoothing;
- removed duplicate proof-sizing blocks;
- removed obsolete `.card-action` handling;
- removed temporary `.card-action` suppression experiments;
- removed temporary DOM-removal code;
- retained correct zero-selection badge behavior;
- retained `.book-selected-count:empty` hiding behavior;
- normalized book-milestone cache-version references;
- removed the extra end-of-file whitespace in `web/pixel-home.css`.

Verification before commit:

```text
git diff --check: passed
pytest: 72 passed
```

The cleaned homepage remained visually correct after the cleanup.

Temporary backups and proof files were moved outside the repository to:

```text
~/prepflow-local-backups/2026-07-24-book-cleanup
```

The book milestone is closed. Do not repeat its forensic cleanup in the next chat.

---

## 4. Visual ownership authority

Read `docs/ART_SYSTEM.md` before producing or changing a book, nurse, character, prop, background, or illustrated sprite.

Current ownership:

- background plate = static environment artwork without characters or dynamic data;
- nurses = separate transparent raster sprites;
- books = separate transparent clickable artwork;
- live counts and selection state = HTML and JavaScript;
- placement, sizing, responsive composition, hover, focus, and state presentation = CSS.

Permanent artwork may contain permanent subject identity, icons, clothing, and permanent PrepFlow branding.

Changing application information must remain outside artwork.

---

## 5. Current background and nurse state

Current combined reference:

```text
web/images/pixel-home-stage.webp
```

This image presently contains:

- the sunset-city environment;
- the female nurse;
- the male nurse.

It is the approved visual reference but not the final ownership structure.

Do not casually crop, regenerate, substitute, or overwrite it.

The active milestone must create:

1. a background-only static environment plate;
2. the female nurse as a transparent sprite;
3. the male nurse as a transparent sprite.

The rebuilt assets must preserve:

- recognizable character identity;
- body proportions;
- clothing and stethoscopes;
- palette;
- upper-left lighting relationship;
- apparent scale;
- approved placement relationship;
- PrepFlow Illustrated Pixel rendering language;
- compatibility with the approved book composition.

Separate pose files should be used first. Do not create a sprite sheet until runtime animation or repeated reuse justifies it.

Do not regenerate or flatten the complete PrepFlow scene when working on one isolated layer.

---

## 6. Exact next visual milestone

> Rebuild the current home scene as a background-only plate plus two separate transparent nurse sprites while preserving the approved character designs, sunset-city setting, proportions, lighting, pixel density, and current book composition.

Begin with observation and layer planning, not immediate redrawing.

Required first sequence:

1. run the current application unchanged;
2. inspect the combined scene at actual desktop size;
3. document the exact background-only boundary;
4. document the female-nurse sprite boundary;
5. document the male-nurse sprite boundary;
6. preserve the existing combined WebP as the rollback reference;
7. choose one representative nurse sprite to establish the extraction/rebuild method;
8. verify the representative sprite in the real application before producing the second nurse or pose variants.

Do not redesign the books during this milestone.

---

## 7. Responsive composition rule

Do not solve scaling by independently changing unrelated elements across many files without checking the complete scene.

Use:

- one clear home-scene container;
- one approved desktop reference composition;
- proportional placement inside that composition;
- a small number of intentional breakpoints;
- readable live controls;
- deliberate narrow-screen reflow.

Current reduced-width layout authority:

```text
web/half-width-composition.css
```

Treat it as layout-only. It does not define permanent book or character artwork.

After layer separation, verify:

- full desktop width;
- the reduced-width development layout;
- reduced-height layout;
- narrow layout;
- book and nurse overlap relationships;
- logo and tagline separation;
- scene extension to the bottom edge.

---

## 8. Local browser workflow

Canonical server command:

```bash
cd ~/projects/prepflow && python3 -m http.server 8004
```

Canonical URL:

```text
http://localhost:8004/web/
```

The server must run from the project root, not from `web/`, because the sibling `packs/` directory must also be served.

Hard refresh:

```text
Ctrl+Shift+R
```

### Verified troubleshooting order

Before changing code during a display problem:

1. confirm a Python server is running;
2. confirm its working directory;
3. open the target asset directly by URL;
4. compare the direct asset with the homepage;
5. inspect the live DOM element;
6. inspect pseudo-elements and dynamically inserted children;
7. only then diagnose CSS, browser cache, or the service worker.

A clean diagnostic origin may use:

```bash
cd ~/projects/prepflow && python3 -m http.server 8005
```

```text
http://localhost:8005/web/
```

Port 8005 is diagnostic only.

### Lesson from the `OPEN BOOK` diagnosis

The visible ovals were not baked into the background and were not `.card-action` elements.

The actual live element was:

```html
<span class="book-selected-count">Open book</span>
```

The correct fix was to leave the badge empty when zero chapters were selected.

When troubleshooting becomes repetitive, stop guessing and inspect the actual rendered DOM.

---

## 9. Local-first and GitHub workflow

During active visual implementation, the local repository is the working source of truth.

Use GitHub to:

- inspect committed baselines;
- preserve verified checkpoints;
- perform large documentation rewrites instead of fragile terminal heredocs;
- synchronize intended branches;
- verify branch hashes.

For multi-file application changes, inspect the actual local working copy rather than reconstructing it from repeated snippets.

For large documentation changes, use the GitHub connector and give Charlie one short pull command.

Do not ask Charlie to paste hundreds of lines into an interactive heredoc when the connector can perform the rewrite.

---

## 10. Command-flow preference

- Give one executable step at a time.
- When Charlie says `next`, continue instead of repeating the prior command.
- Ask for terminal output only when the next decision depends on it.
- Keep Python-server commands separate from ordinary terminal commands.
- Explain whether an asset is a rough study, a review proof, or a usable runtime asset.
- Preserve explicit approval locks.

---

## 11. Fresh-chat resume state

The approved book milestone is complete and synchronized.

The next chat should not:

- redesign the books;
- repeat the book cleanup;
- restore old CSS-drawn covers;
- return to the Pharm-only prototype;
- treat always-visible `OPEN BOOK` labels as desired behavior.

The next chat should begin by reading the restart packet and art system, running the existing scene unchanged, and documenting the three target visual layers before editing an asset.
