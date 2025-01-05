def check_service(service):
    print(f"Checking {service} service...")
    response = os.system(f"systemctl is-active --quiet {service}")
    if response == 0:
        print(f"{service} is running")
    else:
        print(f"{service} is not running. Attempting to restart...")
        os.system(f"sudo systemctl restart {service}")

# Service Monitoring
check_service("nginx")
check_service("mysql")

