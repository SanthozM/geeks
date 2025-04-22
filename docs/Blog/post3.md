---
hide:
  - navigation
---

# Troubleshooting VPN Connectivity: Dealing with IPv6 Issues on Windows

Are you experiencing difficulties connecting to a VPN due to IPv6-related complications? Fear not, you've come to the right place.

At times, when attempting to connect to a VPN through older firewalls or routes utilizing Point-to-Point or other tunnels, IPv4-based authentication may be in place. If your IP address is IPv6-based, it can pose a barrier to accessing the VPN or your data. However, there's a solution: suppressing IPv6 on your Windows machine.

Note: This guide focuses specifically on Windows systems (For Linux use this blog link → Link 😇).

First you can check whether your IPv6 or IPv4 address got utilised by your computer searching for you pubic ip on the bowser((like searching wahtismyipaddress.com))

## To suppress IPv6 and exclusively use IPv4 over IPv6, follow these simple steps:
-> Open `Control Panel`.

-> Navigate to `Network and Sharing settings`.

-> Click on `Change adapter settings`.

-> Select your internet source (e.g., Wi-Fi if you access internet using wifi)

-> Right-click and select `Properties`.

-> Disable the IPv6 option in the properties menu.

By following these steps, you effectively disable or suppress IPv6 on your Windows machine.

Now, let's verify the changes got reflected by viewing your Public IP (like searching wahtismyipaddress.com).

Voilà! You'll notice that the IPv6 address has been suppressed, and only the IPv4 address is displayed. With this adjustment, you should be able to access the desired page using the IPv4 address.

## Should you need to re-enable IPv6, simply follow these steps:
-> Enable the `IPv6 option` in the properties menu.

-> Ensure that the `Automatically obtain IP address and DNS` option is enabled under IPv6 properties.

-> If any issues persist, consider disabling and re-enabling the source (e.g., Wi-Fi in this case).

By toggling these settings, you can effectively manage IPv6 connectivity on your Windows machine and troubleshoot VPN connection issues related to IPv6.

Remember, while IPv6 offers numerous advantages, in certain scenarios, reverting to IPv4 may be necessary to ensure seamless connectivity. With these steps, you're equipped to navigate IPv6-related challenges and optimize your VPN experience on Windows.

----

🤩Stick with the old one(IPv4) when the new one(IPv6) gets tricky😵‍💫, Even in Networks😇

----