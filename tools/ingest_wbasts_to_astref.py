#!/usr/bin/env python3
"""Build a Wishbound-native AstRef library from owner-cleared archive parts.

Public output is source-neutral and Wishbound-first. Original archive/source details
are written only to AstRef/private_provenance/, which must remain Git-ignored.

The importer does not infer that relabeling changes the actual visual content.
Pools remain blocked until image-level review clears individual assets.
"""
from __future__ import annotations
import argparse, csv, hashlib, json, re, zipfile
from pathlib import Path

IMAGE_EXTS={".png",".jpg",".jpeg",".webp",".gif",".bmp"}
POOL_MAP={
    "3696570_a7b0c3fc7d":"WBPOOL-A",
    "4114637_452fc8a874":"WBPOOL-B",
    "818169_28978d7d08":"WBPOOL-C",
    "3697336_ad7a34319e":"WBPOOL-D",
}

ROUTES=[
    ("avery","Avery Lane"),
    ("mia","Mia Hart"),
    ("chloe","Chloe Vale"),
    ("naomi","Naomi Cross"),
    ("lila","Lila Morgan"),
    ("rhea","Rhea Park"),
]

def sha256(data):
    return hashlib.sha256(data).hexdigest()

def classify(rel: str):
    s=rel.lower()
    if any(k in s for k in ("face","expression","mouth","eye","blush")):
        return "expression"
    if any(k in s for k in ("outfit","dress","cloth","body","costume")):
        return "outfit"
    if any(k in s for k in ("bg","background","room","street","park","office","cafe")):
        return "background"
    if any(k in s for k in ("effect","fx","particle","overlay","light")):
        return "effect"
    return "cg"

def safe_slug(s):
    s=re.sub(r"[^a-z0-9]+","_",s.lower()).strip("_")
    return s or "asset"

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("archives", nargs="+", type=Path)
    ap.add_argument("--public-manifest", type=Path, default=Path("AstRef/manifests/wishbound_assets.csv"))
    ap.add_argument("--private-manifest", type=Path, default=Path("AstRef/private_provenance/provenance.csv"))
    ap.add_argument("--summary", type=Path, default=Path("AstRef/manifests/import_summary.json"))
    args=ap.parse_args()

    args.public_manifest.parent.mkdir(parents=True,exist_ok=True)
    args.private_manifest.parent.mkdir(parents=True,exist_ok=True)

    seen={}
    public_rows=[]
    private_rows=[]
    counter=0

    for archive in args.archives:
        with zipfile.ZipFile(archive) as z:
            for n in z.namelist():
                if Path(n).suffix.lower() not in IMAGE_EXTS:
                    continue
                parts=Path(n).parts
                try:
                    i=parts.index("Wbasts")
                    source_id=parts[i+1]
                    rel=Path(*parts[i+2:]).as_posix()
                except Exception:
                    continue
                data=z.read(n)
                digest=sha256(data)
                if digest in seen:
                    continue
                seen[digest]=True
                counter+=1
                pool=POOL_MAP.get(source_id,"WBPOOL-X")
                role=classify(rel)
                route_id,character=ROUTES[(counter-1)%len(ROUTES)]
                asset_id=f"WB-AST-{counter:05d}"
                ext=Path(rel).suffix.lower()
                filename=f"{asset_id.lower()}_{role}{ext}"
                runtime_path=f"game/images/routes/{route_id}/{role}/{filename}"
                status="review_required"

                public_rows.append({
                    "wishbound_asset_id":asset_id,
                    "wishbound_pool":pool,
                    "wishbound_character":character,
                    "wishbound_route":route_id,
                    "wishbound_role":role,
                    "wishbound_scene_type":"",
                    "wishbound_outfit":"",
                    "wishbound_expression":"",
                    "runtime_filename":filename,
                    "runtime_path":runtime_path,
                    "sha256":digest,
                    "publication_state":status,
                })
                private_rows.append({
                    "wishbound_asset_id":asset_id,
                    "source_id":source_id,
                    "archive_name":archive.name,
                    "original_path":n,
                    "sha256":digest,
                })

    pub_fields=list(public_rows[0]) if public_rows else []
    with args.public_manifest.open("w",newline="",encoding="utf-8") as f:
        if pub_fields:
            w=csv.DictWriter(f,fieldnames=pub_fields); w.writeheader(); w.writerows(public_rows)

    priv_fields=list(private_rows[0]) if private_rows else []
    with args.private_manifest.open("w",newline="",encoding="utf-8") as f:
        if priv_fields:
            w=csv.DictWriter(f,fieldnames=priv_fields); w.writeheader(); w.writerows(private_rows)

    args.summary.write_text(json.dumps({
        "identity_model":"wishbound_native",
        "unique_assets":len(public_rows),
        "publication_state":{"review_required":len(public_rows)},
        "public_manifest":args.public_manifest.as_posix(),
        "private_provenance":args.private_manifest.as_posix(),
    },indent=2),encoding="utf-8")
    print(args.summary.read_text(encoding="utf-8"))

if __name__=="__main__":
    main()
