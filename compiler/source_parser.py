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
    r"^(DIF|OBJ|TOP|MSC|KEY|NCLEX|NOT|CONCEPTS):",
    re.IGNORECASE,
)
INLINE_METADATA_RE = re.compile(
    r"\s+(?:(?:Remembering|Understanding|Applying|Analyzing|Evaluating|"
    r"Creating)\s+)?(?:DIF|OBJ|TOP|MSC|KEY|NCLEX|NOT|CONCEPTS):.*$",
    re.IGNORECASE,
)


def strip_inline_metadata(text: str) -> str:
    return INLINE_METADATA_RE.sub("", text).rstrip()


def parse_source_questions(text: str) -> list[dict]:
    lines = [line.strip() for line in text.splitlines()]

    chapter = None
    section = None
    question = None
    questions: list[dict] = []
    reading_rationale = False
    metadata_started = False

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
        if question_match and (not reading_rationale or metadata_started):
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
                "stem": strip_inline_metadata(
                    question_match.group(2).strip()
                ),
                "choices": [],
                "correct_answers": [],
                "rationale": "",
            }
            reading_rationale = False
            metadata_started = False
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

        if METADATA_RE.match(line):
            reading_rationale = False
            metadata_started = True
            continue

        if not question["choices"] and not reading_rationale:
            question["stem"] += " " + strip_inline_metadata(line)
            question["stem"] = question["stem"].rstrip()
            continue

        answer_match = ANSWER_RE.match(line)
        if answer_match:
            question["correct_answers"] = re.findall(
                r"[A-F]",
                answer_match.group(1).upper(),
            )
            reading_rationale = True
            continue

        if metadata_started:
            # Ignore short standalone extraction artifacts such as
            # "U S N T O", but allow educational rationale text that
            # appears after source metadata.
            if not re.search(r"[a-z]", line) and len(line) < 30:
                continue

            if question["correct_answers"]:
                reading_rationale = True
            else:
                continue

        if question["choices"] and not reading_rationale:
            question["choices"][-1]["text"] += " " + line
            continue

        if reading_rationale:
            if question["rationale"]:
                question["rationale"] += " "
            question["rationale"] += strip_inline_metadata(line)
            question["rationale"] = question["rationale"].rstrip()

    if question is not None:
        questions.append(question)

    return questions
