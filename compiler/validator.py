def validate_questions(questions: list[dict]) -> list[str]:
    """
    Validate parsed legacy question dictionaries.

    This validator checks the parser output before the compiler converts
    questions into canonical PrepFlow Question objects.
    """

    problems = []
    seen_stems = set()
    seen_numbers = set()

    for question in questions:
        number = question.get("question_number", "Unknown")
        stem = (question.get("stem") or "").strip()

        if number in seen_numbers:
            problems.append(f"Question {number}: duplicate question number")
        else:
            seen_numbers.add(number)

        if stem in seen_stems:
            problems.append(f"Question {number}: duplicate question text")
        else:
            seen_stems.add(stem)

        if not stem:
            problems.append(f"Question {number}: missing stem")

        if not question.get("choices"):
            problems.append(f"Question {number}: no answer choices")

        if not question.get("correct_answers"):
            problems.append(f"Question {number}: missing correct answer")

        if not question.get("rationale"):
            problems.append(f"Question {number}: missing rationale")

        if not question.get("question_type"):
            problems.append(f"Question {number}: missing question type")

    return problems