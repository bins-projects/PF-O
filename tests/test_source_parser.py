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


def test_parse_wrapped_question_stem() -> None:
    text = """Chapter 1: Nursing Theory

MULTIPLE CHOICE

4. The nursing instructor is researching the five proficiencies regarded as essential for students and
professionals. Which organization added safety as a sixth competency?
a. Quality and Safety Education for Nurses
b. Institute of Medicine
c. American Association of Colleges of Nursing
d. National League for Nursing
ANS: A
QSEN added safety as a sixth competency.
DIF: Remembering
"""

    questions = parse_source_questions(text)

    assert questions[0]["stem"] == (
        "The nursing instructor is researching the five proficiencies regarded as "
        "essential for students and professionals. Which organization added safety "
        "as a sixth competency?"
    )


def test_parse_wrapped_answer_choice() -> None:
    text = """Chapter 1: Nursing Theory

MULTIPLE CHOICE

2. Which definition of nursing is attributed to Florence Nightingale?
a. The imbalance between the patient and the environment decreases the capacity for
health.
b. The nurse focuses on interpersonal processes.
c. The nurse assists the patient toward independence.
d. Human beings interact as energy fields.
ANS: A
Nightingale emphasized the relationship between health and environment.
DIF: Remembering
"""

    questions = parse_source_questions(text)

    assert questions[0]["choices"][0] == {
        "label": "A",
        "text": (
            "The imbalance between the patient and the environment decreases "
            "the capacity for health."
        ),
    }
