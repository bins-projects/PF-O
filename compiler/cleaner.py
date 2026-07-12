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

    lines = remove_leading_chapter_index(cleaned_lines)

    cleaned = "\n".join(lines)

    # Collapse excessive blank lines
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)

    return cleaned.strip() + "\n"
