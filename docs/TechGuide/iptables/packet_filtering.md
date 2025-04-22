# 🚫 Dropping Packets with iptables (Filter Table Guide)

Dropping unwanted packets is one of the primary uses of `iptables` for securing a Linux-based network. This guide explains how to use the **filter table** in iptables to drop specific packets effectively and safely.

---

## 🧠 What is the Filter Table?

The **filter table** is the default table in `iptables`, responsible for handling **packet filtering**. It contains three main built-in chains:

- **INPUT** – Controls packets **destined** for the local system
- **FORWARD** – Controls packets **routed through** the system
- **OUTPUT** – Controls packets **originating** from the local system

---

## 🔥 Why Drop Packets?

Dropping packets is useful to:

- Block specific IPs or ranges
- Deny access to unused ports
- Harden systems against scans and brute force
- Filter suspicious traffic before it reaches applications

---

## 🧰 Basic Drop Example: Block an IP

### Drop incoming packets from a specific IP:

```bash
sudo iptables -A INPUT -s 192.168.1.100 -j DROP
```

> This prevents the IP `192.168.1.100` from interacting with your machine.

---

## 🎯 Drop Packets to Specific Port

### Drop access to SSH port (22):

```bash
sudo iptables -A INPUT -p tcp --dport 22 -j DROP
```

> Useful if you want to temporarily disable SSH without stopping the service.

---

## 🔁 Drop Forwarded Packets

### Block packets passing through (router/gateway setup):

```bash
sudo iptables -A FORWARD -s 10.10.10.10 -j DROP
```

> Blocks routed traffic from `10.10.10.10` across your gateway.

---

## 📤 Drop Outgoing Traffic

### Prevent your system from connecting to a specific server:

```bash
sudo iptables -A OUTPUT -d 123.123.123.123 -j DROP
```

---

## 🧪 View Rules

```bash
sudo iptables -L -n -v --line-numbers
```

---

## 💣 Delete or Flush Rules

### Delete a specific rule:

```bash
sudo iptables -D INPUT <rule-number>
```

### Flush all rules in the INPUT chain:

```bash
sudo iptables -F INPUT
```

---

## 💾 Save Rules Permanently

### On Debian/Ubuntu:

```bash
sudo apt install iptables-persistent
sudo netfilter-persistent save
```

### On RHEL/CentOS:

```bash
sudo service iptables save
```

---

## ✅ Best Practices

- Always test drop rules carefully to avoid locking yourself out.
- Place **DROP** rules after **ACCEPT** rules (order matters!).
- Combine with logging for visibility:
  
```bash
sudo iptables -A INPUT -s 192.168.1.200 -j LOG --log-prefix "Blocked: "
sudo iptables -A INPUT -s 192.168.1.200 -j DROP
```

---

## 📌 Summary

Dropping packets with iptables is a foundational skill for any Linux admin or network engineer. Whether you’re blocking attacks or cleaning up unused access points, the filter table has your back.

---

*Written by Santhosh Murugesan – Teaching Linux defense, one packet at a time.*
