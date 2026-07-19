(() => {
  const originalFetch = window.fetch.bind(window);

  window.fetch = async function prepFlowBatchAwareFetch(input, init) {
    const url = typeof input === "string" ? input : input?.url || "";

    if (!url.includes("drug-reference-cards.json")) {
      return originalFetch(input, init);
    }

    const [baseResponse, batchOneResponse, batchOneBResponse, batchOneCResponse, registryResponse] = await Promise.all([
      originalFetch(input, init),
      originalFetch("./data/drug-reference-cards-batch-01.json?v=20260719-batch-01", { cache: "no-store" }),
      originalFetch("./data/drug-reference-cards-batch-01b.json?v=20260719-batch-01b", { cache: "no-store" }),
      originalFetch("./data/drug-reference-cards-batch-01c.json?v=20260719-batch-01c", { cache: "no-store" }),
      originalFetch("./data/drug-reference.json?v=20260719-batch-01c", { cache: "no-store" }),
    ]);

    if (!baseResponse.ok || !batchOneResponse.ok || !batchOneBResponse.ok || !batchOneCResponse.ok || !registryResponse.ok) {
      return baseResponse;
    }

    const [basePayload, batchOnePayload, batchOneBPayload, batchOneCPayload, registryPayload] = await Promise.all([
      baseResponse.json(),
      batchOneResponse.json(),
      batchOneBResponse.json(),
      batchOneCResponse.json(),
      registryResponse.json(),
    ]);

    const cards = { ...(basePayload.cards || {}) };
    const registryByName = new Map(
      (registryPayload.entries || []).map((entry) => [
        String(entry.genericName || "").toLocaleLowerCase().trim(),
        entry,
      ])
    );

    const batchCards = [
      ...(batchOnePayload.cards || []),
      ...(batchOneBPayload.cards || []),
      ...(batchOneCPayload.cards || []),
    ];

    const seenNames = new Set();

    for (const batchCard of batchCards) {
      const genericName = String(batchCard.genericName || "").trim();
      const normalizedName = genericName.toLocaleLowerCase();
      const registryEntry = registryByName.get(normalizedName);

      if (!registryEntry) {
        throw new Error(`Bulk drug card could not be matched to registry: ${genericName}`);
      }

      if (seenNames.has(normalizedName)) {
        throw new Error(`Duplicate bulk drug card: ${genericName}`);
      }

      seenNames.add(normalizedName);
      const { genericName: _genericName, ...override } = batchCard;
      cards[registryEntry.id] = override;
    }

    return new Response(JSON.stringify({ ...basePayload, cards }), {
      status: 200,
      headers: { "Content-Type": "application/json" },
    });
  };
})();