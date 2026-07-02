# PrepFlow Restart Packet

Read these first (source of truth):

1. PROJECT_STATE.md
2. CHANGELOG.md
3. VISION.md

----------------------------------------

Project:
PrepFlow

Current Version:
0.6.1

Current Sprint:
Sprint 6 — Content Import Pipeline

Status:
Importer prototype complete.

----------------------------------------

Repository Status

- GitHub synced
- Working tree clean
- Sprint checkpoint complete

Always verify first:

git status

Expected:
working tree clean

----------------------------------------

Completed This Session

✓ Med-Surg PDF successfully imported with pypdf
✓ 483 pages verified
✓ ~1.08 million characters extracted
✓ Chapter detection working
✓ 63 chapters detected
✓ Inventory generated for every chapter
✓ Counts MC / SATA / Ordered / Completion
✓ Inventory exported to JSON
✓ Importer committed to GitHub
✓ source_banks ignored by Git
✓ Both Med-Surg and Pharm PDFs stored locally

----------------------------------------

Current Source Banks

source_banks/

medsurg_test_bank.pdf

pharm_test_bank.pdf

These stay LOCAL.
Never commit them to GitHub.

----------------------------------------

Current Objective

Replace the inventory prototype with the production importer.

Goals:

• Parse every question
• Build Question objects
• Preserve rationale and metadata
• Export JSON pack
• Validate output
• Feed directly into PrepFlow compiler

----------------------------------------

Next Coding Session

Primary file:

tools/import_medsurg_bank.py

After that:

compiler/
study/
validator/

----------------------------------------

Immediate Next Goal

Instead of counting questions, actually create Question objects.

For each question capture:

- chapter
- question number
- question type
- prompt
- answer choices
- correct answer
- rationale
- objective
- NCLEX category
- metadata

Output:

output/medsurg_questions.json

----------------------------------------

Long-Term Pipeline

PDF
↓

Importer

↓

Question Objects

↓

Pack Compiler

↓

Validation

↓

PrepFlow Pack

↓

Study Engine

----------------------------------------

First commands next session

git status

python tools/import_medsurg_bank.py

----------------------------------------

Important

The inventory importer is complete.

Do NOT rebuild it.

Continue by replacing the inventory logic with the production parser.