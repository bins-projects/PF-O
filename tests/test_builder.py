from compiler.builder import build_question


def sample_question() -> dict:
    return {
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


def test_build_question_preserves_chapter() -> None:
    built = build_question(
        sample_question(),
        index=1,
        pack_id="fundamentals",
    )

    assert built.origin.chapter == 1
    assert built.origin.source_id == "3"


def test_build_question_generates_pack_namespaced_id() -> None:
    built = build_question(
        sample_question(),
        index=1,
        pack_id="fundamentals",
    )

    assert built.id == "PFQ-fundamentals-000000001"


def test_build_question_preserves_existing_id() -> None:
    question = sample_question()
    question["id"] = "PFQ-fundamentals-000000777"

    built = build_question(
        question,
        index=1,
        pack_id="fundamentals",
    )

    assert built.id == "PFQ-fundamentals-000000777"
