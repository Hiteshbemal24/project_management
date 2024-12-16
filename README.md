# Project Management API

This project is a RESTful API built using Django and Django REST Framework for managing clients and projects. It provides endpoints to create, retrieve, update, and delete clients and projects.

## Table of Contents
- [GitHub Link](#github-link)
- [How to Run the Code](#how-to-run-the-code)
- [How to Run the Machine Test](#how-to-run-the-machine-test)
- [Database Design](#database-design)
- [API Endpoints](#api-endpoints)
- [Technologies Used](#technologies-used)



## How to Run the Code

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```
2. ** setup virtual environment**:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use .\env\Scripts\activate
   ```
3. **install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Run migrations**:
   ```bash
   python manage.py migrate
   ```
5. **Run the server**:
   ```bash
   python manage.py runserver
   ```
6. **Access the Applications**:
   ```bash
   http://127.0.0.1:8000/admin/
   http://127.0.0.1:8000/api/

## How to Run the Machine Test
-Set Up Testing Framework: Ensure you have a testing framework like Django's built-in test framework.

-Create Test Cases: Write your test cases in the tests.py file or a separate test module.
-run test
 ```bash
python manage.py test
```
## Database Design
-check the models.py
-Entities
-Client: Represents a client with attributes like client_name, created_at, and created_by.
-**User **: Represents a user with attributes like name.
-Project: Represents a project with attributes like project_name, client, and users.

## API Endpoints
-List all clients: GET /clients/
-Create a new client: POST /clients/
-Retrieve a client by ID: GET /clients/:id/
-Update a client: PUT /clients/:id/
-Delete a client: DELETE /clients/:id/
-List all projects assigned to the logged-in user: GET /projects/
-Create a new project: POST /projects/

##Technologies Used
-Django
-Django REST Framework
-Python
-poatgreSQL


