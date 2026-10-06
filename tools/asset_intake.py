#!/usr/bin/env python3
"""Wishbound external asset organizer.

Scans user-supplied ZIPs/directories and Student Transfer-style image trees.
It produces metadata manifests and an optional *local-only* normalized tree.
It never marks an asset redistributable automatically.
"""
from __future__ import annotations
import argparse, csv, hashlib, io, json, re, shutil, zipfile
from pathlib import Path
from collections import Counter
try:
    from PIL import Image
except Exception:
    Image = None

IMAGE_EXTS={".png",".jpg",".jpeg",".webp",".gif",".bmp"}

def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def image_meta(data: bytes):
    if Image is None:
        return 0,0,"?",False
    try:
        im=Image.open(io.BytesIO(data))
        w,h=im.size
        alpha=("A" in im.mode) or ("transparency" in im.info)
        return w,h,im.mode,bool(alpha)
    except Exception:
        return 0,0,"?",False

def aspect_class(w,h,alpha):
    if alpha:
        return "layer_or_overlay_candidate"
    if not w or not h:
        return "unknown_image"
    r=w/h
    if r>1.45: return "landscape_scene_or_cg"
    if r<0.80: return "portrait_scene_or_sprite_candidate"
    return "square_or_mixed_cg"

def seq_group(name):
    stem=Path(name).stem
    m=re.match(r"(.+?)[_-](\\d+)$",stem)
    if m: return m.group(1),m.group(2)
    parts=stem.split("_")
    return (parts[0], parts[1] if len(parts)>1 else "")

def classify_student_transfer(rel):
    p=rel.replace("\\","/").lower()
    if "/characters/" in p:
        if "/faces/blush/" in p: return "character_blush"
        if "/faces/mutations/" in p: return "character_expression_mutation"
        if "/faces/face/" in p: return "character_expression"
        if "/outfits/" in p and ("/on." in p or "/off." in p): return "character_accessory_layer"
        if "/outfits/" in p: return "character_outfit_layer"
        return "character_asset"
    rules=[
      ("/images/bg/","background"),("/images/cg/","event_cg"),
      ("/images/anim/","animation_asset"),("/images/transitions/","transition_asset"),
      ("/images/line_action/","dialogue_action_graphic"),("/images/phone_icon/","phone_ui_icon"),
      ("/images/thumbs/","thumbnail"),("/images/misc/","misc_visual"),
      ("/images/movies/","animation_frames_or_movie_asset")]
    for marker,kind in rules:
        if marker in p: return kind
    return "effect_or_misc_visual"

def iter_zip(path):
    with zipfile.ZipFile(path) as z:
        for n in z.namelist():
            if Path(n).suffix.lower() in IMAGE_EXTS:
                yield n,z.read(n)

def iter_dir(path):
    for p in path.rglob("*"):
        if p.is_file() and p.suffix.lower() in IMAGE_EXTS:
            yield p.relative_to(path).as_posix(),p.read_bytes()

def scan(source_id,path,kind):
    iterator=iter_zip(path) if path.is_file() and path.suffix.lower()==".zip" else iter_dir(path)
    rows=[]
    for i,(name,data) in enumerate(iterator,1):
        w,h,mode,alpha=image_meta(data)
        group,variant=seq_group(name)
        if kind=="student_transfer":
            cls=classify_student_transfer(name)
        else:
            cls="cover_or_index" if i==1 or Path(name).stem=="0000" or "package" in name.lower() else aspect_class(w,h,alpha)
        rows.append({
          "asset_id":f"WBEXT-{source_id.upper()}-{i:05d}",
          "source":source_id,"original_path":name,"sequence_group":group,"variant":variant,
          "width":w,"height":h,"mode":mode,"has_alpha":alpha,"class":cls,
          "sha256":digest(data),"rights_status":"review_required",
          "adult_route_status":"review_required",
          "publication":"local_only_until_cleared"
        })
    return rows

def write(rows,out):
    out.mkdir(parents=True,exist_ok=True)
    fields=list(rows[0]) if rows else []
    with (out/"asset_catalog.csv").open("w",newline="",encoding="utf-8") as f:
        if fields:
            w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
    (out/"asset_catalog.json").write_text(json.dumps(rows,indent=2),encoding="utf-8")
    summary={
      "count":len(rows),
      "classes":dict(Counter(r["class"] for r in rows)),
      "sources":dict(Counter(r["source"] for r in rows)),
      "rights":dict(Counter(r["rights_status"] for r in rows)),
    }
    (out/"asset_summary.json").write_text(json.dumps(summary,indent=2),encoding="utf-8")
    return summary

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("inbox",type=Path,help="assets_inbox directory")
    ap.add_argument("--output",type=Path,default=Path("asset_build"))
    args=ap.parse_args()
    rows=[]
    up=args.inbox/"uploaded"
    if up.exists():
        for p in sorted(up.iterdir()):
            if p.suffix.lower()==".zip":
                sid=re.sub(r"[^a-z0-9]+","_",p.stem.lower()).strip("_")[:32]
                rows.extend(scan(sid,p,"uploaded"))
    st=args.inbox/"student-transfer"
    if st.exists():
        rows.extend(scan("student_transfer",st,"student_transfer"))
    summary=write(rows,args.output)
    print(json.dumps(summary,indent=2))

if __name__=="__main__":
    main()
