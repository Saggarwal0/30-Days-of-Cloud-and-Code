# Day 5 - Run the system logger automatically
import time
import day5_system_logger  # imports your logging file

def main():
    print("Logging system data every 10 seconds (change to 900 for 15 minutes).")
    print("Press Ctrl + C to stop.\n")
    while True:
        day5_system_logger.save_to_csv()
        time.sleep(10)  # change to 900 (15 min) when you're ready

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nStopped logging.")
