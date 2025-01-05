import os
import subprocess
import time

def ping_check(host):
    response = os.system(f"ping -c 3 {host}")
    if response == 0:
        print(f"{host} is reachable")
    else:
        print(f"{host} is not reachable")

def traceroute(host):
    print(f"Traceroute to {host}:")
    os.system(f"traceroute {host}")

def dns_check(domain):
    print(f"DNS resolution for {domain}:")
    os.system(f"dig {domain}")

# Network Monitoring
ping_check("8.8.8.8")
traceroute("8.8.8.8")
dns_check("google.com")

