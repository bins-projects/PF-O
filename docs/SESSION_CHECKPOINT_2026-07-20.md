# PrepFlow Session Checkpoint — 2026-07-20

This is a temporary operational checkpoint for the next development session. The durable architectural authorities remain `docs/ARCHITECTURE_BIBLE.md`, `docs/RESTART_PACKET.md`, and `docs/CONTINUITY_REBUILD_PLAN.md`.

## Verified branch state

- Repository: `bins-projects/prepflow-dev`
- Branch: `docs/continuity-rebuild`
- Current verified head before this checkpoint: `f414d80`
- Local branch matched `origin/docs/continuity-rebuild`.
- Working tree was clean.

## Completed this session

1. Removed obsolete DOCX prototype and dependencies at `0ed062f`.
2. Removed legacy Python desktop, terminal, PyInstaller, and Windows-build stack at `3839243`.
3. Updated Restart Packet after cleanup at `7ad4dc4`.
4. Changed the compiler to preserve incoming question IDs and generate Pack-namespaced IDs for new questions. The implementation was completed through `f302c70`.
5. Migrated all three official Packs to globally unique IDs at `f414d80`.

## Permanent question ID state

Current ID format:

```text
PFQ-<pack_id>-<nine-digit sequence>
```

Examples:

```text
PFQ-fundamentals-000000001
PFQ-medical_surgical-000000001
PFQ-pharmacy-000000001
```

Compiler rules now implemented:

```text
Existing incoming ID → preserve it
No incoming ID       → generate a Pack-namespaced ID
```

Verified migration results:

- Fundamentals: 1,040 questions
- Medical-Surgical: 1,443 questions
- Pharmacy: 1,238 questions
- Total questions: 3,721
- Unique IDs: 3,721
- Missing IDs: none
- Cross-Pack collisions: none
- Only question ID fields changed during Pack migration
- Full Python suite: 72 passed

## Browser reference finding

The browser currently does not use question IDs for quiz references. It creates and saves references in this form:

```javascript
{
  packPath,
  questionIndex
}
```

`currentQuestion()` reloads the Pack and resolves the question with:

```javascript
pack.questions[reference.questionIndex]
```

The same reference objects are reused by:

- the shuffled session question list;
- missed-question tracking;
- the review queue;
- the current review question;
- local save/resume state.

Because PrepFlow is unreleased and only a few temporary local saves exist, backward compatibility with version-2 saved sessions is not required. Old saves may be intentionally rejected or cleared once.

## Exact next milestone

Replace browser question references from:

```text
packPath + questionIndex
```

to:

```text
packPath + questionId
```

The milestone must include:

1. create references with `questionId` in `startQuiz()`;
2. resolve questions by permanent ID rather than array position;
3. update missed/review/save references through the shared reference format;
4. bump saved-session version and deliberately reject or clear old version-2 saves;
5. run the 72-test Python suite;
6. perform a real browser smoke test covering quiz start, wrong answer, review, save/quit, and resume;
7. commit and push as one coherent milestone.

Estimated time: approximately 30–45 minutes. Do not start when there is not enough time to complete verification, commit, and push.

## Safe resume instruction

At the next session:

1. inspect this checkpoint in GitHub;
2. verify branch head and `git status`;
3. inspect the current `web/app.js` reference creation, resolution, and saved-session code;
4. make the browser reference migration as one focused milestone.

The pre-rebuild repository remains preserved by tag:

```text
before-continuity-rebuild-2026-07-20
```

## Update — 2026-07-21

### Browser permanent-reference migration completed

Completed at:

```text
e2ec845  refactor: use permanent question IDs in browser sessions
```

The browser now uses `packPath + questionId` references, resolves questions by permanent ID, saves version 3 sessions, and clears incompatible older saves.

Verification completed:

- `git diff --check` passed;
- all 72 Python tests passed;
- all 3,721 official Pack IDs are present and unique;
- real browser smoke test passed for quiz start, incorrect answer, review, save/quit, and resume;
- commit was pushed to and verified on `origin/docs/continuity-rebuild`.

### Exact next milestone

Begin Phase D with a read-only inventory of `web/app.js`.

Identify the smallest pure quiz/session behavior unit that can be extracted and tested without changing the visible browser flow. Do not begin a broad rewrite.
