import random
import time
import csv
from datetime import datetime
import os

os.makedirs("logs", exist_ok=True)
log_file = "logs/sample_logs.csv"

ips = ["192.168.1.10", "192.168.1.20", "10.0.0.5"]
actions = ["ALLOW", "DENY", "FAILED_LOGIN", "FAILED_LOGIN", "FAILED_LOGIN"]

# Eğer dosya yoksa başlık ekle
if not os.path.exists(log_file):
    with open(log_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["timestamp", "ip", "action"])

print("Sürekli log üretimi başladı... (CTRL+C ile durdur)")

while True:
    ip = random.choice(ips)
    action = random.choice(actions)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(log_file, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, ip, action])

    print(f"{timestamp} {ip} {action}")
    time.sleep(1)  # Her 1 saniye log üret