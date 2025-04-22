---
hide:
  - navigation
---

# dnsmasq: failed to create listening socket for port 53: Address already in use
Check what's listening on port 53 (domain) with:
```bash
sudo ss -lp "sport = :domain"
```

Disable any service that is running on this port. It's usually `systemd-resolved`

Here I make sure that you have stopped the `systemd-resolved` service. I'm going to also mask it so it doesn't auto start on reboot.

```bash
sudo systemctl stop systemd-resolved
sudo systemctl disable systemd-resolved
sudo systemctl mask systemd-resolved
```

To undo what you did:
```bash
sudo systemctl unmask systemd-resolved
sudo systemctl enable systemd-resolved
sudo systemctl start systemd-resolved
```