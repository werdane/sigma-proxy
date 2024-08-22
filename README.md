# Sigma Proxy v1

<p align="center">
  <img src="https://github.com/user-attachments/assets/a108ab58-e883-4a65-a2a8-8ef562ce63b5" alt="Image Description" />
</p>
<p align="center">Don't get caught lackin by the opps, keep your IP hidden from the internet!</p>

<p align="center">🔥 Supports Windows 🔥</p>
<p align="center">🔥 Supports Linux 🔥</p>

**Description:**

Sigma Proxy v1 is a versatile Python script designed to enhance operational security by rotating IP addresses using the Tor network. It supports both Windows and Linux operating systems and automates the process of starting and stopping Tor to manage IP address rotation. This tool helps users maintain anonymity by masking their IP addresses while using the internet.

**Key Features:**

- **Cross-Platform Compatibility:** Works on both Windows and Linux systems.
- **Tor Integration:** Utilizes Tor relays as proxies to obscure the user's IP address.
- **IP Rotation:** Automatically rotates IP addresses at a user-defined interval to enhance privacy.
- **Real-time IP Monitoring:** Displays the current IP address before and after rotation to confirm changes.

**How It Works:**

1. **Initialization:**
   - Displays a welcome message and instructions for setting up your browser to use the Tor SOCKS5 proxy (IP: 127.0.0.1, PORT: 9050).
   - Checks for Tor's version and displays it.

2. **IP Address Display:**
   - Retrieves and prints the current IP address using the `https://api.myip.com` API.

3. **IP Rotation Loop:**
   - Continuously rotates the IP address based on the specified delay (default: 30 seconds) while keeping Tor running in the background.
   - If IP rotation is enabled, the script stops and restarts Tor to obtain a new IP address.

4. **Exception Handling:**
   - Handles network connection errors and JSON parsing issues.
   - Ensures that Tor is properly closed if the script encounters an error or is interrupted by the user.

Created by AK
