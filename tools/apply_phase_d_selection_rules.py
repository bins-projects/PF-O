from pathlib import Path

app_path = Path("web/app.js")
index_path = Path("web/index.html")
app = app_path.read_text()
index = index_path.read_text()

replacements = {
    '''  selectionCount.textContent =
    `${selected} ${selected === 1 ? "chapter" : "chapters"} selected`;

  builderSelectionCount.textContent =
    `${selected} ${selected === 1 ? "chapter" : "chapters"} selected`;

  builderBookCount.textContent = selected
    ? `From ${selectedBooks} ${selectedBooks === 1 ? "book" : "books"}`
    : "Open a book to choose chapters";
''': '''  const chapterSelectionText =
    PrepFlowSelectionRules.chapterSelectionText(selected);

  selectionCount.textContent = chapterSelectionText;
  builderSelectionCount.textContent = chapterSelectionText;
  builderBookCount.textContent =
    PrepFlowSelectionRules.bookSelectionText(selected, selectedBooks);
''',
    '''    badge.textContent = count
      ? `${count} ${count === 1 ? "chapter" : "chapters"} selected`
      : "Open book";
''': '''    badge.textContent = PrepFlowSelectionRules.bookBadgeText(count);
''',
    '''  const selected = selectedChapters.size;
  status.textContent = selected
    ? `${selected} ${selected === 1 ? "chapter" : "chapters"} selected. Choose another category or return to your selected category to start.`
    : "Select a category to continue.";
''': '''  const selected = selectedChapters.size;
  status.textContent = PrepFlowSelectionRules.homeStatusText(selected);
''',
}

for old, new in replacements.items():
    if old not in app:
        raise SystemExit("Expected app.js selection block was not found.")
    app = app.replace(old, new, 1)

navigation_script = '  <script src="navigation-rules.js?v=20260721-1"></script>\n'
selection_script = '  <script src="selection-rules.js?v=20260721-1"></script>\n'
if selection_script not in index:
    if navigation_script not in index:
        raise SystemExit("Expected navigation-rules script tag was not found.")
    index = index.replace(navigation_script, navigation_script + selection_script, 1)

app_path.write_text(app)
index_path.write_text(index)
Path(__file__).unlink()
print("Phase D selection-rule integration applied.")
