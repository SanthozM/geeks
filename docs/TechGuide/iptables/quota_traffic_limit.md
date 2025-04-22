# 📊 Traffic Control with iptables `quota` Module

The `quota` module in iptables allows you to **limit traffic by data size** — making it extremely useful for bandwidth-limited environments, metered networks, or temporary usage-based control.

---

## 🧠 What is iptables `quota`?

The `quota` module tracks the amount of traffic that matches a rule and **stops matching after a defined data limit** (in bytes). Once the limit is exceeded, subsequent packets won't match the rule.

---

## 🔧 Real-Time Use Cases

- Limit data usage for a specific IP or subnet
- Cap bandwidth for guest networks
- Enforce metered usage in development environments
- Prevent abuse of internal services

---

## 🛠 Basic Syntax

```bash
iptables -A <CHAIN> -m quota --quota <BYTES> -j <TARGET>
```

Example:
```bash
iptables -A OUTPUT -m quota --quota 10000000 -j ACCEPT
```

> Allows up to **10 MB** of outbound traffic before stopping.

---

## 🧪 Practical Use Case: Limit Traffic for a Specific IP

Let’s say you want to allow only **50MB of outbound traffic** from a machine with IP `192.168.1.100`:

```bash
iptables -A FORWARD -s 192.168.1.100 -m quota --quota 52428800 -j ACCEPT
iptables -A FORWARD -s 192.168.1.100 -j DROP
```

> After 50MB is used, all further packets from that IP will be dropped.

---

## 🎯 Use with Specific Ports or Protocols

Example: Allow up to **20MB** of HTTP traffic (port 80) to leave your machine:

```bash
iptables -A OUTPUT -p tcp --dport 80 -m quota --quota 20971520 -j ACCEPT
iptables -A OUTPUT -p tcp --dport 80 -j REJECT
```

---

## 📌 Important Notes

- `quota` is **not resettable** by iptables itself — it resets on reboot or by flushing the rule.
- It does not provide bandwidth throttling, only data cap enforcement.
- Works best when combined with **logging** or **monitoring scripts**.

---

## 🧹 Reset Quota Rules

To remove/reset a quota rule:

```bash
iptables -D FORWARD -s 192.168.1.100 -m quota --quota 52428800 -j ACCEPT
```

Or flush the entire chain:

```bash
iptables -F
```

---

## 📋 View Current Rules

```bash
iptables -L -v -n --line-numbers
```

> This helps monitor which rule is in effect and track byte counters.

---

## 🔄 Make Rules Persistent

On Debian/Ubuntu:

```bash
sudo apt install iptables-persistent
sudo netfilter-persistent save
```

---

## ✅ Summary

The `quota` module is an effective tool for simple traffic control without needing complex tools like tc or QoS. It’s best for:

- Quick enforcement of data limits
- Lightweight guest access control
- Bandwidth metering in test environments

---

*Written by Santhosh Murugesan – Making traffic count, one byte at a time.*
