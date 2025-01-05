def monitor_logs(log_file):
    print(f"Monitoring logs from {log_file}...")
    os.system(f"tail -f {log_file}")

# Log Monitoring
monitor_logs("/var/log/syslog")

