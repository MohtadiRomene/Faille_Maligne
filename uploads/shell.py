import os
import socket

print("=== EXPLOITATION RÉUSSIE ===")
print(f"Hostname: {socket.gethostname()}")
print(f"User: {os.getenv('USER', 'unknown')}")
print(f"Working Directory: {os.getcwd()}")
print(f"\nFichiers disponibles:")
for file in os.listdir('.'):
    print(f"  - {file}")
    
print(f"\nVariables d'environnement:")
for key, value in os.environ.items():
    print(f"  {key}: {value}")
