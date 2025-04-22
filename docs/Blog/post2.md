---
hide:
  - navigation
---

# Troubleshooting VPN Connectivity: Dealing with IPv6 Issues on Linux

Are you experiencing difficulties connecting to a VPN due to IPv6-related complications? Fear not, you've come to the right place.

At times, when attempting to connect to a VPN through older firewalls or routes utilizing Point-to-Point or other tunnels, IPv4-based authentication may be in place. If your IP address is IPv6-based, it can pose a barrier to accessing the VPN or your data. However, there's a solution: suppressing IPv6 on your Linux machine.

Note: This guide focuses specifically on Linux systems. (For Windows check for the next set of blogs😘)

## To suppress IPv6 and exclusively use IPv4 over IPv6, follow these simple steps:
→ Open terminal
→ Edit the "/etc/sysctl.conf" file as sudo using the gedit, nano, or vi editor. Example: I'm going to use nano
```
sudo nano /etc/systctl.conf
```
→ Now add the below lines at the end of the file.
```
net.ipv6.conf.all.disable_ipv6 = 1
net.ipv6.conf.default.disable_ipv6 = 1
net.ipv6.conf.lo.disable_ipv6 = 1
```
Note: In case the above configuration lines are already present, just change the value from 0 to 1 . By default, most of the Linux machineIPv6 are disabled and might not have this above configuration

→ The above configuration disables IPv6 on all the interfaces. If you want to disable in particular interface, just add the below lines
```
net.ipv6.conf.<interface name>.disable_ipv6 = 1
```
Replace the ~<interface name>~ string with the actual interface name in your system. Check interface details using `ip a` or `ifconfig` command.

→ Now, save the configuration.
→ Once you save the configuration. Give below command in terminal
```
sudo sysctl -p
```
→ Once it's successfully executed, in the terminal it shows the applied changes you have done in /etc/sysctl.conf

---

🤩Stick with the old one(IPv4) when the new one(IPv6) gets tricky😵‍💫, Even in Networks😇

---
