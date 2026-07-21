from pathlib import Path

index_path = Path("web/index.html")
index = index_path.read_text()
link = '  <link rel="stylesheet" href="final-home-alignment.css?v=20260721-1">\n'
anchor = '  <link rel="stylesheet" href="order-mode.css?v=20260721-1">\n'
if link not in index:
    if anchor not in index:
        raise SystemExit("order-mode stylesheet link not found")
    index = index.replace(anchor, anchor + link, 1)
    index_path.write_text(index)

Path("web/final-home-alignment.css").write_text(r'''/* Final fluid home alignment pass. */
.pixel-stage {
  position: relative !important;
}

/* Keep the tagline and logo visually locked as one composition. */
.pixel-logo {
  left: 50% !important;
  top: clamp(54px, 7vh, 92px) !important;
  transform: translateX(-50%) scale(clamp(.72, calc(.58 + 0.18vw), 1)) !important;
  transform-origin: top center !important;
  white-space: nowrap !important;
}

.pixel-tagline {
  left: 50% !important;
  top: clamp(30px, 4.3vh, 58px) !important;
  transform: translateX(-50%) scale(clamp(.78, calc(.66 + 0.12vw), 1)) !important;
  transform-origin: top center !important;
  white-space: nowrap !important;
}

/* Smaller, quieter launcher with the same crisp arcade language. */
#home-launcher {
  left: clamp(18px, 4vw, 72px) !important;
  top: clamp(28px, 7vh, 96px) !important;
  width: clamp(330px, 29vw, 430px) !important;
  max-width: calc(100% - 36px) !important;
}

#home-launcher .launcher-view {
  padding: clamp(16px, 1.45vw, 22px) !important;
  gap: clamp(10px, 1.1vh, 15px) !important;
}

#home-launcher h2 {
  font-size: clamp(17px, 1.15vw, 21px) !important;
  margin-bottom: 2px !important;
}

#home-launcher p,
#home-launcher label,
#home-launcher button,
#home-launcher select {
  font-size: clamp(10px, .72vw, 13px) !important;
}

#home-launcher .launcher-actions {
  gap: 10px !important;
}

.reference-library-callout {
  right: clamp(18px, 4vw, 70px) !important;
  top: clamp(88px, 14vh, 164px) !important;
  transform: scale(clamp(.82, calc(.72 + 0.12vw), 1)) !important;
  transform-origin: top right !important;
}

/* Preserve breathing room around the books as the window narrows. */
.subjects {
  gap: clamp(34px, 7vw, 112px) !important;
  margin-top: clamp(-94px, -8vh, -58px) !important;
}

@media (max-width: 1180px) {
  .pixel-logo {
    left: 57% !important;
    top: 42px !important;
    transform: translateX(-50%) scale(.78) !important;
  }

  .pixel-tagline {
    left: 57% !important;
    top: 24px !important;
    transform: translateX(-50%) scale(.82) !important;
  }

  #home-launcher {
    left: 16px !important;
    top: 24px !important;
    width: clamp(300px, 39vw, 370px) !important;
  }

  .reference-library-callout {
    right: 14px !important;
    top: 116px !important;
    transform: scale(.82) !important;
  }

  .subjects {
    gap: clamp(28px, 5vw, 58px) !important;
  }

  .subject-card {
    transform: scale(.9) !important;
    transform-origin: bottom center !important;
  }

  .subject-card:hover,
  .subject-card:focus-visible {
    transform: translateY(-6px) scale(.9) !important;
  }
}

@media (max-width: 860px) {
  .pixel-logo {
    left: 64% !important;
    top: 28px !important;
    transform: translateX(-50%) scale(.62) !important;
  }

  .pixel-tagline {
    left: 64% !important;
    top: 14px !important;
    transform: translateX(-50%) scale(.68) !important;
  }

  #home-launcher {
    left: 12px !important;
    top: 14px !important;
    width: min(310px, 40vw) !important;
  }

  #home-launcher .launcher-view {
    padding: 13px !important;
    gap: 8px !important;
  }

  .reference-library-callout {
    right: 8px !important;
    top: 94px !important;
    transform: scale(.68) !important;
  }

  .subjects {
    width: calc(100% - 24px) !important;
    grid-template-columns: repeat(3, minmax(0, 1fr)) !important;
    gap: 18px !important;
    margin-top: -46px !important;
  }

  .subject-card {
    width: 150px !important;
    min-width: 150px !important;
    transform: scale(.82) !important;
  }

  .subject-card:hover,
  .subject-card:focus-visible {
    transform: translateY(-5px) scale(.82) !important;
  }
}
''')

Path(__file__).unlink()
print("Final home alignment applied; helper removed.")
