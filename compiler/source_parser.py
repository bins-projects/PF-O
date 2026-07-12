import re


CHAPTER_RE = re.compile(r"^Chapter\s+\d+\s*:", re.IGNORECASE)
SECTION_HEADERS = {
    "MULTIPLE CHOICE",
    "MULTIPLE RESPONSE",
    "COMPLETION",
    "ORDERING",
}
QUESTION_RE = re.compile(r"^(\d+)\.\s+(.+)")
CHOICE_RE = re.compile(r"^([a-gA-G])\.\s+(.+)")
ANSWER_RE = re.compile(r"^ANS:\s*(.*)", re.IGNORECASE)
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

def recover_missing_a_choice(question: dict) -> dict:
    """
    Recover an A choice lost during PDF extraction.
    """

    if (
        question.get("question_type") == "multiple_choice"
        and question.get("correct_answers") == ["A"]
        and question.get("choices")
        and question["choices"][0]["label"] == "B"
        and "?" in question.get("stem", "")
    ):
        stem = question["stem"].strip()

        question_part, possible_answer = stem.rsplit("?", 1)

        if possible_answer.strip():
            question["stem"] = question_part.strip() + "?"
            question["choices"].insert(
                0,
                {
                    "label": "A",
                    "text": possible_answer.strip(),
                },
            )

    return question


def normalize_split_choices(lines: list[str]) -> list[str]:
    """
    Repair PDF extraction where choice markers are split across lines.

    Example:
        a
        .
        Answer text

    becomes:
        a. Answer text
    """
    normalized = []
    index = 0

    while index < len(lines):
        if (
            index + 2 < len(lines)
            and re.fullmatch(r"[a-gA-G]", lines[index])
            and lines[index + 1] == "."
        ):
            normalized.append(
                f"{lines[index]}. {lines[index + 2]}"
            )
            index += 3
            continue

        normalized.append(lines[index])
        index += 1

    return normalized


def parse_source_questions(text: str) -> list[dict]:
    lines = normalize_split_choices([line.strip() for line in text.splitlines()])

    # Join chapter headings that were wrapped across PDF-extracted lines.
    joined_lines: list[str] = []
    index = 0

    while index < len(lines):
        line = lines[index]

        if (
            CHAPTER_RE.match(line)
            and re.search(r"(?:,|\band|\bor)\s*$", line, re.IGNORECASE)
            and index + 1 < len(lines)
        ):
            continuation = lines[index + 1]

            if (
                continuation
                and continuation.upper() not in SECTION_HEADERS
                and not QUESTION_RE.match(continuation)
                and not CHOICE_RE.match(continuation)
                and not ANSWER_RE.match(continuation)
                and not METADATA_RE.match(continuation)
            ):
                joined_lines.append(f"{line} {continuation}")
                index += 2
                continue

        joined_lines.append(line)
        index += 1

    lines = joined_lines

    chapter = None
    section = None
    question = None
    questions: list[dict] = []
    reading_rationale = False
    metadata_started = False
    awaiting_completion_answer = False

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

        # Wrapped stems can begin with clock times such as "0700.".
        # A leading-zero number inside an unfinished question is content,
        # not a new source-question boundary.
        if (
            question_match
            and question is not None
            and not question["choices"]
            and not question["correct_answers"]
            and question_match.group(1).startswith("0")
        ):
            question["stem"] += " " + strip_inline_metadata(line)
            question["stem"] = question["stem"].rstrip()
            continue

        if question_match and (not reading_rationale or metadata_started):
            if question is not None:
                questions.append(recover_missing_a_choice(question))

            question = {
                "chapter": chapter,
                "section": section,
                "source_question_number": int(question_match.group(1)),
                "question_type": {
                    "MULTIPLE CHOICE": "multiple_choice",
                    "MULTIPLE RESPONSE": "multiple_response",
                    "COMPLETION": "completion",
                    "ORDERING": "ordered_response",
                }.get(section, "multiple_choice"),
                "stem": strip_inline_metadata(
                    question_match.group(2).strip()
                ),
                "choices": [],
                "correct_answers": [],
                "rationale": "",
            }
            reading_rationale = False
            metadata_started = False
            awaiting_completion_answer = False
            continue

        if question is None:
            continue

        choice_match = CHOICE_RE.match(line)
        if choice_match and not reading_rationale:
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

        if awaiting_completion_answer:
            if question["question_type"] == "ordered_response":
                question["correct_answers"] = re.findall(
                    r"[A-G]",
                    line.upper(),
                )
            else:
                question["correct_answers"] = [line]

            awaiting_completion_answer = False
            reading_rationale = True
            continue

        answer_match = ANSWER_RE.match(line)
        if answer_match:
            answer_text = answer_match.group(1).strip()

            sequence_language = any(
                phrase in question["stem"].lower()
                for phrase in (
                    "appropriate sequence",
                    "correct order",
                    "prioritize the steps",
                    "prioritize these",
                    "place the events",
                    "place the options",
                )
            )

            if (
                question["question_type"] == "completion"
                and question["choices"]
                and sequence_language
            ):
                question["question_type"] = "ordered_response"

                if answer_text:
                    question["correct_answers"] = re.findall(
                        r"[A-G]",
                        answer_text.upper(),
                    )
                    reading_rationale = True
                else:
                    awaiting_completion_answer = True

                continue

            if question["question_type"] == "completion":
                if answer_text:
                    question["correct_answers"] = [answer_text]
                    reading_rationale = True
                else:
                    awaiting_completion_answer = True
                continue

            question["correct_answers"] = re.findall(
                r"[A-G]",
                answer_text.upper(),
            )
            reading_rationale = True
            continue

        if not question["choices"] and not reading_rationale:
            question["stem"] += " " + strip_inline_metadata(line)
            question["stem"] = question["stem"].rstrip()
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
        questions.append(recover_missing_a_choice(question))

    return questions
