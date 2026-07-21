from pathlib import Path

app_path = Path("web/app.js")
helper_path = Path(__file__)

app = app_path.read_text()

old = '''  quizScore.textContent =
    `First pass: ${firstPassCorrect} correct, ${firstPassMissed} missed`;'''
new = '''  quizScore.textContent = PrepFlowDisplayRules.runningScoreText(
    firstPassCorrect,
    firstPassMissed
  );'''

if old not in app:
    raise SystemExit("Expected post-answer score block not found")

app_path.write_text(app.replace(old, new, 1))
helper_path.unlink()
print("Phase D final display cleanup applied.")
