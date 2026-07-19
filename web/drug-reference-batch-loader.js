(() => {
  const originalFetch = window.fetch.bind(window);

  window.fetch = async function prepFlowBatchAwareFetch(input, init) {
    const url = typeof input === "string" ? input : input?.url || "";

    if (!url.includes("drug-reference-cards.json")) {
      return originalFetch(input, init);
    }

    const [baseResponse, batchResponse, registryResponse] = await Promise.all([
      originalFetch(input, init),
      originalFetch("./data/drug-reference-cards-batch-01.json?v=20260719-batch-01", { cache: "no-store" }),
      originalFetch("./data/drug-reference.json?v=20260719-batch-01", { cache: "no-store" }),
    ]);

    if (!baseResponse.ok || !batchResponse.ok || !registryResponse.ok) {
      return baseResponse;
    }

    const [basePayload, batchPayload, registryPayload] = await Promise.all([
      baseResponse.json(),
      batchResponse.json(),
      registryResponse.json(),
    ]);

    const cards = { ...(basePayload.cards || {}) };
    const registryByName = new Map(
      (registryPayload.entries || []).map((entry) => [
        String(entry.genericName || "").toLocaleLowerCase().trim(),
        entry,
      ])
    );

    for (const batchCard of batchPayload.cards || []) {
      const genericName = String(batchCard.genericName || "").trim();
      const registryEntry = registryByName.get(genericName.toLocaleLowerCase());

      if (!registryEntry) {
        throw new Error(`Bulk drug card could not be matched to registry: ${genericName}`);
      }

      const { genericName: _genericName, ...override } = batchCard;
      cards[registryEntry.id] = override;
    }

    return new Response(JSON.stringify({ ...basePayload, cards }), {
      status: 200,
      headers: { "Content-Type": "application/json" },
    });
  };
})();
