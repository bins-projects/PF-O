# PrepFlow Public Release — 2026-07-24 Book Milestone

## Release identity

This document records the first public deployment of the continuity-rebuild browser version after the approved three-book homepage milestone.

```text
Release source snapshot: 648bcfbf218b11b7786bdb4cd42f5a596e7b4f58
Public release branch: release/2026-07-24-book-milestone
Public production merge commit: 8e8e85b1e9b9604d257b6db52e9bb802fcb91fce
Public pull request: bins-projects/PrepFlow#2
Public site: https://bins-projects.github.io/PrepFlow/web/
Release date: 2026-07-24
```

The release branch exists in both repositories:

```text
bins-projects/prepflow-dev
bins-projects/PrepFlow
```

Both release branches point to the exact tested source snapshot `648bcfb`.

The public `master` hash differs because GitHub created merge commit `8e8e85b` when pull request #2 was merged. The deployed source tree for this release is the tree from `648bcfb`.

## What was released

- the browser-centered PrepFlow application;
- the current Fundamentals, Pharm, and Medical-Surgical Packs;
- the approved three-book homepage artwork;
- the cleaned transparent book-button implementation;
- responsive home composition work completed through the book milestone;
- hidden zero-selection badges and retained real selected-chapter badges;
- current quiz, review, save/resume, selection, ordering, summary, and navigation behavior;
- the continuity-rebuild architecture and current public README.

## Verification completed before release

- `python -m pytest` completed with all 72 tests passing;
- `git diff --check` passed before the cleanup commit;
- the homepage was inspected in the real local browser;
- all three books opened their corresponding chapter-selection screens;
- zero-selection badges remained hidden;
- the approved artwork and spacing were visually accepted by Charlie;
- local, private-development, and public-mirror development branches matched before release;
- the public site was opened after deployment and Charlie confirmed that it looked great.

## Development continues separately

The release is a stable snapshot, not the branch used for daily work.

Active development continues from:

```text
Local repository: ~/projects/prepflow
Active branch: docs/continuity-rebuild
Private development remote: bins-projects/prepflow-dev
Public mirror branch: bins-projects/PrepFlow — docs/continuity-rebuild
```

The local repository is the active working copy. Visual changes are built and checked locally before they are committed or released.

The active development branch is expected to move ahead of the release snapshot. Public `master` should move only through an intentional, tested release promotion.

## Chunked release policy

Future public updates should follow this pattern:

1. finish one coherent milestone on `docs/continuity-rebuild`;
2. run applicable automated tests;
3. inspect the real local browser behavior and layout;
4. commit and synchronize the development branch;
5. create a fixed release branch from the approved development commit;
6. open a release pull request into public `master`;
7. review the exact release scope;
8. merge only after verification;
9. verify the public GitHub Pages site;
10. record the release boundary in continuity documentation.

This allows PrepFlow to receive useful public improvements in chunks while unfinished work remains behind the scenes.

## Rollback reference

For this release, the stable source snapshot is permanently identifiable as:

```text
release/2026-07-24-book-milestone
648bcfbf218b11b7786bdb4cd42f5a596e7b4f58
```

Do not move or reuse that release branch for later work.
