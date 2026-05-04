# Bloom Microservice Website

Corporate website for Bloom Microservice - a software development company specializing in cloud solutions and enterprise applications.

## Tech Stack

- **Backend**: Django 4.2+
- **Admin Theme**: Unfold
- **Translation**: Django Parler (Bilingual - Arabic & English)
- **Frontend**: Tailwind CSS
- **Database**: SQLite (default)

## Applications

- **core**: Site settings, team members
- **pages**: Static pages management
- **services**: Company services
- **projects**: Portfolio/projects
- **jobs**: Job listings
- **cms**: Content management

## Requirements

- Python 3.10+
- Node.js (for CSS development)

## Installation

### 1. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Install Tailwind CSS

```bash
npm install
```

### 4. Environment Variables (Optional)

Create `.env` file in project root:

```env
DJANGO_SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### 5. Run Migrations

```bash
python manage.py migrate
```

### 6. Create Superuser

```bash
python manage.py createsuperuser
```

### 7. Build CSS

```bash
npm run build:css
```

## Running the Project

### Development

```bash
npm run watch:css  # Watch mode for Tailwind
python manage.py runserver
```

Then open `http://localhost:8000`

### Production

```bash
python manage.py collectstatic --noinput
python manage.py migrate
gunicorn config.wsgi:application --bind 0.0.0.0:8000
```

## Project Structure

```
bloom-ms/
├── config/          # Django settings
├── core/            # Core models (Team, Settings)
├── pages/           # Pages management
├── services/        # Services
├── projects/        # Projects/Portfolio
├── jobs/            # Job listings
├── templates/       # HTML templates
├── static/          # Static files
├── media/           # Uploaded files
└── locale/         # Translation files
```

## Admin Panel

- **URL**: `/admin/`
- **Languages**: Arabic & English supported (switch from top bar)
- **Settings**: Modify text and images via Site Settings in admin panel

## Useful Commands

```bash
python manage.py seed_data    # Add sample data
python manage.py makemigrations  # Create migrations
python manage.py check        # Check for errors
```

## Translations

To update translations:

```bash
python manage.py makemessages -a
python manage.py compilemessages
```

## License

All rights reserved © 2024 Bloom Microservice