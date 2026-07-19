(() => {
  const pixelStage = document.querySelector(".pixel-stage");
  const quizBuilder = document.querySelector("#quiz-builder");
  const resumePanel = document.querySelector("#resume-panel");
  const quizCopy = document.querySelector(".home-quiz-copy");
  const blockSize = document.querySelector(".builder-block-size");
  const clearButton = document.querySelector("#clear-selections");
  const buildButton = document.querySelector("#build-quiz");
  const resumeButton = document.querySelector("#resume-session");
  const discardButton = document.querySelector("#discard-session");

  if (!pixelStage || !quizBuilder) return;

  if (resumePanel) {
    if (resumeButton) resumePanel.append(resumeButton);
    if (discardButton) resumePanel.append(discardButton);
  }

  quizBuilder.replaceChildren();
  [quizCopy, blockSize, clearButton, buildButton].forEach((element) => {
    if (element) quizBuilder.append(element);
  });

  pixelStage.append(quizBuilder);
  quizBuilder.hidden = false;

  document.querySelectorAll(".home-control-stack").forEach((stack) => stack.remove());
})();
