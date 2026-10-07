# Wishbound v0.5.0 — production character set + live AstRef integration.
# This late-loading layer replaces the old geometric placeholder visuals.

init -10 python:
    WB_ROUTE_VISUALS = {
        "avery": "images/astref_safe/wb_safe_0042_background.webp",
        "mia": "images/astref_safe/wb_safe_0075_background.webp",
        "chloe": "images/astref_safe/wb_safe_0041_background.webp",
        "naomi": "images/astref_safe/wb_safe_0055_background.webp",
        "lila": "images/astref_safe/wb_safe_0070_background.webp",
        "rhea": "images/astref_safe/wb_safe_0068_background.webp",
    }

    WB_ROUTE_NAMES = {
        "avery": "Avery Lane",
        "mia": "Mia Hart",
        "chloe": "Chloe Vale",
        "naomi": "Naomi Cross",
        "lila": "Lila Morgan",
        "rhea": "Rhea Park",
    }

    WB_ROUTE_SPRITES = {
        "avery": "images/characters/avery.png",
        "mia": "images/characters/mia.png",
        "chloe": "images/characters/chloe.png",
        "naomi": "images/characters/naomi.png",
        "lila": "images/characters/lila.png",
        "rhea": "images/characters/rhea.png",
    }

# Source art is 4:3. Keep the complete composition visible instead of
# center-cropping it. The 960x720 art is centered inside the 1280x720 stage.
init -9 python:
    def wb_fit_bg(path):
        return Composite(
            (1280, 720),
            (0, 0), Solid("#08060b"),
            (160, 0), Transform(path, xysize=(960, 720))
        )

image bg title = wb_fit_bg("images/astref_safe/wb_safe_0047_background.webp")
image bg void = wb_fit_bg("images/astref_safe/wb_safe_0062_background.webp")
image bg bedroom = wb_fit_bg("images/astref_safe/wb_safe_0017_background.webp")
image bg bathroom = wb_fit_bg("images/astref_safe/wb_safe_0056_background.webp")
image bg closet = wb_fit_bg("images/astref_safe/wb_safe_0049_background.webp")
image bg phone = wb_fit_bg("images/astref_safe/wb_safe_0007_prop.webp")
image bg kitchen = wb_fit_bg("images/astref_safe/wb_safe_0070_background.webp")
image bg city = wb_fit_bg("images/astref_safe/wb_safe_0046_background.webp")
image bg event_venue = wb_fit_bg("images/astref_safe/wb_safe_0042_background.webp")
image bg office_lobby = wb_fit_bg("images/astref_safe/wb_safe_0075_background.webp")
image bg photo_studio = wb_fit_bg("images/astref_safe/wb_safe_0041_background.webp")
image bg tattoo_studio = wb_fit_bg("images/astref_safe/wb_safe_0055_background.webp")
image bg cafe = wb_fit_bg("images/astref_safe/wb_safe_0070_background.webp")
image bg rooftop_club = wb_fit_bg("images/astref_safe/wb_safe_0068_background.webp")

# Original adult Wishbound production character set.
image avery = Transform("images/characters/avery.png", zoom=.72)
image mia = Transform("images/characters/mia.png", zoom=.72)
image chloe = Transform("images/characters/chloe.png", zoom=.72)
image naomi = Transform("images/characters/naomi.png", zoom=.62)
image lila = Transform("images/characters/lila.png", zoom=.62)
image rhea = Transform("images/characters/rhea.png", zoom=.62)

screen wb_route_card(rid, nm, age, blurb):
    button:
        xsize 350 ysize 245
        action Return(rid)
        background Solid("#211729")
        hover_background Solid("#3b2747")
        fixed:
            xfill True yfill True
            add Transform(WB_ROUTE_VISUALS[rid], xysize=(350, 245))
            add Solid("#09060b99")
            add Transform(WB_ROUTE_SPRITES[rid], fit="contain", xysize=(145, 195)) xalign .17 yalign .96
            frame:
                xalign .73 yalign .5
                xsize 225 ysize 205
                background Solid("#0a0710b8")
                padding (12, 13)
                vbox:
                    spacing 5
                    xalign .5 yalign .5
                    text nm size 29 bold True xalign .5
                    text "Age [age]" size 18 color "#ef9bea" xalign .5
                    text blurb size 15 xsize 195 text_align .5 xalign .5

screen reality_select():
    modal True
    add wb_fit_bg("images/astref_safe/wb_safe_0062_background.webp")
    add Solid("#07040bc9")
    vbox:
        xalign .5 yalign .5 spacing 15
        text "HOW DOES REALITY ANSWER?" size 42 bold True xalign .5
        text "Choose the adult life reality rewrites around you." size 20 color "#d2c4d8" xalign .5
        grid 3 2:
            spacing 14
            xalign .5
            use wb_route_card('avery','Avery Lane',26,'Event planner. Social confidence and a complicated flirtation.')
            use wb_route_card('mia','Mia Hart',29,'Consultant. Married life expects instant familiarity.')
            use wb_route_card('chloe','Chloe Vale',25,'Creator. Public confidence, fiancé, and cameras everywhere.')
            use wb_route_card('naomi','Naomi Cross',33,'Tattoo artist. Studio owner with an unresolved ex.')
            use wb_route_card('lila','Lila Morgan',28,'Pastry chef. Secret girlfriend and a busy café staff.')
            use wb_route_card('rhea','Rhea Park',30,'DJ/club manager. Nightlife reputation and a knowing bartender.')

screen bedroom_hub():
    modal True
    add Solid("#00000033")
    frame:
        xalign .02 yalign .08 xsize 360 ysize 565
        background Solid("#0d0a12e8")
        padding (20,18)
        vbox:
            spacing 8
            text "REALITY EVIDENCE" size 25 bold True color "#ef9bea"
            text "[evidence_count]/4 discovered" size 20
            bar value StaticValue(evidence_count, 4) xsize 310
            text "Curiosity: [curiosity]" size 18
            text "Boldness: [boldness]" size 18
            text "Acceptance: [acceptance]" size 18
            null height 5
            frame:
                xsize 315 ysize 210
                background Solid("#120d18")
                add Transform(WB_ROUTE_VISUALS.get(reality_id, WB_ROUTE_VISUALS["avery"]), xysize=(295, 166)) xalign .5 yalign .12
                add Transform(WB_ROUTE_SPRITES.get(reality_id, WB_ROUTE_SPRITES["avery"]), fit="contain", xysize=(105, 150)) xalign .16 yalign .91
                text WB_ROUTE_NAMES.get(reality_id, reality_name) size 20 bold True xalign .62 yalign .93
    vbox:
        xalign .79 yalign .50 spacing 14
        text "What do you check?" size 32 bold True xalign .5
        textbutton "MIRROR" action Return('mirror') xsize 380 sensitive not seen_mirror
        textbutton "PHONE" action Return('phone') xsize 380 sensitive not seen_phone
        textbutton "CLOSET" action Return('closet') xsize 380 sensitive not seen_closet
        textbutton "WALLET / ID" action Return('wallet') xsize 380 sensitive not seen_wallet
        if evidence_count >= 3:
            textbutton "FACE THE REST OF THE MORNING" action Return('continue') xsize 380

screen main_menu():
    tag menu
    add wb_fit_bg("images/astref_safe/wb_safe_0047_background.webp")
    add Solid("#08050b77")
    frame:
        xalign .82 yalign .54
        background Solid("#0b0810e8")
        padding (32, 28)
        vbox:
            spacing 11
            text "WISHBOUND" size 54 bold True color "#fff5ff"
            text "Her Morning" size 27 color "#df8bdd"
            text "v0.5.0 • Production Character Set" size 17 color "#bcaec0"
            null height 5
            textbutton "START" action Start() xsize 360
            textbutton "VISUAL ARCHIVE" action ShowMenu('asset_gallery') xsize 360
            textbutton "ASTREF LIBRARY" action ShowMenu('astref_safe_gallery') xsize 360
            textbutton "LOAD" action ShowMenu('load') xsize 360
            textbutton "PREFERENCES" action ShowMenu('preferences') xsize 360
            textbutton "QUIT" action Quit(confirm=True) xsize 360

screen asset_gallery():
    tag menu
    use game_menu("Visual Archive"):
        viewport:
            xfill True
            ymaximum 540
            draggable True
            mousewheel True
            scrollbars "vertical"
            vbox:
                spacing 16
                text "ROUTE VISUALS" size 30 bold True color "#ef9bea"
                text "The old geometric character placeholders have been removed. These are the live route visuals used by the current build." size 18 color "#bcaec0" xsize 1000
                for rid in ["avery","mia","chloe","naomi","lila","rhea"]:
                    frame:
                        xsize 1020 ysize 195
                        background Solid("#251c2ddd")
                        hbox:
                            spacing 18
                            add Transform(WB_ROUTE_VISUALS[rid], xysize=(300, 170)) yalign .5
                            vbox:
                                yalign .5 spacing 8
                                text WB_ROUTE_NAMES[rid] size 28 bold True
                                text WB_ROUTE_VISUALS[rid] size 16 color "#bcaec0"
                null height 8
                textbutton "OPEN FULL ASTREF LIBRARY" action ShowMenu('astref_safe_gallery') xsize 420
