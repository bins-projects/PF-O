import json
from collections import Counter

with open("output/03_questions.json", "r", encoding="utf-8") as f:
    questions = json.load(f)

texts = [q.get("stem", "").strip() for q in questions]
counts = Counter(texts)

duplicates = {text: count for text, count in counts.items() if count > 1}

print(f"Total questions: {len(questions)}")
print(f"Unique questions: {len(counts)}")
print(f"Duplicate groups: {len(duplicates)}")
print(f"Extra duplicate copies: {len(questions) - len(counts)}")

if duplicates:
    print("\nDuplicate questions found:\n")
    for i, (text, count) in enumerate(duplicates.items(), start=1):
        print(f"{i}. Appears {count} times")
        print(text)
        print("-" * 60)
else:
    print("No duplicate questions found.")

