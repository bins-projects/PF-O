from study.loader import load_questions
from study.question import ask_question
from study.session import SessionManager
from study.scoring import ScoreTracker
from study.review import ReviewQueue

def main():
    questions = load_questions()
    session = SessionManager(questions)
    score = ScoreTracker()
    review = ReviewQueue()

    print(f"Loaded {len(questions)} questions.\n")

    while session.has_next_question():
        question = session.get_next_question()
        header = f"Block {session.current_block_number()} • Question {session.question_in_block()} of {session.block_size}"
        is_correct = ask_question(question, header)
        score.record_answer(question, is_correct)

        if not is_correct:
            review.add(question)

        if session.is_block_complete() and session.has_next_question():
            print("\n" + "=" * 40)
            print(f"Block {session.current_block_number()} Complete")
            print("=" * 40)
            print(f"You have {review.count()} review question(s).")
            while review.has_questions():
                review_question = review.next_question()
                print("\n--- Review Question ---")
                review_correct = ask_question(review_question)

                if not review_correct:
                    review.add(review_question)

            print("\n" + "=" * 40)
            print("Review Complete ✓")
            print("All missed questions corrected.")
            print("=" * 40)

            input(f"Press Enter to begin Block {session.current_block_number() + 1}...")


if __name__ == "__main__":
    main()