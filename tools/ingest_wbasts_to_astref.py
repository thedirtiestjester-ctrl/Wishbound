#!/usr/bin/env python3
"""Extract user-cleared Wbasts archives into AstRef while preserving source identity.

Usage:
    python tools/ingest_wbasts_to_astref.py /path/to/Wbasts_Part_001.zip ... /path/to/Wbasts_Part_010.zip

The script deduplicates by SHA-256, preserves original filenames under source-id
folders, writes a manifest, and excludes source sets that are flagged by
AstRef/SAFETY_EXCLUSIONS.yml.
"""
from __future__ import annotations
import argparse, csv, hashlib, json, os, shutil, zipfile
from pathlib import Path

IMAGE_EXTS={".png",".jpg",".jpeg",".webp",".gif",".bmp"}

def sha256(data):
    return hashlib.sha256(data).hexdigest()

def load_excluded(path: Path):
    ids=set()
    if not path.exists():
        return ids
    for line in path.read_text(encoding="utf-8").splitlines():
        line=line.strip()
        if line.startswith("- source_id:"):
            ids.add(line.split(":",1)[1].strip())
    return ids

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("archives", nargs="+", type=Path)
    ap.add_argument("--root", type=Path, default=Path("AstRef/raw"))
    ap.add_argument("--manifest", type=Path, default=Path("AstRef/manifests/wbasts_files.csv"))
    ap.add_argument("--safety", type=Path, default=Path("AstRef/SAFETY_EXCLUSIONS.yml"))
    args=ap.parse_args()

    excluded=load_excluded(args.safety)
    args.root.mkdir(parents=True, exist_ok=True)
    args.manifest.parent.mkdir(parents=True, exist_ok=True)

    seen={}
    rows=[]
    for archive in args.archives:
        with zipfile.ZipFile(archive) as z:
            for n in z.namelist():
                p=Path(n)
                if p.suffix.lower() not in IMAGE_EXTS:
                    continue
                parts=p.parts
                try:
                    i=parts.index("Wbasts")
                    source_id=parts[i+1]
                    rel=Path(*parts[i+2:])
                except Exception:
                    continue
                data=z.read(n)
                digest=sha256(data)
                status="excluded_safety" if source_id in excluded else "eligible_for_repo"
                out=args.root/source_id/rel
                if status=="eligible_for_repo" and digest not in seen:
                    out.parent.mkdir(parents=True, exist_ok=True)
                    out.write_bytes(data)
                    seen[digest]=out.as_posix()
                rows.append({
                    "source_id":source_id,
                    "original_path":n,
                    "relative_path":rel.as_posix(),
                    "sha256":digest,
                    "status":status,
                    "repo_path":seen.get(digest,""),
                })

    with args.manifest.open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=["source_id","original_path","relative_path","sha256","status","repo_path"])
        w.writeheader(); w.writerows(rows)
    print(json.dumps({
        "records":len(rows),
        "written_unique":len(seen),
        "excluded_sources":sorted(excluded),
    },indent=2))

if __name__=="__main__":
    main()
