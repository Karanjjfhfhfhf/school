const navLinks = document.getElementById('navLinks');
const menuToggle = document.getElementById('menuToggle');

menuToggle.addEventListener('click', () => {
    navLinks.classList.toggle('show');
});

const observerOptions = {
    threshold: 0.15,
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        if (entry.isIntersecting) {
            entry.target.classList.add('in-view');
        }
    });
}, observerOptions);

document.querySelectorAll('.fade-in, .slide-up').forEach((section) => {
    observer.observe(section);
});

window.addEventListener('scroll', () => {
    if (window.scrollY > 20) {
        document.querySelector('.navbar').classList.add('scrolled');
    } else {
        document.querySelector('.navbar').classList.remove('scrolled');
    }
});
