import socket
import json
import time
import random

UDP_IP = "127.0.0.1"  
UDP_PORT = 5005       

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

hosts = ["web-server", "db-server", "app-server"]
events = ["login_success", "login_fail", "file_access", "config_change"]

print("[INFO] Log source running... sending logs every 2 seconds")

while True:
    log_entry = {
        "host": random.choice(hosts),
        "event": random.choice(events),
        "severity": random.choice(["INFO", "WARN", "ERROR"]),
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    message = json.dumps(log_entry).encode()
    sock.sendto(message, (UDP_IP, UDP_PORT))
    print(f"[SENT] {log_entry}")
    time.sleep(2)
