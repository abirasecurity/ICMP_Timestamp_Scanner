#!/usr/bin/env python3

import subprocess
import sys
import os
from datetime import datetime

# ANSI color codes matching the image
class Colors:
    PURPLE = '\033[95m'      # Purple for headers
    CYAN = '\033[96m'        # Cyan for IP addresses
    ORANGE = '\033[38;5;208m'  # Orange for warning messages
    GREEN = '\033[92m'       # Green for NOT VULNERABLE
    RED = '\033[91m'         # Red for VULNERABLE (if needed)
    BLUE = '\033[94m'        # Blue for scanning messages
    WHITE = '\033[97m'       # White for normal output
    GRAY = '\033[90m'        # Gray for less important output
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def run_hping3(ip):
    """Run hping3 command on the specified IP and return the output."""
    print(f"\n{Colors.BLUE}[+] Scanning {Colors.CYAN}{ip}{Colors.END} at {Colors.BLUE}{datetime.now().strftime('%Y-%m-%d %I:%M:%S %p')}{Colors.END}")

    try:
        # Run hping3 with ICMP timestamp request
        cmd = ["sudo", "hping3", "--icmp", "--icmp-ts", "-V", "-c", "2", ip]
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate()

        # Return the output regardless of return code
        # We'll handle packet loss in the main function
        return stdout, stderr, process.returncode

    except Exception as e:
        print(f"{Colors.RED}[-] Exception while scanning {ip}: {str(e)}{Colors.END}")
        return None, str(e), -1

def main():
    # Check if running as root
    if os.geteuid() != 0:
        print(f"{Colors.ORANGE}[-] Warning: This script requires root privileges to run hping3{Colors.END}")
        print(f"{Colors.ORANGE}    Consider running with sudo{Colors.END}")

    # Check if input file is provided
    if len(sys.argv) != 2:
        print(f"{Colors.ORANGE}Usage: sudo python3 icmp_ts_scanner.py <ip_list_file>{Colors.END}")
        sys.exit(1)

    ip_file = sys.argv[1]

    # Check if file exists
    if not os.path.isfile(ip_file):
        print(f"{Colors.RED}[-] Error: File '{ip_file}' not found{Colors.END}")
        sys.exit(1)

    # Read IPs from file
    try:
        with open(ip_file, 'r') as f:
            ips = [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"{Colors.RED}[-] Error reading IP file: {str(e)}{Colors.END}")
        sys.exit(1)

    if not ips:
        print(f"{Colors.RED}[-] No valid IPs found in the input file{Colors.END}")
        sys.exit(1)

    print(f"{Colors.BLUE}[+] Loaded {len(ips)} IP addresses from {ip_file}{Colors.END}")

    # Process each IP
    for ip in ips:
        stdout, stderr, return_code = run_hping3(ip)

        # Print the complete original output
        print(f"\n{Colors.PURPLE}--- Complete hping3 Output ---{Colors.END}")
        if stdout:
            print(f"{Colors.WHITE}{stdout}{Colors.END}")
        if stderr:
            print(f"{Colors.WHITE}{stderr}{Colors.END}")

        # Add a separator line
        print(f"{Colors.PURPLE}{'—' * 20}{Colors.END}")

        # Extract and highlight timestamp information
        print(f"\n{Colors.PURPLE}--- Extracted TIMESTAMP Information ---{Colors.END}")

        timestamp_found = False
        if stdout:
            for line in stdout.splitlines():
                # Only include lines with "ICMP timestamp:" and exclude RTT lines
                if "ICMP timestamp:" in line and "ICMP timestamp RTT" not in line:
                    print(f"{Colors.WHITE}{line.strip()}{Colors.END}")
                    timestamp_found = True

        # Check for packet loss or no response
        packet_loss = False
        if stdout and "100% packet loss" in stdout:
            packet_loss = True
            print(f"{Colors.ORANGE}No ICMP timestamp information found in the response{Colors.END}")

        # Determine vulnerability status
        if timestamp_found:
            print(f"\n{Colors.CYAN}{ip}{Colors.END} - {Colors.RED}VULNERABLE{Colors.END}")
        else:
            print(f"\n{Colors.CYAN}{ip}{Colors.END} - {Colors.GREEN}NOT VULNERABLE{Colors.END}")

        print(f"{Colors.PURPLE}{'_' * 20}{Colors.END}")

if __name__ == "__main__":
    main()
