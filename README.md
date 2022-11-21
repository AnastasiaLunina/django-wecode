## About
### Full Stack Application for developers to share their work
- Search the developers, projects, skills using keywords <br>
- Get detailed information about developer <br>
- Get detailed information about each project <br>
- For logged in users the My Account section is available, user can perform CRUD operations to 
add new projects and skills, delete those, as well as update <br>
- Logged in users can leave comments and vote for the projects, this way project's rating is calculated <br>
- Pagination implemented <br>
- Login/Logout <br>

## Setup

1. The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/AnastasiaLunina/django-wecode.git
$ cd django-wecode
```

2. Create a virtual environment to install dependencies in and activate it:

```sh
$ python3 -m venv ./env

# Mac/Linux
$ source env/bin/activate

# Windows
venv\Scripts\activate.bat

# Exit venv
deactivate
```

4. Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```

5. Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd project
(env)$ python manage.py runserver
```
6. And navigate to `http://127.0.0.1:8000/



