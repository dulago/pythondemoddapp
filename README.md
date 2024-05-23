# pythondemoapp
This repo contains the configuration to create a simple Python API that runs on Docker and is monitored using Datadog.
-------------------------------------------------
-------------------------------------------------
Before building a new version of the image, update the DD_VERSION variable value on the Dockerfile to the version you're going to build. You can also change it via args on runtime.
To build a new version of the Docker image just run:
``` 
docker build -t dulago/pythondemoapp:version .
```
And then
``` 
docker push dulago/pythondemoapp:version
```
-------------------------------------------------
To run the image locally:
``` 
docker run -d -p 80:80 -e DD_SERVICE=servicename -e DD_ENV=env -e DD_VERSION=version dulago/pythondemoapp:version
```
> Note that this will bind the Docker host's port 80 to the container. If that's not possible, change the first '80' to a port that's available. You'll then need to call the application using this port.
-------------------------------------------------

To _LOCALLY_ create a client and a server container to comunicate with eachother you can run the following Docker run commands:

``` 
SERVER
docker run --name pythonserver -d -p 80:80 -e DD_SERVICE=pythonserver -e DD_ENV=dev -e DD_VERSION=version dulago/pythondemoapp:version
```

```
CLIENT
docker run --name pythonclient -d -p 8090:80 -e DD_SERVICE=pythonclient -e DD_ENV=dev -e DD_VERSION=version dulago/pythondemoapp:version
```

Available operations are:
- http://localhost:[port]/home - displays a Hello World message
- http://localhost:[port]/ping - returns a "Pong"
- http://localhost:[port]/httprequest - run on the client container to call the server container in the /ping route
- http://localhost:[port]/health - returns a message informing that service is healthy


Then call the client container on /httprequest