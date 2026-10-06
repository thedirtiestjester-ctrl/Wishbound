# Wishbound Asset Library

This directory is the source-of-truth for asset classification and provenance.

## Tracked in Git

- `source_catalog.yml` — every external source currently known to Wishbound.
- `student_transfer_mapping.yml` — how Student Transfer's documented asset structure maps into Wishbound.
- `rights_overrides.example.yml` — template for explicitly clearing individual assets or asset families.
- Generated catalog files may be committed only when they contain metadata, hashes, and labels — not uncleared copyrighted image bytes.

## Local-only raw assets

Put local source material under:

```
assets_inbox/
  uploaded/
    gonna_be.zip
    inga_ouhou.zip
    xchange2r.zip
  student-transfer/
    game/images/...
```

Then run:

```bash
python tools/asset_intake.py assets_inbox --output asset_build
```

The intake tool scans every image, assigns a stable Wishbound asset ID, classifies it, records provenance, and produces a normalized manifest. Raw local-only material is deliberately ignored by Git.

## Publication rule

An asset is shipped in `game/images/` only when its rights state is `cleared` and its content is appropriate for the adult-only Wishbound cast. Everything else remains reference/local-only and can still have a Wishbound replacement target.
