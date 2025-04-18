# [Trip Track App Using Django](https://trip-track-app-using-django.onrender.com)

A practice project to manage and track trips and associated notes, built using Django.

## Project Overview

The Trip Track App provides features for creating, updating, viewing, and deleting trips and their associated notes. The project is hosted at [Trip Track App](https://trip-track-app-using-django.onrender.com).

## Features

- **User Authentication**: Login, logout, and password management are powered by Django's built-in authentication system.
- **Trip Management**: Users can create, update, view, and delete trips.
- **Notes Management**: Users can create, update, view, and delete notes related to trips.
- **Admin Panel**: Use Django's admin interface for managing data.
- **Static File Handling**: Configured with Whitenoise for efficient static file management.

## Installation

Follow the steps below to set up the project locally:

### Prerequisites

- Python 3.x installed on your system
- Virtual environment (optional but recommended)

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/vdanepalli/trip_track_app_using_django.git
   cd trip_track_app_using_django
   ```
2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```
3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Apply database migrations:
   ```bash
   python manage.py migrate
   ```
5. Run the development server:
   ```bash
   python manage.py runserver
   ```
6. Visit the application in your browser:
   ```plaintext
   http://127.0.0.1:8000
   ```


## Project Structure

### Key Files and Directories

- **`manage.py`**: Django's command-line utility for administrative tasks.
- **`config/urls.py`**: Project-wide URL configuration including routes for admin, accounts, and app-specific URLs.
- **`trip/urls.py`**: Application-specific URL routing for trips and notes.

### URL Routing

- **Home**: `/`
- **Dashboard**: `/dashboard/`
- **Create Trip**: `/dashboard/trip/create/`
- **View Trip**: `/dashboard/trip/<int:pk>/`
- **Update Trip**: `/dashboard/trip/<int:pk>/update/`
- **Delete Trip**: `/dashboard/trip/<int:pk>/delete/`
- **Notes Management**: `/dashboard/note/`

## Dependencies

The project depends on the following packages:

```plaintext
asgiref==3.8.1
crispy-tailwind==1.0.3
Django==5.0.4
django-crispy-forms==2.1
gunicorn==21.2.0
packaging==24.0
pillow==10.3.0
sqlparse==0.4.4
whitenoise==6.6.0
```

These dependencies are listed in requirements.txt. Install them using:

```bash
pip install -r requirements.txt
```

## Deployment
The app is configured for production with:
- Gunicorn: A Python WSGI HTTP Server for running Django.
- Whitenoise: For serving static files.

