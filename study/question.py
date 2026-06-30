def format_choices(choices):
    lines = []

    for choice in choices:
        label = choice["label"]
        text = choice["text"]
        lines.append(f"{label}. {text}")

    return "\n".join(lines)


def normalize_answer(answer):
    return answer.strip().upper()


def check_answer(user_answer, correct_answers):
    user_answer = normalize_answer(user_answer)
    correct_set = set(correct_answers)
    user_set = set(user_answer)

    return user_set == correct_set


def ask_question(question, header=None):
    print()

    if header:
        print(header)
    else:
        print(f"Question {question['question_number']}")

    print()
    print(question["stem"])
    print()
    print(format_choices(question["choices"]))
    print()

    answer = input("Your answer: ")
    is_correct = check_answer(answer, question["correct_answers"])

    print()
    if is_correct:
        print("Correct!")
    else:
        correct = ", ".join(question["correct_answers"])
        print("Incorrect.")
        print(f"Correct answer: {correct}")

    print()
    print("Rationale:")
    print(question["rationale"])

    return is_correct