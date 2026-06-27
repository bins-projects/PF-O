import json
import re
from pathlib import Path


QUESTION_RE = re.compile(r"^\s*\*\*(\d+)\.\s*(.+)")


def parse_questions(tokens_path: str, output_path: str) -> list[dict]:
    """
    Parser v0.1

    Reads tokenized document data and groups it into rough question blocks.
    This does not fully understand answers/rationales yet.
    It only detects question boundaries.
    """

    tokens_file = Path(tokens_path)
    output_file = Path(output_path)

    with tokens_file.open("r", encoding="utf-8") as f:
        data = json.load(f)
        tokens = data["tokens"]

    questions = []
    current_question = None

    for token in tokens:
        if isinstance(token, dict):
            text = token.get("text", "").strip()
        else:
            text = str(token).strip()

        if not text:
            continue

        match = QUESTION_RE.match(text)

        if match:
            if current_question:
                questions.append(current_question)

            question_number = int(match.group(1))
            stem_start = match.group(2).strip()

            current_question = {
                "question_number": question_number,
                "stem": stem_start,
                "raw_lines": [text],
                "choices": [],
                "answer": None,
                "rationale": None,
            }
        else:
            if current_question:
                current_question["raw_lines"].append(text)

    if current_question:
        questions.append(current_question)

    output_file.parent.mkdir(parents=True, exist_ok=True)

    with output_file.open("w", encoding="utf-8") as f:
        json.dump(questions, f, indent=2, ensure_ascii=False)

    return questions

