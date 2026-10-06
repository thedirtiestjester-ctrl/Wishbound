# Wishbound Asset Intake Status

## Current Wishbound pools

The image intake system currently recognizes **2,968 unique images** as four neutral production pools.

| Pool | Images | Transparent/layer candidates | Primary production use |
|---|---:|---:|---|
| WBPOOL-A | 943 | 0 | event CG / portrait / background candidates |
| WBPOOL-B | 1,047 | 1,047 | layered character / outfit candidates |
| WBPOOL-C | 680 | 300 | event + character-layer candidates |
| WBPOOL-D | 298 | 199 | character-layer + event candidates |

## Canonical identity

The public project no longer treats these images as belonging to prior characters or prior scenes.

Each accepted image receives a Wishbound-native identity with fields such as:

- `wishbound_asset_id`
- `wishbound_character`
- `wishbound_route`
- `wishbound_role`
- `wishbound_scene_type`
- `wishbound_outfit`
- `wishbound_expression`
- `runtime_filename`
- `runtime_path`
- SHA-256
- publication state

Any archive/source provenance needed for administration is emitted only to ignored `AstRef/private_provenance/`.

## Runtime rule

Wishbound runtime code uses only Wishbound-native IDs and roles. Safety eligibility is still determined from the actual visual content.
