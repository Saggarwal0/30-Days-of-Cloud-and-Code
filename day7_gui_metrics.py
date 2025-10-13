# Day 7 – Mini GUI for Live Metrics
# Simple Tkinter window showing CPU, RAM, and Disk in real time

import tkinter as tk
from tkinter import ttk
import psutil
from datetime import datetime
import csv

CSV_FILE = "metrics.csv"

def write_row(ts, cpu, ram, disk):
    with open(CSV_FILE, "a", newline="") as f:
        w = csv.writer(f)
        if f.tell() == 0:
            w.writerow(["timestamp", "cpu_percent", "ram_percent", "disk_percent"])
        w.writerow([ts, cpu, ram, disk])

class MetricsApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("System Metrics Monitor")
        self.geometry("380x220")
        self.resizable(False, False)

        # label variables
        self.timestamp = tk.StringVar(value="Timestamp: --")
        self.cpu_label = tk.StringVar(value="CPU: -- %")
        self.ram_label = tk.StringVar(value="RAM: -- %")
        self.disk_label = tk.StringVar(value="DISK: -- %")

        # layout
        tk.Label(self, textvariable=self.timestamp, font=("Segoe UI", 9)).pack(pady=5)

        self.pb_cpu = ttk.Progressbar(self, maximum=100, length=300)
        self.pb_ram = ttk.Progressbar(self, maximum=100, length=300)
        self.pb_disk = ttk.Progressbar(self, maximum=100, length=300)
        for pb in [self.pb_cpu, self.pb_ram, self.pb_disk]:
            pb.pack(pady=5)

        tk.Label(self, textvariable=self.cpu_label).pack()
        tk.Label(self, textvariable=self.ram_label).pack()
        tk.Label(self, textvariable=self.disk_label).pack()

        self.log_enabled = tk.BooleanVar(value=False)
        ttk.Checkbutton(self, text="Log to CSV", variable=self.log_enabled).pack(pady=6)

        self.running = True
        self.update_metrics()

    def update_metrics(self):
        cpu = psutil.cpu_percent(interval=0.2)
        ram = psutil.virtual_memory().percent
        disk = psutil.disk_usage("/").percent
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.timestamp.set(f"Timestamp: {ts}")
        self.cpu_label.set(f"CPU: {cpu:.1f}%")
        self.ram_label.set(f"RAM: {ram:.1f}%")
        self.disk_label.set(f"DISK: {disk:.1f}%")

        self.pb_cpu["value"] = cpu
        self.pb_ram["value"] = ram
        self.pb_disk["value"] = disk

        if self.log_enabled.get():
            write_row(ts, cpu, ram, disk)

        if self.running:
            self.after(1000, self.update_metrics)  # every second

if __name__ == "__main__":
    app = MetricsApp()
    app.mainloop()
