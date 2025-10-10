import time
import psutil
import csv
from datetime import datetime

CSV_FILE = "C:\\Users\\sim00\\Downloads\\30_Day_Code_Challenge\\Day04\\metrics.csv"

def log_metrics():
    """Collect and save system metrics to CSV"""
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # append to csv
    with open(CSV_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, cpu, ram, disk])
        print(f"Logged at {timestamp}: CPU {cpu}% RAM {ram}% DISK {disk}%")

def main():
    print("Starting system metrics logger (every 5 minutes)...")
    print("Press Ctrl+C to stop.\n")

    # create header if new file
    try:
        with open(CSV_FILE, "x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["timestamp", "cpu_percent", "ram_percent", "disk_percent"])
    except FileExistsError:
        pass  # file already exists

    # repeat logging every 300 seconds (5 min)
    while True:
        log_metrics()
        time.sleep(300)  # 300 seconds = 5 minutes

if __name__ == "__main__":
    main()
