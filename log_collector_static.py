import random
import time
import csv
from datetime import datetime
import os

# logs klasörü yoksa oluştur
os.makedirs("logs", exist_ok=True)

log_file = "logs/sample_logs.csv"

ips = ["192.168.1.10", "192.168.1.20", "10.0.0.5"]

# FAILED_LOGIN daha fazla olsun (özellikle saldırı simülasyonu)
actions = ["ALLOW", "DENY", "FAILED_LOGIN", "FAILED_LOGIN", "FAILED_LOGIN"]

print("Log üretimi başladı...")

# CSV başlık
with open(log_file, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["timestamp", "ip", "action"])

# 100 log üret (daha fazla veri)
for _ in range(100):
    ip = random.choice(ips)
    action = random.choice(actions)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(log_file, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, ip, action])

    print(f"{timestamp} {ip} {action}")
    time.sleep(0.05)

print("Log üretimi tamamlandı!")