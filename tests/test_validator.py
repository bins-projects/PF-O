from compiler.validator import validate_questions


def test_completion_question_does_not_require_choices() -> None:
    question = {
        "chapter": 1,
        "question_number": 1,
        "question_type": "completion",
        "stem": "What is 70 kg in pounds?",
        "choices": [],
        "correct_answers": ["154"],
        "rationale": "One kilogram equals 2.2 pounds.",
    }

    diagnostics = validate_questions([question])

    assert not any(
        diagnostic.message == "no answer choices"
        for diagnostic in diagnostics
    )
