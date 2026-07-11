from compiler.cleaner import clean_text


def test_removes_docsity_line():
    text = (
        "Question\n"
        "Document shared on https://www.docsity.com/example\n"
        "Answer\n"
    )

    cleaned = clean_text(text)

    assert "docsity" not in cleaned.lower()
    assert "Question" in cleaned
    assert "Answer" in cleaned


def test_preserves_normal_content():
    text = "Chapter 01: Fundamentals\nQuestion 1\n"

    cleaned = clean_text(text)

    assert cleaned.startswith("Chapter 01")


def test_removes_inline_docsity_notice_but_preserves_content():
    text = (
        "Concepts: Care Coordination "
        "Document shared on https://www.docsity.com/example\n"
    )

    cleaned = clean_text(text)

    assert cleaned == "Concepts: Care Coordination\n"
    assert "docsity" not in cleaned.lower()
