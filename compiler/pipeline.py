from dataclasses import dataclass
from pathlib import Path

from compiler.diagnostics import CompilerDiagnostic, DiagnosticSeverity
from compiler.models import Pack
from compiler.normalizer import normalize_questions
from compiler.validator import validate_questions
from compiler.deduplicator import deduplicate_questions
from compiler.builder import build_pack, build_questions
from compiler.exporter import export_pack


@dataclass
class CompilationResult:
    pack: Pack | None
    problems: list[CompilerDiagnostic]
    removed_duplicates: list[str]
    skipped_questions: list[CompilerDiagnostic]
    exported_path: Path | None = None


def question_label(question: dict) -> str:
    number = question.get("question_number", "Unknown")
    chapter = question.get("chapter", "Unknown")
    return f"Chapter {chapter}, Question {number}"


def compile_questions(
    questions: list[dict],
    *,
    pack_id: str,
    title: str,
    export_path: str | Path | None = None,
) -> CompilationResult:
    """
    Compile parsed question dictionaries into a canonical PrepFlow Pack.

    If export_path is provided, export the finished Pack to lean PrepFlow JSON.
    """

    normalized_questions = normalize_questions(questions)

    diagnostics = validate_questions(normalized_questions)

    fatal_diagnostics = [
        diagnostic
        for diagnostic in diagnostics
        if diagnostic.severity == DiagnosticSeverity.FATAL
    ]

    if fatal_diagnostics:
        return CompilationResult(
            pack=None,
            problems=diagnostics,
            removed_duplicates=[],
            skipped_questions=[],
            exported_path=None,
        )

    recoverable_labels = {
        diagnostic.label
        for diagnostic in diagnostics
        if diagnostic.severity == DiagnosticSeverity.RECOVERABLE
    }

    skipped_questions = [
        diagnostic
        for diagnostic in diagnostics
        if diagnostic.severity == DiagnosticSeverity.RECOVERABLE
    ]

    compilable_questions = [
        question
        for question in normalized_questions
        if question_label(question) not in recoverable_labels
    ]

    result = deduplicate_questions(compilable_questions)

    canonical_questions = build_questions(result.questions)

    pack = build_pack(
        canonical_questions,
        pack_id=pack_id,
        title=title,
    )

    exported_path = None

    if export_path is not None:
        exported_path = export_pack(pack, export_path)

    return CompilationResult(
        pack=pack,
        problems=diagnostics,
        removed_duplicates=result.removed,
        skipped_questions=skipped_questions,
        exported_path=exported_path,
    )