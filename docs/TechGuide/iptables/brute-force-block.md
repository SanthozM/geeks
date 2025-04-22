# 🛡️ Combining iptables + fail2ban for Smart Firewall Protection

**fail2ban** is a powerful intrusion prevention system that works in tandem with **iptables** to monitor logs and dynamically block IPs that exhibit malicious behavior (e.g., repeated failed logins, port scans, etc.).

This guide shows how to set up and configure `fail2ban` with `iptables`, along with various blocking configurations.

---

## 📦 What You Need

```bash
sudo apt update
sudo apt install fail2ban iptables -y
```

---

## 🔧 How It Works

1. fail2ban monitors logs (e.g., `/var/log/auth.log`)
2. On suspicious patterns (like failed SSH attempts), it bans the offending IP
3. Banning is done via `iptables` rules (default action)

---

## 🧰 Enable IP Forwarding (if acting as a gateway)

```bash
echo 1 > /proc/sys/net/ipv4/ip_forward
sudo sysctl -w net.ipv4.ip_forward=1
```

---

## 🛠 Basic Configuration

### 1️⃣ Main config: `/etc/fail2ban/jail.local`

Example to protect SSH:

```ini
[sshd]
enabled = true
port = ssh
filter = sshd
logpath = /var/log/auth.log
maxretry = 5
bantime = 3600
findtime = 600
backend = systemd
```

---

### 2️⃣ Set Default Ban Action

In `[DEFAULT]` section of `jail.local`, use:

```ini
banaction = iptables-multiport
banaction_allports = iptables-allports
```

Available actions include:

- `iptables` – basic
- `iptables-multiport` – blocks multiple ports
- `iptables-allports` – bans an IP across all ports

---

## 🔄 Ban Action Examples

### 🚫 Block SSH Bruteforce

```ini
[sshd]
enabled = true
port = ssh
filter = sshd
logpath = /var/log/auth.log
maxretry = 3
bantime = 3600
```

---

### 🔐 Block HTTP Auth Failures

```ini
[apache-auth]
enabled = true
port = http,https
filter = apache-auth
logpath = /var/log/apache2/error.log
maxretry = 3
```

---

### 🔧 Custom Fail2ban Action for Logging + Drop

Create `/etc/fail2ban/action.d/iptables-logdrop.conf`:

```ini
[Definition]
actionstart = <iptables> -N f2b-<name>
              <iptables> -A f2b-<name> -j RETURN
              <iptables> -I INPUT -p <protocol> -j f2b-<name>

actionban = <iptables> -I f2b-<name> 1 -s <ip> -j LOG --log-prefix "F2B-BLOCK: "
            <iptables> -I f2b-<name> 2 -s <ip> -j DROP

actionunban = <iptables> -D f2b-<name> -s <ip> -j DROP
              <iptables> -D f2b-<name> -s <ip> -j LOG --log-prefix "F2B-BLOCK: "

[Init]
name = default
```

Use it in jail like:

```ini
[sshd]
enabled = true
banaction = iptables-logdrop
```

---

## 🔍 Useful Commands

### View banned IPs:

```bash
sudo fail2ban-client status sshd
```

### Manually ban/unban an IP:

```bash
sudo fail2ban-client set sshd banip 192.168.1.50
sudo fail2ban-client set sshd unbanip 192.168.1.50
```

### Reload fail2ban:

```bash
sudo systemctl restart fail2ban
```

---

## 🔁 Make Bans Persistent (Optional)

Fail2ban bans are not persistent after reboot. To make them persistent:

1. Use `iptables-persistent`:
   ```bash
   sudo apt install iptables-persistent
   sudo netfilter-persistent save
   ```

2. Or reload fail2ban on boot with `systemd` hooks.

---

## 🧠 Summary

| Feature               | Enabled by |
|------------------------|------------|
| Dynamic IP banning     | ✅ fail2ban |
| Protocol-based filtering | ✅ iptables |
| All-port blocking      | ✅ `iptables-allports` |
| Logging & alerts       | ✅ custom actions |

Fail2ban and iptables form a **reactive + preventive** defense mechanism that protects against a wide range of attacks with minimal resources.

---

*Written by Santhosh Murugesan – Automating your firewall so you sleep better at night.*
