# 🚀 CKI Project - Setup & Running Guide

## ✅ Phase 1 Complete - Foundation & Modeling

### What's Been Implemented

#### 1. **Database Models** (`knowledge/models.py`)
- ✅ Vendor - Technology vendors
- ✅ Product - Software products and versions
- ✅ Vulnerability - CVE tracking with CVSS scores
- ✅ Exploit - Known exploits
- ✅ ThreatGroup - APT groups and threat actors
- ✅ AttackPattern - MITRE ATT&CK patterns
- ✅ IndicatorOfCompromise (IOC) - IPs, domains, hashes, URLs
- ✅ Article - Scraped content
- ✅ AIAnalysis - AI-powered analysis results
- ✅ Alert - Security alerts
- ✅ Report - Generated reports

#### 2. **Dashboard Interface** (`core/templates/core/home.html`)
- ✅ Modern dark theme with Tailwind CSS v4 + DaisyUI
- ✅ Real-time statistics cards
- ✅ Recent vulnerabilities table
- ✅ Threat groups monitoring
- ✅ AI analysis section
- ✅ Quick action buttons

#### 3. **Admin Interface** (`knowledge/admin.py`)
- ✅ Complete admin interface for all models
- ✅ Search and filter capabilities
- ✅ User-friendly data management

#### 4. **Configuration**
- ✅ SQLite database (development-ready)
- ✅ MySQL/MariaDB configuration ready for production
- ✅ Static files configured
- ✅ Template system configured
- ✅ Django Tailwind integration

---

## 🏃 How to Run the Project

### Prerequisites
- Python 3.12+
- Node.js (for Tailwind CSS)
- Git

### Installation Steps

#### 1. Install Python Dependencies
```bash
pip install django mysqlclient django-tailwind django-browser-reload requests beautifulsoup4 django-apscheduler
```

#### 2. Install Node.js Dependencies
```bash
cd theme/static_src
npm install
npm run build
cd ../..
```

#### 3. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

#### 4. Create Superuser (Optional - already created)
```bash
python create_superuser.py
```
**Default credentials:**
- Username: `admin`
- Password: `admin123`

#### 5. Start Development Server
```bash
python manage.py runserver
```

---

## 🌐 Access Points

### Dashboard
**URL:** http://127.0.0.1:8000/

Features:
- Global threat statistics
- Recent vulnerabilities overview
- Threat groups monitoring
- AI analysis dashboard
- Quick action buttons

### Admin Interface
**URL:** http://127.0.0.1:8000/admin/

Features:
- Full CRUD operations for all models
- Advanced search and filtering
- Bulk operations support
- User management

---

## 📁 Project Structure

```
CKI/
├── cki_project/          # Main Django project
│   ├── settings.py       # Configuration
│   ├── urls.py           # URL routing
│   └── wsgi.py           # WSGI config
├── core/                 # Core application
│   ├── templates/core/   # Dashboard templates
│   ├── views.py          # View controllers
│   └── urls.py           # URL patterns
├── knowledge/            # Knowledge base app
│   ├── models.py         # All data models
│   ├── admin.py          # Admin interface
│   └── migrations/       # Database migrations
├── scraper/              # Web scraper app (Phase 2)
├── ai_engine/            # AI analysis app (Phase 3)
├── scanner/              # Document scanner app (Phase 4)
├── theme/                # UI theme
│   ├── static/css/dist/  # Compiled CSS
│   ├── static_src/       # Source files
│   └── templates/        # Base templates
├── manage.py             # Django management
├── requirements.txt      # Python dependencies
└── ROADMAP.md           # Project roadmap
```

---

## 🗄️ Database Configuration

### Current (Development)
- **Engine:** SQLite3
- **File:** `cki_db.sqlite3`
- **Status:** ✅ Ready to use

### Production (MySQL/MariaDB)
To switch to MySQL/MariaDB:

1. Update `settings.py`:
```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "cki_db",
        "USER": "root",
        "PASSWORD": "your_password",
        "HOST": "localhost",
        "PORT": "3306",
    }
}
```

2. Ensure MariaDB 10.5+ or MySQL 8.0+ is installed

3. Run migrations again:
```bash
python manage.py migrate
```

---

## 🎨 UI Framework

### Tech Stack
- **Tailwind CSS v4** - Utility-first CSS framework
- **DaisyUI** - Component library for Tailwind
- **Dark Theme** - Professional cybersecurity aesthetic

### Customization
To modify the theme:
1. Edit `theme/static_src/src/styles.css`
2. Run: `npm run dev` (development) or `npm run build` (production)

---

## 📊 Current Status

### ✅ Completed (Phase 1)
- [x] Django environment setup
- [x] Modular apps creation
- [x] Database modeling
- [x] Migration system
- [x] Dashboard layout
- [x] Admin interface
- [x] Tailwind CSS integration

### 🔄 Next Phase (Phase 2 - Cyber Scraper Engine)
- [ ] NVD API integration for CVE data
- [ ] Blog scraping with BeautifulSoup
- [ ] Duplicate detection
- [ ] APScheduler for automated tasks
- [ ] Scan monitoring dashboard

---

## 🛠️ Development Tips

### Adding New Data via Admin
1. Go to http://127.0.0.1:8000/admin/
2. Login with admin credentials
3. Select any model to add/edit data

### Testing the Dashboard
The dashboard currently shows placeholder data ("0" values). To see real data:
1. Add some test data via the admin interface
2. Update the view to fetch actual counts from the database

### Hot Reload
- Django auto-reloads on Python file changes
- For CSS changes, run: `npm run dev` in `theme/static_src/`

---

## 📝 Important Files

### Configuration
- `cki_project/settings.py` - Main settings
- `requirements.txt` - Python dependencies
- `theme/static_src/package.json` - Node.js dependencies

### Key Models
- `knowledge/models.py` - All database models
- `knowledge/admin.py` - Admin interface configuration

### Templates
- `theme/templates/base.html` - Base template
- `core/templates/core/home.html` - Dashboard page

---

## 🔐 Security Notes

- Change the default admin password in production
- Set `DEBUG = False` in production
- Use environment variables for sensitive data
- Configure proper `ALLOWED_HOSTS`

---

## 📞 Support

For issues or questions:
1. Check Django documentation: https://docs.djangoproject.com/
2. Tailwind CSS docs: https://tailwindcss.com/docs
3. DaisyUI docs: https://daisyui.com/

---

**Last Updated:** March 3, 2026  
**Project Status:** Phase 1 Complete ✅
