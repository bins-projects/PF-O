(function () {
  function totalBlockCount(totalQuestions, blockSize) {
    const safeTotal = Math.max(0, Number(totalQuestions) || 0);
    const safeBlockSize = Math.max(1, Number(blockSize) || 1);

    return Math.max(1, Math.ceil(safeTotal / safeBlockSize));
  }

  function blockEnd(blockStart, blockSize, totalQuestions) {
    const safeStart = Math.max(0, Number(blockStart) || 0);
    const safeBlockSize = Math.max(1, Number(blockSize) || 1);
    const safeTotal = Math.max(0, Number(totalQuestions) || 0);

    return Math.min(safeStart + safeBlockSize, safeTotal);
  }

  function questionPosition(questionIndex, blockStart) {
    const safeQuestionIndex = Math.max(0, Number(questionIndex) || 0);
    const safeBlockStart = Math.max(0, Number(blockStart) || 0);

    return safeQuestionIndex - safeBlockStart + 1;
  }

  function firstPassPercentage(correctAnswers, totalQuestions) {
    const safeCorrect = Math.max(0, Number(correctAnswers) || 0);
    const safeTotal = Math.max(0, Number(totalQuestions) || 0);

    return safeTotal ? Math.round((safeCorrect / safeTotal) * 100) : 0;
  }

  window.PrepFlowSessionRules = {
    totalBlockCount,
    blockEnd,
    questionPosition,
    firstPassPercentage,
  };
}());
