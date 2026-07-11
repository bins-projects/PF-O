import re


CHAPTER_RE = re.compile(r"^Chapter\s+\d+\s*:", re.IGNORECASE)
SECTION_HEADERS = {
    "MULTIPLE CHOICE",
    "MULTIPLE RESPONSE",
    "COMPLETION",
    "ORDERING",
}
QUESTION_RE = re.compile(r"^(\d+)\.\s+(.+)")
CHOICE_RE = re.compile(r"^([a-fA-F])\.\s+(.+)")
ANSWER_RE = re.compile(r"^ANS:\s*(.+)", re.IGNORECASE)
METADATA_RE = re.compile(
    r"^(DIF|OBJ|TOP|MSC|KEY|NCLEX|NOT):",
    re.IGNORECASE,
)


def parse_source_questions(text: str) -> list[dict]:
    lines = [line.strip() for line in text.splitlines()]

    chapter = None
    section = None
    question = None
    questions: list[dict] = []
    reading_rationale = False

    for line in lines:
        if not line:
            continue

        if CHAPTER_RE.match(line):
            chapter = line
            continue

        if line.upper() in SECTION_HEADERS:
            section = line.upper()
            continue

        question_match = QUESTION_RE.match(line)
        if question_match:
            if question is not None:
                questions.append(question)

            question = {
                "chapter": chapter,
                "section": section,
                "source_question_number": int(question_match.group(1)),
                "question_type": (
                    "multiple_response"
                    if section == "MULTIPLE RESPONSE"
                    else "multiple_choice"
                ),
                "stem": question_match.group(2).strip(),
                "choices": [],
                "correct_answers": [],
                "rationale": "",
            }
            reading_rationale = False
            continue

        if question is None:
            continue

        choice_match = CHOICE_RE.match(line)
        if choice_match:
            question["choices"].append(
                {
                    "label": choice_match.group(1).upper(),
                    "text": choice_match.group(2).strip(),
                }
            )
            continue

        answer_match = ANSWER_RE.match(line)
        if answer_match:
            question["correct_answers"] = re.findall(
                r"[A-F]",
                answer_match.group(1).upper(),
            )
            reading_rationale = True
            continue

        if METADATA_RE.match(line):
            reading_rationale = False
            continue

        if reading_rationale:
            if question["rationale"]:
                question["rationale"] += " "
            question["rationale"] += line

    if question is not None:
        questions.append(question)

    return questions
