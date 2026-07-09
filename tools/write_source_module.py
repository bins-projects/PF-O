import json
from pathlib import Path

IN_PATH = Path("scratch/pharm_module.json")
OUT_PATH = Path("packs/pharmacy.prepflow.json")


def make_question_id(question: dict) -> str:
    section = question.get("section") or "unknown"
    return (
        f"pharm-ch{int(question['chapter']):02d}-"
        f"{section}-q{int(question['source_question_number']):03d}"
    )


def convert_question(question: dict) -> dict:
    choices = [
        {"label": label.upper(), "text": text}
        for label, text in sorted(question.get("choices", {}).items())
    ]

    return {
        "id": make_question_id(question),
        "source": question.get("source"),
        "chapter": question.get("chapter"),
        "chapter_title": question.get("chapter_title"),
        "section": question.get("section"),
        "source_question_number": question.get("source_question_number"),
        "type": question.get("type"),
        "stem": question.get("stem"),
        "choices": choices,
        "correct_answers": [answer.upper() for answer in question.get("answer", [])],
        "rationale": question.get("rationale"),
        "metadata": question.get("metadata"),
    }


def main() -> None:
    questions = json.loads(IN_PATH.read_text(encoding="utf-8"))

    pack = {
        "format": "prepflow_pack",
        "version": "1.0",
        "pack_id": "pharmacy",
        "title": "Pharmacy",
        "questions": [convert_question(question) for question in questions],
    }

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(json.dumps(pack, indent=2), encoding="utf-8")

    print(f"Wrote source module: {OUT_PATH}")
    print(f"Questions: {len(pack['questions'])}")


if __name__ == "__main__":
    main()
