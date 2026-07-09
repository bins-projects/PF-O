from study.loader import list_packs, load_pack
from study.question import ask_question
from study.session import SessionManager
from study.scoring import ScoreTracker
from study.review import ReviewQueue


def choose_chapters(questions):
    chapters = {}

    for question in questions:
        chapter = question.get("chapter")
        title = question.get("chapter_title", "")

        if chapter is not None:
            chapters[chapter] = title

    if not chapters:
        return questions

    print("\nStudy Options:\n")
    print("1. Entire Pack")
    print("2. Choose Chapter(s)")

    choice = input("\nChoose study option: ").strip()

    if choice != "2":
        return questions

    print("\nAvailable Chapters:\n")

    for chapter in sorted(chapters):
        print(f"{chapter}. {chapters[chapter]}")

    selected = input("\nEnter chapter number(s), separated by commas: ").strip()

    selected_chapters = {
        int(item.strip())
        for item in selected.split(",")
        if item.strip().isdigit()
    }

    filtered_questions = [
        question
        for question in questions
        if question.get("chapter") in selected_chapters
    ]

    if not filtered_questions:
        raise ValueError(f"No questions found for chapter(s): {sorted(selected_chapters)}")

    print(f"\nLoaded chapter filter — {len(filtered_questions)} question(s).")
    return filtered_questions


def main():
    packs = list_packs()

    if not packs:
        raise FileNotFoundError("No PrepFlow packs found in packs/.")

    print("Available Packs:\n")

    for index, pack_info in enumerate(packs, start=1):
        print(f"{index}. {pack_info['title']} ({pack_info['question_count']} questions)")

    choice = int(input("\nChoose a pack: "))
    selected_pack = packs[choice - 1]

    pack = load_pack(selected_pack["path"])
    questions = choose_chapters(pack["questions"])

    session = SessionManager(questions)
    score = ScoreTracker()
    review = ReviewQueue()

    print(f"\nLoaded {pack['title']} — {len(questions)} questions.\n")

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
                score.record_review_answer(review_correct)

                if not review_correct:
                    review.add(review_question)

            print("\n" + "=" * 40)
            print("Review Complete ✅")
            print("All missed questions corrected.")
            print("=" * 40)

            input(f"Press Enter to begin Block {session.current_block_number() + 1}...")


if __name__ == "__main__":
    main()