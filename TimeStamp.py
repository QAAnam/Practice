import time
import subprocess

# Run the other Python file
subprocess.call(["python", "Practice/file path acces.py"])

timestamp = int(time.time())

print(timestamp)
from datetime import datetime

timestamp = int(datetime.timestamp(datetime.now()))

print(timestamp)
dt = datetime.fromtimestamp(timestamp)
print(dt.strftime("%Y-%m-%d %H:%M:%S"))
