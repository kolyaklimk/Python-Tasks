const banners = document.querySelectorAll(".banner");
let currentBannerIndex = 0;

function rotateBanners() {
  banners[currentBannerIndex].style.display = "none";
  currentBannerIndex = (currentBannerIndex + 1) % banners.length;
  banners[currentBannerIndex].style.display = "block";
}

const rotationIntervalElement = document.getElementById("rotationInterval");
const rotationIntervalValue = rotationIntervalElement.textContent;

rotationInterval = setInterval(rotateBanners, rotationIntervalValue);

//document.addEventListener("visibilitychange", () => {
////console.log(document.visibilityState);
//  if (document.visibilityState === "visible") {
//    rotationInterval = setInterval(rotateBanners, rotationIntervalValue);
//  } else {
//    clearInterval(rotationInterval);
//  }
//});

window.addEventListener("focus", () => {
console.log("focus");
    rotationInterval = setInterval(rotateBanners, rotationIntervalValue);
});

window.addEventListener("blur", () => {
console.log("blur");
    clearInterval(rotationInterval);});
