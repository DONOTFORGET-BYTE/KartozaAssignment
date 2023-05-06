# Kartoza Assignment (User Portfolio)
This web app has been developed using Django version 4.0 

### Basic Features of The App
    
* Register – Users can register and create a new profile
* Login - Registered users can login using username and password
* User Profile - Once logged in, users can create and update additional information such as home address, phone number and location in the profile page
* Remember me – Cookie Option, users don’t have to provide credentials every time they hit the site
* Forgot Password – Users can easily retrieve their password if they forget it 
* Admin Panel – admin can review users and perform CRUD operations on them ,as well review user logging activities


### To run project
To get this project up and running locally on your computer follow the following steps.
1. Set up a python virtual environment
2. Run the following commands
```
$ pip install -r requirements.txt (this contains the project dependencies)
$ python manage.py migrate (to run migrations)
$ python manage.py createsuperuser (to login to admin panel)
$ python manage.py runserver
```
  
  ### URL's 
3. Open a browser and go to http://localhost:8000/ (main page)
4. http://localhost:8000/admin (admin panel)



