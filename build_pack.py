import hashlib
import json
import os
import zipfile

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "resourcepack")
BUILD = os.path.join(ROOT, "build")
VERSION = open(os.path.join(ROOT, "version.txt"), encoding="utf-8").read().strip()
ZIP = os.path.join(BUILD, f"MysticalRealms_TranslationFixes-{VERSION}.zip")


def validate_json_files():
    for dirpath, _, filenames in os.walk(SRC):
        for name in filenames:
            if name.endswith(".json"):
                path = os.path.join(dirpath, name)
                with open(path, encoding="utf-8") as f:
                    json.load(f)


def sha1_of(path):
    h = hashlib.sha1()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    validate_json_files()

    if os.path.exists(ZIP):
        os.remove(ZIP)
    os.makedirs(BUILD, exist_ok=True)

    # pack.mcmeta must sit at the zip root so the pack loads directly.
    with zipfile.ZipFile(ZIP, "w", zipfile.ZIP_DEFLATED) as z:
        for dirpath, _, filenames in os.walk(SRC):
            for name in filenames:
                full = os.path.join(dirpath, name)
                arcname = os.path.relpath(full, SRC)
                z.write(full, arcname)

    digest = sha1_of(ZIP)
    print(f"OK -> {ZIP}")
    print(f"SHA1: {digest}")
    # Ready to paste into server.properties:
    print(f"resource-pack-sha1={digest}")


if __name__ == "__main__":
    main()
