from pathlib import Path

path = Path("web/app.js")
text = path.read_text()

old = '''  clearSavedSession();
  selectedChapters.clear();
  showSubjects();
'''
new = '''  clearSavedSession();
  selectedChapters.clear();
  updateSelectionStatus();
  showSubjects();
'''
count = text.count(old)
if count < 2:
    raise SystemExit(f"Expected at least 2 selection-clear paths, found {count}")
text = text.replace(old, new)
path.write_text(text)

print(f"Updated {count} selection-clear paths.")
