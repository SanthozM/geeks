# 🔒 Domain-Based Blocking/Forwarding using iptables, ipset, and dnsmasq

This guide shows how to **block domains** using a powerful combo: `iptables`, `ipset`, and `dnsmasq`. This method allows you to dynamically block domains by resolving them to IPs and adding them to a blacklist used by `iptables`.

---

## 🧩 Overview

### 🔗 Components Used:

- **dnsmasq** – Lightweight DNS forwarder that can populate `ipset` with resolved IPs.
- **ipset** – Creates fast and dynamic IP sets for firewall filtering.
- **iptables** – Uses `ipset` to drop traffic to blocked IPs.

---

## 🛠 Step-by-Step Setup

---

### 1️⃣ Install Required Packages

```bash
sudo apt update
sudo apt install dnsmasq ipset iptables -y
```

---

### 2️⃣ Create an IP Set for Blocked Domains

```bash
sudo ipset create blacklist hash:ip
```

To make it persistent across reboots, consider using `/etc/ipset.conf`.

---

### 3️⃣ Configure iptables to Drop Matching IPs

```bash
sudo iptables -I OUTPUT -m set --match-set blacklist dst -j DROP
sudo iptables -I FORWARD -m set --match-set blacklist dst -j DROP
```

> This drops all outgoing and forwarded traffic to any IP in the `blacklist` ipset.

---

### 4️⃣ Configure dnsmasq to Populate ipset

Edit or create `/etc/dnsmasq.d/ipset.conf` and add:

```conf
ipset=/example.com/blacklist
ipset=/ads.example.net/blacklist
ipset=/tracking.badsite.com/blacklist
```

You can add as many domains as you like. All resolved IPs will be pushed to the `blacklist` ipset.

---

### 5️⃣ Enable and Restart dnsmasq

```bash
sudo systemctl restart dnsmasq
sudo systemctl enable dnsmasq
```

> Ensure `dnsmasq` is not being overridden by another DNS service like `systemd-resolved`.

---

### 6️⃣ Test the Setup

Try to `ping` or `curl` one of the blocked domains:

```bash
ping example.com
curl http://example.com
```

You’ll see either no response or the connection failing due to the `iptables` drop rule.

Check the IP set:

```bash
sudo ipset list blacklist
```

---

## 🧠 Why This Is Awesome

- Dynamically blocks domains based on DNS
- Works at the firewall level (not just browser)
- No need for bulky proxy servers
- Great for ad-blocking, malicious domain filtering, etc.

---

## 💡 Tips & Notes

- You can periodically update the domain list from a public blocklist using a cron job.
- Combine with `LOG` rules in iptables to log blocked access attempts.
- Works great on embedded systems and low-resource routers.

---

## 🔄 Make ipset Persistent (Optional)

You can store active sets to reload on boot:

```bash
sudo ipset save > /etc/ipset.conf
```

Then add to `/etc/rc.local` or equivalent startup script:

```bash
ipset restore < /etc/ipset.conf
```

---

## ✅ Conclusion

This method gives you **fine-grained domain control** at the network layer. Lightweight, fast, and effective — perfect for home firewalls, edge devices, or server-side protections.

---

*Written by Santhosh Murugesan – Smarter Networking, One Rule at a Time.*
