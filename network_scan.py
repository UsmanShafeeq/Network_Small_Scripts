import os
import platform
import subprocess

# Function to ping a single IP address
def ping_ip(ip):
    """
    Pings the given IP address and returns True if the host is reachable, otherwise False.
    
    Args:
    ip (str): The IP address to ping.

    Returns:
    bool: True if the IP is reachable, False otherwise.
    """
    # Determine the appropriate parameter for the ping command based on the OS
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    
    # Construct the ping command
    command = ['ping', param, '4', ip]
    
    # Execute the command and return True if the ping was successful
    return subprocess.call(command) == 0

# Function to ping a list of IP addresses
def ping_ips(ip_list):
    """
    Pings each IP address in the provided list and prints the reachability status.
    
    Args:
    ip_list (list): A list of IP addresses to ping.
    """
    print("Starting network reachability check...")
    for ip in ip_list:
        if ping_ip(ip):
            print(f"✅ {ip} is reachable.")
        else:
            print(f"❌ {ip} is not reachable.")

# List of IP addresses to ping
ip_list = [
    '8.8.8.8',    # Google Public DNS
    '10.11.60.1', # Example internal IP address
    '192.168.1.1',# Typical router IP address
]

# Perform the ping test
ping_ips(ip_list)
