# Нихуёво, а? Ахах. Всё до безумия просто, но поебаться придётся. Как же без этого?
# Скрипт модлоадера присрал @b3rg3n.
python early:
    mods = {}

init -501 screen modsloader:
    tag menu

    frame:
        style "mods_menu_frame"

    textbutton _("Вернуться"):
        xpos 40 ypos 660
        action [Hide("modsloader"), Show("main_menu")]

    vbox:
        for lbl, name in sorted(mods.items()):
            textbutton name xpos 40 ypos 260 action Start(lbl)


init -1 style mods_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/modsovr.webp"
