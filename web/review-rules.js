(function () {
  function queueAfterAnswer(reviewQueue, currentQuestion, isCorrect) {
    const nextQueue = [...reviewQueue];

    if (!isCorrect && currentQuestion) {
      nextQueue.push(currentQuestion);
    }

    return nextQueue;
  }

  function nextReviewStep(reviewQueue) {
    if (reviewQueue.length === 0) {
      return {
        finished: true,
        currentQuestion: null,
        reviewQueue: [],
      };
    }

    const [currentQuestion, ...remainingQueue] = reviewQueue;

    return {
      finished: false,
      currentQuestion,
      reviewQueue: remainingQueue,
    };
  }

  window.PrepFlowReviewRules = {
    queueAfterAnswer,
    nextReviewStep,
  };
}());
