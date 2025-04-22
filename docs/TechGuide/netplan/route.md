# Configuring Routes in Netplan

Routing is a crucial aspect of networking, enabling communication between different subnets and networks. In Netplan, routes can be configured for various interfaces like Ethernet, VLAN, and Bridge interfaces. 

---

## What is Routing?

Routing is the process of directing network packets from a source to a destination. Proper routing ensures that data travels through the optimal path to reach its destination. Routes can be static (manually defined) or dynamic (automatically updated).

### Why Do We Need Routing?

1. **Interconnectivity:** To enable communication between different subnets or networks.
2. **Load Balancing:** To distribute traffic across multiple paths for better performance.
3. **Redundancy:** To provide alternate paths in case of a failure in the primary route.
4. **Custom Policies:** To direct specific traffic through preferred paths based on application or priority.

---

## Key Concepts in Netplan Routing

### Routing Table

In Netplan, you can specify a routing table for advanced routing policies. Each routing table is identified by a unique number or name.

### Metrics

The `metric` field in Netplan determines the preference of a route. Lower metrics are preferred over higher ones. This is useful for defining fallback routes or prioritizing certain paths.

### File Location

Routes are configured in YAML files under the `/etc/netplan/` directory. Example file: `/etc/netplan/50-routing-config.yaml`.

---

## Configuring Routes for Ethernet Interfaces

### Static Route Configuration

```yaml
network:
  version: 2
  ethernets:
    enp3s0:
      dhcp4: false
      addresses:
        - 192.168.1.10/24
      routes:
        - to: 192.168.2.0/24
          via: 192.168.1.1
          metric: 100
          table: 100
        - to: 0.0.0.0/0
          via: 192.168.1.1
          metric: 200
          table: 100
```

In this example:
- A static route is configured to the `192.168.2.0/24` network via `192.168.1.1`.
- A default route (`0.0.0.0/0`) is added with a higher metric, making it a fallback route.
- A routing table `100` is used, and a policy routes packets originating from `192.168.1.10` through this table.

### Default Dynamic Route

Dynamic routes are typically managed by routing protocols like OSPF or BGP, not manually configured in Netplan. However, default dynamic routing can be set using DHCP:

```yaml
network:
  version: 2
  ethernets:
    enp4s0:
      dhcp4: true
```

---

## Configuring Routes for VLAN Interfaces

### Static Route Configuration

```yaml
network:
  version: 2
  vlans:
    vlan10:
      id: 10
      link: enp3s0
      addresses:
        - 192.168.10.2/24
      routes:
        - to: 192.168.20.0/24
          via: 192.168.10.1
          metric: 50
          table: 200
      routing-policy:
        - from: 192.168.10.2
          table: 200
```

In this configuration:
- `vlan10` is a VLAN interface linked to `enp3s0`.
- A static route to `192.168.20.0/24` is defined with a lower metric, prioritizing this path.
- A custom routing table `200` is specified.

---

## Configuring Routes for Bridge Interfaces

### Static Route Configuration

```yaml
network:
  version: 2
  bridges:
    br0:
      interfaces:
        - enp3s0
        - enp4s0
      addresses:
        - 10.0.0.1/24
      routes:
        - to: 10.1.0.0/24
          via: 10.0.0.254
          metric: 150
          table: 300
        - to: 0.0.0.0/0
          via: 10.0.0.254
          metric: 250
      routing-policy:
        - from: 10.0.0.1
          table: 300
```

In this setup:
- `br0` is a bridge interface combining `enp3s0` and `enp4s0`.
- Routes are added with metrics to determine priority.
- A custom routing table `300` is specified for advanced policy routing.

---

## Applying and Verifying the Configuration

1. Save the configuration file.
2. Apply the changes:

   ```bash
   sudo netplan apply
   ```

3. Verify the routing table:

   ```bash
   ip route show table 100
   ip route show table 200
   ip route show table 300
   ```

4. Check policies:

   ```bash
   ip rule
   ```

---

## Summary

- Routes in Netplan can be configured for Ethernet, VLAN, and Bridge interfaces.
- Use the `metric` field to prioritize routes.
- Use custom routing tables for advanced routing scenarios.
- Apply routing policies to direct traffic based on source addresses or interfaces.

By leveraging Netplan’s routing capabilities, you can create robust and flexible network configurations tailored to your needs.

