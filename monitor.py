import sys
import psutil
import time

def log_broker_usage(pid, interval=1):
    with open("broker_usage.log", "a") as log_file:
        while True:
            try:
                process = psutil.Process(pid)
                cpu_usage = process.cpu_percent(interval=interval)
                memory_usage = process.memory_info().rss 
                log_file.write(f"CPU: {cpu_usage}%, Memory: {memory_usage} Bytes\n")
                log_file.flush()
                print(f"CPU: {cpu_usage}%, Memory: {memory_usage} Bytes")
                time.sleep(interval)
            except psutil.NoSuchProcess:
                print(f"No process with PID {pid} found.")
                break

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 monitor.py <PID>")
        sys.exit(1)

    broker_pid = int(sys.argv[1])
    interval = 0.5
    log_broker_usage(broker_pid, interval)
