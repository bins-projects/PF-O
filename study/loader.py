import json
from pathlib import Path


def load_questions(path="output/03_questions.json"):
    question_path = Path(path)

    if not question_path.exists():
        raise FileNotFoundError(
            f"Could not find {question_path}. Run the compiler first."
        )

    with question_path.open("r", encoding="utf-8") as file:
        questions = json.load(file)

    return questions