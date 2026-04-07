import csv
from collections import defaultdict

log_file = "logs/sample_logs.csv"

failed_login_counts = defaultdict(int)

# Logları oku
with open(log_file, mode="r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        ip = row["ip"]
        action = row["action"]

        if action == "FAILED_LOGIN":
            failed_login_counts[ip] += 1

print("\n--- TÜM SAYIMLAR (DEBUG) ---")
for ip, count in failed_login_counts.items():
    print(f"{ip} -> {count}")

print("\n--- ALERTS ---")

# Alert kuralı (düşük tuttuk garanti çalışsın)
for ip, count in failed_login_counts.items():
    if count > 5:
        print(f"ALERT: {ip} has {count} failed login attempts!")

print("\n--- ŞÜPHELİ IP ---")

for ip in failed_login_counts:
    if not ip.startswith("192.168"):
        print(f"Suspicious IP detected: {ip}")