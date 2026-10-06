# AstRef — Wishbound Native Asset Library

AstRef is the production intake and assignment layer for Wishbound artwork.

The game-facing library intentionally does **not** carry prior story, character, relationship, or scene context. Once an image is accepted into Wishbound it is identified only by its Wishbound asset ID and its role in the current game.

## Public structure

```
AstRef/
  README.md
  WISHBOUND_POOL_SUMMARY.yml
  route_slots.yml
  manifests/
    wishbound_assets.csv
    import_summary.json
  private_provenance/        # generated locally; ignored by Git
  raw/                       # staging only; not referenced by runtime
```

## Wishbound asset identity

Every accepted asset receives:

- `wishbound_asset_id`
- `wishbound_character`
- `wishbound_route`
- `wishbound_role`
- `wishbound_scene_type`
- `wishbound_outfit`
- `wishbound_expression`
- `runtime_filename`
- `runtime_path`
- dimensions / transparency / SHA-256
- safety/publication state

The game does not use source titles, old character names, old scene names, or old relationship context.

## Runtime categories

- character base
- expression layer
- outfit layer
- accessory layer
- portrait
- background
- event CG
- phone/gallery image
- transformation/effect layer
- transition/UI image

## Provenance

Original archive/source details are written only to `AstRef/private_provenance/` during intake. That folder is excluded from Git and is not packaged into Android builds.

Safety review is still based on the actual visual content. Renaming or recontextualizing an image never bypasses an age/content restriction.
