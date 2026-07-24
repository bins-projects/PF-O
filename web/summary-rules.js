(function () {
  function blockSummaryAction({ mastered, missedCount, blockEnd, totalQuestions }) {
    if (!mastered && missedCount > 0) {
      return {
        action: "review",
        label: "Review Missed Questions",
      };
    }

    if (blockEnd < totalQuestions) {
      return {
        action: "next-block",
        label: "Start Next Block",
      };
    }

    return {
      action: "finish",
      label: "Finish Session",
    };
  }

  window.PrepFlowSummaryRules = {
    blockSummaryAction,
  };
}());
