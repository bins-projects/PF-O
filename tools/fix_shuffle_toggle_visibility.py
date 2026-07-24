from pathlib import Path

path = Path("web/app.js")
text = path.read_text()
old = '''rightHomeControls.append(
  document.querySelector(".builder-block-size"),
  buildQuizButton,
  resumeSessionButton
);
'''
new = '''rightHomeControls.append(
  document.querySelector(".builder-block-size"),
  document.querySelector(".order-mode-toggle"),
  buildQuizButton,
  resumeSessionButton
);
'''
if old not in text:
    raise SystemExit("Expected right-side control stack block not found.")
path.write_text(text.replace(old, new, 1))
print("Shuffle toggle moved into the visible right-side control stack.")
