import os
import time

def cpu_usage():
    print("CPU Usage:")
    os.system("top -bn1 | grep 'Cpu(s)'")

def memory_usage():
    print("Memory Usage:")
    os.system("free -h")

def disk_usage():
    print("Disk Usage:")
    os.system("df -h")

def main():
    while True:
        cpu_usage()
        memory_usage()
        disk_usage()
        print("-" * 40)
        time.sleep(5)  # Wait for 5 seconds before checking again

if __name__ == "__main__":
    main()

