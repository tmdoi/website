window.addEventListener("DOMContentLoaded", function () {
  const scene = document.querySelector("a-scene");
  const dominoes = document.getElementById("dominoes");
  const timer = document.getElementById("timer");

  for (let i = 0; i < 100; i++) {
    const domino = document.createElement("a-entity");
    domino.setAttribute("mixin", "domino");
    domino.setAttribute("position", `0 0.25 ${-0.2 * (i + 1)}`);
    domino.setAttribute("dynamic-body", "mass: 5; friction: 0.5"); // dynamic-body を直接設定
    dominoes.appendChild(domino);
  }

  const firstDomino = dominoes.children[0];
  firstDomino.setAttribute("material", "color: #0000FF"); // 1つ目のドミノを青色に変更

  function countdown(seconds) {
    timer.setAttribute("text", "value", seconds);

    if (seconds > 0) {
      setTimeout(() => {
        countdown(seconds - 1);
      }, 1000);
    }
  }

  countdown(3);

  setTimeout(() => {
    firstDomino.components["dynamic-body"].applyImpulse(
      new THREE.Vector3(0, 0, 5),
      new THREE.Vector3().copy(firstDomino.getAttribute("position"))
    );
  }, 3000);
});
