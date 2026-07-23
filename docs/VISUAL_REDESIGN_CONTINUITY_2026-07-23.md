# PrepFlow Visual Redesign Continuity — 2026-07-23

This document is the authoritative detailed handoff for the unfinished PrepFlow visual redesign. The current home screen is a working visual-development canvas, not a completed design and not technical debt to remove casually.

## Protected working canvas

```text
f393626  wip: checkpoint responsive home and sprite redesign
```

Continue redesign work only on `docs/continuity-rebuild` until the new visual system is intentionally approved and merged. The stable public version remains separate.

## Latest completed visual milestone

```text
e5ed054  fix: stabilize half-width home composition
```

Verified behavior after this milestone:

- the reduced-width launcher and reference panel no longer collide;
- the PrepFlow logo and tagline remain separated and readable;
- the background reaches the bottom of the reduced-height viewport without dead space;
- all three books remain inside the visible composition;
- full-width rendering was checked after the change and was not regressed;
- `git diff --check` passed;
- local and private branch hashes matched after push.

The temporary CSS-built book titles remain imperfect. Do not spend more time polishing those titles because the books are scheduled for raster-sprite replacement.

## Current redesign state

- The home terminal/launcher is dependable enough to use as the redesign canvas at full and reduced width.
- The first focused responsive-composition milestone is complete.
- The current CSS-built books and inline SVG emblems are exploratory placeholders, not the final asset system.
- The layered CSS files represent unfinished visual iterations. Do not remove them merely because they overlap.
- The current background and nurses still exist as one combined static image.
- A real transparent-raster Pharm book proof was successfully rendered inside the live app on 2026-07-23.
- The proof demonstrated that the CSS-built Pharm cover can be replaced by a real raster sprite while preserving live application elements.
- All temporary Pharm preview files were removed afterward. The last verified local status was clean and matched `origin/docs/continuity-rebuild`.

## Authoritative visual direction

- Preserve the current pixel-art sunset-city background style.
- Keep the approved sunset-city environment as the visual reference.
- Rebuild books and buttons as reusable pixel-art sprites rather than ordinary flat interface cards.
- Use Pharm as the first book-sprite prototype, then apply the approved system consistently to Fundamentals and Med-Surg.
- Establish one consistent book silhouette, spine, cover, page depth, emblem area, hover state, and selected state before producing all three variants.
- Establish reusable button styling with consistent normal, hover, pressed, disabled, and selected states.
- Do not generate, redraw, or flatten the complete PrepFlow scene when working on one book, button, character, or other isolated asset.

## Graphics production and file-format rule

Use transparent raster sprite assets for the principal illustrated pixel-art objects and characters.

Approved workflow:

1. Create and refine illustrated books, nurses, props, and similarly textured pixel-art assets as transparent PNG files during design and iteration.
2. After an asset is visually approved, an optimized transparent WebP version may be used in the shipped browser product when it preserves transparency, pixel fidelity, and intended appearance.
3. Reserve SVG for genuinely vector-like interface symbols, simple emblems, and clean scalable icons. Do not use SVG as the default format for textured illustrated books, nurses, or environment artwork.
4. Use CSS for positioning, sizing, responsive composition, hover/pressed/selected movement, glows, and state presentation. Do not use CSS gradients, pseudo-elements, or inline SVG to draw the principal final book or character artwork.
5. The current CSS-built books and inline SVG cover emblems are exploratory mockups only.
6. Pharm is the proof-of-concept sprite. Preview the real transparent raster book asset first, adjust crop/scale/placement, and do not treat temporary proof artwork as the final approved design.
7. Never substitute a generated full-screen screenshot or flattened scene for a transparent isolated sprite.

## Permanent artwork versus live application data

The artwork may contain permanent subject identity such as:

- `PHARM`;
- a capsule or medication emblem;
- permanent PrepFlow branding when it belongs to the book design.

Changing library and application data must remain outside the artwork as live HTML. This includes:

- chapter-selection status;
- button labels;
- accessibility text;
- changing counts or progress;
- data attributes and click behavior.

### Closed-book question-count decision

Do **not** display total question counts on the closed books on the home screen.

Reasoning:

- users choose a book by subject, not by which Pack has the largest total;
- totals clutter the artwork and compete with the visual hierarchy;
- the information is more useful after the book is opened.

Show relevant totals inside the opened book/chapter-selection experience instead. The live chapter-selection status may remain beneath or near each closed book.

The temporary Pharm proof recovered during the 2026-07-23 session had `1,238 QUESTIONS` baked into the image. That proof is useful only for layout testing. The next Pharm asset must remove that baked-in count.

## Pharm proof result and asset warning

The raster proof was successfully displayed in the real app. It confirmed the intended technical approach, but it is **not** the final-quality source sprite.

Important limitations of that proof:

- it was recovered from a prior visual preview rather than from the original transparent source artwork;
- its first recovery crop was incomplete and was replaced by a more complete crop;
- it still contains a baked-in question count that must be removed;
- its crop, transparency edges, scale, placement, and final art treatment still require refinement;
- it must not be treated as the final approved Pharm asset.

Do not ask Charlie to recreate this technical distinction manually. Prepare and verify the complete asset package before requesting a local placement step.

## Background and nurse assets

The currently approved home image contains both nurses and the sunset background in one static asset:

```text
web/images/pixel-home-stage.webp
```

Treat that image as the approved reference and do not casually regenerate, crop, substitute, or replace it.

Future asset work should separate:

1. the environment/background;
2. any lower environment extension or foreground needed for future compositions;
3. reusable nurse character sprites.

The two nurses should retain consistent designs, proportions, palette, and pixel density while supporting different poses for different screens, such as home, studying, reference library, and quiz completion.

## Responsive composition rule

Do not solve scaling by independently adjusting unrelated pieces across several files without checking the complete composition. The final responsive system should use:

- one clear home-scene container;
- one approved desktop reference composition;
- proportional positioning inside that composition;
- a small number of intentional breakpoints;
- minimum readable sizes for live text and controls;
- deliberate reflow at narrow widths rather than accidental transform conflicts.

The focused reduced-width authority currently lives in:

```text
web/half-width-composition.css
```

Treat it as a layout-only layer. Do not use it to establish permanent book artwork or final book typography.

## Local browser-preview workflow

Run the local server from its own dedicated terminal:

```bash
cd ~/projects/prepflow && python3 -m http.server 8004
```

Leave that terminal running while previewing. The server terminal printing a request log during page loads and hard refreshes is normal.

Open:

```text
http://localhost:8004/web/
```

Use `Ctrl+Shift+R` for a hard refresh after visual changes.

Before diagnosing CSS, image, or cache behavior, verify the server is actually running and serving the current project. Do not assume the service worker is responsible. The current `web/sw.js` uses a network-first fetch strategy.

## Command-flow preference

- When Charlie says `next`, treat the previous paste command as completed and continue to the next executable step.
- Do not repeat the previous command.
- When terminal output is genuinely required, say clearly: `Paste the output here before continuing.`
- Ordinary commands should be introduced with `Paste this`.
- Identify the Python-server terminal only when a command must run there.

## Change-control rules

- Do not disable, delete, consolidate, or reinterpret an existing visual layer solely because the CSS cascade is layered.
- Before removing an experimental layer, identify what visual decision it represents and compare the rendered result.
- Capture baseline screenshots before meaningful visual changes.
- Make one isolated visual change at a time.
- Verify full-window and reduced-window behavior after every change.
- Do not perform final CSS cleanup until the responsive composition, books, buttons, and reusable asset strategy are approved.
- Never claim a preview, test, server state, cleanup, or approval that was not verified.
- Stop and reassess when troubleshooting becomes repetitive rather than stacking additional guesses.
- Future chats must treat Charlie's explicit design corrections in this document as authoritative unless newer committed evidence replaces them.

## Exact next visual milestone

Create or recover a proper transparent Pharm book sprite derived from the approved proof direction, but without the baked-in question count, then preview only that isolated asset in the live app.

Required sequence:

1. begin from the clean `docs/continuity-rebuild` branch;
2. verify `git status --short --branch` and current remote synchronization;
3. read this document in full before giving a visual command;
4. start and verify the local server from `~/projects/prepflow` on port `8004`;
5. prepare the complete isolated transparent Pharm sprite outside the app first;
6. verify that the sprite is complete, has usable transparency, contains no question total, and does not include any flattened scene/background;
7. inspect the committed Pharm card HTML and click behavior through GitHub;
8. place only the Pharm raster sprite under a clear reusable asset path;
9. preserve live chapter-selection status, accessibility, data attributes, and click behavior;
10. use CSS only for scale, placement, hover/selected motion, and responsive behavior;
11. preview at full and reduced width;
12. obtain Charlie's visual approval before committing the asset or applying the pattern to Fundamentals and Med-Surg.

Do not begin by regenerating the whole scene, polishing temporary vertical title CSS, redrawing the book with CSS, redesigning all three books, consolidating visual stylesheets, or separating the nurses from the background.

## Recommended continuation order

1. Finalize the Pharm book sprite as the reusable book pattern.
2. Apply the approved pattern to Fundamentals and Med-Surg.
3. Finalize reusable pixel-art button styling.
4. Reassess the background-extension and environment-layer strategy using the stable canvas.
5. Separate the background and nurses into reusable assets while preserving the approved character designs.
6. Create pose variants for other screens.
7. Test desktop, reduced-width, reduced-height, and narrow layouts.
8. Consolidate obsolete experimental CSS only after visual approval.
