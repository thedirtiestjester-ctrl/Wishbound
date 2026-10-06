# Wishbound: Her Morning — v0.2

Original Ren'Py adult transformation/reality-rewrite visual novel prototype.

## Implemented
- 3 adult male starting protagonists (25+)
- 6 rewritten adult female identities (25–33)
- Reality rewrite / retained-memory state engine
- Lewd or Mild reaction tone toggle
- Mirror, Phone, Closet, Wallet exploration
- Reality Evidence tracker
- Route-specific relationship reveals
- Six route-opening locations: event venue, office lobby, photo studio, tattoo studio, café, rooftop club
- Route-specific first-day hooks
- Save/load/preferences screens
- Mobile-first 1280x720 UI
- Original placeholder sprites/backgrounds and effects

## Content boundary
Lewd mode is suggestive rather than sexually explicit: body/clothing awareness, flirting, romantic embarrassment, relationship surprises, and adult innuendo. All romance/sexual-context characters in Wishbound are adults.

## Uploaded reference archives
Three user-supplied archives were inspected only for structural/theme reference. Their own metadata identifies them as third-party commercial "Game CG" / "Full Rip" material. Those files are intentionally **not bundled, copied, committed, or redistributed** in Wishbound v0.2. See `EXCLUDED_ASSETS.md`.

## Build
Open the project in a current Ren'Py SDK and use the Android build workflow. See `BUILD_ANDROID.md`.


## Asset library

Wishbound now has a unified external-asset intake system under `asset_library/`.

- `asset_library/source_catalog.yml` identifies all uploaded image archives and the linked Student Transfer source.
- `asset_library/student_transfer_mapping.yml` maps layered sprites, outfits, expressions, backgrounds, CGs, effects, transitions, phone UI, and thumbnails into Wishbound roles.
- `tools/asset_intake.py` scans local ZIPs/checkouts, assigns stable IDs, dimensions, hashes, sequence groups, technical classes, rights state, adult-route eligibility, and publication state.
- `game/asset_registry.rpy` exposes the normalized asset taxonomy and route needs to the game.
- Raw third-party/reference material is kept under ignored `assets_inbox/` and is never published automatically. Only explicitly cleared material is copied into the distributable `game/images/` tree.

A complete technical manifest has been generated for all 1,923 currently uploaded external images. The source archive hashes are kept in `asset_library/source_catalog.yml` so the catalog can be reproduced against the exact inputs.
