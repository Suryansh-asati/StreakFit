const hamburger = document.querySelector('.hamburger');
const nav = document.querySelector('.nav-2');
hamburger.addEventListener('click', () => {
    nav.classList.toggle('active');
});
