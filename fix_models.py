import urllib.request
import os

print("Téléchargement du bon fichier face_recognition_model-shard1...")

# URLs alternatives à essayer dans l'ordre
urls = [
    "https://github.com/justadudewhohacks/face-api.js/releases/download/0.22.2/face_recognition_model-shard1",
    "https://raw.githubusercontent.com/justadudewhohacks/face-api.js/0.22.2/weights/face_recognition_model-shard1",
    "https://github.com/justadudewhohacks/face-api.js/raw/0.22.2/weights/face_recognition_model-shard1",
]

dest = "static/models/face_recognition_model-shard1"
os.makedirs("static/models", exist_ok=True)

success = False
for i, url in enumerate(urls, 1):
    print(f"\nTentative {i} : {url[:60]}...")
    try:
        urllib.request.urlretrieve(url, dest)
        size = os.path.getsize(dest)
        print(f"Taille : {size:,} bytes")
        if size > 5_000_000:
            print(f"✓ Fichier correct ({size:,} bytes)")
            success = True
            break
        else:
            print(f"✗ Trop petit ({size:,} bytes) — essai suivant")
    except Exception as e:
        print(f"✗ Erreur : {e}")

if not success:
    print("\n→ Toutes les URLs ont échoué. Utilise la méthode manuelle ci-dessous.")
else:
    print("\n✓ Terminé ! Relance uvicorn et teste la reconnaissance faciale.")