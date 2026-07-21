from pathlib import Path

root = Path(__file__).resolve().parents[1]
app_path = root / "web" / "app.js"
app = app_path.read_text(encoding="utf-8")

old_helper = '''function isMultipleResponseQuestion(question) {
  const questionType = question.type || question.question_type;
  const correctAnswers = PrepFlowQuizRules.correctAnswersFor(question);
  const stem = String(question.stem || "");

  return (
    questionType === "multiple_response"
    || correctAnswers.length > 1
    || /select all that apply/i.test(stem)
  );
}

'''

if old_helper not in app:
    raise SystemExit("Expected response-type helper was not found.")

app = app.replace(old_helper, "", 1)
app = app.replace(
    "  const isMultipleResponse = isMultipleResponseQuestion(question);\n",
    "  const isMultipleResponse = PrepFlowQuizRules.isMultipleResponseQuestion(question);\n",
    1,
)

app_path.write_text(app, encoding="utf-8")
Path(__file__).unlink()

print("Phase D response-type integration applied.")
