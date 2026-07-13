const hero = document.querySelector(".hero");
const subjects = document.querySelector(".subjects");
const status = document.querySelector("#status");

const chapterScreen = document.querySelector("#chapter-screen");
const chapterTitle = document.querySelector("#chapter-title");
const chapterList = document.querySelector("#chapter-list");
const selectionCount = document.querySelector("#selection-count");
const startButton = document.querySelector("#start-button");
const blockSizeSelect = document.querySelector("#block-size");

const quizScreen = document.querySelector("#quiz-screen");
const quizSubject = document.querySelector("#quiz-subject");
const quizPosition = document.querySelector("#quiz-position");
const quizProgress = document.querySelector("#quiz-progress");
const questionStem = document.querySelector("#question-stem");
const answerChoices = document.querySelector("#answer-choices");
const feedback = document.querySelector("#feedback");
const feedbackResult = document.querySelector("#feedback-result");
const feedbackRationale = document.querySelector("#feedback-rationale");
const quizScore = document.querySelector("#quiz-score");
const submitAnswer = document.querySelector("#submit-answer");
const continueButton = document.querySelector("#continue-button");

let currentSubject = null;
let currentPack = null;
let sessionQuestions = [];
let sessionIndex = 0;
let correctCount = 0;
let missedCount = 0;
let sessionBlockSize = 15;

function shuffle(items) {
  const copy = [...items];

  for (let index = copy.length - 1; index > 0; index -= 1) {
    const randomIndex = Math.floor(Math.random() * (index + 1));
    [copy[index], copy[randomIndex]] = [copy[randomIndex], copy[index]];
  }

  return copy;
}

function updateSelectionStatus() {
  const selected = chapterList.querySelectorAll(
    'input[type="checkbox"]:checked'
  ).length;

  selectionCount.textContent =
    `${selected} ${selected === 1 ? "chapter" : "chapters"} selected`;

  startButton.disabled = selected === 0;
}

function showSubjects() {
  hero.hidden = false;
  subjects.hidden = false;
  chapterScreen.hidden = true;
  quizScreen.hidden = true;
  status.hidden = false;
  status.textContent = "Select a category to continue.";
}

async function showChapters(button) {
  status.textContent = "Loading chapters…";

  try {
    const response = await fetch(button.dataset.pack);

    if (!response.ok) {
      throw new Error(`Could not load study category: ${response.status}`);
    }

    currentPack = await response.json();
    currentSubject = button.dataset.subject;

    const chapters = new Map();

    currentPack.questions.forEach((question) => {
      const key = `${question.chapter}|${question.chapter_title}`;
      const existing = chapters.get(key);

      if (existing) {
        existing.count += 1;
      } else {
        chapters.set(key, {
          number: question.chapter,
          title: question.chapter_title || "Untitled Chapter",
          count: 1,
        });
      }
    });

    chapterList.replaceChildren();

    chapters.forEach((chapter, key) => {
      const label = document.createElement("label");
      label.className = "chapter-option";

      const checkbox = document.createElement("input");
      checkbox.type = "checkbox";
      checkbox.value = key;
      checkbox.addEventListener("change", updateSelectionStatus);

      const text = document.createElement("span");
      text.className = "chapter-option-text";

      const name = document.createElement("span");
      name.className = "chapter-name";
      name.textContent =
        `Chapter ${chapter.number}: ${chapter.title}`;

      const count = document.createElement("span");
      count.className = "chapter-count";
      count.textContent = `${chapter.count.toLocaleString()} questions`;

      text.append(name, count);
      label.append(checkbox, text);
      chapterList.append(label);
    });

    chapterTitle.textContent = currentSubject;
    hero.hidden = true;
    subjects.hidden = true;
    quizScreen.hidden = true;
    status.hidden = true;
    chapterScreen.hidden = false;

    updateSelectionStatus();
  } catch (error) {
    status.textContent = error.message;
  }
}

function showQuestion() {
  const question = sessionQuestions[sessionIndex];
  const blockStart =
    Math.floor(sessionIndex / sessionBlockSize) * sessionBlockSize;
  const blockSize = Math.min(
    sessionBlockSize,
    sessionQuestions.length - blockStart
  );
  const questionInBlock = (sessionIndex % sessionBlockSize) + 1;
  const blockNumber =
    Math.floor(sessionIndex / sessionBlockSize) + 1;

  quizSubject.textContent = currentSubject;
  quizPosition.textContent =
    `Block ${blockNumber} • Question ${questionInBlock} of ${blockSize}`;

  quizProgress.max = sessionQuestions.length;
  quizProgress.value = sessionIndex + 1;

  questionStem.textContent = question.stem;
  answerChoices.replaceChildren();

  question.choices.forEach((choice) => {
    const label = document.createElement("label");
    label.className = "answer-choice";

    const radio = document.createElement("input");
    radio.type = "radio";
    radio.name = "answer";
    radio.value = choice.label;
    radio.addEventListener("change", () => {
      submitAnswer.disabled = false;
    });

    const text = document.createElement("span");
    text.textContent = `${choice.label}. ${choice.text}`;

    label.append(radio, text);
    answerChoices.append(label);
  });

  feedback.hidden = true;
  submitAnswer.hidden = false;
  submitAnswer.disabled = true;
  continueButton.hidden = true;

  quizScore.textContent =
    `First pass: ${correctCount} correct, ${missedCount} missed`;
}

function startQuiz() {
  const selectedChapters = new Set(
    [...chapterList.querySelectorAll('input[type="checkbox"]:checked')]
      .map((checkbox) => checkbox.value)
  );

  sessionQuestions = shuffle(
    currentPack.questions.filter((question) => {
      const key = `${question.chapter}|${question.chapter_title}`;
      return selectedChapters.has(key)
        && ["mc", "multiple_choice"].includes(question.type);
    })
  );

  if (sessionQuestions.length === 0) {
    status.hidden = false;
    status.textContent =
      "No Multiple Choice questions were found in that selection.";
    return;
  }

  sessionIndex = 0;
  correctCount = 0;
  missedCount = 0;
  sessionBlockSize = Number(blockSizeSelect.value) || 15;

  hero.hidden = true;
  subjects.hidden = true;
  chapterScreen.hidden = true;
  status.hidden = true;
  quizScreen.hidden = false;

  showQuestion();
}

submitAnswer.addEventListener("click", () => {
  const selected = answerChoices.querySelector(
    'input[name="answer"]:checked'
  );

  if (!selected) {
    return;
  }

  const question = sessionQuestions[sessionIndex];
  const correctAnswers = question.correct_answers.map(String);
  const isCorrect = correctAnswers.includes(selected.value);

  if (isCorrect) {
    correctCount += 1;
    feedbackResult.textContent = "Correct!";
  } else {
    missedCount += 1;
    feedbackResult.textContent =
      `Incorrect. Correct answer: ${correctAnswers.join(", ")}`;
  }

  feedbackRationale.textContent = question.rationale || "";
  feedback.hidden = false;

  answerChoices.querySelectorAll("input").forEach((input) => {
    input.disabled = true;
  });

  quizScore.textContent =
    `First pass: ${correctCount} correct, ${missedCount} missed`;

  submitAnswer.hidden = true;
  continueButton.hidden = false;
});

continueButton.addEventListener("click", () => {
  sessionIndex += 1;

  if (sessionIndex >= sessionQuestions.length) {
    status.hidden = false;
    status.textContent =
      `Session complete: ${correctCount} correct, ${missedCount} missed.`;
    showSubjects();
    return;
  }

  showQuestion();
});

document.querySelectorAll(".subject-card").forEach((button) => {
  button.addEventListener("click", () => showChapters(button));
});

document.querySelector("#back-button").addEventListener("click", showSubjects);
document.querySelector("#exit-quiz").addEventListener("click", showSubjects);

document.querySelector("#select-all").addEventListener("click", () => {
  chapterList.querySelectorAll('input[type="checkbox"]').forEach((checkbox) => {
    checkbox.checked = true;
  });

  updateSelectionStatus();
});

document.querySelector("#clear-all").addEventListener("click", () => {
  chapterList.querySelectorAll('input[type="checkbox"]').forEach((checkbox) => {
    checkbox.checked = false;
  });

  updateSelectionStatus();
});

startButton.addEventListener("click", startQuiz);
