from pathlib import Path

index_path = Path("web/index.html")
index = index_path.read_text()
link = '  <link rel="stylesheet" href="half-screen-fine-tune.css?v=20260721-1">\n'
anchor = '  <link rel="stylesheet" href="order-mode.css?v=20260721-1">\n'
if link not in index:
    if anchor not in index:
        raise SystemExit("stylesheet anchor not found")
    index = index.replace(anchor, anchor + link, 1)
    index_path.write_text(index)

Path("web/half-screen-fine-tune.css").write_text(r'''/* Final half-screen proportion tuning. */
@media (min-width: 900px) and (max-width: 1280px) {
  .pixel-stage {
    min-height: clamp(620px, 84vh, 760px) !important;
    padding-bottom: 18px !important;
  }

  #home-launcher {
    width: min(365px, 31vw) !important;
    transform: scale(.94) !important;
    transform-origin: top left !important;
  }

  .pixel-logo {
    transform: translateX(16px) scale(.9) !important;
    transform-origin: top center !important;
  }

  .reference-library-callout {
    transform: scale(.92) !important;
    transform-origin: top right !important;
  }

  .subjects {
    margin-top: -128px !important;
    gap: clamp(54px, 7vw, 86px) !important;
    align-items: end !important;
  }

  .subject-card {
    transform: scale(.93) !important;
    transform-origin: bottom center !important;
  }

  .subject-card:hover,
  .subject-card:focus-visible {
    transform: translateY(-6px) scale(.93) !important;
  }
}
''')

Path(__file__).unlink()
print("Half-screen proportions fine-tuned; helper removed.")
