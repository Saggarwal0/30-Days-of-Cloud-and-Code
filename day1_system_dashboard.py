# day1_system_dashboard.py
# A simple system monitor script for Day 1 of 30 Days of Cloud & Code
# Author: Simran Aggarwal

# 1 Import required libraries

import psutil           # Gives access to system performance metrics
from datetime import datetime   # To display current date and time

# 2️ Define the dashboard function

def show_dashboard():
    # Collect system statistics using psutil
    cpu_usage = psutil.cpu_percent(interval=1)        # % CPU usage after 1s sample
    memory = psutil.virtual_memory().percent          # % RAM usage
    disk = psutil.disk_usage('/').percent             # % Disk usage of main drive
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Display results in a clean formatted way
    print("\n☁️  Simran's Cloud Monitor  ☁️")
    print("-----------------------------------")
    print(f" Time: {current_time}")
    print(f" CPU Usage: {cpu_usage}%")
    print(f" RAM Usage: {memory}%")
    print(f" Disk Usage: {disk}%")
    print("-----------------------------------")
    
# 3️ Run the dashboard once

if __name__ == "__main__":


    show_dashboard()
