Built by ~ Daniel O. Pimentel

Step 1.

Self-Signed keys:

openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout ~/website/ssl/nginx-selfsigned.key -out ~/website/ssl/nginx-selfsigned.crt -subj "/C=US/ST=State/L=City/O=Organization/OU=Unit/CN=localhost"

Step 2.
Build and run:

cd ~/website
docker build -t daniels-nginx .
docker run -d -p 80:80 -p 443:443 --name daniels-nginx-container daniels-nginx
