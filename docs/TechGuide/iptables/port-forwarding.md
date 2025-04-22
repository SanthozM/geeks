# 🔁 Port Forwarding with iptables (DNAT Configuration Guide)

Port forwarding, also known as **Destination NAT (DNAT)**, is used to forward traffic from one IP/port to another internal IP/port. This is especially useful in scenarios where a server is behind a firewall or NAT router and needs to be accessible from the outside world.

---

## 🧠 What is DNAT?

DNAT changes the **destination IP and/or port** of incoming packets. It's used in **port forwarding** to redirect requests from one machine to another on the local network.

---

## 🧰 Use Case Example

Let’s say:

- Your public server IP is `203.0.113.10`
- You want to forward external traffic on port `8080` to an internal web server at `192.168.1.100:80`

---

## 📦 Required Modules

Ensure `iptables` and `ip_forwarding` are enabled.

```bash
echo 1 > /proc/sys/net/ipv4/ip_forward
```

Make it permanent in `/etc/sysctl.conf`:

```bash
net.ipv4.ip_forward = 1
```

Apply the config:

```bash
sudo sysctl -p
```

---

## 🔧 DNAT Rule with iptables

### Step 1: Add the DNAT rule

```bash
sudo iptables -t nat -A PREROUTING -p tcp -d 203.0.113.10 --dport 8080 -j DNAT --to-destination 192.168.1.100:80
```

> This tells iptables to redirect traffic from public IP `203.0.113.10:8080` to internal `192.168.1.100:80`.

---

### Step 2: Allow forwarding of packets

```bash
sudo iptables -A FORWARD -p tcp -d 192.168.1.100 --dport 80 -m state --state NEW,ESTABLISHED,RELATED -j ACCEPT
```

---

### Step 3: (Optional) SNAT to avoid asymmetric routing

If the internal server's default gateway is NOT the forwarding machine:

```bash
sudo iptables -t nat -A POSTROUTING -d 192.168.1.100 -p tcp --dport 80 -j SNAT --to-source 192.168.1.1
```

---

## 🧪 Testing

From a remote machine:

```bash
curl http://203.0.113.10:8080
```

You should reach the internal web server running on `192.168.1.100:80`.

---

## 🔄 List and Delete Rules

### View NAT table

```bash
sudo iptables -t nat -L -n -v
```

### Delete DNAT rule (replace with line number)

```bash
sudo iptables -t nat -D PREROUTING <line-number>
```

---

## 💾 Save Rules

On Ubuntu/Debian:

```bash
sudo apt install iptables-persistent
sudo netfilter-persistent save
```

---

## ✅ Summary

Port forwarding via DNAT is a core technique in network configuration. It enables you to:

- Expose internal services securely
- Host multiple services behind a single IP
- Build custom gateways, proxies, and routers

---

*Written by Santhosh Murugesan – Helping you master Linux networking, one NAT rule at a time.*
