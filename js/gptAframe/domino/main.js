window.addEventListener("DOMContentLoaded", function () {
  const scene = document.querySelector("a-scene");
  const dominoes = document.getElementById("dominoes");

  for (let i = 0; i < 100; i++) {
    const domino = document.createElement("a-entity");
    domino.setAttribute("mixin", "domino");
    domino.setAttribute("position", `0 0.25 ${-0.2 * (i + 1)}`);
    dominoes.appendChild(domino);
  }

  const firstDomino = dominoes.children[0];
  setTimeout(() => {
    firstDomino.setAttribute(
      "animation",
      "property: rotation; to: 0 -90 0; dur: 1000; easing: ease-in"
    );
  }, 3000);
});
