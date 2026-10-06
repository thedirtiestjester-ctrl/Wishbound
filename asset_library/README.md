# Wishbound Asset Library

This legacy catalog layer now feeds the canonical Wishbound-native `AstRef/` system.

## Public metadata

Public files use neutral `WBPOOL-*` pool IDs and Wishbound production roles. They do not preserve prior story, character, scene, or relationship context.

## Private provenance

Any original archive/source path needed for administration belongs only under:

```
AstRef/private_provenance/
```

That directory is Git-ignored and never packaged into the game.

## Canonical workflow

Use:

```bash
python tools/ingest_wbasts_to_astref.py <archive parts...>
```

The importer generates:

- `AstRef/manifests/wishbound_assets.csv`
- `AstRef/manifests/import_summary.json`
- local-only `AstRef/private_provenance/provenance.csv`

Game code should consume Wishbound IDs/roles, not source metadata.
