# ToDo API Project

This is a simple Django REST API project for managing ToDo tasks. Each task is linked to a user and can be created, updated, or deleted via the API.

## Features

- User-linked tasks
- Task fields: title, description, completed status, creation timestamp, priority
- RESTful API endpoints for CRUD operations on tasks

## Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone <your-repo-url>
   cd todo_project


2. Create a virtual environment and activate it:

python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

3.Install dependencies:

pip install -r requirements.txt

4.Make migrations and migrate the database:

python manage.py makemigrations
python manage.py migrate

5.Create a superuser to access the admin panel (optional):

python manage.py createsuperuser

6.Run the development server:

python manage.py runserver

7.Access the API

API root: http://127.0.0.1:8000/api/

Admin panel: http://127.0.0.1:8000/admin/


Requirements

See requirements.txt for the full list of dependencies.

