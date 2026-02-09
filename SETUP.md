# Setup Instructions

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Installation Steps

### 1. Create Virtual Environment (Recommended)

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On Linux/Mac:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Your Information

Edit `app.py` and update the following sections:

#### Contact Information (Lines 15-30)
```python
CONTACT_INFO = {
    'phone': '79001234567',              # YOUR PHONE NUMBER
    'whatsapp_msg': 'Здравствуйте! Нужна юридическая консультация.',
    'email': 'lawyer@example.com',       # YOUR EMAIL
    'address': 'Москва, ул. Тверская, д. 1, офис 101',  # YOUR ADDRESS
    'hours': 'Пн-Пт: 9:00 - 18:00',     # YOUR HOURS
}
```

#### Attorney Information (Lines 32-54)
```python
ATTORNEY_INFO = {
    'name': 'Александр Иванов',          # YOUR NAME
    'title': 'Адвокат',                  # YOUR TITLE
    'specialization': 'Уголовное и гражданское право',
    # ... update other fields as needed
}
```

#### Practice Areas (Lines 56-84)
Add, remove, or modify practice areas as needed.

### 4. Add Your Images

Place your images in `static/img/` folder:

- `lawyer-photo.jpg` - Your professional headshot (800x800px)
- `certificate-1.jpg` through `certificate-4.jpg` - Your documents

See `static/img/README.md` for details.

### 5. Run the Application

#### Development Mode
```bash
python app.py
```

The website will be available at `http://localhost:5000`

#### Production Mode
```bash
gunicorn --bind 0.0.0.0:8000 app:app
```

## Quick Customization

### Change Phone Number
1. Open `app.py`
2. Find `CONTACT_INFO['phone']`
3. Enter your number in international format without the + sign
   - Example: `'79001234567'` for +7 (900) 123-45-67

### Change WhatsApp Message
1. Open `app.py`
2. Find `CONTACT_INFO['whatsapp_msg']`
3. Update the default message

### Change Colors
1. Open `templates/base.html`
2. Find the Tailwind config section (around line 10)
3. Update the color values:
   - `navy` colors for the dark blue theme
   - `gold` colors for accent colors

## Troubleshooting

### Port Already in Use
If port 5000 is already in use:
```bash
# Use a different port
python app.py --port 5001

# Or with gunicorn
gunicorn --bind 0.0.0.0:8001 app:app
```

### Images Not Displaying
- Verify images are in `static/img/` folder
- Check filenames match exactly
- Ensure images are in JPG or PNG format
- Verify file permissions (readable)

### WhatsApp Link Not Working
- Verify phone number format (no + sign, no spaces)
- Example: `79001234567` not `+7 900 123-45-67`
- Test the link in a browser first

## Project Structure

```
project/
├── app.py                  # Main Flask app (EDIT THIS)
├── requirements.txt        # Python dependencies
├── templates/
│   ├── base.html          # Base template (navbar, footer)
│   └── index.html         # Main content
├── static/
│   ├── css/
│   │   └── custom.css     # Custom styles
│   └── img/               # Your images (ADD PHOTOS HERE)
└── README.md              # Full documentation
```

## Next Steps

1. Customize the content in `app.py`
2. Add your images to `static/img/`
3. Test the website locally
4. Deploy to your hosting platform
5. Add Google Maps (see README.md for instructions)

## Support

Refer to README.md for detailed documentation and customization options.
