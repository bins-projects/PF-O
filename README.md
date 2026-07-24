# PrepFlow

PrepFlow is a browser-based nursing study application built around organized question Packs.

It lets you choose chapters, answer one question at a time, review the correct answer and rationale, and repeat missed questions until they are mastered.

## Open PrepFlow

[Open PrepFlow in your browser](https://bins-projects.github.io/PrepFlow/web/)

No account is required. Study progress is stored locally in the browser on the device being used.

Clearing browser or site data may remove a saved session. A session saved in one browser or device does not automatically appear in another.

## Install as an App

PrepFlow can be installed from a supported browser so it opens in its own window.

### Chromebook or Chrome

1. Open PrepFlow in Chrome.
2. Select the install icon in the address bar.
3. Choose **Install**.
4. Open PrepFlow from the device launcher.

### Mac with Safari

1. Open PrepFlow in Safari.
2. Choose **File** and then **Add to Dock**.
3. Name it **PrepFlow** and select **Add**.
4. Open it from the Dock, Applications, or Spotlight.

## How to Study

1. Choose a study category.
2. Select one or more chapters.
3. Add chapters from another category when needed.
4. Choose a block size.
5. Start the quiz.
6. Submit each answer and review the feedback.
7. Complete the block.
8. Repeat missed questions until they are mastered.

PrepFlow automatically saves an unfinished session in one local save slot so it can be resumed later.

## Study Library

PrepFlow currently includes:

- Fundamentals
- Pharm
- Medical-Surgical

## Question Types

The PrepFlow library contains:

- Multiple Choice
- Multiple Response
- Completion
- Ordered Response

Browser support for individual question types may evolve as the active study interface is improved.

## Study Behavior

During a session, PrepFlow:

- presents one question at a time;
- gives immediate Correct or Incorrect feedback;
- shows the correct answer and rationale;
- tracks first-pass performance;
- places missed questions into a review queue;
- repeats missed questions until answered correctly;
- displays final first-pass results after the session is complete.

Selected questions currently use one stable shuffled order for the session.

## Project Direction

PrepFlow also includes a compiler that turns deliberately selected educational source material into cleaned, structured, validated Packs.

The browser application is the active user-facing product. Future downloadable editions should reuse the browser-centered application rather than maintain a separate study system.

Internal architecture and development continuity are documented under `docs/`.
