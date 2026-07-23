# PrepFlow Restart Handoff — July 23, 2026

## Authoritative branch
Continue development from `docs/continuity-rebuild`, not `master`.

Verified branch state before this documentation update:
- Local: `a3664ea`
- Private remote: `a3664ea`
- Public remote: `a3664ea`
- Tests: 72 passed
- Browser app verified locally
- Fundamentals, Pharm, and Medical-Surgical book buttons work

Production remains intentionally unchanged:
- `master`
- `origin/master`
- `public/master`
- Commit: `8987fdf`

The public-facing website therefore still shows the older production version.

## Required workflow
Use the local repository as the working source:
1. Inspect local files.
2. Make one focused change.
3. Test.
4. Commit.
5. Push the current branch to both `origin` and `public`.
6. Verify all three hashes match.

Do not cherry-pick only the final book-button commit onto old `master`.
Do not promote the continuity branch to production without a deliberate release review.

## New-chat starter
Paste this into a new ChatGPT chat:

We are continuing PrepFlow from `~/projects/prepflow`. The authoritative branch is `docs/continuity-rebuild`, not `master`. Read `docs/FINAL_HANDOFF_2026-07-23.md` and `docs/RESTART_PACKET.md` first. The rebuilt branch passed 72 tests, works locally, and is backed up to both remotes. Production master remains unchanged at `8987fdf`. Follow the local-first workflow and give me one executable step at a time.

## Terminal restart command
`cd ~/projects/prepflow && git switch docs/continuity-rebuild && git fetch origin && git fetch public && git status`
