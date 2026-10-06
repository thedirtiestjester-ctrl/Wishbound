style default:
    font "DejaVuSans.ttf"
    color "#f7f1f8"
    size 28

style button:
    background Frame("gui/button.png", 18, 18)
    hover_background Frame("gui/button.png", 18, 18)
    padding (22, 14)

style button_text:
    color "#e4d9e7"
    hover_color "#ffffff"
    selected_color "#df8bdd"
    size 27
    xalign 0.5

screen say(who, what):
    window:
        id "window"
        xalign 0.5
        yalign 1.0
        xsize 1280
        ysize 220
        background "gui/textbox.png"
        if who is not None:
            text who id "who" xpos 80 ypos 18 size 34 color "#ef9bea" bold True
        text what id "what" xpos 80 ypos 68 xsize 1120 size 30

screen input(prompt):
    window:
        xalign .5 yalign .85 xsize 900 ysize 220
        background Solid("#17121ddd")
        vbox:
            xalign .5 yalign .5 spacing 20
            text prompt xalign .5
            input id "input" xalign .5 length 32

screen choice(items):
    vbox:
        xalign .5
        yalign .62
        spacing 14
        for i in items:
            textbutton i.caption action i.action xsize 780 text_xalign .5

screen quick_menu():
    zorder 100
    if quick_menu:
        hbox:
            xalign .98 yalign .985 spacing 12
            textbutton "Back" action Rollback() text_size 20
            textbutton "Save" action ShowMenu('save') text_size 20
            textbutton "Load" action ShowMenu('load') text_size 20
            textbutton "Prefs" action ShowMenu('preferences') text_size 20
            textbutton "Menu" action ShowMenu('main_menu') text_size 20

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
            null height 14
            textbutton "START" action Start() xsize 360
            textbutton "LOAD" action ShowMenu('load') xsize 360
            textbutton "PREFERENCES" action ShowMenu('preferences') xsize 360
            textbutton "QUIT" action Quit(confirm=True) xsize 360

screen game_menu(title, scroll=None, yinitial=0.0):
    tag menu
    add Solid("#0c0912")
    frame:
        xalign .5 yalign .5 xsize 1160 ysize 650
        background Solid("#17121df5")
        padding (35, 30)
        has vbox
        hbox:
            xfill True
            text title size 42 bold True color "#ef9bea"
            textbutton "Return" action Return() xalign 1.0
        null height 18
        transclude

screen save():
    tag menu
    use file_slots(_("Save"))

screen load():
    tag menu
    use file_slots(_("Load"))

screen file_slots(title):
    use game_menu(title):
        vbox:
            spacing 14
            hbox:
                spacing 10
                textbutton "Page 1" action FilePage(1)
                textbutton "Page 2" action FilePage(2)
                textbutton "Page 3" action FilePage(3)
            grid 3 2:
                spacing 18
                for i in range(1, 7):
                    button:
                        xsize 345 ysize 205
                        action FileAction(i)
                        background Solid("#251c2ddd")
                        vbox:
                            xalign .5 yalign .5 spacing 8
                            text "Slot [i]" size 25 bold True xalign .5
                            text FileTime(i, format=_('%b %d, %H:%M'), empty=_('Empty')) size 20 xalign .5
                            text FileSaveName(i) size 19 xalign .5

screen preferences():
    tag menu
    use game_menu(_("Preferences")):
        vbox:
            spacing 24
            text "Text speed" size 28 bold True
            bar value Preference("text speed") xsize 700
            text "Auto-forward" size 28 bold True
            bar value Preference("auto-forward time") xsize 700
            text "Lewd Reactions" size 28 bold True
            hbox:
                spacing 14
                textbutton "ON" action SetField(persistent, "spice_mode", True)
                textbutton "MILD" action SetField(persistent, "spice_mode", False)
            text "Lewd mode changes suggestive reaction lines only; it does not add explicit sex scenes." size 21 color "#bcaec0" xsize 900

screen confirm(message, yes_action, no_action):
    modal True
    zorder 200
    add Solid("#000000aa")
    frame:
        xalign .5 yalign .5 xsize 760
        background Solid("#17121df5")
        padding (35,35)
        vbox:
            spacing 24
            text message xalign .5 text_align .5
            hbox:
                xalign .5 spacing 20
                textbutton "Yes" action yes_action
                textbutton "No" action no_action

screen notify(message):
    zorder 300
    frame at notify_appear:
        xalign .5 yalign .08
        background Solid("#211628ee")
        padding (22,12)
        text message size 22
    timer 2.5 action Hide('notify')

transform notify_appear:
    alpha 0 yoffset -20
    ease .2 alpha 1 yoffset 0
    pause 2.0
    ease .25 alpha 0

screen protagonist_select():
    modal True
    add Solid("#0a0710ee")
    vbox:
        xalign .5 yalign .5 spacing 18
        text "WHO MAKES THE WISH?" size 44 bold True xalign .5
        text "All protagonists are adults." size 22 color "#bdaec0" xalign .5
        hbox:
            spacing 18 xalign .5
            for pid, nm, age, blurb in [
                ('evan','Evan Cole',28,'Shy IT support. Wants to be noticed.'),
                ('marcus','Marcus Reed',31,'Burned-out salesman. Wants life to feel easier.'),
                ('theo','Theo Park',25,'Cocky streamer. Thinks he would make a gorgeous woman.')]:
                button:
                    xsize 350 ysize 260
                    action Return(pid)
                    background Solid("#251c2ddd")
                    hover_background Solid("#3b2747ee")
                    vbox:
                        xalign .5 yalign .5 spacing 10
                        text nm size 31 bold True xalign .5
                        text "Age [age]" size 21 color "#df8bdd" xalign .5
                        text blurb size 22 xsize 290 text_align .5 xalign .5

screen reality_select():
    modal True
    add Solid("#0a0710ee")
    vbox:
        xalign .5 yalign .5 spacing 18
        text "HOW DOES REALITY ANSWER?" size 42 bold True xalign .5
        text "Prototype selector: each life demonstrates a different rewrite." size 21 color "#bdaec0" xalign .5
        grid 3 2:
            spacing 16
            xalign .5
            for rid, nm, age, blurb in [
                ('avery','Avery Lane',26,'Event planner. Social confidence and a complicated flirtation.'),
                ('mia','Mia Hart',29,'Consultant. Married life expects instant familiarity.'),
                ('chloe','Chloe Vale',25,'Creator. Public confidence, fiancé, and cameras everywhere.'),
                ('naomi','Naomi Cross',33,'Tattoo artist. Studio owner with an unresolved ex.'),
                ('lila','Lila Morgan',28,'Pastry chef. Secret girlfriend and a busy café staff.'),
                ('rhea','Rhea Park',30,'DJ/club manager. Nightlife reputation and a knowing bartender.')]:
                button:
                    xsize 350 ysize 205
                    action Return(rid)
                    background Solid("#251c2ddd")
                    hover_background Solid("#3b2747ee")
                    vbox:
                        xalign .5 yalign .5 spacing 7
                        text nm size 29 bold True xalign .5
                        text "Age [age]" size 20 color "#df8bdd" xalign .5
                        text blurb size 19 xsize 300 text_align .5 xalign .5

screen bedroom_hub():
    modal True
    frame:
        xalign .02 yalign .12 xsize 330
        background Solid("#0d0a12d8")
        padding (20,18)
        vbox:
            spacing 10
            text "REALITY EVIDENCE" size 25 bold True color "#ef9bea"
            text "[evidence_count]/4 discovered" size 21
            bar value StaticValue(evidence_count, 4) xsize 285
            text "Curiosity: [curiosity]" size 19
            text "Boldness: [boldness]" size 19
            text "Acceptance: [acceptance]" size 19
    vbox:
        xalign .78 yalign .52 spacing 14
        text "What do you check?" size 32 bold True xalign .5
        textbutton "MIRROR" action Return('mirror') xsize 380 sensitive not seen_mirror
        textbutton "PHONE" action Return('phone') xsize 380 sensitive not seen_phone
        textbutton "CLOSET" action Return('closet') xsize 380 sensitive not seen_closet
        textbutton "WALLET / ID" action Return('wallet') xsize 380 sensitive not seen_wallet
        if evidence_count >= 3:
            textbutton "FACE THE REST OF THE MORNING" action Return('continue') xsize 380

screen evidence_card(title, body):
    modal True
    add Solid("#000000aa")
    frame:
        xalign .5 yalign .5 xsize 820
        background Solid("#17121df5")
        padding (36,32)
        vbox:
            spacing 22
            text title size 38 bold True color "#ef9bea" xalign .5
            text body size 25 xsize 740
            textbutton "Got it" action Return() xalign .5
