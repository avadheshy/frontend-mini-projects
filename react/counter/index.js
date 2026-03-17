const incrementBtn = document.querySelector(".increment");
const decrementBtn = document.querySelector(".decrement");
const resetBtn = document.querySelector(".reset");
const counterValue = document.querySelector(".counter-value");

let count = 0;

function updateCounter(){
    counterValue.textContent = count;
}

incrementBtn.addEventListener("click", () => {
    count++;
    updateCounter();
});

decrementBtn.addEventListener("click", () => {
    count--;
    updateCounter();
});

resetBtn.addEventListener("click", () => {
    count = 0;
    updateCounter();
});