---
hide:
  - navigation
---

# Deploy MKDOCS in the Linux Machine using NGINIX

## 1. Install MkDocs
If you haven't already installed MkDocs, you can do so using pip. Open a terminal and run:

```bash
pip install mkdocs
```

## 2. Create Your MkDocs Project
If you don't have an existing MkDocs project, create one with:

```bash
mkdocs new my-project
cd my-project
```

## 3. Generate Static Files
To build your MkDocs site, run:

```bash
mkdocs build
```

This will generate the static files in the site directory.

## 4. Install a Web Server
You need a web server to serve the static files. Common choices are Nginx or Apache. Here’s how to install Nginx:

```bash
sudo apt update
sudo apt install nginx
```

## 5. Set Up HTTPS with Certbot
To secure your site with HTTPS, you can use Let’s Encrypt and Certbot. Install Certbot:

```bash
sudo apt install certbot python3-certbot-nginx
```

### a. Obtain a Domain Name
Make sure you have a registered domain name pointing to your server's IP address. You can use a service like No-IP for dynamic IP addresses.

### b. Obtain an SSL Certificate
Run Certbot to automatically obtain an SSL certificate:

```bash
sudo certbot --nginx
```

Follow the prompts to enter your email address and agree to the terms of service. Select the domain for which you want to enable HTTPS.

## 6. Configure Nginx
Create an Nginx configuration file for your MkDocs project:

```bash
sudo nano /etc/nginx/sites-available/mkdocs
```

Add the following configuration:
```
nginx
Copy code
server {
    listen 80;
    server_name your_domain.com www.your_domain.com;

    # Redirect all HTTP requests to HTTPS
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl;
    server_name your_domain.com www.your_domain.com;

    ssl_certificate /etc/letsencrypt/live/your_domain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/your_domain.com/privkey.pem;

    location / {
        root /path/to/your/mkdocs/project/site;
        index index.html index.htm;
        try_files $uri $uri/ =404;
    }
}
```
Replace your_domain.com with your actual domain and /path/to/your/mkdocs/project/site with the path to your MkDocs site directory.

## 7. Enable the Nginx Configuration
Link the configuration file and restart Nginx:

```bash
sudo ln -s /etc/nginx/sites-available/mkdocs /etc/nginx/sites-enabled/
sudo nginx -t  # Test the configuration
sudo systemctl restart nginx
```

## 8. Access Your Site
Your MkDocs site should now be accessible via HTTPS at https://your_domain.com.

