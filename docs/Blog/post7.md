# WireGuard VPN Setup Guide

WireGuard is a fast, modern, and secure VPN that uses cutting-edge cryptography. This guide walks you through installing WireGuard, generating keys, configuring the VPN, and understanding the components involved — for both **Debian/Ubuntu** and **Windows** platforms.

---

## 🛠️ Installation

### 🐧 Debian / Ubuntu

```bash
sudo apt update
sudo apt install wireguard -y
```

Ensure your kernel supports WireGuard (Linux Kernel 5.6+ or install the wireguard-dkms package for older versions).

---

### 🪟 Windows

1. Download the installer from [https://www.wireguard.com/install/](https://www.wireguard.com/install/)
2. Install it with admin privileges.
3. Launch the **WireGuard** GUI for configuration.

---

## 🔐 Key Generation

### Debian / Ubuntu

```bash
wg genkey | tee privatekey | wg pubkey > publickey
```

- `privatekey` – Your private key (keep it secure)
- `publickey` – Public key to share with your peers

---

### Windows

1. Open WireGuard GUI
2. Click **Add Tunnel → Add empty tunnel**
3. WireGuard will generate keys automatically
4. You can export this configuration to `.conf` if needed

---

## ⚙️ Configuration

WireGuard configurations consist of `[Interface]` (local settings) and `[Peer]` (remote peer settings).

### Example: Debian / Ubuntu – `/etc/wireguard/wg0.conf`

```ini
[Interface]
PrivateKey = <your_private_key>
Address = 10.0.0.1/24
ListenPort = 51820

[Peer]
PublicKey = <peer_public_key>
AllowedIPs = 10.0.0.2/32
Endpoint = <peer_public_ip>:51820
PersistentKeepalive = 25
```

> Replace `<your_private_key>` and `<peer_public_key>` with actual keys.

---

### Example: Windows (via GUI)

- Use **Add Tunnel** → **Add empty tunnel**
- Enter the same parameters as in the Linux config
- Or import `.conf` files directly

---

## 🚀 Starting and Stopping WireGuard

### Debian / Ubuntu

```bash
sudo wg-quick up wg0     # Start VPN
sudo wg-quick down wg0   # Stop VPN
```

> `wg0` is the default config file name, located in `/etc/wireguard/wg0.conf`

---

### Windows

- Open the WireGuard app
- Select the tunnel
- Click **Activate** to start / **Deactivate** to stop

---

## 🧩 Configuration Components Explained

### [Interface]

| Field        | Description                                   |
|--------------|-----------------------------------------------|
| PrivateKey   | Private key for this device                   |
| Address      | IP address of this device in VPN subnet       |
| ListenPort   | Port to listen for incoming tunnels (default 51820) |

---

### [Peer]

| Field               | Description                                               |
|---------------------|-----------------------------------------------------------|
| PublicKey           | Public key of remote peer                                |
| AllowedIPs          | IPs allowed to route through this peer (can be 0.0.0.0/0) |
| Endpoint            | Public IP & port of the peer (`<ip>:51820`)              |
| PersistentKeepalive | Helps behind NAT – keep-alive packets every X seconds     |

---

## 🔍 Useful Commands (Linux)

```bash
sudo wg show         # Show current VPN status
ip a                 # Show interface details
sudo systemctl enable wg-quick@wg0  # Enable at boot
```

---

## 📁 Default File Locations

| OS      | Path                         |
|---------|------------------------------|
| Linux   | `/etc/wireguard/wg0.conf`    |
| Windows | Handled by GUI or export     |

---

## 🧠 How It Works

1. Each device creates a public/private keypair.
2. Peers authenticate using each other's public keys.
3. Only traffic from allowed IPs is routed through the VPN.
4. The encrypted tunnel allows secure communication between peers.

---

## 🔒 Best Practices

- Never share your **private key**.
- Use a **strong firewall rule** to allow only UDP 51820.
- If using NAT or behind a router, add `PersistentKeepalive = 25` on the client config.

---

## 📚 References

- [WireGuard Official Website](https://www.wireguard.com)
- [wg-quick Manual](https://man7.org/linux/man-pages/man8/wg-quick.8.html)
- [Linux Man Page for wg](https://man7.org/linux/man-pages/man8/wg.8.html)

---

*Documented by Santhosh Murugesan – For internal & learning use.*
