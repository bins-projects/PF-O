from pathlib import Path


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        raise SystemExit(f"Expected block not found: {label}")
    return text.replace(old, new, 1)


index_path = Path("web/index.html")
index = index_path.read_text()
index = replace_once(
    index,
    '  <link rel="stylesheet" href="reference-home.css">\n',
    '  <link rel="stylesheet" href="reference-home.css">\n  <link rel="stylesheet" href="order-mode.css?v=20260721-1">\n',
    "order-mode stylesheet",
)
index = replace_once(
    index,
    '''      <label class="builder-block-size">
        <span>Questions per block</span>
        <select id="global-block-size">
          <option value="1">1</option>
          <option value="3">3</option>
          <option value="5">5</option>
          <option value="10">10</option>
          <option value="15" selected>15</option>
        </select>
      </label>

''',
    '''      <label class="builder-block-size">
        <span>Questions per block</span>
        <select id="global-block-size">
          <option value="1">1</option>
          <option value="3">3</option>
          <option value="5">5</option>
          <option value="10">10</option>
          <option value="15" selected>15</option>
        </select>
      </label>

      <label class="order-mode-toggle" for="shuffle-questions">
        <span>Keep Source Order</span>
        <input id="shuffle-questions" type="checkbox" checked>
        <span class="order-mode-track" aria-hidden="true"><span></span></span>
        <span>Shuffle Questions</span>
      </label>

''',
    "quiz order toggle",
)
index = replace_once(
    index,
    '  <script src="display-rules.js?v=20260721-1"></script>\n',
    '  <script src="display-rules.js?v=20260721-1"></script>\n  <script src="order-rules.js?v=20260721-1"></script>\n',
    "order rules script",
)
index_path.write_text(index)

app_path = Path("web/app.js")
app = app_path.read_text()
app = replace_once(
    app,
    'const globalBlockSizeSelect = document.querySelector("#global-block-size");\n',
    'const globalBlockSizeSelect = document.querySelector("#global-block-size");\nconst shuffleQuestionsToggle = document.querySelector("#shuffle-questions");\n',
    "shuffle toggle query",
)
app = replace_once(
    app,
    'let sessionBlockSize = 15;\n',
    'let sessionBlockSize = 15;\nlet sessionShuffleQuestions = true;\n',
    "session order state",
)
app = replace_once(
    app,
    '''function shuffle(items) {
  const copy = [...items];

  for (let index = copy.length - 1; index > 0; index -= 1) {
    const randomIndex = Math.floor(Math.random() * (index + 1));
    [copy[index], copy[randomIndex]] = [copy[randomIndex], copy[index]];
  }

  return copy;
}

''',
    '',
    "old inline shuffle",
)
app = replace_once(
    app,
    '    sessionBlockSize,\n',
    '    sessionBlockSize,\n    sessionShuffleQuestions,\n',
    "saved order mode",
)
app = replace_once(
    app,
    '  sessionQuestions = shuffle(selectedQuestions);\n',
    '''  sessionShuffleQuestions = shuffleQuestionsToggle.checked;
  sessionQuestions = PrepFlowOrderRules.orderQuestions(
    selectedQuestions,
    sessionShuffleQuestions
  );
''',
    "session ordering",
)
app = replace_once(
    app,
    '    sessionQuestions = saved.sessionQuestions || [];\n',
    '''    sessionQuestions = saved.sessionQuestions || [];
    sessionShuffleQuestions = saved.sessionShuffleQuestions !== false;
    shuffleQuestionsToggle.checked = sessionShuffleQuestions;
''',
    "resume order mode",
)
app_path.write_text(app)

Path("web/order-rules.js").write_text('''(function (global) {
  function shuffledCopy(items, random = Math.random) {
    const copy = [...items];

    for (let index = copy.length - 1; index > 0; index -= 1) {
      const randomIndex = Math.floor(random() * (index + 1));
      [copy[index], copy[randomIndex]] = [copy[randomIndex], copy[index]];
    }

    return copy;
  }

  function orderQuestions(items, shouldShuffle, random = Math.random) {
    return shouldShuffle ? shuffledCopy(items, random) : [...items];
  }

  global.PrepFlowOrderRules = {
    orderQuestions,
  };
})(window);
''')

Path("web/order-mode.css").write_text('''.order-mode-toggle {
  display: grid;
  grid-template-columns: auto 46px auto;
  align-items: center;
  justify-content: center;
  gap: 9px;
  color: #c8dcff;
  font-size: .72rem;
  font-weight: 900;
  letter-spacing: .025em;
}

.order-mode-toggle input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.order-mode-track {
  width: 46px;
  height: 24px;
  padding: 3px;
  border: 2px solid #4d6eb8;
  background: #080d22;
  cursor: pointer;
}

.order-mode-track > span {
  display: block;
  width: 14px;
  height: 14px;
  background: #9cb2d7;
  transition: transform .15s ease, background .15s ease;
}

.order-mode-toggle input:checked + .order-mode-track > span {
  transform: translateX(20px);
  background: #72d63c;
}

.order-mode-toggle input:focus-visible + .order-mode-track {
  outline: 3px solid #28bdf2;
  outline-offset: 3px;
}

@media (max-width: 700px) {
  .order-mode-toggle {
    grid-template-columns: 1fr 46px 1fr;
    font-size: .66rem;
  }
}
''')

Path("web/order-rules.test.html").write_text('''<!doctype html>
<meta charset="utf-8">
<title>PrepFlow order rules tests</title>
<pre id="results"></pre>
<script src="order-rules.js"></script>
<script>
  const results = document.querySelector("#results");
  let passed = 0;

  function test(name, run) {
    try {
      run();
      passed += 1;
      results.textContent += `PASS ${name}\\n`;
    } catch (error) {
      results.textContent += `FAIL ${name}: ${error.message}\\n`;
    }
  }

  function equal(actual, expected) {
    if (JSON.stringify(actual) !== JSON.stringify(expected)) {
      throw new Error(`${JSON.stringify(actual)} !== ${JSON.stringify(expected)}`);
    }
  }

  const source = ["a", "b", "c", "d"];

  test("source order stays unchanged when shuffle is off", () => {
    equal(PrepFlowOrderRules.orderQuestions(source, false), source);
  });

  test("ordering never mutates the selected pool", () => {
    const original = [...source];
    PrepFlowOrderRules.orderQuestions(source, true, () => 0);
    equal(source, original);
  });

  test("shuffle preserves every selected question", () => {
    const ordered = PrepFlowOrderRules.orderQuestions(source, true, () => 0);
    equal([...ordered].sort(), [...source].sort());
  });

  test("shuffle uses a stable copied session order", () => {
    const ordered = PrepFlowOrderRules.orderQuestions(source, true, () => 0);
    equal(ordered, ["b", "c", "d", "a"]);
  });

  results.textContent += `\\n${passed}/4 tests passed.\\n`;
</script>
''')

print("Shuffle / source-order toggle files applied.")
