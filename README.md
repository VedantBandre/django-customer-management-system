# Customer Management System For E-Corp

A clean, modern **Django CMS** to manage customers and orders — featuring a dark **Aurora** theme, Bootstrap 4 UI, colored status badges, powerful filtering, and a full authentication & password-reset flow.

![Django](https://img.shields.io/badge/Django-5.x-0f172a?logo=django)
![Python](https://img.shields.io/badge/Python-3.11+-0f172a?logo=python)
![Bootstrap](https://img.shields.io/badge/Bootstrap-4.3-0f172a?logo=bootstrap)
[![License](https://img.shields.io/badge/license-MIT-green)](./LICENSE)

---
<img width="1867" height="977" alt="image" src="https://github.com/user-attachments/assets/263d7c84-51e9-4a54-ad34-fa70e023bcc4" />


## Features

* **Customers CRUD**

  * Customer detail with contact info, total orders, quick actions
  * Unique email, phone, address fields
* **Orders management**

  * Create / Update / Delete orders
  * **Colored status badges** (Delivered, Pending, Out for Delivery, etc.)
* **Search & Filter (django-filter)**

  * One-line filter bar (labels above fields)
  * Filter by product, status, note, date range (from / to)
* **Beautiful UI**

  * **Aurora Dark theme** via CSS variables
  * **Bootstrap 4** components, responsive layout
  * Equal-height stat cards, tidy tables, subtle hover/tints
* **Navigation & Branding**

  * Navbar integrated with `SITE_NAME`
  * Footer with Brand / Resources / Contact (equalized)
* **Authentication**

  * Login / Register
  * Full password reset flow:

    * request, “email sent”, set new password, complete
  * Auth pages hide navbar/footer via template blocks
* **Profile / Account**

  * Account settings page with profile picture upload

---

## Tech Stack

* **Django 5.x** (SQLite by default)
* **Python 3.11+** (recommended)
* **django-filter**
* **Bootstrap 4.3**, jQuery, Popper
* Static assets served via **Django staticfiles**

---

## Project Structure

```
customer-management-application/
├── crm/                          # Django project
│   ├── settings.py               # Django settings (Django 5.x)
│   ├── urls.py
│   └── wsgi.py
├── accounts/                     # Main app (views, templates, forms)
│   ├── templates/accounts/
│   │   ├── main.html             # Base layout (Aurora theme)
│   │   ├── navbar.html           # Themed navbar (SITE_NAME-aware)
│   │   ├── login.html            # Auth pages (navbar/footer hidden)
│   │   ├── register.html
│   │   ├── password_reset.html
│   │   ├── password_reset_sent.html
│   │   ├── password_reset_form.html
│   │   └── password_reset_done.html
│   └── context_processors.py     # SITE_NAME injection
├── templates/                    # Other templates
│   └── customers.html            # Customer detail + order filters/table
├── static/
│   └── css/main.css              # Aurora variables + UI theme
├── manage.py
└── db.sqlite3
```

---

## Getting Started

### 1) Clone & enter the project

```bash
git clone https://github.com/VedantBandre/customer-management-application.git
cd customer-management-application
```

### 2) Create & activate a virtualenv

```bash
# Linux / macOS
python3 -m venv .venv
source .venv/bin/activate

# Windows
py -3 -m venv .venv
.venv\Scripts\activate
```

### 3) Install dependencies

If the repo includes `requirements.txt`:

```bash
pip install -r requirements.txt
```

Otherwise (minimum set):

```bash
pip install "Django>=5.2" django-filter
```

### 4) Configure (optional but recommended)

In `crm/settings.py`:

* Set `ALLOWED_HOSTS` for production
* Configure email (for password reset)
* Add the **SITE\_NAME** context processor and value:

```python
# crm/settings.py

TEMPLATES[0]["OPTIONS"]["context_processors"] += [
    "accounts.context_processors.site_brand",
]

SITE_NAME = "CRM"  # Shown in navbar/auth pages
```

Email (Gmail example — use an App Password):

```python
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "your_email@gmail.com"
EMAIL_HOST_PASSWORD = "your_app_password"
```

### 5) Apply migrations & create an admin

```bash
python manage.py migrate
python manage.py createsuperuser
```

### 6) Run the server

```bash
python manage.py runserver
```

Visit: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## App Walkthrough

* **Navbar**: brand (from `SITE_NAME`), Dashboard/Products (staff), Settings (non-staff), Login/Logout/Register
* **Dashboard (Home)**: stat cards (Total, Delivered, Pending), customer table
* **Customer Detail**:

  * Contact info & total orders
  * **Filter Orders** (inline, with labels)
  * Orders table with status color badges + actions (Update/Delete)
* **Orders**: create / edit / delete views
* **Account Settings**: update profile & picture
* **Auth**:

  * Login / Register
  * Password reset: request → email sent → set new password → done
  * Auth pages hide navbar/footer via `{% block header %}` / `{% block footer %}` overrides

---

## UI & Theming

* **Aurora Theme**: CSS variables in `static/css/main.css`

  * `--bg`, `--surface`, `--text`, `--muted`, `--primary`, etc.
* **Navbar**: `.app-navbar` styled to match Aurora, uses `{{ SITE_NAME }}`
* **Footer**: Brand/About, Resources, Contact columns; responsive, subtle gradients
* **Tables**: tidy header styles, optional hover tint, status badges via `data-status` attributes
* **Filters**: single-row filter bar, labels above inputs, responsive wrap

---

## Testing (optional)

If you add tests, the standard commands are:

```bash
python manage.py test
# or, with coverage:
pip install coverage
coverage run manage.py test
coverage report -m
```

---

##  Deployment Notes

* Set `DEBUG = False` and configure `ALLOWED_HOSTS`
* Configure static files:

```python
# production example
STATIC_ROOT = BASE_DIR / "staticfiles"
```

Then:

```bash
python manage.py collectstatic
```

* Serve via your preferred stack (e.g., Gunicorn + Nginx). Consider **Whitenoise** for static files on simple setups.

---

## Useful URLs (typical)

* `/` — Dashboard (Home)
  <img width="1867" height="977" alt="image" src="https://github.com/user-attachments/assets/263d7c84-51e9-4a54-ad34-fa70e023bcc4" />


* `/products/` — Products list
  <img width="1867" height="977" alt="image" src="https://github.com/user-attachments/assets/bd7d53fc-d2f4-41da-8196-5609431d9e5e" />


* `/customers/<id>/` — Customer detail + orders
  <img width="1867" height="977" alt="image" src="https://github.com/user-attachments/assets/fad57e4c-88cd-4e76-936b-b644b86ec3c5" />

  
* `/create_order/<customer_id>/`
<img width="1867" height="977" alt="image" src="https://github.com/user-attachments/assets/dfeaa42b-051c-4c36-b2d7-997140920ead" />

  
* `/update_order/<order_id>/`
<img width="1867" height="977" alt="image" src="https://github.com/user-attachments/assets/7e7a1080-d4ba-4899-8eee-303c28cbd3f0" />

  
* `/delete_order/<order_id>/`
<img width="1867" height="977" alt="image" src="https://github.com/user-attachments/assets/70f30ff8-384c-4889-b4e7-d2031f160c21" />


* `/user/`
<img width="1867" height="977" alt="image" src="https://github.com/user-attachments/assets/d500112b-3b6e-443b-8829-dd529dcc2a7f" />


* `/account/` — Account settings (profile)
<img width="1868" height="985" alt="image" src="https://github.com/user-attachments/assets/24ac4c93-f619-4c54-9a39-c555c4f44c7c" />
  

* `/register/`
<img width="1867" height="983" alt="image" src="https://github.com/user-attachments/assets/75deff04-73da-4f42-a733-90eb872c9631" />


* `/Sign in/`
<img width="1867" height="977" alt="image" src="https://github.com/user-attachments/assets/39ec4632-aea2-4598-acfc-1ab7e405b95d" />
  

* `/reset_password/` and the rest of the password reset flow
<p align='center'>
<img width="33%"  alt="image" src="https://github.com/user-attachments/assets/11f3d5ad-88ed-442b-bba3-a0932497af0f" />
<img width="33%"  alt="image" src="https://github.com/user-attachments/assets/b5861873-eb8e-48fd-a8b0-a8937ef49a8e" />
<img width="33%"  alt="image" src="https://github.com/user-attachments/assets/951672c7-1b11-48d6-b216-1edc6e2a9bd6" />
</p>

---

## Contributing

PRs and suggestions welcome!
Open an issue to propose changes, or submit a PR with:

* a clear description (what/why),
* screenshots (UI),
* tests where it makes sense.

---

## License

[MIT License](https://choosealicense.com/licenses/mit/)

---
