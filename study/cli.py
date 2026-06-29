from study.loader import load_questions
from study.session import ask_question
from study.scoring import ScoreTracker


def main():
    questions = load_questions()
    score = ScoreTracker()

    print(f"Loaded {len(questions)} questions.\n")

    for question in questions:
        is_correct = ask_question(question)
        score.record_answer(question, is_correct)

        input("\nPress Enter for next question...")


if __name__ == "__main__":
    main()