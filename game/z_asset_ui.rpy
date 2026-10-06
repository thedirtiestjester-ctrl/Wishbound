# Wishbound v0.3 - asset integration layer.
# Loaded after screens.rpy so these screen definitions replace the prototype layouts.

screen quick_menu():
    zorder 100
    if quick_menu:
        hbox:
            xalign .985 yalign .985 spacing 9
            textbutton "Back" action Rollback() text_size 19
            textbutton "Save" action ShowMenu('save') text_size 19
            textbutton "Load" action ShowMenu('load') text_size 19
            textbutton "Gallery" action ShowMenu('asset_gallery') text_size 19
            textbutton "Prefs" action ShowMenu('preferences') text_size 19
            textbutton "Menu" action ShowMenu('main_menu') text_size 19

screen main_menu():
    tag menu
    add "images/bg_title.png"
    frame:
        xalign .82 yalign .56
        background Solid("#0b0810cc")
        padding (35, 35)
        vbox:
            spacing 16
            text "WISHBOUND" size 56 bold True color "#fff5ff"
            text "Her Morning" size 28 color "#df8bdd"
            text "v0.3 • Asset Integration" size 18 color "#bcaec0"
            null height 10
            textbutton "START" action Start() xsize 360
            textbutton "VISUAL ARCHIVE" action ShowMenu('asset_gallery') xsize 360
            textbutton "LOAD" action ShowMenu('load') xsize 360
            textbutton "PREFERENCES" action ShowMenu('preferences') xsize 360
            textbutton "QUIT" action Quit(confirm=True) xsize 360

screen asset_route_card(rid, nm, age, blurb, sprite):
    button:
        xsize 350 ysize 245
        action Return(rid)
        background Solid("#251c2ddd")
        hover_background Solid("#3b2747ee")
        fixed:
            xfill True yfill True
            add Transform(sprite, zoom=.22) xalign .12 yalign 1.0
            frame:
                xpos 115 ypos 16 xsize 220 ysize 210
                background Solid("#0d0a12b8")
                padding (14,12)
                vbox:
                    spacing 5
                    text nm size 27 bold True xalign .5
                    text "Age [age]" size 18 color "#df8bdd" xalign .5
                    text blurb size 17 xsize 190 text_align .5 xalign .5

screen reality_select():
    modal True
    add "images/bg_void.png"
    add Solid("#08050bd8")
    vbox:
        xalign .5 yalign .5 spacing 15
        text "HOW DOES REALITY ANSWER?" size 42 bold True xalign .5
        text "Choose the adult life reality rewrites around you." size 20 color "#bdaec0" xalign .5
        grid 3 2:
            spacing 14
            xalign .5
            use asset_route_card('avery','Avery Lane',26,'Event planner. Social confidence and a complicated flirtation.','images/sprite_avery_lane.png')
            use asset_route_card('mia','Mia Hart',29,'Consultant. Married life expects instant familiarity.','images/sprite_mia_hart.png')
            use asset_route_card('chloe','Chloe Vale',25,'Creator. Public confidence, fiancé, and cameras everywhere.','images/sprite_chloe_vale.png')
            use asset_route_card('naomi','Naomi Cross',33,'Tattoo artist. Studio owner with an unresolved ex.','images/sprite_naomi_cross.png')
            use asset_route_card('lila','Lila Morgan',28,'Pastry chef. Secret girlfriend and a busy café staff.','images/sprite_lila_morgan.png')
            use asset_route_card('rhea','Rhea Park',30,'DJ/club manager. Nightlife reputation and a knowing bartender.','images/sprite_rhea_park.png')

screen bedroom_hub():
    modal True
    frame:
        xalign .02 yalign .08 xsize 350 ysize 560
        background Solid("#0d0a12d8")
        padding (20,18)
        vbox:
            spacing 9
            text "REALITY EVIDENCE" size 25 bold True color "#ef9bea"
            text "[evidence_count]/4 discovered" size 21
            bar value StaticValue(evidence_count, 4) xsize 300
            text "Curiosity: [curiosity]" size 19
            text "Boldness: [boldness]" size 19
            text "Acceptance: [acceptance]" size 19
            null height 4
            if reality_id == 'avery':
                add Transform('images/sprite_avery_lane.png', zoom=.23) xalign .5
            elif reality_id == 'mia':
                add Transform('images/sprite_mia_hart.png', zoom=.23) xalign .5
            elif reality_id == 'chloe':
                add Transform('images/sprite_chloe_vale.png', zoom=.23) xalign .5
            elif reality_id == 'naomi':
                add Transform('images/sprite_naomi_cross.png', zoom=.20) xalign .5
            elif reality_id == 'lila':
                add Transform('images/sprite_lila_morgan.png', zoom=.20) xalign .5
            else:
                add Transform('images/sprite_rhea_park.png', zoom=.20) xalign .5
    vbox:
        xalign .79 yalign .50 spacing 14
        text "What do you check?" size 32 bold True xalign .5
        textbutton "MIRROR" action Return('mirror') xsize 380 sensitive not seen_mirror
        textbutton "PHONE" action Return('phone') xsize 380 sensitive not seen_phone
        textbutton "CLOSET" action Return('closet') xsize 380 sensitive not seen_closet
        textbutton "WALLET / ID" action Return('wallet') xsize 380 sensitive not seen_wallet
        if evidence_count >= 3:
            textbutton "FACE THE REST OF THE MORNING" action Return('continue') xsize 380

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
                spacing 18
                text "CHARACTERS" size 30 bold True color "#ef9bea"
                text "Wishbound-owned character assets currently wired into the routes." size 19 color "#bcaec0"
                grid 3 2:
                    spacing 14
                    for nm, sprite in [
                        ('Avery Lane','images/sprite_avery_lane.png'),
                        ('Mia Hart','images/sprite_mia_hart.png'),
                        ('Chloe Vale','images/sprite_chloe_vale.png'),
                        ('Naomi Cross','images/sprite_naomi_cross.png'),
                        ('Lila Morgan','images/sprite_lila_morgan.png'),
                        ('Rhea Park','images/sprite_rhea_park.png')]:
                        frame:
                            xsize 330 ysize 235
                            background Solid("#251c2ddd")
                            fixed:
                                xfill True yfill True
                                add Transform(sprite, zoom=.22) xalign .5 yalign .92
                                frame:
                                    xalign .5 yalign 1.0 xsize 300 ysize 44
                                    background Solid("#0a0710dd")
                                    text nm size 21 bold True xalign .5 yalign .5
                null height 8
                text "LOCATIONS" size 30 bold True color "#ef9bea"
                text "All current route locations are now part of the playable visual set." size 19 color "#bcaec0"
                for nm, bg in [
                    ('Bedroom','images/bg_bedroom.png'),
                    ('Bathroom / Mirror','images/bg_bathroom.png'),
                    ('Closet','images/bg_closet.png'),
                    ('Phone / Digital Life','images/bg_phone.png'),
                    ('Kitchen','images/bg_kitchen.png'),
                    ('City','images/bg_city.png'),
                    ('Event Venue','images/bg_event_venue.png'),
                    ('Office Lobby','images/bg_office_lobby.png'),
                    ('Photo Studio','images/bg_photo_studio.png'),
                    ('Tattoo Studio','images/bg_tattoo_studio.png'),
                    ('Café','images/bg_cafe.png'),
                    ('Rooftop Club','images/bg_rooftop_club.png'),
                    ('Wish Void','images/bg_void.png')]:
                    frame:
                        xsize 1020 ysize 185
                        background Solid("#251c2ddd")
                        hbox:
                            spacing 18
                            add Transform(bg, zoom=.21) yalign .5
                            vbox:
                                yalign .5 spacing 8
                                text nm size 28 bold True
                                text bg size 18 color "#bcaec0"
