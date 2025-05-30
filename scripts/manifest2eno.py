import json
import sys
from pathlib import Path

def normalize_artist(name):
    # Normalise les espaces et la casse (titre)
    return " ".join(name.strip().split()).title()

def json_to_eno(manifest):
    lines = []
    lines.append(f'title: {manifest.get("title", "")}')
    lines.append(f'date: {manifest.get("date", "")}')
    authors = manifest.get("authors", [])
    if authors:
        lines.append("release_artists:")
        for author in authors:
            lines.append(f'  - {normalize_artist(author)}')
    return "\n".join(lines)

def process_manifest(manifest_path):
    eno_path = manifest_path.parent / "release.eno"
    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest = json.load(f)
    eno_content = json_to_eno(manifest)
    with open(eno_path, "w", encoding="utf-8") as f:
        f.write(eno_content)
    print(f"{eno_path} généré.")

def main():
    empilements_dir = Path(__file__).parent.parent / "empilements"
    if not empilements_dir.exists():
        print("Dossier empilements/ introuvable.")
        sys.exit(1)
    for manifest_path in empilements_dir.rglob("manifest.json"):
        process_manifest(manifest_path)

if __name__ == "__main__":
    main()