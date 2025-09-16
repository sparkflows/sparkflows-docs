document.addEventListener("DOMContentLoaded", function () {
  function getHeaderOffset() {
    const header = document.querySelector("div.navbar-container");
    return header ? header.offsetHeight + 15 : 60;
  }

  function scrollToHash() {
    if (location.hash && location.pathname === window.location.pathname) {
      const targetId = location.hash.substring(1);
      const targetElem = document.getElementById(targetId);

      if (targetElem) {
        const yOffset = getHeaderOffset();
        const elemTop = targetElem.getBoundingClientRect().top + window.pageYOffset;
        const targetY = elemTop - yOffset;

        window.scrollTo({ top: targetY });
      }
    }
  }

  // --- FIX: wait until after browser’s auto-scroll ---
  if (location.hash) {
    window.setTimeout(scrollToHash, 100); // adjust delay if needed
  }

  // Handle clicks on permalinks, :ref:, sidebar, etc.
  window.addEventListener("hashchange", scrollToHash);
  document.querySelectorAll("a[href^='#']").forEach(anchor => {
    anchor.addEventListener("click", function () {
      if (anchor.pathname === window.location.pathname) {
        window.setTimeout(scrollToHash, 1);
      }
    });
  });
});
