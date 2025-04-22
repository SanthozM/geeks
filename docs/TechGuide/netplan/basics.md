# Netplan

Netplan is a powerful utility that simplifies network configuration on modern Linux systems. It provides a declarative way to configure network interfaces using YAML files, replacing older methods such as `ifconfig` and `/etc/network/interfaces`. 

---

## What is Netplan?

Netplan is a configuration utility for easily managing and applying network settings. Introduced in Ubuntu 17.10, it serves as a bridge between system administrators and low-level networking tools like `systemd-networkd` and `NetworkManager`. With Netplan, you define your network configurations in YAML files, and it handles the backend integration with these renderers.

### Key Features

- **Declarative Configuration**: Network settings are defined in human-readable YAML files.
- **Renderer Independence**: Supports both `systemd-networkd` and `NetworkManager` as backends.
- **Modern Networking**: Supports advanced features like bridges, VLANs, and bonds.
- **Simplified Management**: A single command (`netplan apply`) applies all configurations.

---

## Why Use Netplan?

Netplan streamlines network configuration by:

1. **Reducing Complexity**: YAML syntax is simpler and more intuitive compared to legacy methods.
2. **Centralizing Configurations**: Consolidates all network settings in the `/etc/netplan/` directory.
3. **Supporting Modern Networking**: Provides built-in support for advanced features like DHCP, static IPs, bridges, and VLANs.

---

## Netplan Configuration Files

### Location of Configuration Files

Netplan configuration files are stored in the `/etc/netplan/` directory. These files typically have a `.yaml` extension, such as `01-netcfg.yaml` or `50-cloud-init.yaml`.

### Structure of a Netplan File

A basic Netplan configuration file contains:

1. **`network`**: The root key that holds all network settings.
2. **`version`**: Indicates the YAML schema version (currently version `2`).
3. **`ethernets`, `vlans`, `bonds`, `bridges`**: Define specific types of interfaces.

Example:

```yaml
network:
  version: 2
  ethernets:
    enp0s3:
      dhcp4: true
```

### Why Configuration Files Have Numbers

Files in `/etc/netplan/` often have a prefix like `01-`, `50-`, etc., which determines the order in which they are applied. Lower numbers take precedence over higher numbers. For example:

- `01-netcfg.yaml` will override settings in `50-cloud-init.yaml` if both define the same interface.

This numbering system allows you to prioritize and layer configurations.

### Applying Configuration Files

After creating or modifying a configuration file, you must apply the changes using:

```bash
sudo netplan apply
```

You can test the configuration before applying it permanently:

```bash
sudo netplan try
```

---

## What is a Renderer in Netplan?

The renderer determines how Netplan applies configurations to the system. Netplan supports two renderers:

1. **`networkd` (systemd-networkd):** A lightweight backend suitable for servers and minimal installations.
2. **`NetworkManager`:** A full-featured network manager typically used on desktops and laptops.

### Specifying the Renderer

In the YAML file, you can specify the renderer globally or per interface. Example:

```yaml
network:
  version: 2
  renderer: networkd
  ethernets:
    enp0s3:
      dhcp4: true
```

Or assign a different renderer to specific interfaces:

```yaml
network:
  version: 2
  ethernets:
    enp0s3:
      renderer: NetworkManager
      dhcp4: true
```

### Advanced Options

Netplan also supports advanced configurations like:

- **Bonds**: For link aggregation.
- **Bridges**: For virtualized or containerized environments.
- **VLANs**: For virtual LAN tagging.

Refer to specific guides for these configurations.

---

## Troubleshooting Netplan

### Validating Configuration Files

Ensure the YAML syntax is correct:

```bash
sudo netplan generate
```

### Debugging Errors

Check logs for error messages:

```bash
journalctl -u systemd-networkd
```

### Reverting Changes

If a configuration fails, Netplan will automatically revert to the previous working state when using `netplan try`.

---

## Conclusion

Netplan simplifies network management on Linux systems, offering a modern, declarative approach to configuring interfaces. Understanding its YAML syntax, file ordering, and renderers allows you to unlock powerful networking capabilities while keeping configurations clean and manageable. For more details, refer to the [Netplan Official Documentation](https://netplan.io/reference).

