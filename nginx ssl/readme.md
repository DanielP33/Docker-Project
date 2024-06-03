# Daniel O. Pimentel's Nginx Setup

## Overview

This guide walks you through setting up a Dockerized Nginx server with self-signed SSL certificates.

## Step 1: Generate Self-Signed SSL Certificates

First, create self-signed SSL certificates. This step uses OpenSSL to generate a certificate and a key.

```sh
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout ~/website/ssl/nginx-selfsigned.key -out ~/website/ssl/nginx-selfsigned.crt -subj "/C=US/ST=State/L=City/O=Organization/OU=Unit/CN=localhost"
```
## Step 2: Build and Run the Docker Container

1. Change to the website directory:

```sh
cd ~/website
```

2. Build the Docker image:

```sh
docker run -d -p 80:80 -p 443:443 --name daniels-nginx-container daniels-nginx
```

3. Run the Docker container:

```sh
docker run -d -p 80:80 -p 443:443 --name daniels-nginx-container daniels-nginx
```

