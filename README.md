# Attorney Business Card Website

A professional, responsive business card website for attorneys built with Flask and Tailwind CSS.

## Features

- Modern, professional design with dark blue and gold color scheme
- Fully responsive (mobile-first design)
- Floating WhatsApp button for easy contact
- Sections: Hero, Services, About, Contact Form, Map
- Easy to customize (all configuration in `app.py`)
- SEO-friendly structure
- Template inheritance using Jinja2

## Project Structure

```
.
├── app.py                  # Main Flask application with all configuration
├── requirements.txt        # Python dependencies
├── templates/
│   ├── base.html          # Base template (navbar, footer, layout)
│   └── index.html         # Main page content
├── static/
│   ├── css/
│   │   └── custom.css     # Custom CSS styles
│   └── img/               # Images folder (add your photos here)
└── README.md
```

## Quick Start

### 1. Installation

```bash
# Install dependencies
pip install -r requirements.txt
```

### 2. Configuration

Edit the configuration in `app.py`:

```python
# Line 15-30: Contact Information
CONTACT_INFO = {
    'phone': '79001234567',              # Change to your phone number
    'whatsapp_msg': 'Your message here', # Change WhatsApp message
    'email': 'your@email.com',           # Change to your email
    'address': 'Your address',           # Change to your address
    'hours': 'Mon-Fri: 9:00 - 18:00',   # Change working hours
}

# Line 32-54: Attorney Information
ATTORNEY_INFO = {
    'name': 'Your Name',                 # Change to your name
    'title': 'Attorney',                 # Change your title
    # ... edit other fields
}

# Line 56-84: Practice Areas
PRACTICE_AREAS = [
    # Edit or add new practice areas
]
```

### 3. Add Your Images

Place your images in the `static/img/` folder:

- `lawyer-photo.jpg` - Your professional photo (800x800px recommended)
- `certificate-1.jpg` through `certificate-4.jpg` - Your certificates/documents

See `static/img/README.md` for detailed image requirements.

### 4. Run the Application

```bash
# Development mode
python app.py

# Production mode (with Gunicorn)
gunicorn app:app
```

The website will be available at `http://localhost:5000`

## Customization Guide

### Change Phone Number & WhatsApp

1. Open `app.py`
2. Find `CONTACT_INFO` dictionary (line 15)
3. Edit the `phone` field (use international format without +)
4. Edit the `whatsapp_msg` field to customize the default message

Example:
```python
CONTACT_INFO = {
    'phone': '79001234567',  # Format: country code + number (no + sign)
    'whatsapp_msg': 'Hello! I need legal consultation.',
}
```

### Change Colors

The default color scheme is dark blue and gold. To change:

1. Open `templates/base.html`
2. Find the Tailwind config (line 10-26)
3. Edit the color values:

```javascript
colors: {
    'navy': {
        900: '#0a1628',  // Darkest blue
        800: '#132037',  // Medium blue
        700: '#1e2f47',  // Light blue
    },
    'gold': {
        500: '#d4af37',  // Main gold
        600: '#c5a028',  // Darker gold
    }
}
```

### Add/Remove Practice Areas

1. Open `app.py`
2. Find `PRACTICE_AREAS` list (line 56)
3. Add or remove items:

```python
PRACTICE_AREAS = [
    {
        'icon': '⚖️',  # Use emoji or Font Awesome class
        'title': 'Your Practice Area',
        'description': 'Description of your services'
    },
    # Add more areas here
]
```

### Change Images

Replace images in `static/img/` folder or edit the paths in `templates/index.html`:

```html
<!-- Line 67 for profile photo -->
<img src="{{ url_for('static', filename='img/YOUR-IMAGE.jpg') }}" ...>
```

### Add Google Maps

1. Go to [Google Maps](https://www.google.com/maps)
2. Search for your address
3. Click "Share" → "Embed a map"
4. Copy the iframe code
5. Open `templates/index.html`
6. Find the maps section (line ~515)
7. Replace the placeholder div with your iframe

### Modify Contact Form

The contact form is UI-only by default (shows an alert). To make it functional:

1. Create a backend endpoint to handle form submissions
2. Edit the form handler in `templates/index.html` (line ~535)
3. Send data to your endpoint using fetch/AJAX

## Deployment

### Using Gunicorn (Production)

```bash
gunicorn --bind 0.0.0.0:8000 app:app
```

### Environment Variables

For production, consider using environment variables for sensitive data:

```python
import os

CONTACT_INFO = {
    'phone': os.getenv('PHONE_NUMBER', '79001234567'),
    'email': os.getenv('EMAIL', 'lawyer@example.com'),
}
```

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Technology Stack

- **Backend**: Flask 3.0.0
- **Frontend**: HTML5, Tailwind CSS 3.x
- **Template Engine**: Jinja2
- **Icons**: Font Awesome 6.4.0
- **Fonts**: Google Fonts (Playfair Display, Inter)

## License

This project is free to use and modify for your personal or commercial needs.

## Support

For questions or issues, please refer to the official documentation:
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Tailwind CSS Documentation](https://tailwindcss.com/docs)

## Notes

- The WhatsApp link works on both desktop and mobile
- All images have fallback placeholders (icons)
- The site is fully responsive and mobile-optimized
- SEO meta tags are included in the base template
- Smooth scrolling and animations are enabled by default
