# Configuring Ethernet Interfaces with Netplan

Netplan is a simple and efficient utility for configuring network interfaces in Ubuntu and other Linux distributions that use `systemd` for managing network configurations. 

---

## Prerequisites

Before starting, ensure the following:

1. You are using a Linux distribution that supports Netplan (e.g., Ubuntu 18.04 or later).
2. You have `sudo` privileges to modify network configurations.

---

## Understanding Netplan Configuration Files

Netplan configuration files are located in the `/etc/netplan/` directory and typically have a `.yaml` extension. Examples include:

- `/etc/netplan/01-netcfg.yaml`

Netplan uses YAML syntax, which is indentation-sensitive. Ensure proper formatting while editing.

---

## Steps to Configure an Ethernet Interface

### 1. Identify the Network Interface

List all network interfaces using the following command:

```bash
ip link show
```

Note the name of the Ethernet interface (e.g., `eth0`, `enp3s0`).

---

### 2. Create or Edit a Netplan Configuration File

Use a text editor to create or edit a file in the `/etc/netplan/` directory. For example:

```bash
sudo nano /etc/netplan/01-netcfg.yaml
```

---

### 3. Configure the Ethernet Interface

Below are examples of typical configurations.

#### a. **Dynamic IP Address Configuration (DHCP)**

```yaml
network:
  version: 2
  ethernets:
    enp3s0:
      dhcp4: true
```

#### b. **Static IP Address Configuration**

```yaml
network:
  version: 2
  ethernets:
    enp3s0:
      addresses:
        - 192.168.1.100/24
      gateway4: 192.168.1.1
      nameservers:
        addresses:
          - 8.8.8.8
          - 8.8.4.4
```

#### c. **Multiple IP Addresses on One Interface**

```yaml
network:
  version: 2
  ethernets:
    enp3s0:
      addresses:
        - 192.168.1.100/24
        - 192.168.1.101/24
      gateway4: 192.168.1.1
      nameservers:
        addresses:
          - 8.8.8.8
          - 8.8.4.4
```

---

### 4. Apply the Configuration

Once you have saved the configuration file, apply the changes using:

```bash
sudo netplan apply
```

If the configuration is incorrect, Netplan will report an error. Use `sudo netplan try` to test the configuration interactively before applying it permanently.

---

### 5. Verify the Configuration

Check the status of the interface to confirm it is configured correctly:

```bash
ip addr show enp3s0
```

You can also test connectivity using:

```bash
ping -c 4 8.8.8.8
```

---

## Troubleshooting

1. **Check for Syntax Errors:**
   
   Use the following command to validate the YAML file:
   
   ```bash
   sudo netplan generate
   ```

2. **Review Logs:**
   
   Check system logs for network-related errors:
   
   ```bash
   journalctl -u systemd-networkd
   ```

3. **Revert Changes:**
   
   If the network becomes inaccessible after applying changes, use a recovery shell or boot into a live session to correct the configuration.

---

## Additional Resources

- [Netplan Official Documentation](https://netplan.io/reference)
- `man netplan`

---


