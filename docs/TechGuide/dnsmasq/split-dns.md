To set up split DNS with Dnsmasq, you need to configure different DNS resolutions for internal and external network users. Split DNS is commonly used to handle different DNS responses based on where the request originates. Here’s a guide on configuring Dnsmasq for split DNS.

### Prerequisites
- **Dnsmasq installed** on your server (if not installed, use `sudo apt-get install dnsmasq`).
- **Network interfaces** configured with internal and external IPs.

### Step 1: Configure Dnsmasq

1. **Edit/Create the `.conf` file**
   Open the Dnsmasq configuration file, usually located at `/etc/dnsmasq.conf` or Create a new file under `/etc/dnsmasq.d/`:
   ```bash
   sudo nano /etc/dnsmasq.conf
   ```
???+ Note
    Creating New file under the ``/etc/dnsmasq.d/` is highly recommended

2. **Define DNS server settings for internal and external networks**:
   Use the following configuration options in `dnsmasq.conf`:

   - **Define internal DNS resolutions:**
     Specify internal domains (or subdomains) that should resolve differently for users on the internal network. For example, suppose your internal domain is `internal.example.com`, and internal requests should resolve to the local IP `192.168.1.10`:

     ```ini
     # Serve internal.example.com requests with the internal DNS server
     server=/internal.example.com/192.168.1.10
     ```

   - **Configure external DNS resolutions:**
     Define the public DNS server for other domains. For example, using Google DNS for all other requests:

     ```ini
     # External DNS for all other queries
     server=8.8.8.8
     ```

3. **Bind Dnsmasq to Specific Interfaces:**
   If your server has multiple network interfaces (e.g., `eth0` for external and `eth1` for internal), you can bind Dnsmasq to listen on the internal interface only:
   
   ```ini
   # Listen on internal interface
   interface=eth1
   ```

4. **Add Local DNS Entries (Optional):**
   For specific hostnames in the internal domain, you can use the `address` directive. For example:
   
   ```ini
   # Map a specific hostname to an IP
   address=/server1.internal.example.com/192.168.1.20
   ```

### Step 2: Restart Dnsmasq

After editing the configuration, restart the Dnsmasq service to apply changes:

```bash
sudo systemctl restart dnsmasq
```

### Step 3: Testing the Configuration

1. **From an internal device**:
   Run the following to verify the internal DNS resolution:
   ```bash
   nslookup server1.internal.example.com
   ```

2. **From an external device**:
   Verify the DNS resolves to the public IP:
   ```bash
   nslookup example.com
   ```

This setup will direct internal DNS requests for `internal.example.com` to the internal DNS server while other requests go to the external DNS (Google DNS in this example). Let me know if you need further customization!