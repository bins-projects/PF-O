import re


JUNK_PATTERNS = [
    r"(?i)^document shared on.*$",
    r"(?i)^https?://.*docsity.*$",
    r"(?i)^powered by tcpdf.*$",
    r"(?i)^stuvia\.com.*$",
    r"(?i)^downloaded by:.*$",
    r"(?i)^distribution of this document is illegal.*$",
    r"(?i)^want to earn.*$",
    r"(?i)^nursingtb\.com\s*$",
    r"(?i)^n/a\s*$",
    r"(?i)^fundamentals of nursing\s+\d+(?:st|nd|rd|th)\s+edition\s+yoost test bank\s*$",
    r"(?i)^yoost\s*&\s*crawford:\s*fundamentals of nursing:.*$",
]


CHAPTER_HEADING_RE = re.compile(
    r"^Chapter\s+(\d{1,3})\s*:\s+.+$",
    re.IGNORECASE,
)


def remove_leading_chapter_index(lines: list[str]) -> list[str]:
    """
    Remove a leading table-of-contents-style chapter list.

    A chapter index is recognized when several sequential chapter headings
    appear near the beginning and the first chapter appears again later,
    marking the start of the real content.
    """
    matches: list[tuple[int, int]] = []

    for index, line in enumerate(lines):
        match = CHAPTER_HEADING_RE.match(line.strip())
        if match:
            matches.append((index, int(match.group(1))))

    if len(matches) < 4:
        return lines

    first_line, first_chapter = matches[0]

    for position in range(1, len(matches)):
        repeated_line, repeated_chapter = matches[position]

        if repeated_chapter != first_chapter:
            continue

        index_numbers = [
            chapter
            for _, chapter in matches[:position]
        ]

        if len(index_numbers) < 3:
            continue

        if index_numbers != sorted(set(index_numbers)):
            continue

        return lines[:first_line] + lines[repeated_line:]

    return lines


def remove_obsolete_pharmacy_chapter_32(
    lines: list[str],
) -> list[str]:
    """
    Remove the obsolete Pharmacy chapter appended inside the newer
    third-edition source.

    The contaminated block begins with the exact legacy heading and ends
    immediately before the next chapter heading.
    """
    obsolete_heading = (
        "chapter 32: drug therapy for female reproductive issues"
    )

    cleaned: list[str] = []
    skipping = False

    for line in lines:
        normalized = line.strip().lower()

        if normalized == obsolete_heading:
            skipping = True
            continue

        if skipping and CHAPTER_HEADING_RE.match(line.strip()):
            skipping = False

        if not skipping:
            cleaned.append(line)

    return cleaned


def trim_pharmacy_chapter_3_duplicate_summary(
    lines: list[str],
) -> list[str]:
    """
    Keep the three genuine Chapter 3 questions and remove the condensed
    duplicate summary that follows them before Chapter 4.

    The complete duplicate questions occur later in Chapter 4 with their
    rationales, so retaining the summary would create incomplete copies.
    """
    target_heading = (
        "chapter 3: mathematics review and introduction "
        "to dosage calculations"
    )

    cleaned: list[str] = []
    inside_target = False
    skipping_duplicates = False
    inline_answer_count = 0

    for line in lines:
        normalized = line.strip().lower()

        if normalized == target_heading:
            inside_target = True
            skipping_duplicates = False
            inline_answer_count = 0
            cleaned.append(line)
            continue

        if inside_target and CHAPTER_HEADING_RE.match(line.strip()):
            inside_target = False
            skipping_duplicates = False
            cleaned.append(line)
            continue

        if not inside_target:
            cleaned.append(line)
            continue

        if skipping_duplicates:
            continue

        cleaned.append(line)

        if re.search(r"\bAns>\s*", line, re.IGNORECASE):
            inline_answer_count += 1

            if inline_answer_count == 3:
                skipping_duplicates = True

    return cleaned


def clean_text(text: str) -> str:
    """
    Remove generic extraction artifacts.

    This stage intentionally avoids source-specific parsing.
    It only removes obvious extraction noise while preserving
    educational content.
    """
    lines = []

    for raw in text.splitlines():
        line = raw.rstrip()

        if any(re.match(pattern, line) for pattern in JUNK_PATTERNS):
            continue

        # Remove branding appended to otherwise legitimate content.
        line = re.sub(
            r"(?i)\s*document shared on\s+https?://\S*docsity\S*.*$",
            "",
            line,
        ).rstrip()

        # Remove Stuvia branding appended to legitimate educational text.
        line = re.sub(
            r"(?i)\s*stuvia\.com\s*-\s*"
            r"the marketplace to buy and sell your study material.*$",
            "",
            line,
        ).rstrip()

        # Remove trailing source-title fragments appended to educational text.
        line = re.sub(
            r"(?i)\s*(?:Linton:\s*)?"
            r"(?:Medical-)?Surgical Nursing,\s*\d+"
            r"(?:st|nd|rd|th)\s+Edition\s*$",
            "",
            line,
        ).rstrip()

        # Remove a trailing standalone N/A extraction artifact.
        line = re.sub(
            r"(?i)\s+N/A\s*$",
            "",
            line,
        ).rstrip()

        # Remove source branding when it replaces an answer choice.
        # Example:
        # a. Stuvia.com - The Marketplace to Buy and Sell your Study Material
        line = re.sub(
            r"(?i)^[a-f]\.\s*stuvia\.com.*$",
            "",
            line,
        ).rstrip()

                # Repair section headers contaminated by inline source branding.
        line = re.sub(
            r"(?i)^(MULTIPLE CHOICE|MULTIPLE RESPONSE|COMPLETION|ORDERING)\s+Stuvia\.com.*$",
            r"\1",
            line,
        )
        line = re.sub(
            r"(?i)\s*fundamentals of nursing\s+\d+"
            r"(?:st|nd|rd|th)\s+edition\s+yoost test bank"
            r"(?:\s+nursingtb\.com)?(?:\s+u)?\s*$",
            "",
            line,
        ).rstrip()

        line = re.sub(
            r"(?i)\s*nursingtb\.com(?:\s+u)?\s*$",
            "",
            line,
        ).rstrip()

        if line:
            lines.append(line)

    cleaned_lines = []
    index = 0

    while index < len(lines):
        if (
            index + 3 < len(lines)
            and re.match(
                r"(?i)^extra per year\?$",
                lines[index],
            )
            and lines[index + 1] == "Med C"
            and re.match(
                r"(?i)^extra per year\?$",
                lines[index + 2],
            )
        ):
            index += 3
            continue

        cleaned_lines.append(lines[index])
        index += 1

    cleaned_lines = [
        line
        for line in cleaned_lines
        if not re.fullmatch(
            r"(?i)extra per year\?",
            line.strip(),
        )
    ]

    lines = remove_leading_chapter_index(cleaned_lines)
    lines = remove_obsolete_pharmacy_chapter_32(lines)
    lines = trim_pharmacy_chapter_3_duplicate_summary(lines)

    cleaned = "\n".join(lines)

    # Collapse excessive blank lines
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)

    return cleaned.strip() + "\n"
