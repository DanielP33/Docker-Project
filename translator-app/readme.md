# Translator Web App

## Building the Docker Image

To build the Docker image for the Translator Web App, run the following command:

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
