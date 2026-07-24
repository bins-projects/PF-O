(function (global) {
  function shuffledCopy(items, random = Math.random) {
    const copy = [...items];

    for (let index = copy.length - 1; index > 0; index -= 1) {
      const randomIndex = Math.floor(random() * (index + 1));
      [copy[index], copy[randomIndex]] = [copy[randomIndex], copy[index]];
    }

    return copy;
  }

  function orderQuestions(items, shouldShuffle, random = Math.random) {
    return shouldShuffle ? shuffledCopy(items, random) : [...items];
  }

  global.PrepFlowOrderRules = {
    orderQuestions,
  };
})(window);
