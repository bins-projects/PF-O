from compiler.source_parser import parse_source_questions


def test_parse_single_multiple_choice_question() -> None:
    text = """Chapter 1: Nursing Theory

MULTIPLE CHOICE

1. Which theory should the nurse use to prioritize patient care?
a. Erikson's Psychosocial Theory
b. Paul's Critical-Thinking Theory
c. Maslow's Hierarchy of Needs
d. Rosenstock's Health Belief Model
ANS: C
Maslow's hierarchy helps prioritize physiological and psychological needs.
DIF: Remembering OBJ: 1.5 TOP: Planning
MSC: Management of Care
"""

    questions = parse_source_questions(text)

    assert len(questions) == 1

    question = questions[0]

    assert question["chapter"] == "Chapter 1: Nursing Theory"
    assert question["section"] == "MULTIPLE CHOICE"
    assert question["source_question_number"] == 1
    assert question["question_type"] == "multiple_choice"
    assert question["stem"] == (
        "Which theory should the nurse use to prioritize patient care?"
    )
    assert question["choices"] == [
        {"label": "A", "text": "Erikson's Psychosocial Theory"},
        {"label": "B", "text": "Paul's Critical-Thinking Theory"},
        {"label": "C", "text": "Maslow's Hierarchy of Needs"},
        {"label": "D", "text": "Rosenstock's Health Belief Model"},
    ]
    assert question["correct_answers"] == ["C"]
    assert question["rationale"] == (
        "Maslow's hierarchy helps prioritize physiological and psychological needs."
    )
