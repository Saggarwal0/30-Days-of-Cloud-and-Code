# Day 5 - System Logger (Beginner Version)
import psutil
import csv
from datetime import datetime

# Get system data
def get_metrics():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return time_now, cpu, ram, disk

# Save the data to a CSV file
def save_to_csv():
    time_now, cpu, ram, disk = get_metrics()
    file = open("metrics.csv", "a", newline="")
    writer = csv.writer(file)

    # If file is empty, add headers
    if file.tell() == 0:
        writer.writerow(["timestamp", "cpu_percent", "ram_percent", "disk_percent"])

    writer.writerow([time_now, cpu, ram, disk])
    print("Saved at", time_now, "| CPU:", cpu, "RAM:", ram, "DISK:", disk)
    file.close()

# Run one write if the file is run directly
if __name__ == "__main__":
    print("Running one log write from day5_system_logger.py ...")
    save_to_csv()
