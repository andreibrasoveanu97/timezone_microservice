# Timezone microservice

Simple timezone microservice that returns:
* all available timezones
* specific timezone (given a pair of latitude and longitude values in the EPSG:4326 coordinate reference system.)

## Setup

1. Clone repository
```
git clone https://github.com/andreibrasoveanu97/timezone_microservice/
cd timezone_microservice
```

2. Build the docker image and run the container (assuming there is a form of Docker installed):
```
docker build -t timezone-microservice .
docker run -p 8888:5000 timezone-microservice
```

3. Use the endpoint:
```
/timezones
** Delivers all available timezones

/timezones?lat=y&lon=x 
** Deliver timezone for specified coordinate given a geographic latitude/longitude in EPSG:4326 coordinate reference system
```
## Parallelism

Threading is enabled for the application. In the above example, Gunicorn will run with 1 worker process and 1 thread per worker, providing no parallelism for handling requests. You can adjust these values based on your system's resources and performance requirements. 
