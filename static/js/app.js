// Invoke Functions Call on Document Loaded
document.addEventListener('DOMContentLoaded', function () {
  });

let alertWrapper = document.querySelector('.alert');
let alertClose = document.querySelector('.alert__close');

if (alertWrapper) {
    alertClose.addEventListener('click', () => 
    alertWrapper.style.display = 'none'
    )
}

let searchForm = document.getElementById("projects-search-form");
let paginationButtons = document.querySelectorAll(".page-link");

if (searchForm) {
  paginationButtons.forEach(paginationButton => {
    paginationButton.addEventListener('click', switchButton);
})      
}

function switchButton(e) {
  e.preventDefault();
  // Getting data attribute
  let page = this.dataset.page;
  console.log(page)
  
  // Add hidden search input to form
  searchForm.innerHTML += `<input value=${page} name="page" hidden />`
  searchForm.submit();
}