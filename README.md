# Malicious Python Packages Targeting Sensitive Data

![Malware](https://web.archive.org/web/20231005010037if_/https://www.bleepstatic.com/content/hl-images/2023/10/04/Python-packages.jpg)

## Overview

Hundreds of malicious Python packages have been discovered, capable of stealing sensitive data once launched. These packages have been found to target a wide range of information on infected systems, including:

- Antivirus tools running on the device.
- Tasks list, Wi-Fi passwords, and system information.
- Credentials, browsing history, cookies, and payment information stored on web browsers.
- Data stored in cryptocurrency wallet apps like Atomic and Exodus.
- Discord badges, phone numbers, email addresses, and nitro status.
- Minecraft and Roblox user data.

Additionally, the malware can take screenshots and steal individual files from the compromised system, including data from the Desktop, Pictures, Documents, Music, Videos, and Downloads directories.

## Clipboard Monitoring

One particularly insidious feature of this malware is its constant monitoring of the victim's clipboard. It actively looks for cryptocurrency addresses and, when found, swaps them with the attacker's address. This malicious tactic is used to divert payments to wallets under the attacker's control.

## Checking for Vulnerable Packages

To check if any of the listed packages are installed on your system, you can use the provided Python script. Follow these steps:

1. Download the script [here](check_vulnerable_packages.py).

2. Run the script using Python:

   ```bash
   python vuln_check.py
*Disclaimer: This document provides information on a cybersecurity issue. It is essential to follow best security practices and keep your systems and data secure.*
