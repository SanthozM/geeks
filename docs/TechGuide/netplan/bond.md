Here's a detailed MkDocs post on configuring bond interfaces using Netplan:

---

## Configuring Bond Interfaces Using Netplan

### What is a Bonded Interface?

A **bonded interface** is a method of combining multiple network interfaces into a single logical interface. This is done for **redundancy**, **load balancing**, and **performance enhancement**. Bonding allows you to aggregate multiple physical network interfaces to create a single, higher-speed virtual interface. It also improves network availability, as if one interface fails, the others will take over without network disruption.

### Benefits of Bonded Interfaces:
- **Increased Throughput**: Combining multiple interfaces can provide better bandwidth and higher throughput, especially when transferring large amounts of data.
- **Redundancy and Fault Tolerance**: Bonding multiple interfaces ensures that if one interface goes down, the remaining interfaces can continue to provide connectivity without a service disruption.
- **Load Balancing**: The network load can be evenly distributed across the bonded interfaces, improving overall network efficiency.

### Netplan Overview

Netplan is a utility in Ubuntu and other modern Linux distributions for configuring networking. It is the recommended configuration tool for network settings, replacing older utilities such as `/etc/network/interfaces`. Netplan works with both **systemd-networkd** and **NetworkManager** as the backend to apply configuration changes.

In this guide, we will walk through how to configure bond interfaces using Netplan, their uses, the pros and cons of bonding, and routing configuration.

### Netplan Configuration for Bond Interfaces

#### Step 1: Identifying Network Interfaces

Before configuring bonding, you need to identify the network interfaces available on your system. You can use the following command to list them:

```bash
ip link show
```

Assume the available interfaces are `eth0`, `eth1`, and `eth2`.

#### Step 2: Creating the Netplan Configuration

Netplan configuration files are located in `/etc/netplan/`. Typically, these files have the `.yaml` extension and are named something like `00-installer-config.yaml`. You need to create or modify a file in this directory to configure bonding.

1. Create or edit a configuration file, e.g., `01-bonding.yaml`.

```bash
sudo nano /etc/netplan/01-bonding.yaml
```

2. Add the following configuration to create a bonded interface:

```yaml
network:
  version: 2
  renderer: networkd
  ethernets:
    eth0: {}
    eth1: {}
    eth2: {}
  bonds:
    bond0:
      interfaces:
        - eth0
        - eth1
        - eth2
      parameters:
        mode: balance-rr          # Load balancing mode (round-robin)
        mii-monitor-interval: 100 # Monitoring interval (ms)
        primary: eth0            # Primary interface for failover
```

In the example above:
- **`bond0`** is the new bonded interface.
- **`eth0`, `eth1`, and `eth2`** are the physical interfaces being bonded together.
- **`mode: balance-rr`** sets the bonding mode to round-robin load balancing. Other modes include `active-backup`, `802.3ad`, `balance-xor`, etc.
- **`mii-monitor-interval`** specifies the monitoring interval to check the status of the interfaces.
- **`primary`** defines the primary interface for failover.

#### Step 3: Apply the Configuration

Once you have saved the configuration file, apply the changes with:

```bash
sudo netplan apply
```

You can verify that the bond interface is created successfully by running:

```bash
ip addr show bond0
```

### Routing Configuration with Bond Interfaces

After creating a bonded interface, you may need to configure routing to manage traffic flow across the bond. Routing can be configured to ensure that traffic goes through the correct interface or a combination of interfaces for load balancing or redundancy.

To add routing configuration in Netplan for a bonded interface, follow these steps:

1. Modify the Netplan YAML file to include routing details:

```yaml
network:
  version: 2
  renderer: networkd
  ethernets:
    eth0: {}
    eth1: {}
    eth2: {}
  bonds:
    bond0:
      interfaces:
        - eth0
        - eth1
        - eth2
      parameters:
        mode: balance-rr
        mii-monitor-interval: 100
        primary: eth0
```

2. The `routes` section in this configuration directs all outbound traffic (`0.0.0.0/0`) through the IP address `192.168.1.1`, which is the gateway for the bonded interface.

3. Apply the changes with:

```bash
sudo netplan apply
```

You can check the routing table by running:

```bash
ip route
```

### Bonding Modes

There are several modes you can use for bonding, depending on your needs. Here are the most common ones:

1. **balance-rr**: Round-robin load balancing. This mode uses all interfaces in a rotating manner.
2. **active-backup**: Only one interface is active at any given time, providing fault tolerance.
3. **802.3ad (LACP)**: Combines interfaces into a single logical interface using the Link Aggregation Control Protocol (LACP). This mode requires support from the switch.
4. **balance-xor**: Traffic is distributed based on MAC address or IP hash.
5. **broadcast**: Sends all traffic on all interfaces for redundancy.
6. **transmit-load-balancing**: Uses a round-robin approach, but with more intelligent distribution based on the load.

Each mode has its advantages, and choosing the right one depends on your network topology and requirements.

### Pros and Cons of Bonding

#### Pros:
- **Increased Throughput**: Aggregates the bandwidth of multiple interfaces for faster data transfer.
- **Redundancy**: Ensures that network connectivity remains available even if one interface fails.
- **Load Balancing**: Distributes traffic across multiple interfaces to avoid congestion.
- **Improved Fault Tolerance**: If one network link fails, the bond automatically switches to another link without any service disruption.

#### Cons:
- **Requires Switch Support**: Some modes, like `802.3ad`, require switches that support LACP (Link Aggregation Control Protocol).
- **Configuration Complexity**: Bonding can add complexity to network configurations, especially when multiple switches and advanced bonding modes are used.
- **Potential Overhead**: In certain configurations, especially when using modes like `balance-rr`, the load on the system could increase due to handling multiple interfaces.
- **Single Point of Failure**: In the case of using a non-redundant bonding mode like `balance-rr`, if a failure occurs in the primary interface, it could disrupt the entire bonded interface unless proper failover is configured.

### Conclusion

Configuring bond interfaces using Netplan provides an efficient way to enhance network performance, redundancy, and fault tolerance. By following the steps outlined in this post, you can quickly create and configure bonded interfaces, manage routing, and select the right bonding mode for your use case.

Ensure you thoroughly test the bond setup, especially in production environments, to verify that it meets the desired redundancy and performance criteria.
