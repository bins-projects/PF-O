from pathlib import Path

from compiler.cleaner import clean_text
from compiler.importer import ImportRequest, extract_source


def test_extract_then_clean_pipeline(
    tmp_path: Path,
    monkeypatch,
) -> None:
    source = tmp_path / "book.pdf"
    source.write_bytes(b"placeholder")

    raw_text = (
        "Document shared on https://www.docsity.com/example\n"
        "Chapter 01: Test Chapter\n"
        "Question 1\n"
    )

    monkeypatch.setattr(
        "compiler.importer.read_pdf",
        lambda path: raw_text,
    )

    request = ImportRequest(
        source_path=source,
        pack_id="test-pack",
        title="Test Pack",
        workspace_root=tmp_path / "imports",
    )

    extracted = extract_source(request)
    cleaned = clean_text(extracted.raw_text)

    assert "docsity" not in cleaned.lower()
    assert "Chapter 01: Test Chapter" in cleaned
    assert "Question 1" in cleaned
