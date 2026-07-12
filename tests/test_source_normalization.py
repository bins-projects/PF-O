from compiler.normalizer import normalize_question


def test_normalize_source_parser_question() -> None:
    parsed = {
        "chapter": "Chapter 01: Nursing, Theory, and Professional Practice",
        "section": "MULTIPLE CHOICE",
        "source_question_number": 3,
        "question_type": "multiple_choice",
        "stem": "Who established the American Red Cross?",
        "choices": [
            {"label": "A", "text": "Dorothea Dix"},
            {"label": "B", "text": "Linda Richards"},
            {"label": "C", "text": "Lena Higbee"},
            {"label": "D", "text": "Clara Barton"},
        ],
        "correct_answers": ["D"],
        "rationale": "Clara Barton established the American Red Cross.",
    }

    normalized = normalize_question(parsed)

    assert normalized["chapter"] == 1
    assert normalized["chapter_title"] == (
        "Nursing, Theory, and Professional Practice"
    )
    assert normalized["question_number"] == 3
    assert normalized["question_type"] == "multiple_choice"
    assert normalized["stem"] == parsed["stem"]
    assert normalized["choices"] == parsed["choices"]
    assert normalized["correct_answers"] == ["D"]
    assert normalized["rationale"] == parsed["rationale"]


def test_normalizer_removes_source_title_fragments_from_chapter_title():
    question = {
        "chapter": "Chapter 16: Intravenous Therapy Linton: Medical-Surgical Nursing, 8th Edition",
        "section": "MULTIPLE CHOICE",
        "source_question_number": 1,
        "question_type": "multiple_choice",
        "stem": "What action should the nurse take?",
        "choices": [
            {"label": "A", "text": "Assess the patient."},
            {"label": "B", "text": "Notify the provider."},
        ],
        "correct_answers": ["A"],
        "rationale": "Assessment comes first.",
    }

    normalized = normalize_question(question)

    assert normalized["chapter"] == 16
    assert normalized["chapter_title"] == "Intravenous Therapy"
