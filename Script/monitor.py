import shutil
from datetime import datetime

log_file = "server_monitor.log"

# Get disk usage
disk = shutil.disk_usage("/")
disk_percent = round((disk.used / disk.total) * 100, 2)

# Get current time
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Write results
with open(log_file, "a") as file:
    file.write(f"Date and Time: {current_time}\n")
    file.write(f"Disk Usage: {disk_percent}%\n")
    file.write("-" * 40 + "\n")

print("Monitoring information saved successfully.")
