# Asset Intake Status

## Uploaded image archives

All 1,923 uploaded images are represented by the Wishbound intake system.

| Source | Images | Sequence groups | Transparent/layer candidates | Other technical groups | Public repo status |
|---|---:|---:|---:|---|---|
| [GROOVER] Gonna be-- | 943 | 623 | 0 | 614 square/mixed, 324 portrait, 4 landscape, 1 cover | local/reference only |
| [X-BangBang] Inga Ouhou! | 300 | 22 | 199 | 100 square/mixed, 1 cover | local/reference only |
| [Crowd] X-Change 2 R | 680 | 457 | 300 | 379 square/mixed, 1 cover | local/reference only |

Each archive is keyed in `assets/source_catalog.yml` by SHA-256 so a local intake can confirm it is organizing the exact uploaded source.

## Student Transfer

Student Transfer is registered as a linked external source and mapped into Wishbound's taxonomy:

- characters → pose / expression / blush / mutation / outfit / accessory
- backgrounds → location / room / variant
- CG → event CG
- anim + movies → animation/effect assets
- transitions → reality/scene transitions
- line_action → dialogue/action graphics
- phone_icon → phone UI
- thumbs → gallery/location thumbnails
- misc + root particles → effects/misc visuals

The organizer follows the current Student Transfer documentation for layered characters and the v6 location/room/variant background convention.

## Wishbound adaptation labels

Every ingested external image receives:

- stable Wishbound asset ID
- original source and path
- sequence group / variant
- dimensions and pixel mode
- transparency flag
- technical class
- SHA-256
- rights status
- adult-route eligibility
- publication state

No external image becomes a shipped game asset until rights and adult-route eligibility are explicitly reviewed.
