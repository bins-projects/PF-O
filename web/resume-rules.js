(function () {
  function resumeDescription(saved) {
    const subject = saved.currentSubject || "Custom Quiz";
    const mode = saved.reviewMode ? "reviewing missed questions" : "in progress";

    return `${subject} — Block ${saved.blockNumber}, ${mode}.`;
  }

  function resumeAriaLabel(description) {
    return `Continue session: ${description}`;
  }

  window.PrepFlowResumeRules = {
    resumeDescription,
    resumeAriaLabel,
  };
}());
