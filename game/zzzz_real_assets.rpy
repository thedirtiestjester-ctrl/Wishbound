# Wishbound v0.6 - Dropbox real-asset runtime layer.

init -10 python:
    def wb_real_bg(path):
        return Composite(
            (1280, 720),
            (0, 0), Solid("#07050a"),
            (160, 0), Transform(path, xysize=(960, 720))
        )

    WB_REAL_BACKGROUNDS = sorted([
        f for f in renpy.list_files()
        if f.startswith("images/real_assets/backgrounds/")
    ])
    WB_REAL_PROPS = sorted([
        f for f in renpy.list_files()
        if f.startswith("images/real_assets/props/")
    ])
    WB_REAL_CHARACTER_VARIANTS = {
        rid: sorted([
            f for f in renpy.list_files()
            if f.startswith("images/real_assets/characters/{}/".format(rid))
        ])
        for rid in ("avery","mia","chloe","naomi","lila","rhea")
    }

image bg title = wb_real_bg("images/real_assets/backgrounds/h_181.webp")
image bg void = wb_real_bg("images/real_assets/backgrounds/h_292.webp")
image bg bedroom = wb_real_bg("images/real_assets/backgrounds/h_040.webp")
image bg bathroom = wb_real_bg("images/real_assets/backgrounds/h_260.webp")
image bg closet = wb_real_bg("images/real_assets/backgrounds/h_201.webp")
image bg phone = wb_real_bg("images/real_assets/props/405_551.webp")
image bg kitchen = wb_real_bg("images/real_assets/backgrounds/h_351.webp")
image bg city = wb_real_bg("images/real_assets/backgrounds/h_180.webp")
image bg event_venue = wb_real_bg("images/real_assets/backgrounds/h_160.webp")
image bg office_lobby = wb_real_bg("images/real_assets/backgrounds/h_380.webp")
image bg photo_studio = wb_real_bg("images/real_assets/backgrounds/h_153.webp")
image bg tattoo_studio = wb_real_bg("images/real_assets/backgrounds/h_251.webp")
image bg cafe = wb_real_bg("images/real_assets/backgrounds/h_351.webp")
image bg rooftop_club = wb_real_bg("images/real_assets/backgrounds/h_341.webp")

screen reality_select():
    modal True
    add wb_real_bg("images/real_assets/backgrounds/h_292.webp")
    add Solid("#08050bc8")
    vbox:
        xalign .5 yalign .5 spacing 15
        text "HOW DOES REALITY ANSWER?" size 42 bold True xalign .5
        text "Choose the adult life reality rewrites around you." size 20 color "#d2c4d8" xalign .5
        grid 3 2:
            spacing 14
            xalign .5
            use asset_route_card('avery','Avery Lane',26,'Event planner. Social confidence and a complicated flirtation.','images/characters/avery.png')
            use asset_route_card('mia','Mia Hart',29,'Consultant. Married life expects instant familiarity.','images/characters/mia.png')
            use asset_route_card('chloe','Chloe Vale',25,'Creator. Public confidence, fiancé, and cameras everywhere.','images/characters/chloe.png')
            use asset_route_card('naomi','Naomi Cross',33,'Tattoo artist. Studio owner with an unresolved ex.','images/characters/naomi.png')
            use asset_route_card('lila','Lila Morgan',28,'Pastry chef. Secret girlfriend and a busy café staff.','images/characters/lila.png')
            use asset_route_card('rhea','Rhea Park',30,'DJ/club manager. Nightlife reputation and a knowing bartender.','images/characters/rhea.png')

screen main_menu():
    tag menu
    add wb_real_bg("images/real_assets/backgrounds/h_181.webp")
    add Solid("#07040a66")
    frame:
        xalign .82 yalign .54
        background Solid("#0b0810e8")
        padding (32, 28)
        vbox:
            spacing 11
            text "WISHBOUND" size 54 bold True color "#fff5ff"
            text "Her Morning" size 27 color "#df8bdd"
            text "v0.6.0 • Real Asset Library" size 17 color "#bcaec0"
            null height 5
            textbutton "START" action Start() xsize 360
            textbutton "REAL ASSET LIBRARY" action ShowMenu('real_asset_gallery') xsize 360
            textbutton "LOAD" action ShowMenu('load') xsize 360
            textbutton "PREFERENCES" action ShowMenu('preferences') xsize 360
            textbutton "QUIT" action Quit(confirm=True) xsize 360

screen quick_menu():
    zorder 100
    if quick_menu:
        hbox:
            xalign .992 yalign .988 spacing 7
            textbutton "Back" action Rollback() text_size 17
            textbutton "Save" action ShowMenu('save') text_size 17
            textbutton "Load" action ShowMenu('load') text_size 17
            textbutton "Assets" action ShowMenu('real_asset_gallery') text_size 17
            textbutton "Prefs" action ShowMenu('preferences') text_size 17
            textbutton "Menu" action ShowMenu('main_menu') text_size 17

screen real_asset_gallery():
    tag menu
    use game_menu("Real Asset Library"):
        viewport:
            xfill True
            ymaximum 540
            draggable True
            mousewheel True
            scrollbars "vertical"
            vbox:
                spacing 15
                text "CHARACTER VARIANTS" size 30 bold True color "#ef9bea"
                for rid, nm in [
                    ("avery","Avery Lane"),("mia","Mia Hart"),("chloe","Chloe Vale"),
                    ("naomi","Naomi Cross"),("lila","Lila Morgan"),("rhea","Rhea Park")]:
                    text "{} — {} variants".format(nm, len(WB_REAL_CHARACTER_VARIANTS[rid])) size 23 bold True
                    vpgrid:
                        cols 6
                        spacing 7
                        xfill True
                        ysize 185
                        draggable True
                        mousewheel True
                        for p in WB_REAL_CHARACTER_VARIANTS[rid]:
                            button:
                                xsize 150 ysize 175
                                action Show("real_asset_viewer", path=p)
                                background Solid("#211729")
                                add Transform(p, fit="contain", xysize=(140,165)) xalign .5 yalign .5
                text "ENVIRONMENTS" size 30 bold True color "#ef9bea"
                vpgrid:
                    cols 4
                    spacing 10
                    xfill True
                    for p in WB_REAL_BACKGROUNDS:
                        button:
                            xsize 240 ysize 160
                            action Show("real_asset_viewer", path=p)
                            add Transform(p, xysize=(230,150)) xalign .5 yalign .5
                text "PROPS / UI" size 30 bold True color "#ef9bea"
                grid 5 2:
                    spacing 10
                    for p in WB_REAL_PROPS:
                        button:
                            xsize 190 ysize 160
                            action Show("real_asset_viewer", path=p)
                            add Transform(p, xysize=(180,150)) xalign .5 yalign .5

screen real_asset_viewer(path):
    modal True
    zorder 250
    add Solid("#050307ee")
    frame:
        xalign .5 yalign .5
        xsize 1220 ysize 680
        background Solid("#100b15fa")
        fixed:
            xfill True yfill True
            add Transform(path, fit="contain", xysize=(1120,610)) xalign .5 yalign .45
            textbutton "Close" action Hide("real_asset_viewer") xalign .98 yalign .98
