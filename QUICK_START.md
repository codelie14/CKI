# 🚀 CKI Project - Quick Start Commands

## Installation (First Time Only)

### 1. Install Python Dependencies
```bash
pip install django mysqlclient django-tailwind django-browser-reload requests beautifulsoup4 django-apscheduler
```

### 2. Install Node.js Dependencies
```bash
cd theme/static_src
npm install
npm run build
cd ../..
```

### 3. Setup Database
```bash
python manage.py migrate
python create_superuser.py
```

---

## Running the Application

### Start Development Server
```bash
python manage.py runserver
```

**Access Points:**
- 📊 Dashboard: http://127.0.0.1:8000/
- 🔧 Admin Panel: http://127.0.0.1:8000/admin/

**Default Credentials:**
- Username: `admin`
- Password: `admin123`

---

## Development Workflow

### When Modifying CSS/Tailwind
```bash
# Development mode (auto-watch)
cd theme/static_src
npm run dev
```

### When Modifying Python Code
Django auto-reloads, no action needed!

### When Adding New Models
```bash
python manage.py makemigrations
python manage.py migrate
```

---

## Common Tasks

### Create New Superuser
```bash
python manage.py createsuperuser
```

### Collect Static Files (Production)
```bash
python manage.py collectstatic
```

### Run Tests
```bash
python manage.py test
```

### Open Django Shell
```bash
python manage.py shell
```

---

## File Structure Quick Reference

```
CKI/
├── knowledge/models.py      # Database models
├── knowledge/admin.py       # Admin interface
├── core/templates/core/     # Dashboard templates
├── theme/templates/         # Base templates
└── cki_project/settings.py  # Configuration
```

---

## Troubleshooting

### Server Won't Start?
```bash
# Check if port is in use
netstat -ano | findstr :8000

# Use different port
python manage.py runserver 8080
```

### CSS Not Loading?
```bash
# Rebuild Tailwind
cd theme/static_src
npm run build
```

### Database Issues?
```bash
# Delete SQLite database and recreate
del cki_db.sqlite3
python manage.py migrate
python create_superuser.py
```

---

## Useful URLs

- Dashboard: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/
- API (future): http://127.0.0.1:8000/api/

---

## Next Development Steps

### Phase 2 - Cyber Scraper Engine
1. Set up `scraper/views.py`
2. Implement NVD API integration
3. Add BeautifulSoup scraping
4. Configure APScheduler

---

**Quick Help:** Read SETUP_GUIDE.md for detailed instructions
