<h1 align="center">WorkHub - Django Project</h1>

WorkHub is a web-based platform built with Django designed as job portal featuring a robust 3-tier user system (Finders, Hirers, & Admins). Includes custom dashboards, role-based access control, job posting CRUD, and notification management. Built with Python, namespaced routing, and a custom user model. 🚀

## 📋 Features
- User Authentication (Login/Signup)
- Post a job
- Application tracking
- Responsive UI

## 🛠️ Prerequisites

Before you begin, ensure you have the following installed on your system:
- **Python 3.8+**
- **pip** (Python package manager)
- **Virtualenv** (Recommended)

## 🚀 Getting Started

Follow these steps to get the project up and running on your local machine.

## 1. Clone the Repository

## Bash:
git clone [https://github.com/ShawnJose17/Django-WorkHub.git](https://github.com/ShawnJose17/Django-WorkHub.git)
cd Django-WorkHub

## 2. Set Up a Virtual Environment
It is highly recommended to use a virtual environment to keep dependencies isolated.

## Bash:
## Create virtual environment
python3 -m venv wh-django

# Activate it
# On Windows:
.\wh-django\Scripts\Activate.ps1
# On macOS/Linux:
source wh-django/bin/activate

## 3. Install Dependencies
Install the required Python packages using the requirements file:

## Bash:
pip install django

## 4. Create the project and apps

## Bash:
python3 -m django startproject whproject
cd whproject
python3 manage.py startapp accounts
python3 manage.py startapp finder
python3 manage.py startapp hirer
python3 manage.py startapp main
python3 manage.py startapp whadmin

## 5. Copy paste the source code just like from the project along the Templates folder and static folder

## 6. Database Migrations
Set up the database schema:

## Bash:
python manage.py makemigrations
python manage.py migrate

## 7. Create a Superuser (Optional)
To access the Django Admin panel, create an admin account:

## Bash:
python manage.py createsuperuser

## 8. Run the Development Server

## Bash:
python manage.py runserver

Open your browser and go to http://127.0.0.1:8000/.

## 📂 Project Structure
- WorkHub/: Main project configuration (settings, urls, wsgi).
  
- [App-Name]/: Main application logic (models, views, templates).

- templates/: HTML files.

- static/: CSS, JavaScript, and Images.

## 🤝 Contributing
1.  Fork the Project

2.  Create your Feature Branch (git checkout -b feature/AmazingFeature)

3.  Commit your Changes (git commit -m 'Add some AmazingFeature')

4.  Push to the Branch (git push origin feature/AmazingFeature)

5.  Open a Pull Request

