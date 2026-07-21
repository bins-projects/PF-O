from pathlib import Path

index_path = Path('web/index.html')
index = index_path.read_text()
link = '  <link rel="stylesheet" href="book-emblem-preview.css?v=20260721-1">\n'
anchor = '  <link rel="stylesheet" href="book-shelf.css?v=20260721-1">\n'
if link not in index:
    if anchor not in index:
        raise SystemExit('book shelf stylesheet link not found')
    index = index.replace(anchor, anchor + link, 1)
    index_path.write_text(index)

Path('web/book-emblem-preview.css').write_text(r'''/* Preview: balanced vertical titles and large boxed emblems. */
.subject-card .subject-name {
  position: absolute !important;
  left: 34px !important;
  top: 50% !important;
  margin: 0 !important;
  min-height: 0 !important;
  transform: translate(-50%, -50%) rotate(-90deg) !important;
  transform-origin: center !important;
  white-space: nowrap !important;
  line-height: 1 !important;
  letter-spacing: .07em !important;
  text-align: center !important;
}

.subject-card.fundamentals .subject-name {
  font-size: .88rem !important;
  letter-spacing: .045em !important;
}

.subject-card.pharm .subject-name {
  font-size: 1.28rem !important;
  letter-spacing: .18em !important;
}

.subject-card.med-surg .subject-name {
  font-size: 1.05rem !important;
  letter-spacing: .1em !important;
}

.subject-card.fundamentals .subject-icon,
.subject-card.pharm .subject-icon {
  position: relative !important;
  top: auto !important;
  left: auto !important;
  display: grid !important;
  place-items: center !important;
  width: 108px !important;
  height: 108px !important;
  margin: 10px auto 18px !important;
  border: 4px solid var(--card-accent) !important;
  border-radius: 3px !important;
  background:
    repeating-linear-gradient(to bottom, rgba(255,255,255,.035) 0 2px, transparent 2px 4px),
    #050b20 !important;
  box-shadow:
    0 0 0 3px #020615,
    0 0 0 6px color-mix(in srgb, var(--card-accent) 38%, #18245a),
    inset 0 0 22px color-mix(in srgb, var(--card-accent) 18%, transparent),
    0 0 22px color-mix(in srgb, var(--card-accent) 32%, transparent) !important;
  color: var(--card-accent) !important;
  font-size: 4rem !important;
  text-shadow:
    3px 3px 0 #07102b,
    0 0 14px color-mix(in srgb, var(--card-accent) 72%, transparent) !important;
  overflow: hidden !important;
}

.subject-card.pharm .subject-icon {
  color: transparent !important;
  font-size: 0 !important;
}

.subject-card.pharm .subject-icon::before,
.subject-card.pharm .subject-icon::after {
  content: '' !important;
  position: absolute !important;
  display: block !important;
  pointer-events: none !important;
}

.subject-card.pharm .subject-icon::before {
  width: 76px !important;
  height: 34px !important;
  border: 4px solid #f4fff0 !important;
  border-radius: 20px !important;
  background: linear-gradient(90deg, #76ef50 0 50%, #f3fff0 50% 100%) !important;
  box-shadow:
    4px 4px 0 #0b3518,
    0 0 18px rgba(118,239,80,.8) !important;
  transform: rotate(-34deg) !important;
}

.subject-card.pharm .subject-icon::after {
  width: 4px !important;
  height: 36px !important;
  background: #15371b !important;
  box-shadow: 0 0 8px rgba(255,255,255,.8) !important;
  transform: rotate(56deg) !important;
}

.subject-card .question-count {
  margin-top: 4px !important;
}
''')

Path(__file__).unlink()
print('Boxed emblem and balanced-title preview applied; helper removed.')
