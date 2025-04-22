# Configuring VLANs with Netplan

Netplan makes it easy to configure VLANs (Virtual LANs) on systems running Ubuntu or other Linux distributions that use `systemd`. This guide will walk you through the steps to set up VLANs using Netplan.

---

## Prerequisites

Before proceeding, ensure the following:

1. Your Linux system supports Netplan (e.g., Ubuntu 18.04 or later).
2. You have `sudo` privileges to configure the network.
3. Your network interface supports VLAN tagging.

---

## Understanding VLANs

A VLAN allows you to create multiple logical networks on a single physical interface. Each VLAN is identified by a unique VLAN ID.

---

## Steps to Configure a VLAN

### 1. Identify the Base Interface

List all network interfaces using:

```bash
ip link show
```

Note the name of the physical interface (e.g., `enp3s0`) that will host the VLAN.

---

### 2. Create or Edit a Netplan Configuration File

Use a text editor to create or modify a YAML configuration file in the `/etc/netplan/` directory:

```bash
sudo nano /etc/netplan/02-vlan-config.yaml
```

---

### 3. Define the VLAN Configuration

Below are examples of VLAN configurations.

#### a. **Single VLAN Configuration**

```yaml
network:
  version: 2
  ethernets:
    enp3s0:
      dhcp4: false
  vlans:
    vlan10:
      id: 10
      link: enp3s0
      addresses:
        - 192.168.10.2/24
      gateway4: 192.168.10.1
      nameservers:
        addresses:
          - 8.8.8.8
          - 8.8.4.4
```

#### b. **Multiple VLANs on a Single Interface**

```yaml
network:
  version: 2
  ethernets:
    enp3s0:
      dhcp4: false
  vlans:
    vlan10:
      id: 10
      link: enp3s0
      addresses:
        - 192.168.10.2/24
    vlan20:
      id: 20
      link: enp3s0
      addresses:
        - 192.168.20.2/24
```

In this example:
- `id` specifies the VLAN ID.
- `link` indicates the physical interface associated with the VLAN.
- `addresses` define the IP addresses for each VLAN.

---

### 4. Apply the Configuration

After saving the file, apply the configuration:

```bash
sudo netplan apply
```

If you are unsure about the configuration, use `sudo netplan try` to test it interactively before applying it permanently.

---

### 5. Verify the VLAN Setup

Check the status of the VLAN interfaces:

```bash
ip link show
```

Look for the VLAN interfaces (e.g., `vlan10`, `vlan20`). Verify their IP configurations using:

```bash
ip addr show vlan10
```

Test connectivity using:

```bash
ping -c 4 192.168.10.1
```

---

## Troubleshooting

1. **Check Configuration Syntax:**
   
   Validate the YAML file:
   
   ```bash
   sudo netplan generate
   ```

2. **Review Logs:**
   
   Use the following command to view network-related logs:
   
   ```bash
   journalctl -u systemd-networkd
   ```

3. **Revert Changes:**
   
   If the network becomes inaccessible, use a recovery shell or boot into a live session to fix the configuration.

---

## Additional Resources

- [Netplan Official Documentation](https://netplan.io/reference)
- `man netplan`

---
