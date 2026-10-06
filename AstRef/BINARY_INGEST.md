# AstRef Binary Ingest

GitHub repository write access is configured, but the current ChatGPT GitHub connector cannot transfer local binary files by file handle. It accepts binary blobs only as inline base64/text.

The ten Wbasts ZIP parts total more than 200 MB, so they cannot be safely bridged through inline tool arguments.

Once the archives are available to a normal Git client or GitHub runner, run:

```bash
python tools/ingest_wbasts_to_astref.py Wbasts_Part_001.zip Wbasts_Part_002.zip Wbasts_Part_003.zip Wbasts_Part_004.zip Wbasts_Part_005.zip Wbasts_Part_006.zip Wbasts_Part_007.zip Wbasts_Part_008.zip Wbasts_Part_009.zip Wbasts_Part_010.zip
git add AstRef
git commit -m "Import cleared AstRef image library"
git push
```

The script preserves each source set under `AstRef/raw/<source_id>/`, deduplicates exact byte-identical files, writes `AstRef/manifests/wbasts_files.csv`, and applies `AstRef/SAFETY_EXCLUSIONS.yml`.
