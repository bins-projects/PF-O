from compiler.pipeline import compile_questions


def test_compile_preserves_distinct_questions_with_repeated_numbers() -> None:
    questions = [
        {
            "chapter": 1,
            "chapter_title": "Nursing Theory",
            "question_number": 1,
            "question_type": "multiple_choice",
            "stem": "Which theory prioritizes patient needs?",
            "choices": [
                {"label": "A", "text": "Erikson"},
                {"label": "B", "text": "Maslow"},
            ],
            "correct_answers": ["B"],
            "rationale": "Maslow prioritizes human needs.",
        },
        {
            "chapter": 1,
            "chapter_title": "Nursing Theory",
            "question_number": 1,
            "question_type": "multiple_response",
            "stem": "Which statements describe a profession?",
            "choices": [
                {"label": "A", "text": "Requires specialized knowledge"},
                {"label": "B", "text": "Requires no continuing education"},
            ],
            "correct_answers": ["A"],
            "rationale": "Professions require specialized knowledge.",
        },
    ]

    result = compile_questions(
        questions,
        pack_id="test-pack",
        title="Test Pack",
    )

    assert result.pack is not None
    assert len(result.pack.questions) == 2
    assert result.removed_duplicates == []
