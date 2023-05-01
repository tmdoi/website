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
  firstDomino.components["dynamic-body"].applyImpulse(
    new THREE.Vector3(-5, 0, 0),
    new THREE.Vector3().copy(firstDomino.getAttribute("position"))
    );
  }, 3000);
});
