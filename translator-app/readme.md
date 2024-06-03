# Translator Web App

## Building the Docker Image

1. To build the Docker image for the Translator Web App, run the following command:

```sh
docker build -t translator-web-app .
```


```sh
docker run -p 5000:5000 translator-web-app
```


After pushing the image to Docker Hub, it will be available at:
```sh
https://hub.docker.com/r/danielp393/translator-web-app
```

Pull from my repository:
```sh
docker pull danielp393/translator-web-app:latest
```

2. # Docker Swarm Setup and Service Deployment

## Ensure Docker Swarm is Initialized

If not already done, initialize Docker Swarm on your main machine:

```sh
docker swarm init
```
# Join the Swarm from Other Machines

On the main machine, get the join token:
```sh
docker swarm join-token worker
```

# Deploy the Service with Replicas

On the main machine, deploy your service with the desired number of replicas, in our case 3

```sh
docker service create --name translator-web-app --replicas 3 danielp393/translator-web-app:latest
```

# Verifying the Deployment

To check the status of your service and replicas, use:
```sh
docker service ls
```
