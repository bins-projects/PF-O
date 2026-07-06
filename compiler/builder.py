from compiler.ids import generate_question_id
from compiler.models import Answer, Content, Origin, Question


def build_question(question: dict, index: int) -> Question:
    """
    Convert one parsed legacy question dictionary into a canonical Question.
    """

    answer_type = question["question_type"]
    if answer_type == "multiple_choice":
        answer_type = "mc"

    return Question(
        id=generate_question_id(index),
        version=1,
        origin=Origin(source_id=str(question["question_number"])),
        content=Content(
            stem=question["stem"],
            choices=question["choices"],
            rationale=question["rationale"],
        ),
        answer=Answer(
            type=answer_type,
            value=question["correct_answers"],
        ),
    )


def build_questions(questions: list[dict]) -> list[Question]:
    """
    Convert parsed legacy question dictionaries into canonical Questions.
    """

    return [
        build_question(question, index)
        for index, question in enumerate(questions, start=1)
    ]