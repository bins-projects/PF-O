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


def test_parse_completion_with_answer_on_following_line() -> None:
    text = """Chapter 1: Dosage Calculations

COMPLETION

1. What is the weight in pounds for an individual who weighs 70 kg? lb
ANS:
154
One kilogram equals 2.2 pounds.
DIF: Understanding
"""

    questions = parse_source_questions(text)

    assert len(questions) == 1
    assert questions[0]["question_type"] == "completion"
    assert questions[0]["choices"] == []
    assert questions[0]["correct_answers"] == ["154"]
    assert questions[0]["rationale"] == (
        "One kilogram equals 2.2 pounds."
    )


def test_parse_split_choice_marker() -> None:
    text = """Chapter 1: Test

MULTIPLE CHOICE

1. What is another term for seizure disorder?
a
.
Epilepsy
b
.
Enkephalin
c
.
Narcolepsy
d
.
Neuropathy
ANS: A
A seizure disorder is also called epilepsy.
"""

    questions = parse_source_questions(text)

    assert len(questions) == 1
    assert len(questions[0]["choices"]) == 4
    assert questions[0]["choices"][0]["label"] == "A"
    assert questions[0]["choices"][0]["text"] == "Epilepsy"


def test_recovers_missing_a_choice_when_answer_key_confirms_it() -> None:
    text = """Chapter 25: Drug Therapy for Seizures

MULTIPLE CHOICE

2. What is another term for seizure disorder?
Epilepsy
b. Enkephalin
c. Narcolepsy
d. Neuropathy
ANS: A
A seizure disorder is sometimes called epilepsy.
"""

    questions = parse_source_questions(text)

    assert len(questions) == 1
    assert questions[0]["stem"] == "What is another term for seizure disorder?"
    assert questions[0]["choices"][0]["label"] == "A"
    assert questions[0]["choices"][0]["text"] == "Epilepsy"


def test_wrapped_stem_line_beginning_with_time_is_not_new_question():
    text = """
Chapter 50: Diabetes and Hypoglycemia
MULTIPLE CHOICE
16. A patient with type 1 diabetes has an insulin order for NPH insulin, 35 U, to be given at
0700. The patient has also been instructed not to take anything by mouth.
a. Give the insulin as ordered.
b. Give the insulin with a small snack.
c. Inform the charge nurse.
d. Hold the insulin until after the blood draw.
ANS: D
Holding the insulin is appropriate.
DIF: Cognitive Level: Application
17. What should the nurse assess next?
a. Temperature
b. Blood pressure
c. Blood glucose
d. Respiratory rate
ANS: C
The blood glucose should be assessed.
DIF: Cognitive Level: Application
"""

    questions = parse_source_questions(text)

    assert len(questions) == 2
    assert questions[0]["source_question_number"] == 16
    assert "0700. The patient" in questions[0]["stem"]
    assert len(questions[0]["choices"]) == 4
    assert questions[0]["correct_answers"] == ["D"]


def test_rationale_beginning_with_choice_like_prefix_stays_rationale():
    text = """
Chapter 57: Skin Disorders
MULTIPLE CHOICE
7. Where should the nurse assess for Candida albicans?
a. Scalp
b. Abdominal skinfolds
c. Shaft of the penis
d. Sacrum
ANS: B
C. albicans infection appears most often in skinfolds.
DIF: Cognitive Level: Comprehension
8. What should the nurse assess next?
a. Temperature
b. Blood pressure
c. Skin color
d. Respirations
ANS: C
Skin color should be assessed.
DIF: Cognitive Level: Comprehension
"""

    questions = parse_source_questions(text)

    assert len(questions) == 2
    assert len(questions[0]["choices"]) == 4
    assert questions[0]["rationale"] == (
        "C. albicans infection appears most often in skinfolds."
    )
