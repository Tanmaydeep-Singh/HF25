const addGlassBtn = document.getElementById("addGlass");
const resetBtn = document.getElementById("reset");
const waterLevel = document.getElementById("waterLevel");
const waterText = document.getElementById("waterText");

let glassesDrunk = parseInt(localStorage.getItem("glassesDrunk")) || 0;
const dailyGoal = 8;

function updateWaterDisplay() {
  const percent = Math.min((glassesDrunk / dailyGoal) * 100, 100);
  waterLevel.style.height = `${percent}%`;
  waterText.textContent = `${glassesDrunk} / ${dailyGoal} Glasses`;

  if (glassesDrunk >= dailyGoal) {
    waterText.textContent = "🎉 Goal Reached!";
  }

  localStorage.setItem("glassesDrunk", glassesDrunk);
}

addGlassBtn.addEventListener("click", () => {
  if (glassesDrunk < dailyGoal) {
    glassesDrunk++;
    updateWaterDisplay();
  } else {
    alert("You’ve already reached your daily goal! 🥳");
  }
});

resetBtn.addEventListener("click", () => {
  if (confirm("Reset your daily count?")) {
    glassesDrunk = 0;
    updateWaterDisplay();
    localStorage.removeItem("glassesDrunk");
  }
});

updateWaterDisplay();
