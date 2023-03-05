#Жесты
define config.variants = ["phone", "tablet", "touch", "ios", None]

define config.gestures = { "n" : "game_menu",
                           "w" : "help",
                           "e" : "toggle_skip",
                           "s" : "hide_windows"}
init -1700 python:
    _game_menu_screen = "save"
