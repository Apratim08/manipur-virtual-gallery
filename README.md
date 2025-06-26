# Manipur Virtual Art Gallery

A beautiful, responsive website showcasing the rich artistic heritage of Manipur, India, with an integrated AI chatbot.

## 🌟 Features

- **Interactive Gallery**: Beautiful carousel showcasing Manipur's traditional arts
- **AI-Powered Chatbot**: Intelligent responses about Manipur's art and culture
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile
- **Modern UI**: Clean design with smooth animations

## 🚀 Live Demo

Visit the live website: [Your Website URL will go here]

## 🛠️ Technologies Used

- **Frontend**: HTML5, CSS3, JavaScript
- **Backend**: Python Flask
- **AI**: OpenAI GPT-3.5-turbo (with fallback mock responses)
- **Styling**: Custom CSS with modern design patterns

## 🏃‍♂️ Quick Start

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set up your OpenAI API key in `.env`
4. Run: `python app.py`
5. Visit: `http://localhost:5000`

## 📁 Project Structure

```
manipur-virtual-gallery/
├── app.py              # Flask backend
├── requirements.txt    # Dependencies
├── templates/
│   └── index.html     # Main HTML template
└── static/
    ├── css/style.css  # Styling
    └── js/script.js   # JavaScript functionality
```

## Features Overview

### Gallery Carousel
- Auto-playing slideshow with manual navigation
- Responsive design that adapts to different screen sizes
- Smooth transitions and hover effects
- Indicator dots for direct slide navigation

### AI Chatbot
- Powered by OpenAI's GPT-3.5-turbo
- Specialized knowledge about Manipur's art and culture
- Minimizable chat interface
- Real-time responses with loading indicators

### Responsive Design
- Mobile-first approach
- Hamburger menu for mobile navigation
- Flexible layouts that work on all screen sizes
- Touch-friendly interactive elements

## Customization

### Adding New Gallery Images
1. Replace the Unsplash URLs in `templates/index.html` with your own images
2. Update the alt text and descriptions for each slide
3. Add or remove slides by modifying the HTML structure

### Modifying the Chatbot
- Edit the system prompt in `app.py` to change the chatbot's personality
- Adjust the `max_tokens` and `temperature` parameters for different response styles
- Customize the chatbot UI in the CSS file

### Styling Changes
- All styles are in `static/css/style.css`
- Colors, fonts, and layouts can be easily modified
- The design uses CSS custom properties for consistent theming

## Deployment

For production deployment, consider:

1. **Using a production WSGI server**:
   ```bash
   gunicorn -w 4 -b 0.0.0.0:5000 app:app
   ```

2. **Setting up environment variables** on your hosting platform

3. **Using a reverse proxy** like Nginx for serving static files

4. **Enabling HTTPS** for secure communication

## Contributing

Feel free to contribute to this project by:
- Adding more information about Manipur's art forms
- Improving the UI/UX design
- Adding new features like user accounts or favorites
- Optimizing performance

## License

This project is open source and available under the MIT License.

## About Manipur

Manipur is a state in northeastern India known for its rich cultural heritage, including:
- Classical Manipuri dance (one of eight classical Indian dance forms)
- Traditional handloom textiles
- Exquisite pottery and crafts
- Vibrant paintings and visual arts
- Rich musical traditions

This virtual gallery aims to preserve and showcase these beautiful art forms to a global audience.
