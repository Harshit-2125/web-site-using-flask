// code.js
let currentIndex = 0;
const slides = document.querySelectorAll('.testimonial-slide');
const totalSlides = slides.length;

function showReview(index) {
    const wrapper = document.getElementById('testimonial-wrapper');
    wrapper.style.transform = `translateX(${-100 * index}%)`;
}

function nextReview() {
    currentIndex++;
    if (currentIndex >= totalSlides) {
        currentIndex = 0; // Go back to the first review in forward animation
    }
    showReview(currentIndex);
}

function prevReview() {
    currentIndex--;
    if (currentIndex < 0) {
        currentIndex = totalSlides - 1; // This prevents the slider from moving backward
    }
    showReview(currentIndex);
}

// Automatic sliding every 4 seconds
setInterval(() => {
    nextReview();
}, 4000);
