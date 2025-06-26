// Gallery Carousel Functionality
let currentSlideIndex = 0;
let slides, indicators;

// Initialize carousel
document.addEventListener('DOMContentLoaded', function() {
    // Initialize DOM elements
    slides = document.querySelectorAll('.carousel-slide');
    indicators = document.querySelectorAll('.indicator');
    
    showSlide(0);
    
    // Auto-play carousel
    setInterval(() => {
        changeSlide(1);
    }, 5000);
    
    // Initialize chatbot
    initializeChatbot();
});

function showSlide(index) {
    // Hide all slides
    slides.forEach(slide => slide.classList.remove('active'));
    indicators.forEach(indicator => indicator.classList.remove('active'));
    
    // Show current slide
    slides[index].classList.add('active');
    indicators[index].classList.add('active');
    
    currentSlideIndex = index;
}

function changeSlide(direction) {
    let newIndex = currentSlideIndex + direction;
    
    if (newIndex >= slides.length) {
        newIndex = 0;
    } else if (newIndex < 0) {
        newIndex = slides.length - 1;
    }
    
    showSlide(newIndex);
}

function currentSlide(index) {
    showSlide(index - 1);
}

// Smooth scroll to gallery
function scrollToGallery() {
    document.getElementById('gallery').scrollIntoView({
        behavior: 'smooth'
    });
}

// Mobile Navigation
const hamburger = document.querySelector('.hamburger');
const navMenu = document.querySelector('.nav-menu');

if (hamburger) {
    hamburger.addEventListener('click', () => {
        hamburger.classList.toggle('active');
        navMenu.classList.toggle('active');
    });
}

// Close mobile menu when clicking on a link
document.querySelectorAll('.nav-menu a').forEach(link => {
    link.addEventListener('click', () => {
        hamburger.classList.remove('active');
        navMenu.classList.remove('active');
    });
});

// Chatbot Functionality
let isChatbotMinimized = false;

function initializeChatbot() {
    const chatbot = document.getElementById('chatbot');
    chatbot.classList.add('minimized');
    isChatbotMinimized = true;
}

function toggleChatbot() {
    const chatbot = document.getElementById('chatbot');
    const toggle = document.getElementById('chatbot-toggle');
    
    if (isChatbotMinimized) {
        chatbot.classList.remove('minimized');
        toggle.style.transform = 'rotate(0deg)';
    } else {
        chatbot.classList.add('minimized');
        toggle.style.transform = 'rotate(180deg)';
    }
    
    isChatbotMinimized = !isChatbotMinimized;
}

function handleKeyPress(event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
}

async function sendMessage() {
    const messageInput = document.getElementById('messageInput');
    const message = messageInput.value.trim();
    
    if (!message) return;
    
    // Add user message to chat
    addMessageToChat(message, 'user');
    messageInput.value = '';
    
    // Show loading indicator
    const loadingDiv = document.createElement('div');
    loadingDiv.className = 'message bot-message';
    loadingDiv.innerHTML = '<div class="loading"></div>';
    loadingDiv.id = 'loading-message';
    
    const chatMessages = document.getElementById('chatMessages');
    chatMessages.appendChild(loadingDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
    
    try {
        console.log('Sending message to server:', message);
        const response = await fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: message })
        });
        
        console.log('Response status:', response.status);
        const data = await response.json();
        console.log('Response data:', data);
        
        // Remove loading indicator
        const loadingMessage = document.getElementById('loading-message');
        if (loadingMessage) {
            loadingMessage.remove();
        }
        
        if (response.ok) {
            addMessageToChat(data.response, 'bot');
        } else {
            console.error('Server error:', data.error);
            addMessageToChat(`Sorry, I encountered an error: ${data.error || 'Please try again.'}`, 'bot');
        }
    } catch (error) {
        console.error('Network error:', error);
        // Remove loading indicator
        const loadingMessage = document.getElementById('loading-message');
        if (loadingMessage) {
            loadingMessage.remove();
        }
        
        addMessageToChat('Sorry, I\'m having trouble connecting. Please check your internet connection and try again.', 'bot');
    }
}

function addMessageToChat(message, sender) {
    const chatMessages = document.getElementById('chatMessages');
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${sender}-message`;
    
    const messageText = document.createElement('p');
    messageText.textContent = message;
    messageDiv.appendChild(messageText);
    
    chatMessages.appendChild(messageDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

// Header scroll effect
window.addEventListener('scroll', () => {
    const header = document.querySelector('.header');
    if (window.scrollY > 100) {
        header.style.background = 'rgba(255, 255, 255, 0.98)';
        header.style.boxShadow = '0 2px 20px rgba(0,0,0,0.1)';
    } else {
        header.style.background = 'rgba(255, 255, 255, 0.95)';
        header.style.boxShadow = 'none';
    }
});

// Intersection Observer for animations
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

// Observe elements for animation
document.addEventListener('DOMContentLoaded', () => {
    const animatedElements = document.querySelectorAll('.feature, .about-text, .contact-item');
    
    animatedElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });
});

// Gallery image preloading for better performance
function preloadImages() {
    const imageUrls = [
        'https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=800&h=600&fit=crop',
        'https://images.unsplash.com/photo-1571896349842-33c89424de2d?w=800&h=600&fit=crop',
        'https://images.unsplash.com/photo-1578643463396-0997cb5328c1?w=800&h=600&fit=crop',
        'https://images.unsplash.com/photo-1541961017774-22349e4a1262?w=800&h=600&fit=crop',
        'https://images.unsplash.com/photo-1557804506-669a67965ba0?w=800&h=600&fit=crop'
    ];
    
    imageUrls.forEach(url => {
        const img = new Image();
        img.src = url;
    });
}

// Call preload function when page loads
document.addEventListener('DOMContentLoaded', preloadImages);
