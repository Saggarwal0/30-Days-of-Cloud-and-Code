# Day 2 (Loop): Log CPU, RAM, and Disk every few seconds

import psutil
from datetime import datetime
import csv
import time
from pathlib import Path

# where to save the CSV (same folder as this script)
file_path = Path(__file__).parent / "metrics.csv"

# how often to record (seconds) and how many times
interval_seconds = 5     # change this if you want (e.g., 2, 10, etc.)
num_samples = 30         # how many rows to write

# create the CSV with header if it doesn't exist yet
if not file_path.exists():
    with open(file_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["timestamp", "cpu_percent", "ram_percent", "disk_percent"])

print("Logging to:", file_path)
print(f"Interval: {interval_seconds}s, Samples: {num_samples}")

try:
    for i in range(num_samples):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # take a sample
        cpu = psutil.cpu_percent(interval=1)            # 1-second avg CPU
        ram = psutil.virtual_memory().percent
        # root path: "/" works for most systems, including Windows (maps to the current drive)
        disk = psutil.disk_usage("/").percent

        # append to CSV
        with open(file_path, "a", newline="") as f:
            w = csv.writer(f)
            w.writerow([timestamp, cpu, ram, disk])

        print(f"[{i + 1}/{num_samples}] Saved at {timestamp}  CPU={cpu}%  RAM={ram}%  Disk={disk}%")

        # wait until the next sample (minus the 1s already spent in cpu_percent)
        time.sleep(max(0, interval_seconds - 1))

    print("Done logging.")

except KeyboardInterrupt:
    print("\nStopped by user. Partial data saved.")
