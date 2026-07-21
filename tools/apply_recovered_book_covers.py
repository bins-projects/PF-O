from pathlib import Path

css_path = Path("web/book-shelf.css")
if not css_path.exists():
    raise SystemExit("web/book-shelf.css not found; apply the book shelf refresh first")

marker = "/* Recovered front-cover hierarchy v1 */"
css = css_path.read_text()
if marker in css:
    Path(__file__).unlink()
    print("Recovered book covers already applied; helper removed.")
    raise SystemExit(0)

css += r'''

/* Recovered front-cover hierarchy v1 */

/* The former page-block pseudo-element could rise above the cover in the
   accumulated legacy cascade. Keep page depth in the shell shadow instead. */
.subject-card::after {
  content: none !important;
  display: none !important;
}

.subject-card {
  padding: 28px 18px 48px 34px !important;
  overflow: hidden !important;
  box-shadow:
    -10px 0 0 var(--book-depth),
    -13px 0 0 #020614,
    7px 0 0 #909ba5,
    7px 7px 0 #909ba5,
    12px 13px 0 rgba(0,0,0,.48) !important;
}

.subject-card .subject-icon {
  display: grid !important;
  place-items: center !important;
  width: 62px !important;
  height: 62px !important;
  margin: 0 auto 15px !important;
  border: 2px solid var(--card-accent) !important;
  border-radius: 3px !important;
  background:
    repeating-linear-gradient(to bottom, rgba(255,255,255,.025) 0 2px, transparent 2px 4px),
    rgba(2,8,25,.9) !important;
  color: var(--card-accent) !important;
  font-size: 2rem !important;
  line-height: 1 !important;
  text-shadow: 3px 3px 0 #080d24 !important;
  box-shadow:
    3px 3px 0 rgba(0,0,0,.42),
    inset 0 0 0 2px rgba(255,255,255,.025) !important;
}

.subject-card.pharm .subject-icon {
  color: #ff637d !important;
}

.subject-copy {
  display: grid !important;
  gap: 0 !important;
  margin: 0 !important;
  text-align: center !important;
}

.subject-copy::before {
  content: "PREPFLOW" !important;
  display: block !important;
  margin: 0 0 16px !important;
  color: var(--card-accent) !important;
  font-family: "Courier New", monospace !important;
  font-size: .58rem !important;
  font-weight: 900 !important;
  letter-spacing: .18em !important;
  line-height: 1 !important;
  text-align: center !important;
  text-transform: uppercase !important;
}

.subject-card .subject-name {
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  min-height: 2.2em !important;
  margin: 0 !important;
  color: #f7fbff !important;
  font-family: "Courier New", monospace !important;
  font-size: 1rem !important;
  font-weight: 900 !important;
  font-style: italic !important;
  letter-spacing: -.035em !important;
  line-height: 1.08 !important;
  text-align: center !important;
  text-transform: uppercase !important;
  text-shadow: 3px 3px 0 #070b20 !important;
}

.subject-card .subject-name::before,
.subject-card .subject-name::after {
  content: none !important;
  display: none !important;
}

.subject-card .question-count {
  display: block !important;
  margin: 12px 0 0 !important;
  color: var(--card-accent) !important;
  font-family: "Courier New", monospace !important;
  font-size: .65rem !important;
  font-weight: 900 !important;
  letter-spacing: .045em !important;
  line-height: 1.2 !important;
  text-align: center !important;
  text-transform: uppercase !important;
  text-shadow: 2px 2px 0 #070b20 !important;
}

.subject-card .card-action {
  right: 13px !important;
  bottom: 13px !important;
  left: 35px !important;
  min-height: 31px !important;
  padding: 6px 7px !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  border: 2px solid var(--card-accent) !important;
  background: rgba(3,9,26,.92) !important;
  color: var(--card-accent) !important;
  font-family: "Courier New", monospace !important;
  font-size: .62rem !important;
  font-weight: 900 !important;
  letter-spacing: .06em !important;
  line-height: 1 !important;
  opacity: 1 !important;
  transform: none !important;
  text-transform: uppercase !important;
}

.subject-card .card-action span {
  display: none !important;
}

.subject-card:hover,
.subject-card:focus-visible {
  box-shadow:
    -10px 0 0 color-mix(in srgb, var(--card-accent) 70%, #07112c),
    -13px 0 0 #020614,
    9px 0 0 #a4adb5,
    9px 10px 0 #a4adb5,
    15px 17px 0 rgba(0,0,0,.52),
    0 0 22px color-mix(in srgb, var(--card-accent) 34%, transparent) !important;
}
'''

css_path.write_text(css)
Path(__file__).unlink()
print("Recovered front-cover hierarchy applied; helper removed.")
