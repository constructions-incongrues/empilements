import os
import argparse
import re

def normalize(text):
    text = text.title()  # Met en majuscule la première lettre de chaque mot
    return text

def process_folder(folder):
    for root, _, files in os.walk(folder):
        for filename in files:
            name, ext = os.path.splitext(filename)
            if ' - ' in name:
                artist, title = name.split(' - ', 1)
                artist = normalize(artist)
                title = normalize(title)
                new_name = f"{artist} - {title}{ext.lower()}"
                src = os.path.join(root, filename)
                dst = os.path.join(root, new_name)
                if src != dst:
                    print(f"Renommage : {src} -> {dst}")
                    os.rename(src, dst)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Normalise récursivement les noms de fichiers (artiste et titre)")
    parser.add_argument("folder", help="Dossier à traiter")
    args = parser.parse_args()
    process_folder(args.folder)