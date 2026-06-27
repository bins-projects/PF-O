import json
import sys
from pathlib import Path

from compiler.docx_reader import read_docx
from compiler.tokenizer import tokenize
from compiler.parser import parse_questions


def main():
    print("PrepFlow Compiler")
    print("Version 0.1")
    print()

    if len(sys.argv) < 2:
        print("Usage:")
        print('python3 -m compiler.cli "path/to/question_bank.docx"')
        return

    source_path = sys.argv[1]
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)

    raw_document = read_docx(source_path)

    raw_path = output_dir / "01_raw_document.json"
    with raw_path.open("w", encoding="utf-8") as file:
        json.dump(raw_document, file, indent=2, ensure_ascii=False)

    tokenized = tokenize(raw_document)

    token_path = output_dir / "02_tokens.json"
    with token_path.open("w", encoding="utf-8") as file:
        json.dump(tokenized, file, indent=2, ensure_ascii=False)

    question_path = output_dir / "03_questions.json"
    questions = parse_questions(str(token_path), str(question_path))

    print("Loaded document.")
    print(f"Source: {raw_document['source_path']}")
    print(f"Paragraphs: {raw_document['paragraph_count']}")
    print(f"Raw artifact: {raw_path}")
    print()
    print("Tokenized document.")
    print(f"Tokens: {tokenized['token_count']}")
    print(f"Token artifact: {token_path}")
    print()
    print("Parsed questions.")
    print(f"Question blocks: {len(questions)}")
    print(f"Question artifact: {question_path}")


if __name__ == "__main__":
    main()

