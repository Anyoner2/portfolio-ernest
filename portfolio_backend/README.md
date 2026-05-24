# Ernest Anyona — Portfolio Backend

Django REST API powering the portfolio website.

## Setup

```bash
# 1. Create virtual environment
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run migrations
python manage.py makemigrations
python manage.py migrate

# 4. Create admin user
python manage.py createsuperuser

# 5. Start server
python manage.py runserver
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /api/contacts/ | Send a contact message |
| GET | /api/contacts/ | List all messages |
| GET | /api/projects/ | List all projects |
| POST | /api/projects/ | Add a new project |
| GET | /api/projects/<id>/ | Get single project |
| PUT | /api/projects/<id>/ | Update a project |
| DELETE | /api/projects/<id>/ | Delete a project |
| GET | /api/projects/featured/ | Get featured projects only |
| GET | /api/blog/ | List published blog posts |
| POST | /api/blog/ | Create a blog post |
| GET | /api/blog/<slug>/ | Get single blog post |

## Admin Panel
Visit http://localhost:8000/admin to manage all data.

## Email Setup (Gmail)
1. Enable 2FA on your Google account
2. Go to Google Account → Security → App Passwords
3. Generate a password for "Mail"
4. Add it to your environment variables (see `.env.example`) as `EMAIL_HOST_PASSWORD`

### Environment variables
This project reads sensitive configuration from environment variables. A sample file is provided at `.env.example`. Important variables include:

- `DJANGO_SECRET_KEY` — keep secret in production
- `DJANGO_DEBUG` — `True` for development, `False` for production
- `DJANGO_ALLOWED_HOSTS` — comma-separated hosts
- `EMAIL_*` — SMTP settings (or omit to use console backend locally)

To load environment variables locally you can use your shell or a tool like `python-dotenv`.

### Local .env support
1. Copy `.env.example` to `.env` in `portfolio_backend`
2. Update values in `.env` for your local setup
3. Restart the Django server; `settings.py` will load `.env` automatically

> Do not commit `.env` to source control.

### Testing email locally
For quick local testing the project defaults to the console email backend when `DEBUG=True`. This prints outgoing email to the runserver console instead of sending it.

To test sending an email in the Django shell:

```powershell
cd "C:\Users\Administrator\OneDrive\Desktop\portfolio ernest"
.venv\Scripts\activate
python portfolio_backend\manage.py shell
```

Then run:

```python
from django.core.mail import send_mail
send_mail('Test', 'This is a test', 'sender@example.com', ['recipient@example.com'])
```

If you want to send real emails, set `DJANGO_DEBUG=False` and provide the SMTP credentials in your environment (see `.env.example`).

## Deploy to Render (free)
1. Push to GitHub
2. Go to render.com → New Web Service
3. Connect your repo
4. Set build command: `pip install -r requirements.txt`
5. Set start command: `gunicorn portfolio_backend.wsgi`
