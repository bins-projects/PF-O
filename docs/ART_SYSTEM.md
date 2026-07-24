# PREPFLOW ART SYSTEM

> Durable authority for PrepFlow artwork, visual ownership, production formats, and approved rendering rules. Current branch state, localhost state, and the next executable task belong in `docs/RESTART_PACKET.md`.

---

# 1. Visual Identity

PrepFlow uses the visual language **PrepFlow Illustrated Pixel**.

This is modern illustrated pixel art, not chunky retro pixel art.

Core principles:

- use crisp, intentional forms rather than random pixel noise;
- build assets from broad readable color and shadow masses before adding detail;
- use dark palette-related outlines rather than pure black everywhere;
- reserve the strongest contrast for interactive assets and characters;
- use moderate contrast for supporting props;
- keep backgrounds quieter so controls and characters remain readable;
- use selective material texture rather than equally dense texture everywhere;
- preserve approved supplied artwork and vector paths rather than recreating them unnecessarily.

The viewpoint is chosen per asset. Books may use a three-quarter view, people may face or turn naturally, tools should use the clearest readable angle, and environments should follow coherent scene perspective. There is no universal three-quarter-camera rule.

---

# 2. Visual Ownership Boundaries

The home scene is divided into separate layers with separate responsibilities.

## 2.1 Background plate

The background plate owns:

- environment;
- skyline;
- sunset;
- room or platform architecture;
- static environmental lighting;
- noninteractive scenery.

It must not own:

- nurses;
- books;
- chapter counts;
- selection state;
- buttons;
- dynamic text;
- progress;
- changing application data.

Current reference asset:

```text
web/images/pixel-home-stage.webp
```

That file presently includes the nurses and remains the approved visual reference until the background-and-nurse separation milestone is completed. The next background milestone must create a background-only plate while preserving the approved setting and composition.

## 2.2 Nurse sprites

Nurses must become separate transparent raster assets.

Nurse sprites own:

- character design;
- clothing;
- pose;
- facial expression;
- character-specific shading;
- character-specific props permanently attached to that pose.

Nurse sprites must not be permanently baked into the rebuilt background plate.

The nurses should retain consistent identity, proportions, palette, rendering density, outline language, lighting direction, and apparent scale. Use separate pose files initially. A sprite sheet is not required until animation or repeated runtime use justifies it.

## 2.3 Book assets

Books are separate transparent clickable artwork.

Runtime files:

```text
web/images/book-sprite-preview/prepflow-fundamentals-book.png
web/images/book-sprite-preview/prepflow-pharm-book.png
web/images/book-sprite-preview/prepflow-medsurg-book.png
```

Books own:

- permanent subject title;
- permanent cover color;
- permanent cover icon;
- permanent PrepFlow branding;
- cover, spine, pages, tabs, and material rendering.

Books do not own:

- question totals;
- chapter-selection counts;
- accessibility text;
- Pack paths;
- click behavior;
- disabled state;
- hover movement;
- focus rings;
- changing status text.

## 2.4 HTML and JavaScript

HTML and JavaScript own:

- subject buttons;
- Pack paths;
- accessibility labels;
- live chapter-selection state;
- selected chapter counts;
- saved-session state;
- button enable/disable behavior;
- click behavior;
- opened-book state;
- quiz and progress data.

A zero-selection book badge must remain empty and hidden. A selected-chapter badge may appear only when one or more chapters are selected.

## 2.5 CSS

CSS owns:

- placement;
- display size;
- equal spacing;
- responsive layout;
- hover movement;
- pressed state;
- disabled presentation;
- focus presentation;
- glow;
- drop shadow;
- dynamic badge placement.

CSS must not redraw principal final book or nurse artwork with gradients, pseudo-elements, or replacement illustrations.

Current authoritative book presentation layer:

```text
web/approved-book-buttons.css
```

---

# 3. Artwork and Live Data

Permanent artwork may contain permanent identity, including subject titles, subject icons, and permanent PrepFlow branding.

Changing application information remains live HTML and JavaScript, including question totals, selected chapter counts, progress, button instructions, saved-session state, accessibility labels, Pack paths, and quiz scores.

Do not bake total question counts into closed home-screen books. Relevant totals belong inside the opened chapter-selection experience.

---

# 4. Production Formats

## 4.1 Transparent illustrated assets

Use transparent PNG masters during design and approval for books, nurses, illustrated props, textured foreground objects, and similar detailed sprites.

An optimized transparent WebP derivative may be used after approval when it preserves transparency, edge fidelity, color fidelity, and intended appearance.

## 4.2 SVG

Use SVG for clean interface symbols, simple scalable icons, approved cover emblems, and diagrams or line symbols that benefit from preserved paths.

Do not use SVG as the default final format for textured illustrated books, nurses, or environment artwork. Preserve approved SVG paths when supplied.

## 4.3 Background plates

Use an optimized static WebP for a completed background plate when visual fidelity remains acceptable. Keep an editable source master outside the runtime folder.

## 4.4 Dynamic interface elements

Use HTML and CSS for dynamic text, controls, status, and layout. Do not flatten dynamic application information into screenshots or background artwork.

---

# 5. Asset Folder Roles

Runtime browser assets belong under:

```text
web/images/
```

Current book runtime location:

```text
web/images/book-sprite-preview/
```

Future repository organization should distinguish:

```text
art/source/
```

Editable masters, preserved SVG paths, construction sources, and approved source artwork.

```text
art/review/
```

Temporary comparisons, proof renders, enlarged inspections, and visual review images.

```text
web/images/
```

Only approved runtime exports actually used by the browser.

Temporary ZIP installers, timestamped backups, screenshots, superseded proofs, and comparison images must not become permanent runtime assets. Generated transfer files may remain local under ignored working locations.

---

# 6. Approved Book System

## 6.1 Construction lock

The approved hardcover construction is the v21 geometry.

Required geometry:

- visible front cover;
- visible back cover;
- full-depth continuous spine panel;
- visible page block;
- visible back-cover underside;
- all planes meet clearly;
- page block enters the spine and follows perspective;
- rear hinge remains hidden behind the page block;
- spine bottom edge runs from the true lower outer front-cover corner to the true lower outer back-cover corner;
- no floor shadow is baked into the transparent book asset.

This construction applies to all three subject books.

## 6.2 Tabs

Each book has three tabs. They are vertically separated, aligned with page perspective, and placed approximately 20%, 50%, and 80% through page-block depth.

## 6.3 Rendering master

Approved production rule:

- transparent PNG master;
- 1024 × 1024 pixels;
- smooth alpha;
- no hard alpha threshold;
- no tiny-palette final quantization;
- no dithering or scattered speckling;
- normal browser image smoothing.

Desktop display rule:

```text
256 CSS pixels
```

The current 256-pixel desktop size is approved for the present composition. Responsive sizes may change deliberately after full-composition testing.

## 6.4 Borders

Use one strong dark outer silhouette, one primary gold or cream cover border, and at most one quiet secondary inset border.

Do not use several alternating colored diagonal lines. Parallel colored outlines create a braided appearance and are prohibited.

## 6.5 Page grain

The visible page edges must behave like pages.

Fore-edge grain:

- many fine restrained lines;
- lines run lengthwise from top toward bottom;
- lines are distributed through page-block thickness.

Bottom-edge grain:

- many fine restrained lines;
- lines run from spine toward fore-edge;
- lines are distributed through page-block thickness.

Do not use a few crosswise bands running from cover to cover.

## 6.6 Subject locks

### Fundamentals

- title: `FUNDAMENTALS`;
- blue cover family;
- approved chart/clipboard SVG path;
- shared vertical title-strip system.

### Pharm

- title: `PHARM`;
- green cover family;
- approved capsule artwork;
- shared vertical title-strip system;
- established the approved smooth-edge and corrected-page-grain recipe.

### Med-Surg

- title: `MED-SURG`;
- purple cover family;
- approved stethoscope SVG path;
- deeper silver-lavender icon panel;
- shared vertical title-strip system.

---

# 7. Homepage Composition

The current homepage uses one static scene plate, separate transparent book buttons, live HTML/CSS launcher controls, live chapter-selection badges, and nurses still baked into the current reference plate pending separation.

Books must remain evenly spaced. The complete transparent book is the clickable button.

Do not place an always-visible `OPEN BOOK` oval over each book. A chapter-selection badge should appear only when it communicates actual selected state.

The book art should remain visually subordinate to the main logo and nurses but prominent enough to read as the primary subject choices.

---

# 8. Asset Development Workflow

For one isolated asset:

1. inspect the current runtime asset and scene;
2. identify the exact decision being tested;
3. preserve locked geometry and approved source artwork;
4. create a rough proof only when needed;
5. state whether the proof is a study or usable runtime asset;
6. compare it at actual application size;
7. test it in the real local application;
8. obtain explicit visual approval;
9. export the approved runtime asset;
10. document the lock;
11. commit and push only after verification.

Do not regenerate or flatten the complete PrepFlow scene when changing one isolated asset. Do not produce all related assets before the first representative asset establishes the rendering recipe.

---

# 9. Local Visual Verification

Run the local server from the project root:

```bash
cd ~/projects/prepflow && python3 -m http.server 8004
```

Canonical preview:

```text
http://localhost:8004/web/
```

The server must run from `~/projects/prepflow`, not `~/projects/prepflow/web`, because the sibling `packs/` directory must also be served.

Use `Ctrl+Shift+R` for a hard refresh.

Before changing CSS or artwork during a display problem:

1. verify a server process is running;
2. verify its working directory;
3. open the target image directly by URL;
4. compare the direct asset with the homepage;
5. inspect the actual live DOM element;
6. inspect pseudo-elements and generated children;
7. only then diagnose caching or the service worker.

A clean diagnostic origin may use:

```text
http://localhost:8005/web/
```

Port 8005 is a troubleshooting origin, not the canonical project URL.

---

# 10. Decision Status Language

Documentation must distinguish:

## Implemented and approved

Present in the real local application and explicitly approved.

## Approved but not implemented

A decided direction that still requires production work.

## Experimental

A temporary proof or local test that is not a permanent rule.

## Superseded

An earlier proof, workflow, or design that must not be restored.

Temporary experiments do not become permanent architecture merely because they exist in Git history or local backups.

---

# 11. Current Status

## Implemented and approved

- three transparent 1024 × 1024 subject-book PNG masters;
- v21 construction across all three books;
- corrected page-grain direction;
- smooth-edge rendering;
- clean-border language;
- 256-pixel desktop display;
- equal spacing;
- transparent clickable button structure;
- zero-selection badges hidden;
- selected chapter state retained as live application data.

## Approved but not implemented

- background-only static plate;
- nurses separated into transparent sprites;
- reusable nurse pose variants;
- permanent source/review/export art folders if not yet created.

## Superseded

- CSS-drawn principal books;
- inline cover-emblem replacement artwork;
- Pharm-only prototype milestone;
- native 256 hard-edge book export;
- hard alpha threshold;
- tiny-palette quantization;
- braided multi-color outlines;
- crosswise cover-to-cover page bands;
- always-visible `OPEN BOOK` ovals;
- baked closed-book question totals.

---

# 12. Change Control

Update this document whenever a durable art, asset-ownership, rendering, format, or folder rule changes.

Do not place temporary branch status, current commit hashes, or the next executable task here. Those belong in `docs/RESTART_PACKET.md`.

When a newer approved decision replaces an older rule, update this document to reflect current truth and mark the old approach superseded where historical confusion is likely.
