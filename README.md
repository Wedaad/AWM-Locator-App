# awm-locator-app
Advanced Web Mapping - Location based service app built using Django &amp; Python

All the code for this project is on a branch called dev-branch.

## This project is made up of:
- a Django project 
- 3 docker containers:
    1. Postgis - spatial DB
    2. Pgadmin4 - for database management 
    3. location_app - which conatins the Django project
    
 The external libraries used for this project can be found in the ENV.yml file
 
 ## Locator App
 ### Html files
 - A sign-up page which allows new users to register
 - A login page which allows existing users to login
 - A menu page which displays what services are available to the user
 - A map page which displays a map and plots the users current location with a little pop-up message containing their location (map is generated using leafletJs)
  
 
 ### Views
 - A register view which is connected to the registration form when a new user is registered
 - A login view which is conneted to the login form
 All forms are generated using crispy forms
 
 ### Static files
 - Static files are managed using whitenoise library
 - There is a css stylesheet 
 - Javacript is used for the map 
 
 
