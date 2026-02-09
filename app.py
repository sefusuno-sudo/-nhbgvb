"""
Attorney Business Card Website - Flask Application
Main entry point for the Flask web application
"""

from flask import Flask, render_template
from urllib.parse import quote

app = Flask(__name__)

# ==============================================================================
# CONFIGURATION - Edit these values to customize your business card
# ==============================================================================
CONTACT_INFO = {
    # Phone number in international format (without + sign)
    # Example: '79001234567' for Russian number
    'phone': '+37368976567',

    # Default WhatsApp message (in Russian, but you can change to any language)
    'whatsapp_msg': 'Bună ziua! Am nevoie de consultanță juridică.',
    # Your professional email
    'email': 'lawyer@example.com',

    # Office address
    'address': 'Chișinău, str. Exemplu, nr. 1, birou 101',

    # Business hours
    'hours': 'Пн-Пт: 9:00 - 18:00',
}

ATTORNEY_INFO = {
    # Your name and title
    'name': 'ION SARBU',
    'title': 'Avocat',
    'specialization': 'Drept penal și civil',

    # Hero section
    'hero_title': 'Asistență juridică profesională',
    'hero_subtitle': 'Protejarea drepturilor și intereselor dumneavoastră',

    # About section
    'about_title': 'О специалисте',
    'about_text': '''
        Более 15 лет успешной практики в области уголовного и гражданского права.
        Член Адвокатской палаты города Москвы. Защита интересов клиентов в судах
        всех инстанций. Индивидуальный подход к каждому делу.
    ''',

    # Credentials
    'credentials': [
        'Адвокатское удостоверение № 77/12345',
        'Член АП г. Chișinău с 2008 года',
        'Более 200 успешно завершенных дел'
    ]
}

# Areas of practice
PRACTICE_AREAS = [
    {
        'icon': '⚖️',
        'title': 'Уголовное право',
        'description': 'Защита по уголовным делам на всех стадиях процесса'
    },
    {
        'icon': '🏛️',
        'title': 'Гражданское право',
        'description': 'Споры по договорам, взыскание задолженности, защита прав потребителей'
    },
    {
        'icon': '👨‍👩‍👧',
        'title': 'Семейное право',
        'description': 'Развод, раздел имущества, алименты, опека'
    },
    {
        'icon': '🏢',
        'title': 'Корпоративное право',
        'description': 'Юридическое сопровождение бизнеса, споры между учредителями'
    },
    {
        'icon': '🏠',
        'title': 'Жилищное право',
        'description': 'Сделки с недвижимостью, приватизация, выселение'
    },
    {
        'icon': '💼',
        'title': 'Трудовое право',
        'description': 'Трудовые споры, восстановление на работе, взыскание зарплаты'
    }
]

# ==============================================================================
# ROUTES
# ==============================================================================

@app.route('/')
def index():
    """Main page route"""
    # Generate WhatsApp link with encoded message
    whatsapp_link = f"https://wa.me/{CONTACT_INFO['phone']}?text={quote(CONTACT_INFO['whatsapp_msg'])}"

    return render_template(
        'index.html',
        contact=CONTACT_INFO,
        attorney=ATTORNEY_INFO,
        practice_areas=PRACTICE_AREAS,
        whatsapp_link=whatsapp_link
    )

@app.route('/health')
def health():
    """Health check endpoint"""
    return {'status': 'ok'}, 200

# ==============================================================================
# ERROR HANDLERS
# ==============================================================================

@app.errorhandler(404)
def page_not_found(e):
    """404 error handler"""
    return render_template('index.html'), 404

@app.errorhandler(500)
def internal_error(e):
    """500 error handler"""
    return render_template('index.html'), 500

# ==============================================================================
# APPLICATION ENTRY POINT
# ==============================================================================

if __name__ == '__main__':
    # For development only
    app.run(host='0.0.0.0', port=5000, debug=True)
