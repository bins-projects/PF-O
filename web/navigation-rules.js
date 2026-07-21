(function () {
  function nextQuestionStep(questionIndex, blockEnd) {
    const nextQuestionIndex = questionIndex + 1;

    return {
      questionIndex: nextQuestionIndex,
      blockComplete: nextQuestionIndex >= blockEnd,
    };
  }

  window.PrepFlowNavigationRules = {
    nextQuestionStep,
  };
}());
