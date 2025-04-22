# 🔀 Understanding IP Masquerading with iptables (NAT Configuration)

**IP Masquerading** using `iptables` is a powerful technique for enabling multiple devices on a private network to access the internet using a single public IP. This guide will walk through what it is, how it works, and how to configure it using the `MASQUERADE` target.

---

## 🧠 What is IP Masquerading?

IP Masquerading is a form of **Source NAT (SNAT)**. It rewrites the source IP address of outgoing packets to the public IP of the gateway (usually your router or firewall) so that internal devices can reach the internet.

---

## 🔧 Why Use MASQUERADE?

- Automatically uses the public IP of the outgoing interface
- Ideal for **dynamic IP addresses** (e.g., DHCP-based connections)
- Useful for home labs, routers, or VPN gateways

---

## 🧰 Prerequisites

- A Linux machine acting as a router (two interfaces: internal and external)
- iptables installed
- IP forwarding enabled

---

## ⚙️ Enabling IP Forwarding

```bash
echo 1 > /proc/sys/net/ipv4/ip_forward
```

To make it persistent:

```bash
# Edit the sysctl config file
sudo nano /etc/sysctl.conf

# Uncomment or add:
net.ipv4.ip_forward = 1

# Apply changes
sudo sysctl -p
```

---

## 🚀 MASQUERADE Configuration with iptables

Assume:

- `eth0` is the **external interface** (connected to internet)
- `eth1` is the **internal interface** (connected to LAN)

### Add MASQUERADE Rule:

```bash
sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
```

### Forward Traffic from LAN to WAN:

```bash
sudo iptables -A FORWARD -i eth1 -o eth0 -j ACCEPT
sudo iptables -A FORWARD -i eth0 -o eth1 -m state --state RELATED,ESTABLISHED -j ACCEPT
```

---

## 🧪 Example Scenario

You have a Linux box that connects to the internet on `eth0` and your LAN is connected to `eth1`. The LAN devices use the Linux box as their gateway.

When a LAN device accesses a website:

1. Packet from LAN hits the Linux box on `eth1`
2. MASQUERADE changes source IP to public IP of `eth0`
3. Response comes back to `eth0`
4. iptables tracks the connection and forwards it to the original internal IP via `eth1`

---

## 💾 Saving iptables Rules

On Debian/Ubuntu:

```bash
sudo apt install iptables-persistent
sudo netfilter-persistent save
```


## 🧠 Bonus Tip: View Active NAT Rules

```bash
sudo iptables -t nat -L -n -v
```

---

## ✅ Final Thoughts

Using the `MASQUERADE` target in iptables is a simple and effective way to provide internet access to internal devices on a network. It's widely used in:

- Home routers
- VPN servers
- Custom firewall setups

Stay smart. Stay secure. And always test your firewall rules before deploying to production.

---

*Written by Santhosh Murugesan – Simplifying Linux Networking One Rule at a Time.*
