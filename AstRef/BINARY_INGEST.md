# AstRef Binary Intake

AstRef binary intake is now Wishbound-first.

## Intake outputs

Running the importer produces:

- `AstRef/manifests/wishbound_assets.csv`
- `AstRef/manifests/import_summary.json`
- local-only `AstRef/private_provenance/provenance.csv`

The public manifest contains only Wishbound-native identity fields. It does not expose prior story/character/scene context.

## Assignment

New assets begin as `assignment_status=unassigned`.

Use `AstRef/assignments.json` to deliberately map a `WB-AST-*` ID to:

- a Wishbound character
- route
- role
- scene type
- outfit
- expression
- final runtime path

This prevents arbitrary reassignment and keeps character consistency intentional.
