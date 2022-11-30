## About
### Full Stack Application for developers to share their projects
- Search the developers, projects, skills using keywords <br>
- Get detailed information about developer <br>
- Get detailed information about each project <br>
- After user is logged in, user is redirected to Edit profile section, where user can add information such as profile picture, bio, skills
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
6. And navigate to http://127.0.0.1:8000/

## Search and Pagination
Search implemented by quering the value of `search_query` attribute from HTML
<br>
Pagination implemented using `Paginator` class built in in Django

## Login
I used `User` class from built in Django authentication system, I got user data from the `request.POST` and then query it with `objects.get` method from `User` class instance passing `username` as an argument. Then using `authenticate` method check if the given credentials are valid, return a `User` object. Then redirect user to the same page user was before log in by adding `?next={{request.path}}` to URL

## Register
register user with `user_register` method and accessing the data from `UserCreationForm` class which is built in in `django.contrib.auth.forms`. After user is regerested and logged in, user redirected to edit profile section. 

## Edit profile
Used built in decorator `@login_required(login_url='login')` to run the method only if user is logged in.
<br>
Django uses request and response objects to pass state through the system.
When a page is requested, Django creates an HttpRequest object that contains metadata about the request. Then Django loads the appropriate view, passing the HttpRequest as the first argument to the view function.
<br>
Then getting particular user with `request.user.profile` and adding `instance=profile` as an argument to `ProfileForm` pre-render user's information in form


### CRUD operations with skills 
Used built in decorator `@login_required(login_url='login')` to run the method only if user is logged in.
Then getting particular user with `request.user.profile` and adding `instance=profile` as an argument to `ProfileForm` pre-render user's information in form
#### Create 
getting particular user
`profile = request.user.profile`

accessing the data from model
creating an instance of `SkillForm` class
`form = SkillForm(request.POST)`
checking if the form is valid with built in `form.is_valid()` 
Then using `form.save()` method to create the skill. 

#### Update 
getting particular user
`profile = request.user.profile`

accessing the data from model
`form = SkillForm(request.POST, instance=skill)`
creating an instance of `SkillForm` class
checking if the form is valid with built in `form.is_valid()` 
Then using `form.save()` method to update the skill. 
This method creates and saves a database object from the data bound to the form. 
<em>A subclass of ModelForm can accept an existing model instance as the keyword argument instance; if this is supplied, save() will update that instance.</em> If it’s not supplied, save() will create a new instance of the specified model: 

#### Delete
Getting a particular user
`profile = request.user.profile`
Quering needed skill from all skills 
`skill = profile.skill_set.get(id=pk)`
Then delete it useng `skill.delete()` method




### Used `django.contrib.messages.api` to send the notifications throughout the app.