# django-budgeting-app
> An app for personal budget planning using the [envelope method](https://www.thebalance.com/what-is-envelope-budgeting-1293682). The app is a conversion (with upgrades) of the Express.js app I built [previously](https://github.com/thomas-dunlop/budgeting-app) to Django and served as a good introduction for me to Python and the Django framwork.
> Live demo [_here_](https://envelope-budgeting-app.herokuapp.com/envelopebudgeting/). 

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Setup](#setup)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)


## General Information
The purpose of the project was to teach myself Python and Django and demonstrate competancy in the following areas:
- Ability to write HTTP endpoints using Django. 
- Ability to implement a front end using HTML and CSS. 
- Ability to build a database using PostgreSQL. 
- Ability to deploy the app to production (Heroku). 


## Technologies Used
- Django - version 3,2,7
- Postgres - version 13.3
- gunicorn - version 20.1.0


## Features
List the ready features here:
- The simple front end (built with HTML and Javascript) allows the user to view currently created envelopes, add new envelopes, delete individual envelopes, and update individual envelopes. The front end also allows users to add and delete transactions (expenses such as buying food or fixing a car). The server then automatically updates the relevant envelope. For example, if the user added a transaction for buying catfood, the server would reduce the budget in the Pet envelope.
- Back end server to handle CRUD operations.
- PostgreSQL database for storing envelopes and transactions.


## Setup
Dependencies are stored in the `requirements.txt` file. The following dependencies are required: 
- asgiref==3.4.1
- dj-database-url==0.5.0
- Django==3.2.7
- gunicorn==20.1.0
- psycopg2-binary==2.9.1
- pytz==2021.1
- sqlparse==0.4.2
- whitenoise==5.3.0


## Project Status
Project is: _complete_


## Room for Improvement

Room for improvement:
- Improve sloppy production transition (the secret key has not been parameterized, for instance). 
- User account creation and authentication. 
- Better front end (even with CSS, it looks pretty basic right now). 
- Features to autoupdate envelopes on a monthly cadence. 
