# PrepFlow Visual Redesign Continuity — 2026-07-23

> **Updated 2026-07-24:** The three-book artwork milestone is complete, visually approved, and preserved in Git. The current local working copy contains a verified cleanup of the book CSS and selection-badge behavior that still needs its final test, commit, and two-remote synchronization before the next chat begins.

This document is the detailed handoff for the active visual redesign. Durable art rules now live in:

```text
docs/ART_SYSTEM.md
```

Durable technical ownership boundaries live in:

```text
docs/ARCHITECTURE_BIBLE.md
```

Current branch state and the exact next command belong in:

```text
docs/RESTART_PACKET.md
```

---

## 1. Active branch and protected milestones

Continue visual redesign work on:

```text
docs/continuity-rebuild
```

The stable production `master` branches remain separate until an intentional promotion.

Important preserved commits on the private branch:

```text
61851cd  checkpoint: preserve approved homepage book artwork
8960ccf  docs: add durable PrepFlow art system
41e3b03  docs: define visual asset ownership boundaries
```

At commit `61851cd`, the approved book artwork and preliminary runtime implementation were pushed to both `origin` and `public`, and all three branch hashes were verified equal.

The later documentation commits were created first on `origin`. The final milestone procedure must push the completed branch to both remotes and verify matching hashes again.

---

## 2. Completed and approved three-book milestone

The following runtime assets are approved:

```text
web/images/book-sprite-preview/prepflow-fundamentals-book.png
web/images/book-sprite-preview/prepflow-pharm-book.png
web/images/book-sprite-preview/prepflow-medsurg-book.png
```

Approved result:

- all three books use the locked v21 hardcover construction;
- all three are transparent 1024 × 1024 PNG masters;
- all three use smooth alpha and normal browser image smoothing;
- all three use the corrected page-grain direction;
- all three use the approved clean-border language;
- all three display at 256 CSS pixels in the current desktop composition;
- all three remain real `<button class="subject-card">` elements;
- all three open the correct chapter-selection screen;
- the complete book artwork is clickable;
- the obsolete always-visible `OPEN BOOK` ovals are gone;
- zero-selection badges are empty and hidden;
- selected-chapter state remains live HTML and JavaScript;
- question totals remain off the closed-book artwork.

The visible set was explicitly approved by Charlie on 2026-07-24.

Do not restore:

- CSS-drawn principal books;
- inline cover-emblem replacements;
- the Pharm-only prototype;
- native 256 hard-edge exports;
- braided multi-color borders;
- crosswise cover-to-cover page bands;
- baked question totals;
- always-visible `OPEN BOOK` labels.

---

## 3. Current local implementation state

Authoritative book presentation layer:

```text
web/approved-book-buttons.css
```

Current live state owner:

```text
web/app.js
```

Current local cleanup, verified visually but not yet committed at the time of this update:

- duplicate proof-sizing blocks were removed from `web/approved-book-buttons.css`;
- one production 256-pixel desktop rule remains;
- normal image smoothing remains explicit;
- temporary `.card-action` suppression experiments were removed;
- temporary DOM-removal code was removed from `web/app.js`;
- obsolete `.card-action` update logic was removed;
- zero-count `.book-selected-count` badges remain empty;
- `.book-selected-count:empty` hides the badge;
- temporary cache labels were consolidated into one book-milestone version;
- `git diff --check` passed after removing the extra blank line at the end of `web/pixel-home.css`.

The local browser was inspected after cleanup and remained visually correct.

Do not overwrite these local uncommitted cleanup changes with the earlier checkpoint versions before the final cleanup commit is made.

---

## 4. Visual ownership and production authority

Read `docs/ART_SYSTEM.md` before producing or changing any book, nurse, character, prop, background, or illustrated sprite.

Current ownership summary:

- background plate = static environment artwork;
- nurses = future separate transparent raster sprites;
- books = separate transparent clickable artwork;
- live counts and selection state = HTML and JavaScript;
- placement, sizing, responsive behavior, hover, focus, and state presentation = CSS.

Permanent artwork may contain permanent identity such as subject titles, icons, and permanent PrepFlow branding.

Changing application information must remain outside artwork.

---

## 5. Current background and nurse state

Current reference asset:

```text
web/images/pixel-home-stage.webp
```

This image presently contains both the sunset-city environment and the two nurses.

It is the approved visual reference, but it is not the final ownership structure.

The next art milestone must separate:

1. a background-only static environment plate;
2. the female nurse as a transparent sprite;
3. the male nurse as a transparent sprite.

The rebuilt assets must preserve:

- recognizable character identity;
- proportions;
- clothing and stethoscopes;
- palette;
- lighting direction;
- apparent scale;
- approved composition;
- PrepFlow Illustrated Pixel rendering language.

Separate pose files should be used first. Do not create a sprite sheet unless runtime animation later justifies it.

Do not regenerate or flatten the entire PrepFlow scene when working on one isolated asset.

---

## 6. Responsive composition rule

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

---

## 7. Local browser workflow

Canonical server command:

```bash
cd ~/projects/prepflow && python3 -m http.server 8004
```

Canonical URL:

```text
http://localhost:8004/web/
```

The server must run from the project root, not from `web/`, because the sibling `packs/` directory must be served.

Hard refresh:

```text
Ctrl+Shift+R
```

### Verified troubleshooting sequence

Before changing code during a display problem:

1. confirm a Python server is actually running;
2. confirm the server process working directory;
3. open the target runtime asset directly by URL;
4. compare the direct asset with the homepage;
5. inspect the live DOM element with DevTools;
6. inspect pseudo-elements and dynamically inserted children;
7. only then diagnose the CSS cascade, cache, or service worker.

A clean diagnostic origin may use:

```bash
cd ~/projects/prepflow && python3 -m http.server 8005
```

Diagnostic URL:

```text
http://localhost:8005/web/
```

Port 8005 bypasses the old 8004 browser origin and was used to verify the current files without the prior origin cache. It is not the canonical project port.

### Lesson from the `OPEN BOOK` diagnosis

The visible ovals were not baked into the background and were not `.card-action` elements.

The actual live element was:

```html
<span class="book-selected-count">Open book</span>
```

The correct fix was to leave the badge empty when zero chapters are selected, not to stack more CSS suppression rules.

When troubleshooting becomes repetitive, stop guessing and inspect the actual rendered DOM.

---

## 8. Local-first and GitHub workflow

During visual iteration, the local repository is the working source of truth.

GitHub is used to:

- inspect the last committed baseline;
- preserve a verified checkpoint;
- perform large documentation rewrites when that avoids fragile terminal heredocs;
- synchronize after local verification;
- verify remote branch hashes.

For multi-file application changes, inspect the actual local working copy rather than reconstructing it from repeated snippets.

For large documentation changes, prefer the GitHub connector and then use one short local pull command.

Do not ask Charlie to paste hundreds of lines into an interactive terminal heredoc when a connector update is available.

---

## 9. Command-flow preference

- Give one executable step at a time.
- When Charlie says `next`, continue to the next step rather than repeating the prior command.
- Ask for terminal output only when the next decision depends on it.
- Keep Python-server commands separate from ordinary terminal commands.
- Do not use `Ctrl+K, then S` as a required save step for files written directly by terminal scripts.
- Explain whether an asset is a rough study, a review proof, or a usable runtime asset.

---

## 10. Exact remaining work before the new chat

The books are designed and protected. Do not start the nurse/background rebuild yet.

Complete this forensic closeout first:

1. update `docs/RESTART_PACKET.md` with the current branch, commits, local cleanup state, localhost lessons, and exact next-session instruction;
2. update the dated visual handoff and durable docs so they agree;
3. review `git status --short` and the focused diff;
4. ensure timestamped backups and proof files remain untracked and unstaged;
5. run the existing automated tests;
6. verify the cleaned homepage at full width and reduced width;
7. verify each book still opens the correct chapter screen;
8. verify selected-chapter badges still appear only for actual selections;
9. commit the production cleanup and final handoff documentation;
10. push `docs/continuity-rebuild` to both `origin` and `public`;
11. fetch both remotes and verify local, origin, and public hashes match;
12. begin the next chat from the updated restart packet.

---

## 11. Exact next visual milestone after closeout

> Rebuild the current home scene as a background-only plate plus two separate transparent nurse sprites while preserving the approved character designs, sunset-city setting, proportions, lighting, pixel density, and current book composition.

Start that milestone by inspecting the approved current scene and documenting the target layer boundaries before editing or generating any asset.

Do not redesign the books during the nurse/background milestone.
