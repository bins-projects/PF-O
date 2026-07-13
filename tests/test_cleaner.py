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


def test_removes_stuvia_multiline_artifact_block() -> None:
    from compiler.cleaner import clean_text

    text = """Question content
Stuvia.com - The Marketplace to Buy and Sell your Study Material
extra per year?
Med C
extra per year?
a. Answer one
b. Answer two
"""

    cleaned = clean_text(text)

    assert "Stuvia.com" not in cleaned
    assert "extra per year?" not in cleaned
    assert "Med C" not in cleaned
    assert "a. Answer one" in cleaned


def test_removes_stuvia_from_choice_line() -> None:
    from compiler.cleaner import clean_text

    text = """Question stem
a. Stuvia.com - The Marketplace to Buy and Sell your Study Material
b. Normal answer
"""

    cleaned = clean_text(text)

    assert "Stuvia.com" not in cleaned
    assert "Normal answer" in cleaned


def test_removes_inline_stuvia_branding_but_preserves_content() -> None:
    source = (
        "Where should the nurse assess the patient? "
        "Stuvia.com - The Marketplace to Buy and Sell your Study Material\n"
        "C. albicans infection appears most often in skinfolds.\n"
    )

    cleaned = clean_text(source)

    assert "Where should the nurse assess the patient?" in cleaned
    assert "C. albicans infection appears most often in skinfolds." in cleaned
    assert "Stuvia" not in cleaned
    assert "Marketplace to Buy and Sell" not in cleaned


def test_removes_trailing_medsurg_source_title_fragments() -> None:
    source = (
        "The nurse should assess the patient. "
        "Linton: Medical-Surgical Nursing, 8th Edition\n"
        "The next intervention is reassessment. "
        "Medical-Surgical Nursing, 8th Edition\n"
        "The expected answer is communication. "
        "Surgical Nursing, 8th Edition\n"
    )

    cleaned = clean_text(source)

    assert "The nurse should assess the patient." in cleaned
    assert "The next intervention is reassessment." in cleaned
    assert "The expected answer is communication." in cleaned
    assert "Linton:" not in cleaned
    assert "Medical-Surgical Nursing, 8th Edition" not in cleaned
    assert "Surgical Nursing, 8th Edition" not in cleaned


def test_removes_trailing_na_extraction_artifact() -> None:
    source = (
        "The process is called socialization. N/A\n"
    )

    cleaned = clean_text(source)

    assert cleaned.strip() == "The process is called socialization."


def test_removes_standalone_na_metadata_artifact() -> None:
    source = (
        "OBJ: 3 TOP: Enculturation\n"
        "N/A\n"
        "MSC: NCLEX:\n"
    )

    cleaned = clean_text(source)

    assert "\nN/A\n" not in f"\n{cleaned}"
    assert "OBJ: 3 TOP: Enculturation" in cleaned
    assert "MSC: NCLEX:" in cleaned

def test_removes_obsolete_embedded_pharmacy_chapter_32() -> None:
    source = """Chapter 25: Drug Therapy for Psychiatric Problems
25. Valid psychiatric question
ANS: A
Chapter 32: Drug Therapy For Female Reproductive Issues
1. Obsolete duplicated question
ANS: B
Obsolete rationale.
Chapter 26: Drug Therapy For Insomnia
1. Valid insomnia question
ANS: C
"""

    cleaned = clean_text(source)

    assert "Chapter 25: Drug Therapy for Psychiatric Problems" in cleaned
    assert "25. Valid psychiatric question" in cleaned
    assert "Chapter 32: Drug Therapy For Female Reproductive Issues" not in cleaned
    assert "Obsolete duplicated question" not in cleaned
    assert "Obsolete rationale" not in cleaned
    assert "Chapter 26: Drug Therapy For Insomnia" in cleaned
    assert "1. Valid insomnia question" in cleaned


def test_preserves_unrelated_chapter_32() -> None:
    source = """Chapter 32: An Unrelated Legitimate Chapter
1. Keep this question
ANS: A
"""

    cleaned = clean_text(source)

    assert "Chapter 32: An Unrelated Legitimate Chapter" in cleaned
    assert "1. Keep this question" in cleaned

def test_trims_pharmacy_chapter_3_duplicate_summary() -> None:
    source = """Chapter 3: Mathematics Review and Introduction to Dosage Calculations
First real question?
A.
First choice
B.
Second choice Ans> B
Second real question?
A.
First choice
B.
Second choice Ans> A
Third real question?
A.
First choice
B.
Second choice Ans> B
Duplicate fourth question?
A.
First choice
B.
Second choice Ans> A
Duplicate fifth question?
_____ mL Ans> 5
Chapter 04: Medical Systems Of Weights And Measures
1. Complete Chapter 4 question
ANS: A
Complete rationale.
"""

    cleaned = clean_text(source)

    assert "First real question?" in cleaned
    assert "Second real question?" in cleaned
    assert "Third real question?" in cleaned
    assert "Duplicate fourth question?" not in cleaned
    assert "Duplicate fifth question?" not in cleaned
    assert "Chapter 04: Medical Systems Of Weights And Measures" in cleaned
    assert "Complete Chapter 4 question" in cleaned

def test_removes_standalone_extra_per_year_artifact() -> None:
    from compiler.cleaner import clean_text

    source = """Question stem
A. First answer
extra per year?
B. Second answer
ANS: B
The rationale remains.
"""

    cleaned = clean_text(source)

    assert "extra per year?" not in cleaned
    assert "A. First answer" in cleaned
    assert "B. Second answer" in cleaned
    assert "The rationale remains." in cleaned
