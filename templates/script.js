document.addEventListener("DOMContentLoaded", function() {
  const selectedCountry = document.getElementById("selectedCountry");
  const countryDropdown = document.getElementById("countryDropdown");

  selectedCountry.addEventListener("click", function() {
    countryDropdown.classList.toggle("show");
  });

  const countryItems = document.querySelectorAll(".dropdown ul li");
  countryItems.forEach(function(item) {
    item.addEventListener("click", function() {
      const countryCode = item.getAttribute("data-code");
      const countryName = item.textContent;

      selectedCountry.innerHTML = `
        <span class="country-code">${countryCode}</span>
        <span class="country-name">${countryName}</span>
      `;

      countryDropdown.classList.remove("show");
    });
  });
});
