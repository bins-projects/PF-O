(function () {
  function parseSavedSession(raw, expectedVersion) {
    if (!raw) {
      return { saved: null, shouldClear: false };
    }

    try {
      const saved = JSON.parse(raw);

      if (!saved || saved.version !== expectedVersion) {
        return { saved: null, shouldClear: true };
      }

      return { saved, shouldClear: false };
    } catch {
      return { saved: null, shouldClear: true };
    }
  }

  window.PrepFlowSavedSessionRules = {
    parseSavedSession,
  };
}());
