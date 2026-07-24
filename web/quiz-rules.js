(function () {
  function normalizeAnswers(rawAnswers) {
    const answers = Array.isArray(rawAnswers) ? rawAnswers : [rawAnswers];

    return answers
      .filter((answer) => answer !== null && answer !== undefined)
      .map((answer) => String(answer).trim().toUpperCase())
      .filter(Boolean);
  }

  function correctAnswersFor(question) {
    return normalizeAnswers(
      question.correct_answers ?? question.correct_answer ?? []
    );
  }

  function isMultipleResponseQuestion(question) {
    const questionType = question.type || question.question_type;
    const correctAnswers = correctAnswersFor(question);
    const stem = String(question.stem || "");

    return (
      questionType === "multiple_response"
      || correctAnswers.length > 1
      || /select all that apply/i.test(stem)
    );
  }

  function evaluateAnswer(question, selectedAnswers) {
    const correctAnswers = correctAnswersFor(question);
    const normalizedSelectedAnswers = normalizeAnswers(selectedAnswers);
    const correctSet = new Set(correctAnswers);
    const selectedSet = new Set(normalizedSelectedAnswers);

    return {
      isCorrect:
        selectedSet.size === correctSet.size
        && [...selectedSet].every((answer) => correctSet.has(answer)),
      correctAnswers,
    };
  }

  window.PrepFlowQuizRules = {
    normalizeAnswers,
    correctAnswersFor,
    isMultipleResponseQuestion,
    evaluateAnswer,
  };
}());
