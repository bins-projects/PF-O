from compiler.builder import build_question
from compiler.exporter import question_to_dict


def test_chapter_title_survives_build_and_export() -> None:
    question = {
        "chapter": 1,
        "chapter_title": "Nursing, Theory, and Professional Practice",
        "question_number": 1,
        "question_type": "multiple_choice",
        "stem": "Example question?",
        "choices": [
            {"label": "A", "text": "First"},
            {"label": "B", "text": "Second"},
        ],
        "correct_answers": ["A"],
        "rationale": "Example rationale.",
    }

    built = build_question(question, index=1)
    exported = question_to_dict(built)

    assert exported["chapter"] == 1
    assert exported["chapter_title"] == (
        "Nursing, Theory, and Professional Practice"
    )
