def validate_questions(questions: list[dict]) -> list[str]:
    """
    Validate parsed questions and return a list of problems found.
    """

    problems = []

    for question in questions:
        number = question["question_number"]

        if not question["stem"]:
            problems.append(f"Question {number}: missing stem")

        if not question["choices"]:
            problems.append(f"Question {number}: no answer choices")

        if not question["correct_answers"]:
            problems.append(f"Question {number}: missing correct answer")

        if not question["rationale"]:
            problems.append(f"Question {number}: missing rationale")

        if not question["question_type"]:
            problems.append(f"Question {number}: missing question type")

    return problems
