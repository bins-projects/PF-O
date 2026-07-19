(() => {
  const launch = document.querySelector("#open-drug-reference");
  const screen = document.querySelector("#drug-reference-screen");
  const close = document.querySelector("#close-drug-reference");
  const searchInput = document.querySelector("#drug-reference-search");
  const filter = document.querySelector("#drug-reference-filter");
  const results = document.querySelector("#drug-reference-results");
  const detail = document.querySelector("#drug-reference-detail");
  const tabs = [...document.querySelectorAll("[data-reference-tab]")];

  if (!launch || !screen) return;

  const referenceLaunch = document.querySelector(".reference-launch");
  const originalHideAllScreens = window.hideAllScreens;
  const originalShowSubjects = window.showSubjects;

  let entries = [];
  let activeTab = "search";
  let selectedId = null;

  const routeAliases = {
    pill: "oral", pills: "oral", tablet: "oral", tablets: "oral",
    capsule: "oral", capsules: "oral", liquid: "oral", syrup: "oral",
    iv: "iv", intravenous: "iv", infusion: "iv",
    shot: "injection", shots: "injection", injectable: "injection",
    cream: "topical", ointment: "topical", lotion: "topical", gel: "topical",
    patch: "transdermal", inhaler: "inhaled", inhaled: "inhaled",
    nebulizer: "inhaled", nebulized: "inhaled",
    "eye drops": "ophthalmic", eye: "ophthalmic",
    "ear drops": "otic", ear: "otic", nasal: "nasal"
  };

  function normalized(value) {
    return String(value || "").toLocaleLowerCase().replace(/\s+/g, " ").trim();
  }

  function searchTerms(entry) {
    return [
      entry.genericName,
      ...(entry.pharmSpellings || []),
      ...(entry.brandNames || []),
      ...(entry.drugClasses || []),
      ...(entry.bodySystems || []),
      ...(entry.routes || []),
      ...(entry.dosageForms || []),
    ].map(normalized).join(" ");
  }

  function valuesForTab(entry) {
    if (activeTab === "class") return entry.drugClasses || [];
    if (activeTab === "system") return entry.bodySystems || [];
    if (activeTab === "route") return entry.routes || [];
    if (activeTab === "az") return [entry.genericName.charAt(0).toUpperCase()];
    return [];
  }

  function populateFilter() {
    const label = {
      search: "All medications",
      az: "All letters",
      class: "All drug classes",
      system: "All body systems",
      route: "All routes",
    }[activeTab];

    const values = new Set();
    entries.forEach((entry) => valuesForTab(entry).forEach((value) => value && values.add(value)));

    filter.replaceChildren(new Option(label, ""));
    [...values].sort((a, b) => a.localeCompare(b)).forEach((value) => {
      filter.append(new Option(value, value));
    });
    filter.hidden = activeTab === "search";
  }

  function filteredEntries() {
    let query = normalized(searchInput.value);
    Object.entries(routeAliases).forEach(([alias, replacement]) => {
      query = query.replace(new RegExp(`\\b${alias}\\b`, "g"), replacement);
    });

    const selectedFilter = filter.value;
    return entries.filter((entry) => {
      const matchesSearch = !query || query.split(" ").every((term) => searchTerms(entry).includes(term));
      const matchesFilter = !selectedFilter || valuesForTab(entry).includes(selectedFilter);
      return matchesSearch && matchesFilter;
    });
  }

  function renderResults() {
    const matches = filteredEntries();
    results.replaceChildren();

    const count = document.createElement("p");
    count.className = "drug-reference-count";
    count.textContent = `${matches.length} ${matches.length === 1 ? "medication" : "medications"}`;
    results.append(count);

    matches.forEach((entry) => {
      const button = document.createElement("button");
      button.className = "drug-result";
      button.classList.toggle("active", entry.id === selectedId);
      button.innerHTML = `
        <strong>${entry.genericName}</strong>
        <span>${(entry.brandNames || []).join(", ") || "Generic entry"}</span>
        <small>${(entry.routes || []).join(" • ")}</small>
      `;
      button.addEventListener("click", () => {
        selectedId = entry.id;
        renderResults();
        renderDetail(entry);
      });
      results.append(button);
    });
  }

  function section(title, value) {
    const text = value || "Pending verified drug-card extraction.";
    return `<section><h4>${title}</h4><p>${text}</p></section>`;
  }

  function renderDetail(entry) {
    const card = entry.card || {};
    const routes = (entry.routes || []).map((route) => `<span>${route}</span>`).join("");
    const forms = (entry.dosageForms || []).map((form) => `<span>${form}</span>`).join("");

    detail.innerHTML = `
      <header class="drug-card-heading">
        <div>
          <p class="drug-card-kicker">${entry.id}</p>
          <h3>${entry.genericName}</h3>
          <p>${(entry.brandNames || []).join(", ") || "No brand name recorded in the Pharm Pack"}</p>
        </div>
        <span class="drug-card-status">${entry.cardStatus}</span>
      </header>

      <div class="drug-card-tags">
        ${routes || "<span>Route review needed</span>"}
        ${forms}
      </div>

      <section class="drug-card-overview">
        <div><strong>Drug class</strong><span>${(entry.drugClasses || []).join(", ") || "Pending"}</span></div>
        <div><strong>Body system</strong><span>${(entry.bodySystems || []).join(", ") || "Pending"}</span></div>
        <div><strong>Pharm appearances</strong><span>${entry.questionCount || 0} questions</span></div>
      </section>

      <div class="drug-card-sections">
        ${section("Indications", card.indications)}
        ${section("Mechanism of action", card.mechanism)}
        ${section("Typical dosing", card.dosing)}
        ${section("Route-specific administration", card.routeAdministration)}
        ${section("Contraindications", card.contraindications)}
        ${section("Major warnings", card.warnings)}
        ${section("Common side effects", card.commonAdverseEffects)}
        ${section("Serious adverse effects", card.seriousAdverseEffects)}
        ${section("Interactions", card.interactions)}
        ${section("Labs and monitoring", card.monitoring)}
        ${section("Patient teaching", card.patientTeaching)}
        ${section("Nutrition and food considerations", card.nutrition)}
        ${section("Source", card.source)}
      </div>
    `;
  }

  async function loadReference() {
    if (entries.length) return;

    const [registryResponse, cardsResponse] = await Promise.all([
      fetch("./data/drug-reference.json"),
      fetch("./data/drug-reference-cards.json"),
    ]);

    if (!registryResponse.ok) {
      throw new Error(`Could not load drug reference: ${registryResponse.status}`);
    }

    const payload = await registryResponse.json();
    const cardPayload = cardsResponse.ok ? await cardsResponse.json() : { cards: {} };
    const cards = cardPayload.cards || {};

    entries = (payload.entries || []).map((entry) => {
      const override = cards[entry.id];
      if (!override) return entry;
      return {
        ...entry,
        ...override,
        card: {
          ...(entry.card || {}),
          ...(override.card || {}),
        },
      };
    });
  }

  function hideHomeReferenceLaunch() {
    if (referenceLaunch) referenceLaunch.hidden = true;
  }

  function showHomeReferenceLaunch() {
    if (referenceLaunch) referenceLaunch.hidden = false;
  }

  window.hideAllScreens = function patchedHideAllScreens() {
    originalHideAllScreens();
    screen.hidden = true;
    hideHomeReferenceLaunch();
  };

  window.showSubjects = function patchedShowSubjects() {
    originalShowSubjects();
    screen.hidden = true;
    showHomeReferenceLaunch();
  };

  async function openReference() {
    try {
      window.hideAllScreens();
      await loadReference();
      screen.hidden = false;
      populateFilter();
      renderResults();
      searchInput.focus();
    } catch (error) {
      window.showSubjects();
      const status = document.querySelector("#status");
      status.hidden = false;
      status.textContent = error.message;
    }
  }

  launch.addEventListener("click", openReference);
  close.addEventListener("click", window.showSubjects);
  searchInput.addEventListener("input", renderResults);
  filter.addEventListener("change", renderResults);

  tabs.forEach((tab) => {
    tab.addEventListener("click", () => {
      activeTab = tab.dataset.referenceTab;
      tabs.forEach((candidate) => candidate.classList.toggle("active", candidate === tab));
      populateFilter();
      renderResults();
    });
  });

  showHomeReferenceLaunch();
})();
