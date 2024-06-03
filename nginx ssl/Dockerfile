# Use the official Nginx image from the Docker Hub
FROM nginx:latest

# Copy the custom index.html to the default Nginx HTML directory
COPY index.html /usr/share/nginx/html/index.html

# Copy the custom Nginx configuration file
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copy the SSL certificates
COPY ssl /etc/nginx/ssl
