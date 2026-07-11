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

from pathlib import Path


def test_parse_real_fundamentals_sample() -> None:
    sample = Path(
        "output/imports/fundamentals/02_clean.txt"
    ).read_text(encoding="utf-8")

    questions = parse_source_questions(sample)

    assert len(questions) > 1000


def test_source_metadata_does_not_append_to_last_choice() -> None:
    text = """Chapter 1: Nursing Theory

MULTIPLE CHOICE

1. Which theory should guide priority care?
a. Erikson
b. Paul
c. Maslow
d. Rosenstock
ANS: C
Maslow helps prioritize patient needs.
DIF: Remembering OBJ: 1.5 TOP: Planning
MSC: NCLEX Client Needs Category: Safe and Effective Care Environment
Concepts: Care Coordination
"""

    questions = parse_source_questions(text)

    assert questions[0]["choices"][-1] == {
        "label": "D",
        "text": "Rosenstock",
    }


def test_parse_rationale_that_appears_after_metadata() -> None:
    text = """Chapter 15: Nursing Informatics

MULTIPLE CHOICE

11. Which informatics competency level describes this nurse?
a. Beginner
b. Experienced
c. Specialist
d. Innovator
ANS: B
NOT: Concepts: Technology and Informatics
U S N T O
Experienced nurses understand data relationships and identify trends.
DIF: Analyzing OBJ: 15.4 TOP: Evaluation
"""

    questions = parse_source_questions(text)

    assert questions[0]["rationale"] == (
        "Experienced nurses understand data relationships and identify trends."
    )


def test_inline_metadata_does_not_append_to_stem() -> None:
    text = """Chapter 26: Infection Prevention

MULTIPLE CHOICE

1. Which isolation precaution should the nurse implement for hepatitis A? DIF: Applying
a. Airborne
b. Droplet
c. Contact
d. Protective
ANS: C
Contact precautions are appropriate.
"""

    questions = parse_source_questions(text)

    assert questions[0]["stem"] == (
        "Which isolation precaution should the nurse implement for hepatitis A?"
    )


def test_inline_metadata_does_not_append_to_rationale() -> None:
    text = """Chapter 6: Nursing Process

MULTIPLE CHOICE

1. Which patient should receive priority care?
a. A patient with cold symptoms
b. A patient with a twisted ankle
c. A patient with an obstructed airway
d. A patient requesting discharge teaching
ANS: C
An obstructed airway is an immediate threat. Analyzing OBJ: 6.3 TOP: Assessment
"""

    questions = parse_source_questions(text)

    assert questions[0]["rationale"] == (
        "An obstructed airway is an immediate threat."
    )
