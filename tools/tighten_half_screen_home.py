from pathlib import Path

index_path = Path("web/index.html")
index = index_path.read_text()
link = '  <link rel="stylesheet" href="responsive-home.css?v=20260721-2">\n'
if "responsive-home.css" not in index:
    index = index.replace("</head>", link + "</head>", 1)
    index_path.write_text(index)

css_path = Path("web/responsive-home.css")
css = css_path.read_text() if css_path.exists() else ""
marker = "/* Half-screen composition refinement */"
block = r'''

/* Half-screen composition refinement */
@media (min-width: 760px) and (max-width: 1280px) {
  .pixel-stage {
    min-height: 700px !important;
  }

  .pixel-logo {
    top: 34px !important;
    left: 52% !important;
    transform: translateX(-50%) scale(.78) !important;
    transform-origin: top center !important;
  }

  .pixel-tagline {
    top: 42px !important;
    left: 52% !important;
    transform: translateX(-50%) scale(.88) !important;
    transform-origin: top center !important;
  }

  #home-launcher {
    top: 30px !important;
    left: 22px !important;
    width: min(370px, 36vw) !important;
    padding: 14px 16px !important;
  }

  #home-launcher h2,
  #home-launcher .launcher-title {
    font-size: 18px !important;
    margin-bottom: 5px !important;
  }

  #home-launcher p,
  #home-launcher .launcher-copy {
    font-size: 11px !important;
    line-height: 1.35 !important;
    margin-bottom: 8px !important;
  }

  #home-launcher .launcher-view {
    gap: 8px !important;
  }

  #home-launcher .builder-block-size,
  #home-launcher .order-mode-control {
    min-height: 42px !important;
  }

  #home-launcher .launcher-actions,
  #home-launcher .builder-actions {
    gap: 8px !important;
  }

  #home-launcher button {
    min-height: 38px !important;
  }

  .reference-library-callout {
    top: 178px !important;
    right: 28px !important;
    transform: scale(.88) !important;
    transform-origin: top right !important;
  }

  .subjects {
    margin-top: -210px !important;
    gap: clamp(34px, 5vw, 70px) !important;
    transform: scale(.88) !important;
    transform-origin: top center !important;
  }
}

@media (min-width: 760px) and (max-width: 980px) {
  #home-launcher {
    width: 340px !important;
  }

  .pixel-logo,
  .pixel-tagline {
    left: 65% !important;
  }

  .subjects {
    margin-top: -185px !important;
    transform: scale(.78) !important;
  }
}
'''
if marker not in css:
    css_path.write_text(css + block)

Path(__file__).unlink()
print("Half-screen composition tightened; helper removed.")
