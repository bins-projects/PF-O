from compiler.diagnostics import CompilerDiagnostic, DiagnosticSeverity


def validate_questions(questions: list[dict]) -> list[CompilerDiagnostic]:
    """
    Validate normalized legacy question dictionaries.

    This validator checks normalized compiler input before the compiler
    converts questions into canonical PrepFlow Question objects.
    """

    diagnostics = []
    seen_stems = {}
    seen_numbers = {}

    for question in questions:
        number = question.get("question_number", "Unknown")
        chapter = question.get("chapter", "Unknown")
        label = f"Chapter {chapter}, Question {number}"
        number_key = (chapter, number)

        stem = (question.get("stem") or "").strip()

        if number_key in seen_numbers:
            original_label = seen_numbers[number_key]
            diagnostics.append(
                CompilerDiagnostic(
                    severity=DiagnosticSeverity.ADVISORY,
                    label=label,
                    message=(
                        "duplicate question number "
                        f"(original: {original_label})"
                    ),
                )
            )
        else:
            seen_numbers[number_key] = label

        if stem:
            if stem in seen_stems:
                original_label = seen_stems[stem]
                preview = stem[:120]
                diagnostics.append(
                    CompilerDiagnostic(
                        severity=DiagnosticSeverity.ADVISORY,
                        label=label,
                        message=(
                            "duplicate question text "
                            f"(original: {original_label}; stem: {preview!r})"
                        ),
                    )
                )
            else:
                seen_stems[stem] = label

        if not stem:
            diagnostics.append(
                CompilerDiagnostic(
                    severity=DiagnosticSeverity.FATAL,
                    label=label,
                    message="missing stem",
                )
            )

        if not question.get("choices"):
            diagnostics.append(
                CompilerDiagnostic(
                    severity=DiagnosticSeverity.FATAL,
                    label=label,
                    message="no answer choices",
                )
            )

        if not question.get("correct_answers"):
            diagnostics.append(
                CompilerDiagnostic(
                    severity=DiagnosticSeverity.RECOVERABLE,
                    label=label,
                    message="missing correct answer",
                )
            )

        if not question.get("rationale"):
            diagnostics.append(
                CompilerDiagnostic(
                    severity=DiagnosticSeverity.RECOVERABLE,
                    label=label,
                    message="missing rationale",
                )
            )

        if not question.get("question_type"):
            diagnostics.append(
                CompilerDiagnostic(
                    severity=DiagnosticSeverity.FATAL,
                    label=label,
                    message="missing question type",
                )
            )

    return diagnostics