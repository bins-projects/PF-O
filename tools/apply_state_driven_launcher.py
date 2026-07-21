from pathlib import Path


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        raise SystemExit(f"Expected block not found: {label}")
    return text.replace(old, new, 1)


index_path = Path("web/index.html")
index = index_path.read_text()
index = replace_once(
    index,
    '  <link rel="stylesheet" href="order-mode.css?v=20260721-1">\n',
    '  <link rel="stylesheet" href="order-mode.css?v=20260721-1">\n  <link rel="stylesheet" href="home-launcher.css?v=20260721-1">\n',
    "launcher stylesheet",
)

launcher = '''
        <section id="home-launcher" class="home-launcher" aria-label="Quiz controls">
          <section id="quiz-builder" class="launcher-view launcher-setup" aria-label="Quiz setup">
            <div class="home-quiz-copy">
              <strong>Build Your Quiz</strong>
              <span>Select chapters from the books below, then start your quiz.</span>
              <small id="builder-selection-count">0 chapters selected</small>
              <span id="builder-book-count" class="sr-only">Open a book to choose chapters</span>
            </div>

            <label class="builder-block-size home-block-size">
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
              <span>Source Order</span>
              <input id="shuffle-questions" type="checkbox" checked>
              <span class="order-mode-track" aria-hidden="true"><span></span></span>
              <span>Shuffle</span>
            </label>

            <div class="launcher-actions">
              <button id="clear-selections" class="home-clear-selections" disabled>Clear Selection</button>
              <button id="build-quiz" class="home-start-quiz" disabled>Start Quiz <span aria-hidden="true">▶</span></button>
            </div>
          </section>

          <section id="resume-panel" class="launcher-view launcher-resume" aria-label="Saved quiz" hidden>
            <div class="resume-copy">
              <span class="resume-star" aria-hidden="true">★</span>
              <div>
                <strong>Quiz in Progress</strong>
                <p id="resume-description"></p>
              </div>
            </div>
            <button id="resume-session" class="home-start-quiz">Continue Quiz <span aria-hidden="true">▶</span></button>
            <button id="discard-session" class="home-clear-selections">Start Over</button>
          </section>
        </section>
'''

index = replace_once(
    index,
    '        <p class="pixel-tagline">Study. Practice. Master.</p>\n',
    '        <p class="pixel-tagline">Study. Practice. Master.</p>\n' + launcher,
    "launcher placement",
)

old_controls = '''    <section id="quiz-builder" class="quiz-builder" aria-label="Quiz setup">
      <div class="builder-summary">
        <strong id="builder-selection-count">0 chapters selected</strong>
        <span id="builder-book-count">Open a book to choose chapters</span>
      </div>

      <label class="builder-block-size">
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

      <button id="clear-selections" class="secondary-button" disabled>Clear Selections</button>
      <button id="build-quiz" class="start-button" disabled>Build Quiz ▶</button>
    </section>

    <section id="resume-panel" class="resume-panel" hidden>
      <div class="resume-copy">
        <span class="resume-star" aria-hidden="true">★</span>
        <div>
          <strong>Continue your saved session</strong>
          <p id="resume-description"></p>
        </div>
      </div>
      <button id="resume-session" class="start-button">Continue Session</button>
      <button id="discard-session" class="secondary-button">Start Over</button>
    </section>

'''
index = replace_once(index, old_controls, "old home controls")
index_path.write_text(index)

app_path = Path("web/app.js")
app = app_path.read_text()
app = replace_once(
    app,
    'const status = document.querySelector("#status");\n',
    'const status = document.querySelector("#status");\nconst homeLauncher = document.querySelector("#home-launcher");\n',
    "launcher query",
)

old_relocation = '''const pixelStage = document.querySelector(".pixel-stage");

const leftHomeControls = document.createElement("div");
leftHomeControls.className = "home-control-stack home-control-stack-left";

const rightHomeControls = document.createElement("div");
rightHomeControls.className = "home-control-stack home-control-stack-right";

pixelStage.append(leftHomeControls, rightHomeControls);

leftHomeControls.append(
  document.querySelector(".builder-summary"),
  clearSelectionsButton,
  discardSessionButton
);

rightHomeControls.append(
  document.querySelector(".builder-block-size"),
  document.querySelector(".order-mode-toggle"),
  buildQuizButton,
  resumeSessionButton
);

/* The original containers remain only as hidden structural shells. */
quizBuilder.hidden = true;
resumePanel.hidden = true;

'''
app = replace_once(app, old_relocation, "DOM relocation workaround")

old_refresh = '''function refreshResumePanel() {
  const saved = readSavedSession();
  const hasSavedSession = Boolean(saved);

  resumeSessionButton.hidden = !hasSavedSession;
  discardSessionButton.hidden = !hasSavedSession;

  if (!saved) {
    resumeDescription.textContent = "";
    return;
  }

  const description = PrepFlowResumeRules.resumeDescription(saved);

  resumeDescription.textContent = description;
  resumeSessionButton.title = description;
  resumeSessionButton.setAttribute(
    "aria-label",
    PrepFlowResumeRules.resumeAriaLabel(description)
  );
}
'''
new_refresh = '''function refreshResumePanel() {
  const saved = readSavedSession();
  const hasSavedSession = Boolean(saved);

  quizBuilder.hidden = hasSavedSession;
  resumePanel.hidden = !hasSavedSession;
  subjects.classList.toggle("saved-session-active", hasSavedSession);

  document.querySelectorAll(".subject-card").forEach((book) => {
    book.disabled = hasSavedSession;
  });

  if (!saved) {
    resumeDescription.textContent = "";
    return;
  }

  const description = PrepFlowResumeRules.resumeDescription(saved);

  resumeDescription.textContent = description;
  resumeSessionButton.title = description;
  resumeSessionButton.setAttribute(
    "aria-label",
    PrepFlowResumeRules.resumeAriaLabel(description)
  );
}
'''
app = replace_once(app, old_refresh, new_refresh, "saved/setup launcher modes")

app = replace_once(
    app,
    '  quizBuilder.hidden = true;\n  resumePanel.hidden = true;\n',
    '  homeLauncher.hidden = true;\n  quizBuilder.hidden = true;\n  resumePanel.hidden = true;\n',
    "hide launcher",
)

old_show = '''  hero.hidden = false;
  subjects.hidden = false;
  quizBuilder.hidden = false;
  status.hidden = true;
'''
new_show = '''  hero.hidden = false;
  subjects.hidden = false;
  homeLauncher.hidden = false;
  status.hidden = true;
'''
app = replace_once(app, old_show, new_show, "show launcher")
app_path.write_text(app)

Path("web/home-launcher.css").write_text('''.home-launcher {
  position: absolute;
  z-index: 5;
  top: 188px;
  left: 34px;
  width: min(430px, calc(50% - 58px));
  color: #f7fbff;
  font-family: "Courier New", monospace;
}

.launcher-view {
  display: grid;
  gap: 13px;
  padding: 18px;
  border: 3px solid #28bdf2;
  background: linear-gradient(rgba(255,255,255,.024) 50%, transparent 50%) 0 0/100% 4px, rgba(5,10,34,.96);
  box-shadow: 0 0 0 3px #080c25, 0 0 0 6px rgba(40,189,242,.35), 0 10px 0 rgba(0,0,0,.22);
  text-align: left;
}

.home-quiz-copy {
  display: grid;
  gap: 5px;
}

.home-quiz-copy strong,
.launcher-resume .resume-copy strong {
  color: #fff;
  font-size: 1.1rem;
  font-weight: 900;
  letter-spacing: .06em;
  text-transform: uppercase;
  text-shadow: 3px 3px 0 #10183f;
}

.home-quiz-copy > span:not(.sr-only),
.launcher-resume p {
  margin: 0;
  color: #c8dcff;
  font-size: .76rem;
  line-height: 1.4;
}

.home-quiz-copy small {
  color: #28bdf2;
  font-size: .78rem;
  font-weight: 900;
  letter-spacing: .05em;
  text-transform: uppercase;
}

.home-block-size {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
  padding: 10px 12px;
  border: 2px solid #4d6eb8;
  background: #080d22;
  color: #dbe9ff;
  font-size: .72rem;
  font-weight: 900;
  letter-spacing: .04em;
  text-transform: uppercase;
}

.home-block-size select {
  width: 66px;
  padding: 8px;
  border: 2px solid #72d63c;
  background: #080d22;
  color: #fff;
  font: inherit;
}

.launcher-actions {
  display: grid;
  grid-template-columns: minmax(0, 1fr) 150px;
  gap: 12px;
  align-items: stretch;
}

.home-start-quiz {
  min-width: 0;
  padding: 12px;
  border: 3px solid #72d63c;
  background: linear-gradient(180deg,#174f38,#0c2e25);
  color: #eaffdf;
  font: 900 .93rem "Courier New", monospace;
  letter-spacing: .06em;
  text-transform: uppercase;
  box-shadow: 0 0 0 3px #07151a, 0 0 16px rgba(114,214,60,.28);
  cursor: pointer;
}

.home-start-quiz:disabled {
  filter: grayscale(.7);
  opacity: .48;
  cursor: not-allowed;
}

.home-clear-selections {
  justify-self: start;
  padding: 8px 0;
  border: 0;
  background: transparent;
  color: #9cb2d7;
  font: 900 .7rem "Courier New", monospace;
  text-decoration: underline;
  text-transform: uppercase;
  cursor: pointer;
}

.home-clear-selections:disabled {
  opacity: .35;
  cursor: not-allowed;
}

.launcher-resume .resume-copy {
  display: grid;
  grid-template-columns: auto 1fr;
  gap: 12px;
  align-items: start;
}

.launcher-resume .resume-star {
  color: #ffd45c;
  font-size: 1.6rem;
}

.launcher-resume .home-start-quiz,
.launcher-resume .home-clear-selections {
  width: 100%;
  justify-self: stretch;
}

.subjects.saved-session-active .subject-card {
  opacity: .42;
  filter: grayscale(.65);
  cursor: default;
}

@media (max-width: 900px) {
  .home-launcher {
    top: 182px;
    left: 20px;
    width: calc(55% - 30px);
  }

  .launcher-actions {
    grid-template-columns: 1fr;
  }
}
''')

Path(__file__).unlink()
print("State-driven left launcher applied.")
