import json
import re
from pathlib import Path

CLEAN_PATH = Path("scratch/pharm_clean.txt")
OUT_PATH = Path("scratch/pharm_module.json")

chapter_re = re.compile(r"^Chapter\s+(\d+):\s+(.+)$")
question_re = re.compile(r"^(\d+)\.\s+(?=[A-Z])(.+)$")
choice_re = re.compile(r"^([a-f])\.\s+(.+)$", re.IGNORECASE)
source_section_re = re.compile(r"^(MULTIPLE CHOICE|MULTIPLE RESPONSE|COMPLETION|ORDERING)$", re.IGNORECASE)

def main():
    lines = CLEAN_PATH.read_text(encoding="utf-8").splitlines()

    chapter = None
    chapter_title = None
    questions = []
    current = None
    section = None
    source_section = None
    answer_pending = False

    for raw in lines:
        line = raw.strip()
        if not line or line == ".":
            continue

        m = chapter_re.match(line)
        if m:
            chapter = int(m.group(1))
            chapter_title = m.group(2)
            source_section = None
            answer_pending = False
            continue

        m = source_section_re.match(line)
        if m:
            source_section = m.group(1).lower().replace(" ", "_")
            continue

        m = question_re.match(line)
        if m:
            if current:
                questions.append(current)

            current = {
                "source": "pharm",
                "chapter": chapter,
                "chapter_title": chapter_title,
                "question_number": int(m.group(1)),
                "section": source_section,
                "source_question_number": int(m.group(1)),
                "type": source_section or "unknown",
                "stem": m.group(2),
                "choices": {},
                "answer": [],
                "rationale": "",
                "metadata": "",
            }
            section = "stem"
            continue

        if not current:
            continue

        m = choice_re.match(line)
        if m:
            section = "choices"
            current["choices"][m.group(1).lower()] = m.group(2)
            continue

        if line.startswith("ANS:"):
            ans = line.replace("ANS:", "").strip()
            if ans:
                current["answer"] = [a.strip().lower() for a in ans.split(",") if a.strip()]
                section = "rationale"
            else:
                answer_pending = True
                section = "answer"
            continue

        if answer_pending:
            current["answer"] = [line.strip()]
            answer_pending = False
            section = "rationale"
            continue

        if line.startswith("DIF:"):
            section = "metadata"
            current["metadata"] = line
            continue

        if section == "stem":
            current["stem"] += " " + line
        elif section == "choices":
            # continuation of previous choice
            if current["choices"]:
                last = list(current["choices"])[-1]
                current["choices"][last] += " " + line
        elif section == "rationale":
            current["rationale"] += (" " if current["rationale"] else "") + line
        elif section == "metadata":
            current["metadata"] += " " + line

    if current:
        questions.append(current)

    OUT_PATH.write_text(json.dumps(questions, indent=2), encoding="utf-8")
    print(f"Parsed {len(questions)} questions")
    print(f"Wrote parsed module data: {OUT_PATH}")

if __name__ == "__main__":
    main()
