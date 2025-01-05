import os
import logging
import subprocess
import psutil
import time

# Setup logging configuration
logging.basicConfig(filename='logs/monitoring.log', level=logging.INFO, 
                    format='%(asctime)s - %(message)s')

# Function to check ping
def ping_check(host):
    logging.info(f"Checking ping for {host}...")
    response = os.system(f"ping -c 3 {host}")
    if response == 0:
        logging.info(f"{host} is reachable")
    else:
        logging.info(f"{host} is not reachable")

# Function to check disk usage
def check_disk_usage():
    logging.info("Checking disk usage...")
    disk = psutil.disk_usage('/')
    logging.info(f"Disk usage: {disk.percent}%")

# Function to check CPU usage
def check_cpu_usage():
    logging.info("Checking CPU usage...")
    cpu = psutil.cpu_percent(interval=1)
    logging.info(f"CPU usage: {cpu}%")

# Function to check memory usage
def check_memory_usage():
    logging.info("Checking memory usage...")
    memory = psutil.virtual_memory()
    logging.info(f"Memory usage: {memory.percent}%")

# Function to check active network connections
def check_network_connections():
    logging.info("Checking active network connections...")
    result = subprocess.run(['ss', '-tuln'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    logging.info(f"Active network connections:\n{result.stdout.decode()}")

# Function to check service status
def check_service(service_name):
    logging.info(f"Checking {service_name} service status...")
    result = subprocess.run(['systemctl', 'is-active', service_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    status = result.stdout.decode().strip()
    
    if status == "active":
        logging.info(f"{service_name} is running")
    else:
        logging.info(f"{service_name} is not running. Attempting to restart...")
        restart_service(service_name)

# Function to restart a service
def restart_service(service_name):
    logging.info(f"Attempting to restart {service_name}...")
    result = subprocess.run(['sudo', 'systemctl', 'restart', service_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode == 0:
        logging.info(f"{service_name} restarted successfully")
    else:
        logging.error(f"Failed to restart {service_name}: {result.stderr.decode()}")

# Dashboard function to show system health
def dashboard():
    logging.info("Starting system monitoring dashboard...")
    
    # Monitoring loop (running every 10 seconds)
    while True:
        # Check system metrics and services
        ping_check('8.8.8.8')  # Check Google DNS
        check_disk_usage()
        check_cpu_usage()
        check_memory_usage()
        check_network_connections()
        check_service('nginx')  # Example: Replace with your service name like 'mysql' or 'httpd'
        check_service('mysql')
        
        logging.info("Sleeping for 10 seconds before the next round of checks...")
        time.sleep(10)  # Wait for 10 seconds before repeating

# Run the monitoring dashboard
if __name__ == "__main__":
    dashboard()

