import json
import sys
from collections import defaultdict
from pathlib import Path

from compiler.diagnostics import CompilerDiagnostic
from compiler.pipeline import compile_questions


def print_validation_failure(problems: list[CompilerDiagnostic]) -> None:
    print()
    print("Validation failed.")
    print(f"Problems found: {len(problems)}")
    print()

    grouped_problems = defaultdict(list)

    for problem in problems:
        grouped_problems[problem.label].append(
            f"[{problem.severity.value}] {problem.message}"
        )

    for question_label, issues in grouped_problems.items():
        print(question_label)
        for issue in issues:
            print(f"  - {issue}")
        print()

    print("Compilation aborted.")


def compile_json(source_path: str) -> None:
    packs_dir = Path("packs")
    packs_dir.mkdir(exist_ok=True)

    with open(source_path, "r", encoding="utf-8") as file:
        questions = json.load(file)

    pack_id = Path(source_path).stem
    export_path = packs_dir / f"{pack_id}.prepflow.json"

    result = compile_questions(
        questions,
        pack_id=pack_id,
        title=Path(source_path).stem,
        export_path=export_path,
    )

    fatal_problems = [
        problem
        for problem in result.problems
        if problem.severity.value == "fatal"
    ]

    if fatal_problems:
        print_validation_failure(fatal_problems)
        sys.exit(1)

    print("Loaded question JSON.")
    print(f"Source: {source_path}")
    print(f"Question blocks: {len(questions)}")
    print()
    print("Validation.")
    print(f"Problems found: {len(result.problems)}")
    print()
    print(f"Canonical questions built: {len(result.pack.questions)}")
    print(f"Pack built: {result.pack.id}")
    print(f"Pack exported: {result.exported_path}")


def main() -> None:
    print("PrepFlow Compiler")
    print("Version 0.1")
    print()

    if len(sys.argv) < 2:
        print("Usage:")
        print('python3 -m compiler.cli "path/to/questions.json"')
        return

    source_path = sys.argv[1]
    suffix = Path(source_path).suffix.lower()

    if suffix == ".json":
        compile_json(source_path)
    else:
        print(f"Unsupported source file type: {suffix}")
        sys.exit(1)


if __name__ == "__main__":
    main()
