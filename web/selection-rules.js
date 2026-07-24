(function () {
  function pluralize(count, singular, plural) {
    return `${count} ${count === 1 ? singular : plural}`;
  }

  function chapterSelectionText(selected) {
    return `${pluralize(selected, "chapter", "chapters")} selected`;
  }

  function bookSelectionText(selected, selectedBooks) {
    return selected
      ? `From ${pluralize(selectedBooks, "book", "books")}`
      : "Open a book to choose chapters";
  }

  function bookBadgeText(count) {
    return count
      ? `${pluralize(count, "chapter", "chapters")} selected`
      : "Open book";
  }

  function homeStatusText(selected) {
    return selected
      ? `${pluralize(selected, "chapter", "chapters")} selected. Choose another category or return to your selected category to start.`
      : "Select a category to continue.";
  }

  window.PrepFlowSelectionRules = {
    chapterSelectionText,
    bookSelectionText,
    bookBadgeText,
    homeStatusText,
  };
}());
