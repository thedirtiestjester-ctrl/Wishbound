define config.name = _("Wishbound: Her Morning")
define config.version = "0.6.0"
define build.name = "wishbound_her_morning"
define config.save_directory = "WishboundHerMorning-02"
define config.window = "auto"
define config.has_sound = True
define config.has_music = True
define config.has_voice = False
define config.enter_transition = Dissolve(.20)
define config.exit_transition = Dissolve(.20)
define config.after_load_transition = Dissolve(.20)
define config.end_game_transition = Fade(.35, .15, .35)
define config.default_text_cps = 35
define config.default_afm_time = 15

define config.screen_width = 1280
define config.screen_height = 720

init python:
    build.classify('**.rpy', None)
    build.classify('**.rpyc', 'archive')
    build.classify('game/images/**', 'archive')
    build.classify('game/gui/**', 'archive')
    build.documentation('*.md')

# Sanitized redistributable build trigger v0.5.2
