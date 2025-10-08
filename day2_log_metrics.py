"""
Day 2: Log CPU/RAM/Disk to a CSV file (metrics.csv)
-Appends one row per ruin: timestamp,cpu.ram,disk
-Builds on Day 1 (dashboard) and sets up data for charts/alerts
"""

from datetime import datetime
from pathlib import Path
import csv
import psutil # pip install psutil

#Resolve repo root so metrics.cvs lives at the top Level (not inside Day02/)
REPO_ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = REPO_ROOT / "metrics.csv"

def system_root_path() -> Path:
    """
    Cross-platform disk root for psutil.disk_usage()
    On Windows, Path.home().anchor returns e.g. 'C:\\'
    On Linux/macOS,'/ is fine
    """
    anchor = Path.home().anchor #'' on *nix,'C:\\' on Windows
    return Path(anchor) if anchor else Path("/")

def sample_metrics() -> tuple[str, float,float]:
    """Collect a single snapshot of system metrics."""
    now = datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage(str(system_root_path())).percent
    return now, cpu, ram, disk

def write_row(csv_path: Path, row:tuple[str, float,float,float]) -> None:
    """Append a row; create header if file doesn't exist yet"""
    new_file = not csv_path.exists()
    with csv_path.open("a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if new_file:
            w.writerow(["timestamp", "cpu_percent","disk_percent"])
        w.writerow(row)
def main():
    row = sample_metrics()
    write_row(CSV_PATH,row)
    print(f"Logged: {row} -> {CSV_PATH}")

if __name__ == "__main__":
    main()