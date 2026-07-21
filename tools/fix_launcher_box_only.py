from pathlib import Path

index_path = Path("web/index.html")
index = index_path.read_text()

# Remove the regressed final alignment layer if it is still present.
index = index.replace('  <link rel="stylesheet" href="final-home-alignment.css?v=20260721-1">\n', '')

link = '  <link rel="stylesheet" href="launcher-box-fix.css?v=20260721-1">\n'
if link not in index:
    index = index.replace("</head>", link + "</head>", 1)
index_path.write_text(index)

Path("web/final-home-alignment.css").unlink(missing_ok=True)

Path("web/launcher-box-fix.css").write_text(r'''/* Launcher-only correction. Do not scale books or their live text here. */
#home-launcher {
  left: clamp(14px, 2.8vw, 48px) !important;
  top: clamp(88px, 11vh, 150px) !important;
  width: clamp(286px, 25vw, 382px) !important;
  max-width: calc(100% - 28px) !important;
  transform: none !important;
}

#home-launcher .launcher-view {
  padding: clamp(12px, 1.1vw, 18px) !important;
  gap: clamp(7px, .8vh, 11px) !important;
}

#home-launcher h2 {
  font-size: clamp(16px, 1.15vw, 20px) !important;
  margin: 0 !important;
}

#home-launcher p {
  margin: 0 !important;
  line-height: 1.35 !important;
}

#home-launcher .launcher-actions {
  gap: 8px !important;
}

@media (max-width: 1040px) {
  #home-launcher {
    left: 12px !important;
    top: 18px !important;
    width: clamp(268px, 37vw, 326px) !important;
  }

  #home-launcher .launcher-view {
    padding: 12px !important;
    gap: 7px !important;
  }

  #home-launcher h2 {
    font-size: 16px !important;
  }

  #home-launcher p,
  #home-launcher label,
  #home-launcher button,
  #home-launcher select {
    font-size: 10px !important;
  }
}
''')

Path(__file__).unlink()
print("Launcher box reduced and moved clear of the PrepFlow name; helper removed.")
