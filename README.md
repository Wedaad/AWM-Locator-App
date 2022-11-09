# awm-locator-app
Advanced Web Mapping - Location based service app built using Django &amp; Python

All the code for this project is on a branch called dev-branch.

## What the project contains:
- a Django project 
- 3 docker containers which communicate on the same network:
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

## Deployment
- Created a DigitalOcean droplet that had docker preinstalled
- Aquired a domain name (wedaadharuna.online)
- Unfortuantely deployment of this project was unsuccessful. However these are the steps that were done:
    1. Registered domain name to get SSL cert using certbot
    2. Successfully installed Nginx server
    3. Created 3 containers on Docker VM
    4. Pushed local Docker image of Django project to Dockerhub
    5. Pulled and installed Django project image on VM
    6. Modified settings.py to use environment variables
    7. Added server and headers .conf files to local Nginx directory

However after all these steps deployment resulted in a 404 not found when testing. So I commented out all the settings that related to deployment and left the settings.py as is when it works testing locally on docker on my laptop. 
 
 DNS record modification
![image](https://user-images.githubusercontent.com/57072598/200922725-89137592-7c32-4ead-a782-312329b1908b.png)

Digital Ocean Droplet
![image](https://user-images.githubusercontent.com/57072598/200924275-bde85f04-0dea-4d88-91ee-a7b9fff158b0.png)

Nginx web server on wedaadharuna.online
![image](https://user-images.githubusercontent.com/57072598/200924664-7c6a0e00-dec0-484b-b937-c430b8ab8867.png)

Nginx 404 not found during deployment testing
![image](https://user-images.githubusercontent.com/57072598/200926041-45bb884a-47d8-4dfc-9464-d0ca33f8c014.png)

A lovely map that displays location when running in a Docker container locally
![image](https://user-images.githubusercontent.com/57072598/200925410-97fed9a1-a301-4895-8f05-bf09e029f457.png)

