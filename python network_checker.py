import os
import platform
import subprocess

# Function to ping an IP address
def ping_ip(ip):
    # Determine the ping command parameter based on the OS
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    # Build the ping command
    command = ['ping', param, '1', ip]
    # Run the command and check the result
    return subprocess.call(command, stdout=subprocess.DEVNULL) == 0

# Function to ping a list of IP addresses and report their reachability
def check_network(ip_list):
    for ip in ip_list:
        if ping_ip(ip):
            print(f"[+] {ip} is reachable.")
        else:
            print(f"[-] {ip} is not reachable.")

# List of IP addresses to check
ip_list = [
    '8.8.8.8',    # Google DNS
    '192.168.1.1', # Local Router
    '10.0.0.1',   # Example IP
]

# Run the network check
if __name__ == "__main__":
    print("Checking network reachability...\n")
    check_network(ip_list)
    print("\nNetwork check complete.")
