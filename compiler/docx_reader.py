from docx import Document


def read_docx(path):
    document = Document(path)

    paragraphs = []
    for index, paragraph in enumerate(document.paragraphs):
        paragraphs.append({
            "index": index,
            "text": paragraph.text,
        })

    return {
        "source_path": path,
        "paragraph_count": len(paragraphs),
        "paragraphs": paragraphs,
    }

