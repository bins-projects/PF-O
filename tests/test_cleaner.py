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


def test_removes_leading_chapter_index():
    text = """Book title
Chapter 01: First
Chapter 02: Second
Chapter 03: Third

Chapter 01: First
MULTIPLE CHOICE
1. Example question
ANS: A
"""

    cleaned = clean_text(text)

    assert cleaned.count("Chapter 01: First") == 1
    assert "Chapter 02: Second" not in cleaned
    assert "Chapter 03: Third" not in cleaned
    assert "1. Example question" in cleaned


def test_clean_text_removes_nursing_test_bank_branding() -> None:
    text = """Fundamentals of Nursing 2nd Edition Yoost Test Bank
NURSINGTB.COM
Yoost & Crawford: Fundamentals of Nursing: Active Learning for Collaborative Practice,
a. The patient agrees with the diagnosis. Fundamentals of Nursing 2nd Edition Yoost Test Bank NURSINGTB.COM U
ANS: B NURSINGTB.COM
The rationale remains educational content. NURSINGTB.COM
"""

    cleaned = clean_text(text)

    assert "Fundamentals of Nursing 2nd Edition Yoost Test Bank" not in cleaned
    assert "NURSINGTB.COM" not in cleaned
    assert "Yoost & Crawford:" not in cleaned
    assert "a. The patient agrees with the diagnosis." in cleaned
    assert "ANS: B" in cleaned
    assert "The rationale remains educational content." in cleaned
