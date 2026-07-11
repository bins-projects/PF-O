from dataclasses import dataclass
from pathlib import Path
import re

from compiler.cleaner import clean_text
from compiler.pdf_reader import read_pdf


PACK_ID_RE = re.compile(r"^[a-z0-9]+(?:[-_][a-z0-9]+)*$")


@dataclass(frozen=True)
class ImportRequest:
    source_path: Path
    pack_id: str
    title: str
    workspace_root: Path = Path("output/imports")


@dataclass(frozen=True)
class ExtractionResult:
    request: ImportRequest
    source_type: str
    raw_text: str
    raw_artifact: Path


@dataclass(frozen=True)
class CleaningResult:
    extraction: ExtractionResult
    cleaned_text: str
    cleaned_artifact: Path


def validate_request(request: ImportRequest) -> None:
    if not request.pack_id:
        raise ValueError("Pack ID cannot be empty.")

    if not PACK_ID_RE.fullmatch(request.pack_id):
        raise ValueError(
            "Pack ID must contain lowercase letters, numbers, "
            "hyphens, or underscores."
        )

    if not request.title.strip():
        raise ValueError("Pack title cannot be empty.")


def detect_source_type(source_path: Path) -> str:
    suffix = source_path.suffix.lower()

    if suffix == ".pdf":
        return "pdf"

    raise ValueError(f"Unsupported source file type: {suffix or '[none]'}")


def extract_source(request: ImportRequest) -> ExtractionResult:
    """
    Begin an agnostic PrepFlow import.

    This stage detects the source format, extracts raw text, and writes an
    inspectable artifact. Cleaning, structure detection, and parsing belong
    to later importer stages.
    """
    validate_request(request)

    source_type = detect_source_type(request.source_path)

    if source_type == "pdf":
        raw_text = read_pdf(request.source_path)
    else:
        raise AssertionError(f"Unhandled source type: {source_type}")

    workspace = request.workspace_root / request.pack_id
    workspace.mkdir(parents=True, exist_ok=True)

    raw_artifact = workspace / "01_raw.txt"
    raw_artifact.write_text(raw_text, encoding="utf-8")

    return ExtractionResult(
        request=request,
        source_type=source_type,
        raw_text=raw_text,
        raw_artifact=raw_artifact,
    )

def clean_extraction(extraction: ExtractionResult) -> CleaningResult:
    """Clean extracted source text and preserve an inspectable artifact."""
    cleaned_text = clean_text(extraction.raw_text)

    cleaned_artifact = (
        extraction.raw_artifact.parent / "02_clean.txt"
    )
    cleaned_artifact.write_text(cleaned_text, encoding="utf-8")

    return CleaningResult(
        extraction=extraction,
        cleaned_text=cleaned_text,
        cleaned_artifact=cleaned_artifact,
    )
