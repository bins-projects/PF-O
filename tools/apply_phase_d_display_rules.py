from pathlib import Path

app_path = Path("web/app.js")
index_path = Path("web/index.html")
helper_path = Path(__file__)

app = app_path.read_text()
index = index_path.read_text()

replacements = {
'''    quizPosition.textContent =
      `Block ${blockNumber} of ${totalBlockCount()} • Review • ${reviewQueue.length + 1} remaining`;''': '''    quizPosition.textContent = PrepFlowDisplayRules.quizPositionText({
      blockNumber,
      totalBlocks: totalBlockCount(),
      reviewMode: true,
      reviewRemaining: reviewQueue.length + 1,
      questionInBlock: null,
      blockLength,
    });''',
'''    quizPosition.textContent =
      `Block ${blockNumber} of ${totalBlockCount()} • Question ${questionInBlock} of ${blockLength}`;''': '''    quizPosition.textContent = PrepFlowDisplayRules.quizPositionText({
      blockNumber,
      totalBlocks: totalBlockCount(),
      reviewMode: false,
      reviewRemaining: null,
      questionInBlock,
      blockLength,
    });''',
'''  quizScore.textContent =
    `First pass: ${firstPassCorrect} correct, ${firstPassMissed} missed`;''': '''  quizScore.textContent = PrepFlowDisplayRules.runningScoreText(
    firstPassCorrect,
    firstPassMissed
  );''',
'''  summaryScore.textContent = `First-pass score: ${percentage}%`;
  summaryMessage.textContent =
    `${firstPassCorrect} of ${totalQuestions} correct on the first attempt.`;''': '''  summaryScore.textContent = PrepFlowDisplayRules.finalScoreText(percentage);
  summaryMessage.textContent = PrepFlowDisplayRules.finalMessage(
    firstPassCorrect,
    totalQuestions
  );''',
'''  if (mastered) {
    summaryTitle.textContent = `Block ${blockNumber} Mastered`;
    summaryScore.textContent =
      `First pass: ${blockCorrect} of ${blockLength} correct.`;
    summaryMessage.textContent =
      "All missed questions have now been answered correctly.";
  } else {
    summaryTitle.textContent = `Block ${blockNumber} Complete`;
    summaryScore.textContent =
      `First pass: ${blockCorrect} of ${blockLength} correct.`;
    summaryMessage.textContent =
      missedCount === 0
        ? "No review is needed."
        : `${missedCount} ${missedCount === 1 ? "question needs" : "questions need"} review.`;
  }''': '''  summaryTitle.textContent = PrepFlowDisplayRules.blockTitle(
    blockNumber,
    mastered
  );
  summaryScore.textContent = PrepFlowDisplayRules.firstPassBlockScoreText(
    blockCorrect,
    blockLength
  );
  summaryMessage.textContent = PrepFlowDisplayRules.blockMessage(
    missedCount,
    mastered
  );''',
}

for old, new in replacements.items():
    if old not in app:
        raise SystemExit(f"Expected app.js block not found:\n{old}")
    app = app.replace(old, new, 1)

script_anchor = '  <script src="resume-rules.js?v=20260721-1"></script>\n'
display_script = '  <script src="display-rules.js?v=20260721-1"></script>\n'
if display_script not in index:
    if script_anchor not in index:
        raise SystemExit("Expected index.html script anchor not found")
    index = index.replace(script_anchor, script_anchor + display_script, 1)

app_path.write_text(app)
index_path.write_text(index)
helper_path.unlink()
print("Phase D batched display-rule integration applied.")
