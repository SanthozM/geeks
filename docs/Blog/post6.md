---
hide:
  - navigation
---

# Block DNS over HTTPS(DoH) using DNSMASQ

To stop DNS over HTTPS (DoH) using Dnsmasq, you’ll need to block known DoH IP addresses or domains that provide DNS over HTTPS services. Dnsmasq alone cannot directly block HTTPS traffic, but it can prevent DNS lookups to popular DoH providers. Here’s a step-by-step guide:

## 1. Block DoH Provider Domains
Create a list of domains used by popular DoH providers (like Google, Cloudflare, and Mozilla) and configure Dnsmasq to block these domains.

1. **Edit your `dnsmasq.conf` file**:
   ```bash
   sudo nano /etc/dnsmasq.conf
   ```

2. **Add blocking rules**:
   Use the `address` directive to redirect DNS queries for these domains to an unreachable IP (e.g., `0.0.0.0`).

   ```ini
   # Block popular DoH providers
   address=/dns.google/0.0.0.0
   address=/cloudflare-dns.com/0.0.0.0
   address=/mozilla.cloudflare-dns.com/0.0.0.0
   address=/dns.quad9.net/0.0.0.0
   ```

3. **Save and close the file**.

## 2. Restart Dnsmasq

After updating the configuration, restart Dnsmasq to apply the changes:

```bash
sudo systemctl restart dnsmasq
```

## 3. Verify the Blocking

You can test if the DoH domains are blocked by trying to resolve them:

```bash
nslookup dns.google
```

## 4. Commonly used DNS over HTTPS - Domains
Here is a list of some commonly used DNS-over-HTTPS (DoH) domains and server IPs for popular providers like Google, Cloudflare, Quad9, and others. Blocking these can help prevent DoH traffic on your network.

``` Bash
# 1. Google Public DNS
     - dns.google
     - dns.google.com

# 2. Cloudflare DNS
     - cloudflare-dns.com
     - mozilla.cloudflare-dns.com

# 3. Quad9
     - dns.quad9.net

# 4. Cisco OpenDNS
     - doh.opendns.com

# 5. NextDNS
     - dns.nextdns.io

# 6. AdGuard DNS
     - dns.adguard.com
     - dns-family.adguard.com

# 7. CleanBrowsing DNS
     - doh.cleanbrowsing.org

# 8. Comodo Secure DNS
     - doh.securedns.com

# 9. Yandex DNS
     - doh.yandex.net
```

If the setup is successful, these domains should resolve to `0.0.0.0`, effectively blocking access to them.

## 5. Additional Measures

Since some browsers or applications may still use hardcoded DoH IPs, blocking them entirely requires firewall rules:

1. **Block DoH IPs with a firewall** (e.g., `iptables` or `ufw`).
   
2. **Configure Group Policy for browsers**: If managing a network, disable DoH in browsers through administrative policies, especially in environments where you have control over end-user devices.

This setup should help you control and prevent DNS over HTTPS usage effectively in your network.