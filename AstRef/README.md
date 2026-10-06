# AstRef — Wishbound Asset Reference Library

AstRef is Wishbound's normalized reference layer for externally supplied art sets.

## Current intake

Ten uploaded `Wbasts_Part_*.zip` archives were scanned as one set. They contain **2,968 unique images** across four commercial Game CG sources:

| Source ID | Reference title | Images | Transparent layers |
|---|---|---:|---:|
| 3696570_a7b0c3fc7d | [GROOVER] Gonna be?? | 943 | 0 |
| 4114637_452fc8a874 | [Milk Factory] character-set dump | 1,047 | 1,047 |
| 818169_28978d7d08 | [Crowd] X-Change 2 R | 680 | 300 |
| 3697336_ad7a34319e | [X-BangBang] Inga Ouhou!? | 298 | 199 |

The embedded source metadata identifies these as commercial Game CG/gallery dumps. Raw image bytes are therefore **not published in this public repository**. AstRef keeps the complete technical identity, grouping, intended Wishbound role, and replacement slot for every image.

## Repository structure

```
AstRef/
  README.md
  SOURCE_SUMMARY.yml
  route_slots.yml
  indexes/
    3696570_a7b0c3fc7d.index.txt.gz
    4114637_452fc8a874.index.txt.gz
    818169_28978d7d08.index.txt.gz
    3697336_ad7a34319e.index.txt.gz
  raw/
    README.md              # raw images stay local / ignored
```

Each compressed index contains one line per unique image with:

```
astref_id | original_path | width | height | alpha | wishbound_role |
sequence_group | variant | sha256
```

## Wishbound production roles

- `character_fullbody_or_outfit_layer`
- `character_face_expression_or_overlay_layer`
- `portrait_or_character_reference`
- `background_or_event_reference`
- `event_cg_reference`
- `scene_or_event_reference`

Raw external images never become distributable game assets automatically. When an original/cleared replacement is created, preserve its `ASTREF-*` ID in the replacement manifest so route/event intent survives the swap.
