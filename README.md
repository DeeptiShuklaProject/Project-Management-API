# Project-Management-API



## Overview
The Project Management API is a RESTful API built with Django and Django REST Framework for TechForing Limited. This API allows teams to collaborate on projects by managing users, projects, tasks, and comments. The API is designed to be consumed by both web and mobile applications.

## Features
- User registration and authentication
- Project creation and management
- Task assignment and status updates
- Commenting on tasks
- JWT-based authentication for secure access
- Swagger UI documentation for easy API exploration

### Clone the Repository
```bash
git clone https://github.com/DeeptiShuklaProject/Project-Management-API.git
cd project-management-api


### Prerequisites
- Python 3.8 or higher
- PostgreSQL
- pip (Python package installer)


## Technology Stack
- **Backend**: Django, Django REST Framework
- **Database**: PostgreSQL
- **Documentation**: Swagger (drf-yasg)
- **Authentication**: JWT (JSON Web Tokens)

## Installation
pip install -r requirements.txt
Or
pip install drf-yasg

## Migrate the Database
python manage.py makemigrations api 
python manage.py migrate

python manage.py runserver

## Swagger UI Access
To access your API documentation
Open your browser and navigate to http://127.0.0.1:8000/swagger/ to view your API documentation.

## API Endpoints

Register User: http://127.0.0.1:8000/api/users/register/ (POST)
Login User: http://127.0.0.1:8000/api/users/login/ (POST)
List Projects: http://127.0.0.1:8000/api/projects/ (GET)
Create Task: http://127.0.0.1:8000/api/projects/{project_id}/tasks/ (POST)


## Contribution
Contributions are welcome! Please create a pull request or open an issue for suggestions or improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for more information.

## Contact
For any inquiries or support, please contact:

Name: Deepti Shukla
Email: deeptishukla515@gmail.com
