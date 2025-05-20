# ICMP_Timestamp_Scanner
A Python utility for scanning multiple IP addresses with ICMP timestamp requests using hping3.

## Overview

This tool automates the process of sending ICMP timestamp requests to a list of IP addresses and extracting the timestamp information from the responses. It uses the `hping3` utility to perform the scans and provides both the complete output and the extracted timestamp information.

## Features

- Reads IP addresses from a text file
- Sends ICMP timestamp requests to each IP
- Displays complete hping3 output
- Extracts and highlights timestamp information
- Handles errors gracefully
- Provides timestamps for scan operations

## Requirements

- Python 3.6+
- hping3 installed on the system
- Root/sudo privileges (required for sending ICMP packets)

## Installation

1. Ensure hping3 is installed:

```
#On Debian/Ubuntu
sudo apt-get install hping3

#On CentOS/RHEL
sudo yum install hping3
```

2. Clone or download this script to your system

## Usage

1. Create a text file with target IP addresses, one per line:

```
192.168.1.1
10.0.0.1
8.8.8.8
```

2. Run the script with sudo:

```
sudo python3 icmp_ts_scanner.py ip_list.txt
```

3. Review the output for each IP address

```
Output Example

[+] Loaded 3 IP addresses from ip_list.txt

[+] Scanning 192.168.1.1 at 2025-05-20 08:45:23 PM

--- Complete hping3 Output ---
using eth0, addr: 192.168.0.100, MTU: 1500
HPING 192.168.1.1 (eth0 192.168.1.1): icmp mode set, 28 headers + 0 data bytes
len=40 ip=192.168.1.1 ttl=64 id=30750 tos=0 iplen=40
icmp_seq=0 rtt=2.3 ms
ICMP timestamp: Originate=74431552 Receive=74467670 Transmit=74467670
ICMP timestamp RTT tsrtt=64

len=40 ip=192.168.1.1 ttl=64 id=30751 tos=0 iplen=40
icmp_seq=1 rtt=1.8 ms
ICMP timestamp: Originate=74432552 Receive=74468670 Transmit=74468670
ICMP timestamp RTT tsrtt=64

--- Extracted TIMESTAMP Information ---
ICMP timestamp: Originate=74431552 Receive=74467670 Transmit=74467670
ICMP timestamp: Originate=74432552 Receive=74468670 Transmit=74468670
```

# Ethical Usage

This tool is intended for:

1. Security professionals conducting authorized penetration tests
2. Website owners testing their own sites for vulnerabilities
3. Educational purposes to understand clickjacking protections

Always obtain proper authorization before testing any website you don't own

# License
MIT License

# Contributing
Contributions are welcome! Please feel free to submit a Pull Request
