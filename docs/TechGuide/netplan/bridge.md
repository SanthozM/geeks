# Configuring Bridge Interfaces with Netplan

A bridge interface is a virtual network device that combines multiple physical or virtual network interfaces into a single logical interface. This is commonly used in scenarios like virtualization, where virtual machines (VMs) need to connect to the host's physical network, or in containers for seamless network connectivity.

---

## What is a Bridge Interface?

A bridge acts like a virtual network switch, enabling devices connected to its member interfaces to communicate as if they were on the same physical network. Unlike a traditional network interface, a bridge can:

1. Forward traffic between its member interfaces.
2. Isolate traffic from different physical or virtual devices.
3. Support advanced networking features like VLANs, spanning tree protocols, and virtualized environments.

### Common Use Cases for Bridge Interfaces

- **Virtualization Platforms:** Allow VMs to share the host's physical network connection.
- **Network Segmentation:** Simplify configurations by grouping multiple interfaces under a single bridge.
- **Containers:** Provide containerized applications direct access to the network.

---

## Steps to Configure a Bridge Interface

### 1. Identify Member Interfaces

Use the following command to list available network interfaces:

```bash
ip link show
```

Decide which physical or virtual interfaces will be part of the bridge (e.g., `enp3s0`, `enp4s0`).

---

### 2. Create or Edit a Netplan Configuration File

Open or create a new configuration file in the `/etc/netplan/` directory. For example:

```bash
sudo nano /etc/netplan/03-bridge-config.yaml
```

---

### 3. Define the Bridge Configuration

Here are some examples of bridge configurations:

#### a. **Basic Bridge Configuration**

```yaml
network:
  version: 2
  ethernets:
    enp3s0:
      dhcp4: false
    enp4s0:
      dhcp4: false
  bridges:
    br0:
      interfaces:
        - enp3s0
        - enp4s0
      dhcp4: true
```

In this example:
- `br0` is the bridge interface.
- `interfaces` lists the member interfaces (`enp3s0`, `enp4s0`).
- `dhcp4: true` enables DHCP for the bridge, assigning an IP address to `br0`.

#### b. **Bridge with Static IP Address**

```yaml
network:
  version: 2
  ethernets:
    enp3s0:
      dhcp4: false
    enp4s0:
      dhcp4: false
  bridges:
    br0:
      interfaces:
        - enp3s0
        - enp4s0
      addresses:
        - 192.168.1.100/24
      gateway4: 192.168.1.1
      nameservers:
        addresses:
          - 8.8.8.8
          - 8.8.4.4
```

#### c. **Bridge for Virtualization (With No IP Address)**

```yaml
network:
  version: 2
  ethernets:
    enp3s0:
      dhcp4: false
  bridges:
    br0:
      interfaces:
        - enp3s0
      dhcp4: false
      parameters:
        stp: true
        forward-delay: 4
```

In this case:
- The bridge does not get an IP address but can be used by VMs or containers.
- `stp: true` enables Spanning Tree Protocol to prevent loops in the network.
- `forward-delay` specifies the time (in seconds) a port waits before forwarding packets.

---

### 4. Apply the Configuration

Save the file and apply the configuration:

```bash
sudo netplan apply
```

To test the configuration before applying permanently, use:

```bash
sudo netplan try
```

---

### 5. Verify the Bridge Setup

Check the status of the bridge interface:

```bash
ip link show br0
```

Ensure the bridge has the expected IP address and member interfaces:

```bash
bridge link
```

Test connectivity with:

```bash
ping -c 4 8.8.8.8
```

---

## Troubleshooting

1. **Configuration Errors:**
   Validate the YAML file with:
   
   ```bash
   sudo netplan generate
   ```

2. **Logs:**
   Check logs for detailed error messages:
   
   ```bash
   journalctl -u systemd-networkd
   ```

3. **Bridge Status:**
   Ensure the bridge interface is active and includes the member interfaces:
   
   ```bash
   brctl show
   ```

---

## Additional Resources

- [Netplan Official Documentation](https://netplan.io/reference)
- `man netplan`
- `man bridge`

---
