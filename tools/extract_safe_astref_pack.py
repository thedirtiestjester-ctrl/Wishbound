#!/usr/bin/env python3
"""Extract the visually reviewed Wishbound-safe AstRef pack.

This importer is deliberately narrow. It packages only the 76 images that were
visually reviewed for this build: 66 environment/background images and 10
nonsexual prop/UI/object images. It never extracts character/sexual CG pools.

Usage:
    python tools/extract_safe_astref_pack.py part008.zip part009.zip
"""
from __future__ import annotations
import argparse, csv, hashlib, shutil, zipfile
from pathlib import Path

IMAGE_EXTS={".png",".jpg",".jpeg",".webp",".gif",".bmp"}
SAFE_EXACT={
    "202_101.webp","202_102.webp","207_101.webp","306_201.webp","306_304.webp",
    "401_101.webp","405_551.webp","602_301.webp","604_201.webp","606_101.webp",
}
EXPECTED_COUNT=76

def is_safe_candidate(name: str) -> bool:
    base=Path(name).name
    return base.startswith("H_") or base in SAFE_EXACT

def role_for(name: str) -> str:
    return "background" if Path(name).name.startswith("H_") else "prop"

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("archives", nargs="+", type=Path)
    ap.add_argument("--output", type=Path, default=Path("game/images/astref_safe"))
    ap.add_argument("--manifest", type=Path, default=Path("AstRef/manifests/packaged_safe_assets.csv"))
    args=ap.parse_args()

    found={}
    for archive in args.archives:
        with zipfile.ZipFile(archive) as z:
            for n in z.namelist():
                if Path(n).suffix.lower() not in IMAGE_EXTS or not is_safe_candidate(n):
                    continue
                data=z.read(n)
                digest=hashlib.sha256(data).hexdigest()
                found.setdefault(Path(n).name,(data,digest,role_for(n)))

    if len(found) != EXPECTED_COUNT:
        raise SystemExit(f"Expected {EXPECTED_COUNT} reviewed assets, found {len(found)}. Refusing to package an unreviewed set.")

    if args.output.exists():
        shutil.rmtree(args.output)
    args.output.mkdir(parents=True,exist_ok=True)
    args.manifest.parent.mkdir(parents=True,exist_ok=True)

    rows=[]
    for i,old_name in enumerate(sorted(found),1):
        data,digest,role=found[old_name]
        ext=Path(old_name).suffix.lower()
        asset_id=f"WB-SAFE-{i:04d}"
        filename=f"{asset_id.lower().replace('-','_')}_{role}{ext}"
        out=args.output/filename
        out.write_bytes(data)
        rows.append({
            "wishbound_asset_id":asset_id,
            "role":role,
            "runtime_path":f"images/astref_safe/{filename}",
            "sha256":digest,
            "publication_state":"cleared_reviewed",
        })

    with args.manifest.open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]))
        w.writeheader(); w.writerows(rows)

    backgrounds=sum(r["role"]=="background" for r in rows)
    props=sum(r["role"]=="prop" for r in rows)
    print(f"Packaged {len(rows)} reviewed AstRef assets: {backgrounds} backgrounds, {props} props.")

if __name__=="__main__":
    main()
