import re


CHAPTER_HEADING_RE = re.compile(
    r"^Chapter\s+(\d+)\s*:\s*(.+)$",
    re.IGNORECASE,
)


def normalize_question(question: dict) -> dict:
    """
    Normalize supported legacy question dictionary formats into one
    compiler input schema.

    Canonical compiler input fields:

    - id
    - source
    - chapter
    - chapter_title
    - question_number
    - question_type
    - stem
    - choices
    - correct_answers
    - rationale
    - metadata
    """

    correct_answer = question.get("correct_answers")

    if correct_answer is None:
        correct_answer = question.get("correct_answer")

    if isinstance(correct_answer, str):
        correct_answers = [correct_answer]
    elif isinstance(correct_answer, list):
        correct_answers = correct_answer
    elif correct_answer is None:
        correct_answers = []
    else:
        correct_answers = [str(correct_answer)]

    chapter = question.get("chapter")
    chapter_title = question.get("chapter_title")

    if isinstance(chapter, str):
        chapter_match = CHAPTER_HEADING_RE.match(chapter.strip())
        if chapter_match:
            chapter = int(chapter_match.group(1))
            chapter_title = chapter_match.group(2).strip()
            chapter_title = re.sub(
                r"\s+Linton:(?:\s+Medical(?:-Surgical)?(?:\s+Nursing)?(?:,\s*\d+(?:st|nd|rd|th)\s+Edition)?-?)?\s*$",
                "",
                chapter_title,
                flags=re.IGNORECASE,
            ).strip()

    question_number = question.get("question_number")
    if question_number is None:
        question_number = question.get("source_question_number")

    return {
        "id": question.get("id"),
        "source": question.get("source"),
        "chapter": chapter,
        "chapter_title": chapter_title,
        "question_number": question_number,
        "question_type": question.get("question_type"),
        "stem": question.get("stem") or question.get("prompt") or "",
        "choices": question.get("choices") or {},
        "correct_answers": correct_answers,
        "rationale": question.get("rationale") or "",
        "metadata": question.get("metadata") or {},
    }


def normalize_questions(questions: list[dict]) -> list[dict]:
    """
    Normalize a list of supported question dictionaries.
    """

    return [normalize_question(question) for question in questions]