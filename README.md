# Manipur Virtual Art Gallery

A beautiful, responsive website showcasing the rich artistic heritage of Manipur, India, with an integrated AI chatbot.

## � Live Website

**Visit the live website: [https://manipur-virtual-gallery.onrender.com](https://manipur-virtual-gallery.onrender.com)**

## �🌟 Features

- **Interactive Gallery**: Beautiful carousel showcasing Manipur's traditional arts
- **AI-Powered Chatbot**: Intelligent responses about Manipur's art and culture
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile
- **Modern UI**: Clean design with smooth animations

## 🎨 Gallery Highlights

The website features an auto-playing carousel showcasing:
- **Classical Manipuri Dance**: One of India's eight classical dance forms
- **Traditional Handloom**: Exquisite textiles and weaving craftsmanship
- **Pottery & Ceramics**: Beautiful ceramic art reflecting cultural heritage
- **Traditional Paintings**: Vibrant artwork depicting cultural narratives
- **Handicrafts**: Intricate crafts passed down through generations

## 🤖 Interactive Chatbot

The chatbot provides informative responses about:
- Manipuri classical dance traditions
- Traditional art forms and techniques
- Cultural heritage and history
- Handloom textiles and craftsmanship
- Pottery and ceramic arts

## 🛠️ Technologies Used

- **Frontend**: HTML5, CSS3, JavaScript
- **Backend**: Python Flask
- **Deployment**: Render.com
- **AI**: OpenAI GPT-3.5-turbo (with intelligent fallback responses)
- **Styling**: Custom CSS with modern design patterns

## 🏃‍♂️ Local Development

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/manipur-virtual-gallery.git
   cd manipur-virtual-gallery
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run locally:
   ```bash
   python app.py
   ```

4. Visit: `http://localhost:5000`

## 📁 Project Structure

```
manipur-virtual-gallery/
├── app.py              # Flask backend with chatbot logic
├── requirements.txt    # Python dependencies
├── runtime.txt         # Python version for deployment
├── templates/
│   └── index.html     # Main HTML template
└── static/
    ├── css/style.css  # Modern responsive styling
    └── js/script.js   # Interactive JavaScript features
```

## 🎯 About Manipur's Art

Manipur, known as the "Jewel of India," is renowned for:
- **Classical Dance**: Graceful Manipuri dance with spiritual themes
- **Handloom Textiles**: Fine quality fabrics with intricate designs
- **Traditional Pottery**: Skilled ceramic artistry
- **Cultural Paintings**: Vibrant depictions of mythology and culture
- **Rich Heritage**: Blend of Hindu and indigenous traditions

## 📄 License

MIT License - feel free to use this project for educational and personal purposes.

---

**🌟 Experience the rich cultural heritage of Manipur at [manipur-virtual-gallery.onrender.com](https://manipur-virtual-gallery.onrender.com)**

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
