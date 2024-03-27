// Get the container element
const container = document.getElementById('content-container');

// Get all navigation links
const navLinks = document.querySelectorAll('.nav-link');

// Function to load the content for a specific page
const loadContent = (selectedPage) => {
  // Fetch the content of the selected page using AJAX
  fetch(selectedPage + '.html') // Assuming the content is in separate HTML files with corresponding names
    .then((response) => response.text())
    .then((data) => {
      // Replace the content of the container with the fetched data
      container.innerHTML = data;
    })
    .catch((error) => {
      console.error('Error:', error);
    });
};

// Add event listener to each navigation link
navLinks.forEach((link) => {
  link.addEventListener('click', (event) => {
    event.preventDefault();

    // Get the selected page from the data attribute
    const selectedPage = link.getAttribute('data-page');

    // Load the content for the selected page
    loadContent(selectedPage);
  });
});

// Load the home page content by default
loadContent('home');
