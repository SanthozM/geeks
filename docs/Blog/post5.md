---
hide:
  - navigation
---

# Network Control: Block Domains and Show a Custom Message with dnsmasq

You can create a **local HTML server** that serves a "This page is blocked" message and use `dnsmasq` to redirect blocked domains to this local server. Here's how to do it:

## Step 1: Create a Simple HTML Page

First, create a simple HTML page that shows the "This page is blocked" message.

1. Create a directory to hold the HTML files:
   ```bash
   mkdir -p /var/www/blocked
   ```
2. Create an `index.html` file inside the directory with the blocked message:
   ```bash
   sudo nano /var/www/blocked/index.html
   ```
   Add the following content:
   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>Blocked</title>
       <style>
           body {
               text-align: center;
               font-family: Arial, sans-serif;
               margin-top: 50px;
           }
           h1 {
               color: red;
           }
       </style>
   </head>
   <body>
       <h1>This Page is Blocked!</h1>
       <p>The site you are trying to access has been blocked by your administrator.</p>
   </body>
   </html>
   ```

## Step 2: Set Up a Simple Local Web Server

To serve the HTML page, you can use a lightweight web server such as **Python's HTTP server** or **NGINX/Apache**. Here, I'll use Python’s built-in HTTP server for simplicity:

1. Navigate to the directory where your HTML file is located:
   ```bash
   cd /var/www/blocked
   ```
2. Run the Python HTTP server on a specific port (for example, port 8080):
   ```bash
   python3 -m http.server 8080
   ```
   This will start a local HTTP server serving the `index.html` file.
   Now, if you go to `http://localhost:8080` or `http://<your-server-ip>:8080` in your browser, you should see the "This Page is Blocked" message.

## Step 3: Configure dnsmasq to Redirect Blocked Domains

Next, configure `dnsmasq` to redirect blocked domains to your local HTML server.

1. Open the `dnsmasq` configuration file:
   ```bash
   sudo nano /etc/dnsmasq.conf
   ```
2. Add entries for the domains you want to block and redirect them to your local server (replace `192.168.1.100` with your server's IP address):
   ```bash
   # Redirect blocked domains to local web server running on 192.168.1.100:8080
   address=/example.com/192.168.1.100
   address=/ads.example.com/192.168.1.100
   ```
3. Restart `dnsmasq` to apply the changes:
   ```bash
   sudo systemctl restart dnsmasq
   ```
## Step 4: Verify the Setup

To test if the setup is working:

1. Try to access a blocked domain (e.g., `example.com`) from a browser on a client machine in your network.
1. You should see the custom "This Page is Blocked" message served from your local HTML server.

This approach gives you a simple and effective way to show a blocked page for specific domains using `dnsmasq`!