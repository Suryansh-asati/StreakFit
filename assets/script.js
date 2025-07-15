const hamburger = document.querySelector('.hamburger');
const nav = document.querySelector('.nav-2');
hamburger.addEventListener('click', () => {
    nav.classList.toggle('active');
});

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