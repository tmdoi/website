window.addEventListener("DOMContentLoaded", function () {
  const scene = document.querySelector("a-scene");
  const dominoes = document.getElementById("dominoes");
  const timer = document.getElementById("timer");

  function createDominoes(num, startX, startY, startZ, dir) {
    const dominoSize = 0.2;
    let posX = startX;
    let posY = startY;
    let posZ = startZ;

    for (let i = 0; i < num; i++) {
      const domino = document.createElement("a-box");
      domino.setAttribute("width", "0.25");
      domino.setAttribute("height", "0.5");
      domino.setAttribute("depth", "0.05");
      domino.setAttribute("color", "#FFC107");
      domino.setAttribute("position", `${posX} ${posY} ${posZ}`);
      domino.setAttribute("dynamic-body", "shape: box; mass: 0.25; friction: 0.5");
      
      // Set domino rotation
      switch (dir) {
        case 2: // Negative x-axis
          domino.setAttribute("rotation", "0 0 90");
          break;
        case 3: // Positive x-axis
          domino.setAttribute("rotation", "0 0 -90");
          break;
        default: // z-axis (default rotation is fine)
          break;
      }

      dominoes.appendChild(domino);

      // Update domino position
      switch (dir) {
        case 0: // Negative z-axis
          posZ -= dominoSize;
          break;
        case 1: // Positive z-axis
          posZ += dominoSize;
          break;
        case 2: // Negative x-axis
          posX -= dominoSize;
          break;
        case 3: // Positive x-axis
          posX += dominoSize;
          break;
        default: // Default is negative z-axis
          posZ -= dominoSize;
          break;
      }
    }

    return {x: posX, y: posY, z: posZ};
  }

  let nextPos = createDominoes(124, 0, 0.25, 0, 1);

  const firstDomino = dominoes.children[0];
  firstDomino.setAttribute("color", "#0000FF");

  function countdown(seconds) {
    timer.setAttribute("text", "value", seconds);

    if (seconds > 0) {
      setTimeout(() => {
        countdown(seconds - 1);
      }, 1000);
    }
  }

  countdown(3);
  firstDomino.setAttribute("rotation", "25 0 0");

  // firstDomino.addEventListener("body-loaded", () => {
  //  setTimeout(() => {
  //    firstDomino.setAttribute("rotation", "15 0 0");
  //  }, 3000);
  // });
});
