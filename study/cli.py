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
        is_correct = ask_question(question)
        score.record_answer(question, is_correct)

        if not is_correct:
            review.add(question)
            
        if session.is_block_complete() and session.has_next_question():
            print("\n" + "=" * 40)
            print(f"Block {session.current_block_number()} Complete")
            print("=" * 40)
            input("Press Enter to begin the next block...")

        input("\nPress Enter for next question...")

if __name__ == "__main__":
    main()        