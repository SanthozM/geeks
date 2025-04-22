# DHCP Server (==Only on Ubuntu 20.04 and above versions==)

This guide provides step-by-step instructions to set up a DHCP server using `dnsmasq` on a specific network interface.

## Prerequisites

Before you begin, ensure you have the following:

- A Linux machine with a network interface for serving DHCP.
- `dnsmasq` installed.
- Sudo privileges on the machine.

## Step 1: Install Dnsmasq

To install `dnsmasq`, use your distribution's package manager. On a Debian/Ubuntu-based system, you can run:

```bash
sudo apt update
sudo apt install dnsmasq
```

## Step 2: List interface

To list avaialbe interface in the linux machine, you can run:

```linux
ip a
```

This will give the network interface name


## Step 3: Configure dnsmasq

Edit the dnsmasq configuration file, usually located at `/etc/dnsmasq.conf` (which is the default configuration). But the best advised method is to create a new configuration file under `/etc/dnsmasq.d`. Here's a basic configuration for dnsmasq as a DHCP server:

```bash
# /etc/dnsmasq.d/eth0-dnscpser.conf

# Enable DHCP server on a specific interface
interface=eth0   # Replace with your network interface

# Specify the range of IP addresses to allocate for DHCP clients
dhcp-range=192.168.1.100,192.168.1.150,12h   # Start, end of range, lease time

# Define the default gateway for DHCP clients
dhcp-option=option:router,192.168.1.1

# Define DNS server for clients
dhcp-option=option:dns-server,8.8.8.8,8.8.4.4

# Define subnet mask for the network
dhcp-option=option:netmask,255.255.255.0

# Optional: Define a static IP mapping for specific clients
dhcp-host=00:11:22:33:44:55,192.168.1.50   # MAC address and static IP

```

## Step 4: Start and Enable dnsmasq
Once the configuration is ready, restart the dnsmasq service and enable it to start on boot:

```bash
sudo systemctl restart dnsmasq
sudo systemctl enable dnsmasq
```

## Step 5: Verify the DHCP Lease
To verify that dnsmasq is working correctly, you can check the DHCP leases file, usually located at /var/lib/misc/dnsmasq.leases. This file contains information about the current DHCP leases.

```bash
cat /var/lib/misc/dnsmasq.leases
```

## Step 6: Troubleshooting
If things aren’t working as expected, check the system logs for dnsmasq messages to see if there are any errors:
```bash
sudo journalctl -xe | grep dnsmasq
```

This setup provides a basic dnsmasq-based DHCP server that serves IP addresses in the range 192.168.1.100 to 192.168.1.150 for 12 hours. You can adjust this based on your requirements.

!!! note
    If you face {++Port 53 already in use error++} Click --> [Link](../../Blog/post4.md){:target="_blank"} <-- this to redirect to the Blog post