define config.name = "Doki Doki Literature Club!"
define config.save_on_mobile_background = False
define gui.show_name = False
define config.version = "1.1.5"
define gui.about = _("")
define build.name = "DDLC"
define config.has_sound = True
define config.has_music = True
define config.has_voice = False
define config.main_menu_music = "bgm/1.ogg" #audio.t1
define config.enter_transition = Dissolve(.2)
define config.exit_transition = Dissolve(.2)
define config.after_load_transition = None
define config.end_game_transition = Dissolve(.5)
define config.window = "auto"
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)
default preferences.text_cps = 50
default preferences.afm_time = 15
default preferences.music_volume = 0.75
default preferences.sfx_volume = 0.75
define config.save_directory = "DDLC-modloader"
define config.window_icon = "gui/window_icon.webp"
define config.allow_skipping = True
define config.has_autosave = False
define config.autosave_on_quit = False
define config.autosave_slots = 0
define config.layers = [ 'master', 'transient', 'screens', 'overlay', 'front' ]
define config.image_cache_size = 64
define config.predict_statements = 50
define config.rollback_enabled = config.developer
define config.menu_clear_layers = ["front"]
define config.gl_test_image = "white"

python early:
    config.allow_duplicate_labels = True
    mods = {}

init python:
    if len(renpy.loadsave.location.locations) > 1: del(renpy.loadsave.location.locations[1])
    renpy.game.preferences.pad_enabled = False
    def replace_text(s):
        s = s.replace('--', u'\u2014') 
        s = s.replace(' - ', u'\u2014') 
        return s
    config.replace_text = replace_text

    def game_menu_check():
        if quick_menu: renpy.call_in_new_context('_game_menu')

    config.game_menu_action = game_menu_check

    def force_integer_multiplier(width, height):
        if float(width) / float(height) < float(config.screen_width) / float(config.screen_height):
            return (width, float(width) / (float(config.screen_width) / float(config.screen_height)))
        else:
            return (float(height) * (float(config.screen_width) / float(config.screen_height)), height)

init -2 python:
    layout.ARE_YOU_SURE = _("Вы уверены?")
    layout.DELETE_SAVE = _("Вы действительно хотите удалить сохранение?")
    layout.OVERWRITE_SAVE = _("Вы действительно хотите перезаписать сохранение?")
    layout.LOADING = _("При загрузке несохранённое прохождение будет утеряно.\nВы уверены, что хотите продолжить?")
    layout.QUIT = _("Вы действительно хотите выйти?")
    layout.MAIN_MENU = _("Вы действительно хотите вернуться в главное меню?\nЭто приведёт к потере прогресса.")
    layout.END_REPLAY = _("Вы уверены, что хотите остановить повтор?")
    layout.SLOW_SKIP = _("Вы уверены, что хотите начать пропуск текста?")
    layout.FAST_SKIP_UNSEEN = _("Вы уверены, что хотите пропустить непрочитанный текст до следующего выбора?")
    layout.FAST_SKIP_SEEN = _("Вы уверены, что хотите перейти к следующему выбору?")

init -999:
    define config.variants = [ "large", "pc", "touch", None ]
    define config.hw_video = False
    $ number_of_options = 13
    $ bergenmods = False
    $ modistalled = False