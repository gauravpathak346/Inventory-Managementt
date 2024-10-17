# Inventory-Management
Inventory Management task by Blooprint Cons.
# Inventory Management System API

This is a backend API for an Inventory Management System built using Django Rest Framework (DRF) with JWT authentication, MYSQL, and Redis caching.
### Set venv  for vertual environment 

## Features
- JWT-based authentication
- CRUD operations for managing inventory items
- Redis caching for optimizing read operations
- Unit tests for API functionality
- Logging for debugging and monitoring

## Setup Instructions

### Prerequisites
- Python 3.x
- PostgreSQL or MySQL (Database: `todo`)
- Redis
- Django
### Project Setup
We created a new Django project and an app to handle inventory management.

### Install Django and DRF: Run the following command to install Django and Django Rest Framework:
pip install django djangorestframework djangorestframework-simplejwt redis psycopg2-binary
1. Create a Django Project:
    django-admin startproject inventory_system
     cd inventory_system
2. Create a Django App:
    python manage.py startapp inventory

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/inventory-management.git
   cd inventory-management
2. Install the required dependencies:

    pip install -r requirements.txt

3. Set up the PostgreSQL or MySQL database in settings.py:
4. Run migrations:
    python manage.py migrate
5. Create a superuser for admin access:
    python manage.py createsuperuser
6. Start the development server:
    python manage.py runserver

### API Endpoints

### Token Generation

POST /api/token/
# Request: {"username": "gaurav", "password": "Trash@6681"}
# Response: JWT access and refresh tokens
### Inventory Item CRUD

### Create Item: POST /api/items/
Read Item: GET /api/items/{id}/
Update Item: PUT /api/items/{id}/
Delete Item: DELETE /api/items/{id}/

### Running Tests
To run the tests, use the following command:
python manage.py test


### Start the server with

python manage.py runserver
