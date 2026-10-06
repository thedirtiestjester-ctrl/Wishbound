# Wishbound-native asset taxonomy.
# Runtime/game-facing metadata contains only Wishbound identities and roles.

init -20 python:
    WB_ASSET_CLASSES = {
        "character": "Character base or full-body layer",
        "expression": "Face/expression/emotion layer",
        "outfit": "Wardrobe/body layer",
        "accessory": "Accessory overlay",
        "portrait": "Character portrait",
        "background": "Full-scene environment",
        "cg": "Illustrated Wishbound story event",
        "phone": "Phone/gallery/social image",
        "effect": "Transformation/reality/effect layer",
        "transition": "Scene/reality transition",
        "ui": "Interface visual",
    }

    WB_ROUTE_ASSET_NEEDS = {
        "avery": ["bedroom","bathroom","phone","closet","event_venue","avery_sprite","avery_expressions","avery_outfits"],
        "mia": ["bedroom","bathroom","phone","closet","office_lobby","mia_sprite","mia_expressions","mia_outfits"],
        "chloe": ["bedroom","bathroom","phone","closet","photo_studio","chloe_sprite","chloe_expressions","chloe_outfits"],
        "naomi": ["bedroom","bathroom","phone","closet","tattoo_studio","naomi_sprite","naomi_expressions","naomi_outfits"],
        "lila": ["bedroom","bathroom","phone","closet","cafe","lila_sprite","lila_expressions","lila_outfits"],
        "rhea": ["bedroom","bathroom","phone","closet","rooftop_club","rhea_sprite","rhea_expressions","rhea_outfits"],
    }

    WB_ASSET_IDENTITY_MODEL = "wishbound_native"
    WB_PUBLICATION_STATES = ("review_required","cleared","local_only","blocked")
