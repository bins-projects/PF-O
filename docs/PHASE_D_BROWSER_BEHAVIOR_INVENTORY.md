# Phase D Browser Behavior Inventory

## Scope

This inventory reviews `web/app.js` to identify the smallest safe boundary between quiz/session rules and browser DOM behavior.

No browser behavior is changed by this document.

## Current behavior areas

### Already pure or nearly pure

- `shuffle(items)`
- `normalizedCorrectAnswers(question)`
- `isMultipleResponseQuestion(question)`
- answer comparison currently embedded in the Submit Answer handler

### State-dependent quiz rules

- current question reference selection
- question resolution by permanent ID
- block start and end calculation
- first-pass correct and missed tracking
- missed-question queue creation
- review-until-mastered behavior
- next-block and final-summary transitions
- save/resume state restoration

### DOM and presentation behavior

- showing and hiding screens
- rendering answer controls
- progress and score labels
- feedback and rationale display
- chapter-selection controls
- button event handling

## Smallest safe first extraction

Extract answer evaluation into a pure browser rule such as:

```javascript
evaluateAnswer(question, selectedAnswers)
```

The function should return structured information such as:

```javascript
{
  isCorrect,
  correctAnswers
}
```

It should own:

- normalization of stored correct answers;
- normalization of selected answers;
- exact-set comparison for Multiple Response;
- ordinary single-answer comparison for Multiple Choice.

It must not own:

- DOM updates;
- score counter changes;
- missed-question queue changes;
- review transitions;
- save/resume behavior;
- rationale display.

## Required test cases

1. correct single-answer selection;
2. incorrect single-answer selection;
3. correct Multiple Response selection in a different order;
4. Multiple Response with one answer missing;
5. Multiple Response with an extra answer selected;
6. lowercase or whitespace-normalized answer values;
7. `correct_answer` singular field;
8. `correct_answers` array field.

## Verification gate

The visible browser flow must remain unchanged:

- quiz starts normally;
- Multiple Choice grading remains correct;
- Multiple Response requires the exact answer set;
- first-pass counters remain correct;
- missed questions still enter review;
- review continues until mastered;
- save/quit and resume still work.

## Test infrastructure finding

The repository currently has no established JavaScript test runner, and Node.js is not installed in the local Linux environment.

The implementation milestone should therefore include the smallest practical browser-centered test harness rather than introducing a large frontend toolchain.

## Proposed first implementation milestone

1. add a small pure quiz-rules module;
2. move answer normalization and comparison into it;
3. call it from the existing Submit Answer handler;
4. add focused browser-native tests for the cases above;
5. run the existing 72 Python tests;
6. repeat the real browser smoke test;
7. commit and push as one coherent milestone.
