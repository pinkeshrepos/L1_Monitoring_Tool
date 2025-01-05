def network_connections():
    print("Active Network Connections:")
    os.system("ss -tuln")

# Network Connections Monitoring
network_connections()

