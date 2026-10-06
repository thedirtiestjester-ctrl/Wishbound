# Wishbound: Her Morning — v0.3

Original Ren'Py adult transformation/reality-rewrite visual novel.

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
- Wishbound-native AstRef asset identity system

## Content boundary

Wishbound's romance/sexual-context characters are adults. Lewd mode remains suggestive rather than graphically explicit.

## Wishbound-native asset system

Accepted artwork is identified only by its Wishbound role:

- character / expression / outfit / accessory
- portrait
- background
- event CG
- phone/gallery image
- transformation/effect
- transition/UI

Game-facing metadata does not preserve prior character names, scene meanings, relationships, or story context.

The canonical asset layer lives under `AstRef/`. Public manifests use `WB-AST-*` asset IDs and `WBPOOL-*` pool IDs. Original archive/source details are generated only under ignored `AstRef/private_provenance/` and are not part of the runtime or Android build.

Safety review is based on what an image actually depicts; changing its Wishbound narrative identity does not bypass age/content restrictions.

## Build

Use the current GitHub Android workflow or a current Ren'Py SDK. See `BUILD_ANDROID.md`.
