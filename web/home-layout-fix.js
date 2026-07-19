(() => {
  const pixelStage = document.querySelector(".pixel-stage");
  const quizBuilder = document.querySelector("#quiz-builder");
  const resumePanel = document.querySelector("#resume-panel");
  const quizCopy = document.querySelector(".home-quiz-copy");
  const blockSize = document.querySelector(".builder-block-size");
  const clearButton = document.querySelector("#clear-selections");
  const buildButton = document.querySelector("#build-quiz");
  const resumeButton = document.querySelector("#resume-session");
  const discardButton = document.querySelector("#discard-session");

  if (!pixelStage || !quizBuilder || !quizCopy || !blockSize || !buildButton) return;

  if (resumePanel) {
    if (resumeButton) resumePanel.append(resumeButton);
    if (discardButton) resumePanel.append(discardButton);
  }

  const actionRow = document.createElement("div");
  actionRow.append(blockSize, buildButton);

  const footerRow = document.createElement("div");
  if (clearButton) footerRow.append(clearButton);

  quizBuilder.replaceChildren(quizCopy, actionRow, footerRow);
  pixelStage.append(quizBuilder);

  quizBuilder.removeAttribute("hidden");
  quizBuilder.style.cssText = [
    "position:absolute",
    "z-index:5",
    "top:190px",
    "left:34px",
    "width:430px",
    "max-width:calc(50% - 58px)",
    "min-width:0",
    "display:flex",
    "flex-direction:column",
    "gap:12px",
    "padding:18px",
    "border:3px solid #28bdf2",
    "background:rgba(5,10,34,.94)",
    "box-shadow:0 0 0 3px #080c25,0 0 0 6px rgba(40,189,242,.35),0 10px 0 rgba(0,0,0,.22)",
    "color:#f7fbff",
    "font-family:'Courier New',monospace",
    "text-align:left",
    "visibility:visible",
    "opacity:1"
  ].join(";");

  quizCopy.style.cssText = "display:flex;flex-direction:column;gap:5px;position:static;margin:0;padding:0;text-align:left";
  const title = quizCopy.querySelector("strong");
  const instructions = quizCopy.querySelector("span:not(.sr-only)");
  const selection = quizCopy.querySelector("small");
  if (title) title.style.cssText = "display:block;color:#fff;font-size:18px;font-weight:900;letter-spacing:.06em;text-transform:uppercase";
  if (instructions) instructions.style.cssText = "display:block;color:#c8dcff;font-size:12px;line-height:1.35;text-transform:none";
  if (selection) selection.style.cssText = "display:block;color:#28bdf2;font-size:12px;font-weight:900;letter-spacing:.05em;text-transform:uppercase";

  actionRow.style.cssText = "display:grid;grid-template-columns:minmax(0,1fr) 150px;gap:12px;align-items:stretch";
  blockSize.style.cssText = "display:flex;align-items:center;justify-content:space-between;gap:10px;position:static;margin:0;padding:10px 12px;border:2px solid #4d6eb8;background:#080d22;color:#dbe9ff;font-size:11px;font-weight:900;letter-spacing:.04em;text-transform:uppercase";
  const select = blockSize.querySelector("select");
  if (select) select.style.cssText = "width:66px;padding:8px;border:2px solid #72d63c;background:#080d22;color:#fff;font:inherit";

  buildButton.style.cssText = "position:static;width:auto;min-width:0;margin:0;padding:12px;border:3px solid #72d63c;background:linear-gradient(180deg,#174f38,#0c2e25);color:#eaffdf;font-family:'Courier New',monospace;font-size:15px;font-weight:900;letter-spacing:.06em;text-transform:uppercase;box-shadow:0 0 0 3px #07151a,0 0 16px rgba(114,214,60,.28)";

  footerRow.style.cssText = "display:flex;justify-content:flex-start;min-height:16px";
  if (clearButton) clearButton.style.cssText = "position:static;margin:0;padding:0;border:0;background:transparent;color:#9cb2d7;font-family:'Courier New',monospace;font-size:11px;font-weight:900;text-decoration:underline;text-transform:uppercase";

  document.querySelectorAll(".home-control-stack").forEach((stack) => stack.remove());
})();
