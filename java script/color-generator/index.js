const buttons = document.querySelectorAll(".box");
const outer = document.querySelector(".outer");

buttons.forEach(button => {
    button.addEventListener("click", () => {
        const color = button.dataset.color;
        outer.style.backgroundColor = color;
    });
});