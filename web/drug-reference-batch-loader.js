(() => {
  const originalFetch = window.fetch.bind(window);
  const batchPaths = [
    "./data/drug-reference-cards-batch-01.json?v=20260719-batch-01",
    "./data/drug-reference-cards-batch-01b.json?v=20260719-batch-01b",
    "./data/drug-reference-cards-batch-01c.json?v=20260719-batch-01c",
    "./data/drug-reference-cards-batch-02a.json?v=20260719-batch-02a",
    "./data/drug-reference-cards-batch-02b.json?v=20260719-batch-02b",
    "./data/drug-reference-cards-batch-02c.json?v=20260719-batch-02c",
    "./data/drug-reference-cards-batch-02d.json?v=20260719-batch-02d",
    "./data/drug-reference-cards-batch-02e.json?v=20260719-batch-02e",
    "./data/drug-reference-cards-batch-02f.json?v=20260719-batch-02f",
    "./data/drug-reference-cards-batch-02g.json?v=20260719-batch-02g",
    "./data/drug-reference-cards-batch-02h.json?v=20260719-batch-02h",
    "./data/drug-reference-cards-batch-02i.json?v=20260719-batch-02i",
    "./data/drug-reference-cards-batch-02j.json?v=20260719-batch-02j",
    "./data/drug-reference-cards-batch-03a.json?v=20260720-batch-03a",
    "./data/drug-reference-cards-batch-03b.json?v=20260720-batch-03b",
    "./data/drug-reference-cards-batch-03c.json?v=20260720-batch-03c",
    "./data/drug-reference-cards-batch-03d.json?v=20260720-batch-03d",
    "./data/drug-reference-cards-batch-03e.json?v=20260720-batch-03e",
    "./data/drug-reference-cards-batch-03f.json?v=20260720-batch-03f",
    "./data/drug-reference-cards-batch-03g.json?v=20260720-batch-03g",
    "./data/drug-reference-cards-batch-03h.json?v=20260720-batch-03h",
    "./data/drug-reference-cards-batch-03i.json?v=20260720-batch-03i",
    "./data/drug-reference-cards-batch-03j.json?v=20260720-batch-03j",
    "./data/drug-reference-cards-batch-04a.json?v=20260720-batch-04a",
    "./data/drug-reference-cards-batch-04b.json?v=20260720-batch-04b",
    "./data/drug-reference-cards-batch-04c.json?v=20260720-batch-04c",
    "./data/drug-reference-cards-batch-04d.json?v=20260720-batch-04d",
  ];

  window.fetch = async function prepFlowBatchAwareFetch(input, init) {
    const url = typeof input === "string" ? input : input?.url || "";
    if (!url.includes("drug-reference-cards.json")) return originalFetch(input, init);

    const responses = await Promise.all([
      originalFetch(input, init),
      ...batchPaths.map((path) => originalFetch(path, { cache: "no-store" })),
      originalFetch("./data/drug-reference.json?v=20260720-batch-04d", { cache: "no-store" }),
    ]);

    const baseResponse = responses[0];
    const batchResponses = responses.slice(1, -1);
    const registryResponse = responses[responses.length - 1];
    if (!baseResponse.ok || !registryResponse.ok || batchResponses.some((response) => !response.ok)) return baseResponse;

    const basePayload = await baseResponse.json();
    const batchPayloads = await Promise.all(batchResponses.map((response) => response.json()));
    const registryPayload = await registryResponse.json();
    const cards = { ...(basePayload.cards || {}) };
    const registryByName = new Map((registryPayload.entries || []).map((entry) => [String(entry.genericName || "").toLocaleLowerCase().trim(), entry]));
    const batchCards = batchPayloads.flatMap((payload) => payload.cards || []);
    const seenNames = new Set();

    for (const batchCard of batchCards) {
      const genericName = String(batchCard.genericName || "").trim();
      const normalizedName = genericName.toLocaleLowerCase();
      const registryEntry = registryByName.get(normalizedName);
      if (!registryEntry) throw new Error(`Bulk drug card could not be matched to registry: ${genericName}`);
      if (seenNames.has(normalizedName)) throw new Error(`Duplicate bulk drug card: ${genericName}`);
      seenNames.add(normalizedName);
      const { genericName: _genericName, ...override } = batchCard;
      cards[registryEntry.id] = override;
    }

    return new Response(JSON.stringify({ ...basePayload, cards }), { status: 200, headers: { "Content-Type": "application/json" } });
  };
})();