import re


JUNK_PATTERNS = [
    r"(?i)^document shared on.*$",
    r"(?i)^https?://.*docsity.*$",
    r"(?i)^powered by tcpdf.*$",
    r"(?i)^stuvia\.com.*$",
    r"(?i)^downloaded by:.*$",
    r"(?i)^distribution of this document is illegal.*$",
    r"(?i)^want to earn.*$",
]


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

        lines.append(line)

    cleaned = "\n".join(lines)

    # Collapse excessive blank lines
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)

    return cleaned.strip() + "\n"
