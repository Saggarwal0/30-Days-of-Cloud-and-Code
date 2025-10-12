import pandas as pd
import matplotlib.pyplot as plt

def load_data(filename):
    try:
        data = pd.read_csv(filename)
        return data
    except FileNotFoundError:
        print("File not found. Make sure metrics.csv exists.")
        exit()

def calculate_averages(data):
    avg_cpu = data["cpu_percent"].mean()
    avg_ram = data["ram_percent"].mean()
    avg_disk = data["disk_percent"].mean()
    print(f"Average CPU Usage:  {avg_cpu:.2f}%")
    print(f"Average RAM Usage:  {avg_ram:.2f}%")
    print(f"Average Disk Usage: {avg_disk:.2f}%")

def plot_data(data):
    plt.figure(figsize=(10,5))
    plt.plot(data["timestamp"], data["cpu_percent"], label="CPU", marker="o")
    plt.plot(data["timestamp"], data["ram_percent"], label="RAM", marker="o")
    plt.plot(data["timestamp"], data["disk_percent"], label="DISK", marker="o")
    plt.xlabel("Timestamp")
    plt.ylabel("Usage (%)")
    plt.title("System Usage Over Time")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    filename = "metrics.csv"
    data = load_data(filename)
    calculate_averages(data)
    plot_data(data)

if __name__ == "__main__":
    main()
