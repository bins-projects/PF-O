# PrepFlow Visual Redesign Continuity — 2026-07-23

> **Updated 2026-07-24 after public release:** The approved three-book milestone is complete, tested, released publicly, and preserved as a fixed source snapshot. Active visual development now moves to separating the background and nurses while public production remains on the released book milestone.

Durable visual rules:

```text
docs/ART_SYSTEM.md
```

Current release record:

```text
docs/RELEASE_2026-07-24_BOOK_MILESTONE.md
```

Current branch and resume authority:

```text
docs/RESTART_PACKET.md
```

---

## 1. Release boundary

The released visual source snapshot is:

```text
648bcfbf218b11b7786bdb4cd42f5a596e7b4f58
```

Frozen release branch:

```text
release/2026-07-24-book-milestone
```

That release branch exists in both:

```text
bins-projects/prepflow-dev
bins-projects/PrepFlow
```

Public production was promoted through:

```text
PR: bins-projects/PrepFlow#2
Public master merge commit: 8e8e85b1e9b9604d257b6db52e9bb802fcb91fce
Public site: https://bins-projects.github.io/PrepFlow/web/
```

The merge commit hash differs from the source snapshot because GitHub created a merge commit. The deployed source tree corresponds to `648bcfb`.

Charlie opened the public site after deployment and confirmed that it looked great.

Daily work continues on:

```text
Local repository: ~/projects/prepflow
Branch: docs/continuity-rebuild
```

The release branch is a frozen rollback and comparison point. Do not continue ordinary development on it.

---

## 2. Completed and publicly released three-book milestone

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
- all three use the corrected page-grain direction;
- all three use the approved clean-border language;
- all three display at 256 CSS pixels in the current desktop composition;
- all three remain real `<button class="subject-card">` elements;
- the complete artwork is clickable;
- each book opens the correct chapter-selection screen;
- zero-selection badges are empty and hidden;
- selected-chapter badges remain live HTML and JavaScript;
- question totals remain off the closed-book artwork;
- the obsolete always-visible `OPEN BOOK` ovals are gone;
- the three-book spacing and visual weight were approved.

Verification before release:

- `python -m pytest` completed with 72 passing tests;
- `git diff --check` passed before the cleanup commit;
- the real local browser was inspected;
- chapter-selection behavior was checked;
- both development remotes matched the approved source snapshot;
- the deployed public site was checked after release.

Do not restore:

- CSS-drawn principal books;
- inline cover-emblem replacements;
- the Pharm-only prototype;
- native-256 hard-edge exports;
- braided multi-color borders;
- crosswise cover-to-cover page bands;
- baked question totals;
- always-visible `OPEN BOOK` labels.

---

## 3. Current implementation ownership

Authoritative book presentation layer:

```text
web/approved-book-buttons.css
```

Live state owner:

```text
web/app.js
```

HTML and JavaScript own:

- real subject buttons;
- Pack paths;
- accessibility labels;
- chapter-opening behavior;
- selected-chapter state;
- live selected-count text.

CSS owns:

- placement;
- size;
- spacing;
- responsive behavior;
- hover, focus, active, and disabled presentation;
- visibility of empty badges.

Artwork owns only permanent visual identity such as the subject title, subject icon, book construction, and permanent color treatment.

Changing application information must not be baked into artwork.

---

## 4. Current background and nurse state

Approved combined reference:

```text
web/images/pixel-home-stage.webp
```

The image currently contains:

- the sunset-city environment;
- the female nurse;
- the male nurse.

It remains the approved composition reference but is not the final ownership structure.

The next milestone must create:

1. a background-only plate;
2. a transparent female nurse sprite;
3. a transparent male nurse sprite.

The original combined image must remain preserved and unchanged as a comparison reference.

The separated layers must preserve:

- recognizable nurse identity;
- face and hair character;
- body proportions;
- clothing and stethoscopes;
- palette relationships;
- apparent scale;
- upper-left lighting direction;
- the current sunset-city mood;
- the current relationship to the books;
- PrepFlow Illustrated Pixel rendering language.

Do not use the separation milestone as an excuse to redesign the nurses, books, city, or overall composition.

Separate pose files should be used before considering a sprite sheet.

Do not create a sprite sheet unless animation or repeated runtime state later justifies it.

---

## 5. Next milestone sequence

Work locally first.

Recommended sequence:

1. run the current homepage unchanged;
2. capture the approved full-width and reduced-width reference composition;
3. inspect the combined background image at native resolution;
4. define the exact layer boundaries for the environment, female nurse, and male nurse;
5. preserve the combined image as immutable reference artwork;
6. create the background-only plate without changing the city composition;
7. create the female nurse transparent sprite;
8. create the male nurse transparent sprite;
9. compose all three layers in the real application;
10. verify the books retain their current size, spacing, and click behavior;
11. verify full-width, reduced-width, reduced-height, and narrow layouts;
12. approve the base sprites before creating alternate poses;
13. commit and synchronize the milestone only after real-browser verification.

Do not begin by generating an entirely new scene.

Do not replace all layers at once without intermediate comparison proofs.

---

## 6. Responsive composition rule

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

Treat it as layout-only. It does not define permanent book or nurse artwork.

The complete scene must be evaluated as a composition. Do not independently resize unrelated elements across several files without comparing the whole page.

---

## 7. Local browser workflow

Canonical server:

```bash
cd ~/projects/prepflow && python3 -m http.server 8004
```

Canonical URL:

```text
http://localhost:8004/web/
```

The server must run from the project root so the sibling `packs/` directory is available.

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

Before changing code during a display problem:

1. confirm the server is running;
2. confirm its working directory;
3. open the target asset directly;
4. compare the direct asset with the homepage;
5. inspect the actual live DOM element;
6. inspect inserted children and pseudo-elements;
7. only then diagnose CSS, cache, or service-worker behavior.

The `OPEN BOOK` diagnosis proved that visible UI must be traced in the real DOM rather than inferred from old class names.

---

## 8. Public release workflow for later visual chunks

Visual development may continue privately and locally while the current public site remains stable.

When a new visual milestone is ready:

1. finish it on `docs/continuity-rebuild`;
2. run automated and browser verification;
3. synchronize both development remotes;
4. create a new fixed release branch from the approved commit;
5. open a release pull request into public `master`;
6. review the exact changed assets and runtime files;
7. merge only after approval;
8. verify the deployed public site;
9. record the new release boundary.

Do not move the existing `release/2026-07-24-book-milestone` branch.

---

## 9. Exact visual resume instruction

> Continue the PrepFlow visual redesign from the local repository at `~/projects/prepflow` on branch `docs/continuity-rebuild`. The approved three-book version is publicly deployed and frozen at source snapshot `648bcfb` with public `master` merge commit `8e8e85b`. Preserve `web/images/pixel-home-stage.webp` as the approved combined reference. Begin by defining the layer boundaries for a background-only plate plus separate female and male nurse sprites. Preserve the current nurse identities, city mood, lighting, scale, book composition, and PrepFlow Illustrated Pixel style. Work locally first, verify the real browser, give one executable step at a time, and release later work only as a separate tested milestone chunk.
