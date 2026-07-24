(function () {
  function quizPositionText({
    blockNumber,
    totalBlocks,
    reviewMode,
    reviewRemaining,
    questionInBlock,
    blockLength,
  }) {
    if (reviewMode) {
      return `Block ${blockNumber} of ${totalBlocks} • Review • ${reviewRemaining} remaining`;
    }

    return `Block ${blockNumber} of ${totalBlocks} • Question ${questionInBlock} of ${blockLength}`;
  }

  function runningScoreText(correct, missed) {
    return `First pass: ${correct} correct, ${missed} missed`;
  }

  function firstPassBlockScoreText(correct, total) {
    return `First pass: ${correct} of ${total} correct.`;
  }

  function finalScoreText(percentage) {
    return `First-pass score: ${percentage}%`;
  }

  function finalMessage(correct, total) {
    return `${correct} of ${total} correct on the first attempt.`;
  }

  function blockTitle(blockNumber, mastered) {
    return `Block ${blockNumber} ${mastered ? "Mastered" : "Complete"}`;
  }

  function blockMessage(missedCount, mastered) {
    if (mastered) {
      return "All missed questions have now been answered correctly.";
    }

    if (missedCount === 0) {
      return "No review is needed.";
    }

    return `${missedCount} ${missedCount === 1 ? "question needs" : "questions need"} review.`;
  }

  window.PrepFlowDisplayRules = {
    quizPositionText,
    runningScoreText,
    firstPassBlockScoreText,
    finalScoreText,
    finalMessage,
    blockTitle,
    blockMessage,
  };
}());
