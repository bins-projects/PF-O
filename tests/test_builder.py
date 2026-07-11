from compiler.builder import build_question


def test_build_question_preserves_chapter() -> None:
    question = {
        "chapter": 1,
        "question_number": 3,
        "question_type": "multiple_choice",
        "stem": "Who established the American Red Cross?",
        "choices": [
            {"label": "A", "text": "Dorothea Dix"},
            {"label": "D", "text": "Clara Barton"},
        ],
        "correct_answers": ["D"],
        "rationale": "Clara Barton established the American Red Cross.",
    }

    built = build_question(question, index=1)

    assert built.origin.chapter == 1
    assert built.origin.source_id == "3"
