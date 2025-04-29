document.addEventListener("DOMContentLoaded", () => {
  const hamburger = document.querySelector(".hamburger");
  const nav = document.querySelector("nav");

  hamburger.addEventListener("click", () => {
    hamburger.classList.toggle("active");
    nav.classList.toggle("active");
  });

  // Close menu when clicking outside
  document.addEventListener("click", (e) => {
    if (
      !nav.contains(e.target) &&
      !hamburger.contains(e.target) &&
      nav.classList.contains("active")
    ) {
      nav.classList.remove("active");
      hamburger.classList.remove("active");
    }
  });
});
