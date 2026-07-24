from compiler.ids import generate_question_id
from compiler.models import Answer, Content, Origin, Pack, Question


def build_question(question: dict, index: int, pack_id: str) -> Question:
    """
    Convert one normalized question dictionary into a canonical Question.

    Preserve an existing permanent ID when present. Assign a Pack-namespaced
    ID only when the incoming question does not already have one.
    """

    answer_type = question["question_type"]
    if answer_type == "multiple_choice":
        answer_type = "mc"

    question_id = question.get("id") or generate_question_id(pack_id, index)

    return Question(
        id=question_id,
        version=1,
        origin=Origin(
            chapter=question["chapter"],
            chapter_title=question.get("chapter_title") or "",
            source_id=str(question["question_number"]),
        ),
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


def build_questions(questions: list[dict], pack_id: str) -> list[Question]:
    """
    Convert normalized question dictionaries into canonical Questions.
    """

    return [
        build_question(question, index, pack_id)
        for index, question in enumerate(questions, start=1)
    ]


def build_pack(
    questions: list[Question],
    pack_id: str,
    title: str,
    version: str = "1.0",
    schema_version: str = "0.1",
    created: str = "",
    source: dict | None = None,
) -> Pack:
    """
    Build a canonical PrepFlow Pack from canonical Questions.
    """

    return Pack(
        id=pack_id,
        title=title,
        version=version,
        schema_version=schema_version,
        created=created,
        source=source or {},
        questions=questions,
    )
