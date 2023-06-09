# Kartoza Assignment (User Portfolio)
This web app has been developed using Django version 4.0 

### Basic Features of The App
    
* Register – Users can register and create a new profile
* Login - Registered users can login using username and password
* User Profile - Once logged in, users can create and update additional information such as home address, phone number and location in the profile page
* Main Page - On the navigation tab is a map option ,once clicked will navigate the user to the maps page ,where all the locations for the registered users will be shown
* Main Page - Once logged in, on the navigation tab a user icon will be available ,when clicked will show a pop up modal with user profile details
* Remember me – Cookie Option, users don’t have to provide credentials every time they hit the site
* Forgot Password – Users can easily retrieve their password if they forget it 
* Admin Panel – admin can review users and perform CRUD operations on them ,as well review user logging activities recorded under UserActivity Model


### To run project
Make sure python version 3.9 is installed on windows machine.
To get this project up and running locally on your computer follow the following steps.
1. download project to local machine
2. open project directory with cmd (command prompt)
3. in cmd type:
```
$ py -m venv project-name (this will create a virtual environment for the project)
```
4. navigate to the project-name defined above and activate the virtual environment:
```
$ cd project-name\Scripts
$ activate
```
5. navigate back to the main directory and type the following:
```
$ pip install -r requirements.txt (this will install the project dependencies)
$ python manage.py createsuperuser (to login to admin panel)
$ python manage.py runserver
```
6. if you dont use the sqlite file provided with some dummy data for testing ,manually run the migrations to instantiate the database
```
$ python manage.py make migrations
$ python manage.py migrate
```

### RUNNING TESTS
There are some test cases defined. These tests:
* ensure all the urls are reachable
* ensure when a user is created a profile is attached to them
* ensure a user will be able to perform CRUD operations on their profile
* ensure all critical apps are installed
These tests can be found within the tests folder of each app.
To run the tests, in cmd execute the following command:
```
$ python manage.py test
```
  
 ### URL's 
* http://localhost:8000/ (main page)
* http://localhost:8000/admin (admin panel)
* http://localhost:8000/map (maps page)



