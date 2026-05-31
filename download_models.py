import urllib.request
import os

files = {
    "https://raw.githubusercontent.com/WebDevSimplified/Face-Recognition-JavaScript/master/models/tiny_face_detector_model-weights_manifest.json":
        "static/models/tiny_face_detector_model-weights_manifest.json",
    "https://raw.githubusercontent.com/WebDevSimplified/Face-Recognition-JavaScript/master/models/tiny_face_detector_model-shard1":
        "static/models/tiny_face_detector_model-shard1",
    "https://raw.githubusercontent.com/WebDevSimplified/Face-Recognition-JavaScript/master/models/face_landmark_68_model-weights_manifest.json":
        "static/models/face_landmark_68_model-weights_manifest.json",
    "https://raw.githubusercontent.com/WebDevSimplified/Face-Recognition-JavaScript/master/models/face_landmark_68_model-shard1":
        "static/models/face_landmark_68_model-shard1",
    "https://raw.githubusercontent.com/WebDevSimplified/Face-Recognition-JavaScript/master/models/face_recognition_model-weights_manifest.json":
        "static/models/face_recognition_model-weights_manifest.json",
    "https://raw.githubusercontent.com/WebDevSimplified/Face-Recognition-JavaScript/master/models/face_recognition_model-shard1":
        "static/models/face_recognition_model-shard1",
}

os.makedirs("static/models", exist_ok=True)

for url, dest in files.items():
    fname = os.path.basename(dest)
    print(f"→ {fname} ...", end=" ", flush=True)
    try:
        urllib.request.urlretrieve(url, dest)
        size = os.path.getsize(dest)
        print(f"OK ({size:,} bytes)")
    except Exception as e:
        print(f"ERREUR : {e}")

print("\nVérification finale :")
for dest in files.values():
    size = os.path.getsize(dest)
    print(f"  {os.path.basename(dest)}: {size:,} bytes")