document.addEventListener("DOMContentLoaded", function () {
    const fontSizeInput = document.getElementById("fontSize");
    const textColorInput = document.getElementById("textColor");
    const bgColorInput = document.getElementById("bgColor");
    const content = document.getElementById("h1");

    fontSizeInput.addEventListener("input", function () {
        content.style.fontSize = fontSizeInput.value + "px";
    });

    textColorInput.addEventListener("input", function () {
        content.style.color = textColorInput.value;
    });

    bgColorInput.addEventListener("input", function () {
        document.body.style.backgroundColor = bgColorInput.value;
    });
});
