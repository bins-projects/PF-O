import json
from pathlib import Path

from compiler.models import Pack, Question


def question_to_dict(question: Question) -> dict:
    """
    Convert a canonical Question into the lean PrepFlow pack format.
    """

    return {
        "id": question.id,
        "chapter": question.origin.chapter,
        "chapter_title": question.origin.chapter_title,
        "type": question.answer.type,
        "stem": question.content.stem,
        "choices": question.content.choices,
        "correct_answers": question.answer.value,
        "rationale": question.content.rationale,
    }


def pack_to_dict(pack: Pack) -> dict:
    """
    Convert a canonical Pack into the lean PrepFlow pack format.
    """

    return {
        "format": "prepflow_pack",
        "version": "1.0",
        "pack_id": pack.id,
        "title": pack.title,
        "questions": [
            question_to_dict(question)
            for question in pack.questions
        ],
    }


def export_pack(pack: Pack, output_path: str | Path) -> Path:
    """
    Export a canonical PrepFlow Pack to lean JSON.
    """

    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as file:
        json.dump(pack_to_dict(pack), file, indent=2, ensure_ascii=False)

    return path