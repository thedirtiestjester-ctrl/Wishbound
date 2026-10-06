# Wishbound asset taxonomy / adaptation registry.
# Raw external assets are never referenced here until cleared and copied into game/images.

init -20 python:
    WB_ASSET_CLASSES = {
        "character_expression": "Layered face/expression art",
        "character_blush": "Blush/emotion overlay",
        "character_expression_mutation": "Hair/makeup/transformation face variant",
        "character_outfit_layer": "Body/outfit layer",
        "character_accessory_layer": "Accessory overlay",
        "background": "Full-scene environment",
        "event_cg": "Illustrated story event",
        "animation_asset": "Animation frame/particle",
        "transition_asset": "Scene/reality transition",
        "dialogue_action_graphic": "Dialogue or action UI visual",
        "phone_ui_icon": "Phone interface icon",
        "thumbnail": "Gallery/location thumbnail",
        "misc_visual": "Miscellaneous reusable visual",
        "animation_frames_or_movie_asset": "Frame animation/movie component",
        "effect_or_misc_visual": "Root particle/effect asset",
    }

    WB_ROUTE_ASSET_NEEDS = {
        "avery": ["bedroom","bathroom","phone","closet","event_venue","avery_sprite","avery_expressions","avery_outfits"],
        "mia": ["bedroom","bathroom","phone","closet","office_lobby","mia_sprite","mia_expressions","mia_outfits"],
        "chloe": ["bedroom","bathroom","phone","closet","photo_studio","chloe_sprite","chloe_expressions","chloe_outfits"],
        "naomi": ["bedroom","bathroom","phone","closet","tattoo_studio","naomi_sprite","naomi_expressions","naomi_outfits"],
        "lila": ["bedroom","bathroom","phone","closet","cafe","lila_sprite","lila_expressions","lila_outfits"],
        "rhea": ["bedroom","bathroom","phone","closet","rooftop_club","rhea_sprite","rhea_expressions","rhea_outfits"],
    }

    WB_EXTERNAL_PUBLICATION_STATES = ("cleared","local_only","reference_only","blocked")
