const menuBtn = document.querySelector(".menu-btn");
const sidebar = document.getElementById("sidebar");

function setMenu(open) {
  document.body.classList.toggle("menu-open", open);
  menuBtn.setAttribute("aria-expanded", open);
  if (open) sidebar.querySelector("pagefind-searchbox input")?.focus();
}

menuBtn.addEventListener("click", (e) => {
  e.stopPropagation();
  setMenu(!document.body.classList.contains("menu-open"));
});
document.addEventListener("click", (e) => {
  if (!sidebar.contains(e.target)) setMenu(false);
});
document.addEventListener("keydown", (e) => {
  if (e.key === "Escape") setMenu(false);
});
