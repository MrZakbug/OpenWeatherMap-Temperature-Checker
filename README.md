# Temperature Checker using OpenWeatherMap API

Hello to Temperature Checker using OpenWeatherMap API. This is a simple WebApp which lets you check temperature for geolocation you provide.

Installation and usage:

1.
    a. download the files included in the repository
    
    b. navigate to 'niceweathervenv' directory through command prompt or terminal and activate virtual enviroment prepared for the project
    
    c. in cmd/terminal run command 'python manage.py runserver'
    
    d. server should start now
    
    e. open your prefered internet browser and go to http://127.0.0.1:8000
    
    f. use the app

2. If you have Python version 3.6 or higher installed already on you computer, you can install all the requirements by running commpand 'pip install -r \PATH\requirements.txt' in cmd/terminal, where PATH is the path to requirements.txt file included in the project. Then go to point 1c and go on from there.

3. If you have Docker and Docker-Compose installed you can navigate to project files and run command 'docker-compose up' in the cmd/terminal to create and run docker container.


To use application just provide valid data for Latitude and Longitude in the form on the start page of application, accept ToS and submit. You should be redirected to the page showing temperature result for geolocation you provided, and name of the closest weather station to it. You can alternatively change url of result page providing valid values and refresh the page, which will show the result for the values provided in the url of the page.
