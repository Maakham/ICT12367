const count = document.querySelector(".count");
const input = document.querySelector("input");

input.addEventListener("keyup", function () {
  count.textContent = input.value.length;
});
//   ranbow random background color
class BackgroundColorLoop {
  constructor(intervalTime = 1000) {
    this.intervalTime = intervalTime;
    this.intervalId = null;
  }

  // Generates random color and updates background
  changeColor() {
    const r = Math.floor(Math.random() * 256);
    const g = Math.floor(Math.random() * 256);
    const b = Math.floor(Math.random() * 256);
    document.body.style.backgroundColor = `rgb(${r}, ${g}, ${b})`;
    console.log(`New color: rgb(${r}, ${g}, ${b})`);
  }

  // Starts the loop
  start() {
    if (!this.intervalId) {
      this.intervalId = setInterval(
        () => this.changeColor(),
        this.intervalTime,
      );
    }
  }

  // Stops the loop
  stop() {
    clearInterval(this.intervalId);
    this.intervalId = null;
  }
}

// Usage: Create instance and start
const bgLoop = new BackgroundColorLoop(0.1); // Changes every 1s
bgLoop.start();

const doc = new BackgroundColorLoop(0.5);
doc.start();
