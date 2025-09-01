import socket
import json

UDP_IP = "127.0.0.1"  
UDP_PORT = 5005       

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print(f"[INFO] Collector running on {UDP_IP}:{UDP_PORT}...\nWaiting for logs...")

while True:
    data, addr = sock.recvfrom(1024) 
    try:
        log = json.loads(data.decode())
        print(f"[LOG] From {addr}: {log}")
    except json.JSONDecodeError:
        print(f"[ERROR] Received malformed data from {addr}")
