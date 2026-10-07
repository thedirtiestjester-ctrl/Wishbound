# Wishbound v0.4 - reviewed AstRef pack browser.
# Pack status: 76 reviewed assets committed and packaged.
# Loaded after z_asset_ui.rpy and therefore owns the final main/quick menu definitions.

init -15 python:
    WB_ASTREF_SAFE_FILES = sorted([
        f for f in renpy.list_files()
        if f.startswith("images/astref_safe/")
        and f.lower().endswith((".png", ".jpg", ".jpeg", ".webp"))
    ])

screen quick_menu():
    zorder 100
    if quick_menu:
        hbox:
            xalign .992 yalign .988 spacing 7
            textbutton "Back" action Rollback() text_size 17
            textbutton "Save" action ShowMenu('save') text_size 17
            textbutton "Load" action ShowMenu('load') text_size 17
            textbutton "Gallery" action ShowMenu('asset_gallery') text_size 17
            textbutton "AstRef" action ShowMenu('astref_safe_gallery') text_size 17
            textbutton "Prefs" action ShowMenu('preferences') text_size 17
            textbutton "Menu" action ShowMenu('main_menu') text_size 17

screen main_menu():
    tag menu
    add "images/bg_title.png"
    frame:
        xalign .82 yalign .54
        background Solid("#0b0810dd")
        padding (32, 28)
        vbox:
            spacing 11
            text "WISHBOUND" size 54 bold True color "#fff5ff"
            text "Her Morning" size 27 color "#df8bdd"
            text "v0.4 • Expanded Visual Library" size 17 color "#bcaec0"
            null height 5
            textbutton "START" action Start() xsize 360
            textbutton "VISUAL ARCHIVE" action ShowMenu('asset_gallery') xsize 360
            textbutton "ASTREF LIBRARY" action ShowMenu('astref_safe_gallery') xsize 360
            textbutton "LOAD" action ShowMenu('load') xsize 360
            textbutton "PREFERENCES" action ShowMenu('preferences') xsize 360
            textbutton "QUIT" action Quit(confirm=True) xsize 360

screen astref_safe_gallery():
    tag menu
    use game_menu("AstRef Library"):
        vbox:
            spacing 10
            text "{} reviewed environments & props".format(len(WB_ASTREF_SAFE_FILES)) size 22 color "#bcaec0"
            text "Wishbound-native IDs only. Tap an asset for a full preview." size 18 color "#8f8196"
            vpgrid:
                cols 4
                spacing 12
                xfill True
                ymaximum 500
                draggable True
                mousewheel True
                scrollbars "vertical"
                for p in WB_ASTREF_SAFE_FILES:
                    button:
                        xsize 245 ysize 180
                        action Show("astref_safe_viewer", path=p)
                        background Solid("#251c2ddd")
                        hover_background Solid("#3b2747ee")
                        fixed:
                            xfill True yfill True
                            add Transform(p, xysize=(225, 140)) xalign .5 yalign .15
                            text p.rsplit("/",1)[-1].split(".")[0].upper() size 14 xalign .5 yalign .94 color "#e8dfea"

screen astref_safe_viewer(path):
    modal True
    zorder 250
    add Solid("#050307ee")
    frame:
        xalign .5 yalign .5
        xsize 1220 ysize 680
        background Solid("#100b15fa")
        padding (20,20)
        fixed:
            xfill True yfill True
            add Transform(path, xysize=(1140, 590)) xalign .5 yalign .42
            text path.rsplit("/",1)[-1].split(".")[0].upper() size 20 xalign .5 yalign .965 color "#df8bdd"
            textbutton "Close" action Hide("astref_safe_viewer") xalign .98 yalign .98
