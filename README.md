# project_birdnest_2023

Solution for Reaktor's [Developer Trainee, Summer 2023](https://www.reaktor.com/careers/developer-trainee-summer-2023-6514340002/) -program's [pre-assignment](https://assignments.reaktor.com/birdnest/?_gl=1*1j2qtbo*_ga*NDk1MzkwODM2LjE2NzEzMDkwODE.*_ga_DX023XT0SX*MTY3MzgxMzYxOC4yMS4wLjE2NzM4MTM2MTguNjAuMC4w).

## Link to the app:

https://birdnest-frontend-hellurei-dev.apps.sandbox-m2.ll9k.p1.openshiftapps.com/

***NOTICE!*** The application is running on OpenShift container platform, on a developer sandbox account. It will be removed after 30 days when the free trial period ends (deployed 17.1.2023). Also the application has to be temporarily shut down once in 12 hours due to the developer sandbox terms of use - therefore the application will be unavailable between 8pm-8am. I know this service is not meant to be used as a production environment, but it is very difficult to find a free hosting service these days.

The page should show a list of pilots whose drones have violated the no fly zone in the past ten minutes. The list is ordered by the 'Last seen' field. The oldest sightings are at the top of the list and should disappear once the drone has not been seen in over ten minutes. The newest sightings will appear at the bottom of the list.

## Project Description

The frontend React app is served with nginx proxy server. The backend Django application is run on both gunicorn and daphne servers (each in their own containers) to serve http and websocket connections separately.

The backend uses Django Rest Framework to respond to http requests. When the application is first opened in browser, the list of pilots currently in the database is fetched and displayed. This list will keep updating through a websocket connection.

Django Channels is used for handling websocket connection between client and server, with redis channel layer. A django-admin command [broadcast.py](https://github.com/hjeronen/project_birdnest_2023/blob/main/backend/birdnest/management/commands/broadcast.py) fetches the drone data from the given API endpoint, and uses the module [drone_control.py](https://github.com/hjeronen/project_birdnest_2023/blob/main/backend/birdnest/drone_control.py) to check which drones have been within 100 meters from the nest. Function get_pilots() will then fetch the pilot information for these drones, and update_pilot_list() updates the data in the database. Function broadcast_pilots() then sends the updated list of pilots to the pilot_list channel that the client is connected to.

The django-admin command broadcast.py is run on a continuous loop (every few seconds) also in its own container (I'm sure there would have been a better way to do this, a subprocess or a background worker etc....)

The backend is configured to use a PostgreSQL database for "permanent" storage - this is also running inside a container, since it is rather difficult to get free server space from anywhere. All data is lost when the container is stopped.

## Running Locally

Requires Docker to be installed and Docker Desktop App to be running.

After cloning the repository, create a .env file at the root of the project, the same directory where the docker-compose.yml file is. It should have the following contents:

``````
SECRET_KEY=super_secret_key_here
DJANGO_PRODUCTION=true
POSTGRES_DB=db_name
POSTGRES_USER=db_username
POSTGRES_PASSWORD=db_password
POSTGRES_HOST=host.docker.internal
POSTGRES_PORT=5432
``````

After saving the .env file, you can start the application with command `docker compose up`. When all the containers are running, go to http://localhost:3000/ on your browser.
