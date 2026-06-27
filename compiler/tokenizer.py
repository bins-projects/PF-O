import re


def classify_paragraph(text):
    stripped = text.strip()

    if not stripped:
        return "blank"

    if re.match(r"^\*\*\d+\.\*\*", stripped):
        return "question_start"

    if re.match(r"^[a-f]\.", stripped, re.IGNORECASE):
        return "choice"

    if stripped.lower().startswith("**answer:"):
        return "answer"

    if stripped.lower().startswith("**rationale:"):
        return "rationale"

    if stripped.startswith("---"):
        return "separator"

    return "text"


def tokenize(raw_document):
    tokens = []

    for paragraph in raw_document["paragraphs"]:
        text = paragraph["text"]

        tokens.append({
            "paragraph_index": paragraph["index"],
            "type": classify_paragraph(text),
            "text": text,
        })

    return {
        "source_path": raw_document["source_path"],
        "token_count": len(tokens),
        "tokens": tokens,
    }

