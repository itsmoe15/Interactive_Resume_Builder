// Starfield Animation
const canvas = document.getElementById('starfield');
const ctx = canvas.getContext('2d');

// Set canvas size
function resizeCanvas() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
}

resizeCanvas();

// Create stars
const stars = Array(150).fill().map(() => ({
    x: Math.random() * canvas.width,
    y: Math.random() * canvas.height,
    radius: Math.random() * 1.5 + 0.5,
    speed: Math.random() * 0.5 + 0.1,
    alpha: Math.random()
}));

// Draw stars
function drawStars() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    stars.forEach(star => {
        ctx.beginPath();
        ctx.arc(star.x, star.y, star.radius, 0, Math.PI * 2);
        ctx.fillStyle = `rgba(255, 255, 255, ${star.alpha})`;
        ctx.fill();
        
        // Move star
        star.x += star.speed;
        
        // Reset star position when it goes off screen
        if (star.x > canvas.width) {
            star.x = 0;
            star.y = Math.random() * canvas.height;
            star.alpha = Math.random();
        }
    });

    requestAnimationFrame(drawStars);
}

document.addEventListener('DOMContentLoaded', function() {
    // Navbar elements
    const hamburger = document.querySelector('.hamburger');
    const menuWrapper = document.querySelector('.menu-wrapper');
    const navLinks = document.querySelectorAll('.nav-link');
    
    // CV Builder elements
    const createCvBtn = document.getElementById('create-cv-btn');
    const aiAssistantBtn = document.getElementById('ai-assistant-btn');
    const viewCvsBtn = document.getElementById('view-cvs-btn');
    const atsCheckerBtn = document.getElementById('ats-checker-btn');
    
    // Toggle mobile menu
    hamburger.addEventListener('click', () => {
        hamburger.classList.toggle('active');
        menuWrapper.classList.toggle('active');
    });
    
    // Close menu when clicking on a link (mobile)
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            if (window.innerWidth <= 992) {
                hamburger.classList.remove('active');
                menuWrapper.classList.remove('active');
            }
        });
    });
    
    // CV Builder button handlers
    createCvBtn.addEventListener('click', function() {
        window.location.href = '/cv-maker';
    });
    
    aiAssistantBtn.addEventListener('click', function() {
        window.location.href = '/chatbot';
    });
    
    viewCvsBtn.addEventListener('click', function() {
        window.location.href = '/my-cvs';
    });
    
    atsCheckerBtn.addEventListener('click', function() {
        window.location.href = '/ats-checker';
    });
    
    
    // Handle window resize
    window.addEventListener('resize', () => {
        resizeCanvas();
        if (window.innerWidth > 992) {
            hamburger.classList.remove('active');
            menuWrapper.classList.remove('active');
        }
    });
    
    // Start animations
    drawStars();
});
