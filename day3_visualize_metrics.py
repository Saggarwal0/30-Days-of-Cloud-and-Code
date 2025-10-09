# Day 3: Visualizing my CPU, RAM, and Disk usage from Day 2

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# --- find the CSV file automatically ---
base_path = Path(__file__).parent.parent
csv_locations = [
    base_path / "Day02" / "metrics.csv",          # normal folder
    base_path / "Day02" / "Day02" / "metrics.csv" # nested folder (if it exists)
]

csv_file = None
for path in csv_locations:
    if path.exists():
        csv_file = path
        break

if csv_file is None:
    print("Could not find metrics.csv. Make sure you ran Day 2 first.")
    exit()

print("Using CSV file:", csv_file)

# --- read the CSV data ---
data = pd.read_csv(csv_file)
print("Columns in CSV:", list(data.columns))
print(data.head())

# --- clean the timestamp column ---
# Force pandas to treat the timestamp as full date + time
if "timestamp" in data.columns:
    data["timestamp"] = pd.to_datetime(
        data["timestamp"],
        format="%Y-%m-%d %H:%M:%S",
        errors="coerce"  # convert bad rows to NaT instead of crashing
    )
    # Drop any rows that failed to convert
    data = data.dropna(subset=["timestamp"])
else:
    print("CSV file missing 'timestamp' column!")
    exit()

# --- make the chart ---
plt.figure(figsize=(10, 6))

if "cpu_percent" in data.columns:
    plt.plot(data["timestamp"], data["cpu_percent"], color="red", label="CPU")
if "ram_percent" in data.columns:
    plt.plot(data["timestamp"], data["ram_percent"], color="blue", label="RAM")
if "disk_percent" in data.columns:
    plt.plot(data["timestamp"], data["disk_percent"], color="green", label="Disk")

plt.title("System Usage Over Time")
plt.xlabel("Time")
plt.ylabel("Percent Used")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)

# Save and show the chart
plt.tight_layout()
plt.savefig("metrics_chart.png", bbox_inches="tight")
plt.show()

print("Chart saved as metrics_chart.png")
