const hamburger = document.querySelector('.hamburger');
const nav = document.querySelector('.nav-2');
hamburger.addEventListener('click', () => {
    nav.classList.toggle('active');
    hamburger.classList.toggle('active');
});
const menuToggle = document.getElementById('menu-toggle');
if (menuToggle) {
    menuToggle.addEventListener('click', () => {
        nav.classList.toggle('active');
        hamburger.classList.toggle('active');
    });
}


// Preloader functionality
window.addEventListener('load', () => {
    const loader = document.getElementById('load');
    const body = document.body;
    
    // Add fade-out animation to loader
    loader.classList.add('fade-out');
    
    // Wait for fade-out animation to complete before hiding loader
    setTimeout(() => {
        loader.style.display = 'none';
        body.classList.remove('loading');
    }, 500);
});

document.addEventListener('DOMContentLoaded', () => {
    // Select the theme toggle checkbox and the html element
    const themeToggleCheckbox = document.querySelector('input[type="checkbox"].theme-toggle');
    const root = document.documentElement;

    // --- Function to apply the saved theme and sync the toggle ---
    const applyTheme = () => {
        // Retrieve the saved theme from localStorage
        const savedTheme = localStorage.getItem('theme');
        let isLight = false;
        if (savedTheme) {
            isLight = savedTheme === 'light';
            root.classList.toggle('light', isLight);
        } else {
            // If no theme is saved, check the user's system preference
            const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
            isLight = !prefersDark;
            root.classList.toggle('light', isLight);
        }
        // Sync the checkbox state
        if (themeToggleCheckbox) themeToggleCheckbox.checked = isLight;
    };

    // --- Event listener for the toggle checkbox ---
    if (themeToggleCheckbox) {
        themeToggleCheckbox.addEventListener('change', () => {
            // Set the theme based on the checkbox state
            const isLight = themeToggleCheckbox.checked;
            root.classList.toggle('light', isLight);
            // Save the user's preference to localStorage
            localStorage.setItem('theme', isLight ? 'light' : 'dark');
        });
    }

    // --- Apply the theme and sync toggle when the page loads ---
    applyTheme();
});
