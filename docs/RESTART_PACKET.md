# PrepFlow Restart Packet

This document is a quick project briefing used to begin a new ChatGPT session.

The repository documentation is the source of truth.

---

## Project

PrepFlow

Version: 0.6.0

Current Sprint:
Sprint 6 — Pack Validation

Status:
Active Development

---

## Read These First

1. PROJECT_STATE.md
2. CHANGELOG.md
3. VISION.md

These documents are the authoritative project state.

---

## Current Objective

Continue improving the Pack Validation system.

Current priorities:

- Improve compiler validation reporting
- Improve compiler output
- Continue parser robustness improvements
- Add compiler success summary
- Continue pack integrity verification

---

## Resume Coding Here

Primary file:

```
compiler/validator.py
```

Secondary file:

```
compiler/cli.py
```

---

## Current State

Completed:

- Validator crash fixed (`set()` bug).
- Duplicate question reporting improved.
- Validation output grouped by question.
- Duplicate question numbers identify the original conflicting question.
- Compiler validation reporting improvements committed and pushed to GitHub.

Repository status:

- Working tree should be clean before new work begins.

---

## Startup Checklist

Verify repository:

```bash
git status
```

Run compiler:

```bash
python -m compiler.cli "cardiac questions.docx"
```

If validation fails:

- Fix reported problems.
- Re-run compiler.
- Repeat until clean.

---

## Development Workflow

For every completed milestone:

1. Verify compiler.
2. Verify `git status`.
3. Commit.
4. Push to GitHub.
5. Update:
   - CHANGELOG.md
   - PROJECT_STATE.md
6. Regenerate this RESTART_PACKET.md.

---

## Important Rule

Repository documentation is always the source of truth.

If this packet ever disagrees with the documentation, trust the documentation.