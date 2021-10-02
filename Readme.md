# cloudy
Cloudy - amazing backend service to maintain periodical checking and storing the local copy of openweathermap giving you easily filterable results.

## Deployment
+ clone the repo
+ create .env file inside main directory, in our case it is 'cloudy' folder (top one, not the one with settings.py)
+ put these value into `.env`: 
```
    SECRET_KEY=<DJANGO_PROJECT_SECRET_KEY>
    API_KEY=OPENWEATHERMAP_API_KEY
    URL_WEATHER="URL"
    POSTGRES_DB=<DB_NAME>
    POSTGRES_USER=<USERNAME_FOR_DB>
    POSTGRES_PASSWORD=<PASSWORD_FOR_DB>
    POSTGRES_PORT=<POSTGRES_PORT, usually 5432>
    POSTGRES_HOST=db
    DEBUG=<LEAVE IT EMPTY FOR PRODUCTION, PUT ANYTHING TO ENABLE DEBUGGING>
```
We can not work on all cities on openweathermap, there are just too many cities (200 000+). 
So we limit the count by `CITY_LIMT` env value. It is better to keep it low.
+ create docker containers
```
docker-compose up -d --build
```

+ make database migrations
```
docker-compose exec core python manage.py makemigrations
docker-compose exec core python manage.py migrate
```
+ create super user for admin panel
```
docker-compose exec core python manage.py createsuperuser
```
Follow all instructions of interactive form, just enter username and password, others are optional.
+ collect static files
```
docker-compose exec core python manage.py collectstatic
```
+ restart containers (just in case)
```
docker-compose restart
```
+ load cities from openweathermap api, we have a dedicated command for this
```
docker-compose exec core python manage.py load_cities
```

That's it. If you haven't faced issues until this step, project should be already running.
Check out `localhost:1465/docs/`

## Configure web server
You should configure web server, you can use nginx,  it is much more easy. It really does not matter which web 
server you use, just do not forget to add two endpoints for static files:
+ `/static/` - this is for all js/css/html files
+ `/files/` - this is for other service files which can be downloaded
Both enpdoints have corresponding folders: `static` and `files` inside main directory, so just redirect the requests here to server those files.

## URLs
+ `/admin/` - admin panel (you'll be asked to enter username and password of superuser, you created it a few steps earlier)
+ `/docs/` - documentation about API