from dataclasses import dataclass
from enum import Enum


class DiagnosticSeverity(str, Enum):
    FATAL = "fatal"
    RECOVERABLE = "recoverable"
    ADVISORY = "advisory"


@dataclass
class CompilerDiagnostic:
    severity: DiagnosticSeverity
    label: str
    message: str