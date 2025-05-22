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
# Sample Output for a Vulnerable Host:

[+] Scanning 192.168.1.10 at 2025-05-22 07:30:45 PM

--- Complete hping3 Output ---
using eth0, addr: 192.168.1.5, MTU: 1500
HPING 192.168.1.10 (eth0 192.168.1.10): icmp mode set, 28 headers + 0 data bytes
len=46 ip=192.168.1.10 ttl=64 id=6924 icmp_seq=0 rtt=2.3 ms
ICMP timestamp: Originate=0 Receive=3845283574 Transmit=3845283574
len=46 ip=192.168.1.10 ttl=64 id=6925 icmp_seq=1 rtt=1.8 ms
ICMP timestamp: Originate=0 Receive=3845283575 Transmit=3845283575

--- 192.168.1.10 hping statistic ---
2 packets transmitted, 2 packets received, 0% packet loss
round-trip min/avg/max = 1.8/2.1/2.3 ms
————————————————

--- Extracted TIMESTAMP Information ---
ICMP timestamp: Originate=0 Receive=3845283574 Transmit=3845283574
ICMP timestamp: Originate=0 Receive=3845283575 Transmit=3845283575

192.168.1.10 - VULNERABLE
____________________

# Sample Output for a Not Vulnerable Host (No Response):

[+] Scanning 34.44.181.215 at 2025-05-22 07:32:18 PM

--- Complete hping3 Output ---
using eth0, addr: 192.168.1.5, MTU: 1500
HPING 34.44.181.215 (eth0 34.44.181.215): icmp mode set, 28 headers + 0 data bytes

--- 34.44.181.215 hping statistic ---
2 packets transmitted, 0 packets received, 100% packet loss
round-trip min/avg/max = 0.0/0.0/0.0 ms
————————————————

--- Extracted TIMESTAMP Information ---
No ICMP timestamp information found in the response

34.44.181.215 - NOT VULNERABLE
____________________

#Sample Output for a Not Vulnerable Host (Responds but No Timestamp):
[+] Scanning 8.8.8.8 at 2025-05-22 07:33:42 PM

--- Complete hping3 Output ---
using eth0, addr: 192.168.1.5, MTU: 1500
HPING 8.8.8.8 (eth0 8.8.8.8): icmp mode set, 28 headers + 0 data bytes
len=28 ip=8.8.8.8 ttl=56 id=40894 icmp_seq=0 rtt=28.6 ms
len=28 ip=8.8.8.8 ttl=56 id=40895 icmp_seq=1 rtt=27.9 ms

--- 8.8.8.8 hping statistic ---
2 packets transmitted, 2 packets received, 0% packet loss
round-trip min/avg/max = 27.9/28.3/28.6 ms
————————————————

--- Extracted TIMESTAMP Information ---
No ICMP timestamp information found in the response

8.8.8.8 - NOT VULNERABLE
____________________
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
