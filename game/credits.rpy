init python:
    import datetime

image credits_cg1:
    "images/cg/credits/1.webp"
    size (640, 360)
    8.6
    "images/menu/notfound.webp"

image credits_cg2:
    "images/cg/credits/2.webp"
    size (640, 360)
    8.6
    "images/menu/notfound.webp"

image credits_cg3:
    "images/cg/credits/3.webp"
    size (640, 360)
    8.6
    "images/menu/notfound.webp"

image credits_cg4:
    "images/cg/credits/4.webp"
    size (640, 360)
    8.6
    "images/menu/notfound.webp"

image credits_cg5:
    "images/cg/credits/5.webp"
    size (640, 360)
    8.6
    "images/menu/notfound.webp"

image credits_cg6:
    "images/cg/credits/6.webp"
    size (640, 360)
    8.6
    "images/menu/notfound.webp"

image credits_cg7:
    "images/cg/credits/7.webp"
    size (640, 360)
    8.6
    "images/menu/notfound.webp"

image credits_cg8:
    "images/cg/credits/8.webp"
    size (640, 360)
    8.6
    "images/menu/notfound.webp"

image credits_cg9:
    "images/cg/credits/9.webp"
    size (640, 360)
    8.6
    "images/menu/notfound.webp"

image credits_cg10:
    "images/cg/credits/10.webp"
    size (640, 360)
    8.6
    "images/menu/notfound.webp"

image credits_cg1_locked:
    "images/cg/credits/1b.webp"
    size (640, 360)
    8.6
    "images/menu/notfound.webp"

image credits_cg2_locked:
    "images/cg/credits/2b.webp"
    size (640, 360)
    8.6
    "images/menu/notfound.webp"

image credits_cg3_locked:
    "images/cg/credits/3b.webp"
    size (640, 360)
    8.6
    "images/menu/notfound.webp"

image credits_cg4_locked:
    "images/cg/credits/4b.webp"
    size (640, 360)
    8.6
    "images/menu/notfound.webp"

image credits_cg5_locked:
    "images/cg/credits/5b.webp"
    size (640, 360)
    8.6
    "images/menu/notfound.webp"

image credits_cg6_locked:
    "images/cg/credits/6b.webp"
    size (640, 360)
    8.6
    "images/menu/notfound.webp"

image credits_cg7_locked:
    "images/cg/credits/7b.webp"
    size (640, 360)
    8.6
    "images/menu/notfound.webp"

image credits_cg8_locked:
    "images/cg/credits/8b.webp"
    size (640, 360)
    8.6
    "images/menu/notfound.webp"

image credits_cg9_locked:
    "images/cg/credits/9b.webp"
    size (640, 360)
    8.6
    "images/menu/notfound.webp"

image credits_cg10_locked:
    "images/cg/credits/10b.webp"
    size (640, 360)
    8.6
    "images/menu/notfound.webp"

image credits_cg1_clearall:
    "images/cg/credits/1.webp"
    size (640, 360)

image credits_cg2_clearall:
    "images/cg/credits/2.webp"
    size (640, 360)

image credits_cg3_clearall:
    "images/cg/credits/3.webp"
    size (640, 360)

image credits_cg4_clearall:
    "images/cg/credits/4.webp"
    size (640, 360)

image credits_cg5_clearall:
    "images/cg/credits/5.webp"
    size (640, 360)

image credits_cg6_clearall:
    "images/cg/credits/6.webp"
    size (640, 360)

image credits_cg7_clearall:
    "images/cg/credits/7.webp"
    size (640, 360)

image credits_cg8_clearall:
    "images/cg/credits/8.webp"
    size (640, 360)

image credits_cg9_clearall:
    "images/cg/credits/9.webp"
    size (640, 360)

image credits_cg10_clearall:
    "images/cg/credits/10.webp"
    size (640, 360)

image credits_logo:
    "gui/logo.webp"
    truecenter
    zoom 0.6 alpha 0 subpixel True
    linear 2.0 alpha 1
    4.5
    linear 2.0 alpha 0

image credits_ts:
    "images/bg/splash-white.webp"
    xalign 0.5 yalign 0.6
    zoom 0.65 alpha 0 subpixel True
    linear 2.0 alpha 1
    4.5
    linear 2.0 alpha 0

style credits_header:
    font "gui/font/RifficFree-Bold.ttf"
    color "#ffaae6"
    size 36
    text_align 0.5
    outlines []

style credits_text:
    font "gui/font/Halogen.ttf"
    color "#fff"
    size 36
    text_align 0.5
    outlines []

style monika_credits_text:
    font "gui/font/song.ttf"
    color "#fff"
    size 40
    text_align 0.5
    outlines []

image credits_header = ParameterizedText(style="credits_header", ypos=-40)
image credits_text = ParameterizedText(style="credits_text", ypos=40)
image monika_credits_text = ParameterizedText(style="monika_credits_text", xalign=0.5)


transform credits_scroll:
    subpixel True
    yoffset 740
    linear 15 yoffset -380

transform credits_text_scroll:
    anchor (0.5, 0.5) subpixel True
    yoffset 920
    linear 15 yoffset -200

transform credits_sticker_scroll:
    subpixel True
    yoffset 940
    7.8
    linear 15 yoffset -180

transform credits_scroll_right:
    xalign 0.9
    credits_scroll

transform credits_scroll_left:
    xalign 0.1
    credits_scroll

transform credits_text_scroll_right:
    xpos 960
    credits_text_scroll

transform credits_text_scroll_left:
    xpos 320
    credits_text_scroll

transform credits_sticker_1:
    yanchor 1.00
    xalign 0.32
    credits_sticker_scroll
transform credits_sticker_2:
    yanchor 1.00
    xalign 0.44
    credits_sticker_scroll
transform credits_sticker_3:
    yanchor 1.00
    xalign 0.56
    credits_sticker_scroll
transform credits_sticker_4:
    yanchor 1.00
    xalign 0.68
    credits_sticker_scroll

define credits_ypos = 250

image mcredits_1a:
    ypos credits_ypos
    xoffset -205
    "black"
    10.33
    Text("Every day,", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.webp", 13.0, ramplen=4, alpha=False)
image mcredits_1b:
    ypos credits_ypos
    xoffset -35
    "black"
    11.75
    Text("I imagine a future where", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.webp", 12.0, ramplen=4, alpha=False)
image mcredits_1c:
    ypos credits_ypos
    xoffset 170
    "black"
    13.76
    Text("I can be with you", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.webp", 15.0, ramplen=4, alpha=False)
image mcredits_2a:
    ypos credits_ypos + 50
    xoffset -226
    "black"
    19.45
    Text("In my hand", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.webp", 13.0, ramplen=4, alpha=False)
image mcredits_2b:
    ypos credits_ypos + 50
    xoffset -10
    "black"
    20.9
    Text(" is a pen that will write a poem", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.webp", 9.0, ramplen=4, alpha=False)
image mcredits_2c:
    ypos credits_ypos + 50
    xoffset 225
    "black"
    23.27
    Text("of me and you", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.webp", 15.0, ramplen=4, alpha=False)

image mcredits_3:
    ypos credits_ypos + 100
    "black"
    28.35
    Text("The ink flows down into a dark puddle", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.webp", 16.0, ramplen=4, alpha=False)

image mcredits_4:
    ypos credits_ypos + 150
    xoffset -5
    "black"
    32.9
    Text(" Just move your hand -- write the way into his heart!", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.webp", 9.0, ramplen=4, alpha=False)

image mcredits_5:
    ypos credits_ypos + 200
    "black"
    37.5
    Text("But in this world of infinite choices", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.webp", 16.0, ramplen=4, alpha=False)

image mcredits_6a:
    ypos credits_ypos + 250
    xoffset -145
    "black"
    42.0
    Text(" What will it take", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.webp", 10.0, ramplen=4, alpha=False)
image mcredits_6b:
    ypos credits_ypos + 250
    xoffset 85
    "black"
    43.47
    Text(" just to find that special day?", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.webp", 10.0, ramplen=4, alpha=False)

image mcredits_7:
    "black"
    alpha 0.0
    48.62
    linear 1.5 alpha 1.0

image mcredits_1_test:
    ypos credits_ypos + 300
    Text("What will it take just to find that special day?", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.webp", 15.0, ramplen=4)

image end_glitch1:
    "bg/end-glitch1.webp"
    alpha 0.0
    time 1.0
    alpha 1.0
    block:
        yoffset 1280 ytile 2
        linear 1 yoffset 0
        repeat
    time 9.45
    "end_glitch2"
    time 22.1
    "end_glitch3"
    time 28.65
    "end_glitch4"

image end_glitch2:
    "bg/end-glitch2.webp"
    block:
        yoffset 1280 ytile 2
        linear 4 yoffset 0
        repeat

image end_glitch3:
    "bg/end-glitch3.webp"
    block:
        yoffset 1280 ytile 2
        linear 4 yoffset 0
        repeat

image end_glitch4:
    parallel:
        "bg/end-glitch4.webp"
        1.25
        "bg/end-glitch3.webp"
        0.1
        repeat
    parallel:
        yoffset 1280 ytile 2
        linear 4 yoffset 0
        repeat

label credits:
    $ persistent.autoload = "credits"
    $ config.keymap['game_menu'] = []
    $ config.keymap['hide_windows'] = []
    $ renpy.display.behavior.clear_keymap_cache()
    $ quick_menu = False
    $ config.skipping = False
    $ config.allow_skipping = False
    scene black
    play music "bgm/end-voice.ogg" noloop

    show noise zorder 9:
        alpha 0.0
        linear 1.5 alpha 1.0
        time 2.0
        parallel:
            0.05
            choice:
                alpha 0.5
            choice:
                alpha 0.75
            choice:
                alpha 1.0
            repeat
        parallel:
            linear 0.375 alpha 0.7
            linear 0.375 alpha 1.0
        time 2.75
        alpha 0.95
        time 6.45
        alpha 0.3
        time 6.95
        alpha 0.9
        time 8.65
        linear 0.8 alpha 0
        alpha 0.5
        time 22.1
        alpha 0.85
        time 22.35
        alpha 0.5
        time 28.20
        alpha 0.3
        linear 0.45 alpha 0.9
        alpha 0.4
    show vignette zorder 10:
        alpha 0.75
        parallel:
            0.36
            alpha 0.75
            repeat
        parallel:
            0.49
            alpha 0.7
            repeat
    show end_glitch1 zorder 2
    show black as bar zorder 9:
        alpha 0.3
        size (1280,500)
        block:
            ypos 720
            linear 15 ypos -500
            repeat


    pause 41
    scene black
    pause 0.5
    $ consolehistory = []
    call updateconsole ("renpy.music.play(\"ddlc.ogg\")", "Проигрывается аудиозапись \"ddlc.ogg\"...") from _call_updateconsole
    pause 1.0
    call hideconsole from _call_hideconsole
    play music "<to 50.0>bgm/credits.ogg" noloop
    show mcredits_1a zorder 50
    show mcredits_1b zorder 49
    show mcredits_1c zorder 48
    show mcredits_2a zorder 47
    show mcredits_2b zorder 46
    show mcredits_2c zorder 45
    show mcredits_3 zorder 44
    show mcredits_4 zorder 43
    show mcredits_5 zorder 42
    show mcredits_6a zorder 41
    show mcredits_6b zorder 40
    show mcredits_7 zorder 51

    pause 50
    jump credits2

label credits2:
    python:
        sayoriTime = renpy.random.random() * 4 + 4
        natsukiTime = renpy.random.random() * 4 + 4
        yuriTime = renpy.random.random() * 4 + 4
        monikaTime = renpy.random.random() * 4 + 4
        sayoriPos = 0
        natsukiPos = 0
        yuriPos = 0
        monikaPos = 0
        sayoriOffset = 0
        natsukiOffset = 0
        yuriOffset = 0
        monikaOffset = 0
        sayoriZoom = 1
        natsukiZoom = 1
        yuriZoom = 1
        monikaZoom = 1
        imagenum = 0
    scene black
    $ consolehistory = []
    play music "<from 50.0>bgm/credits.ogg" noloop
    $ starttime = datetime.datetime.now()
    pause 0.88
    show credits_logo
    pause 9.12
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    show expression ("credits_cg1" + lockedtext) as credits_image_1 at credits_scroll_right
    show credits_header "Концепт и Геймдизайн" as credits_header_1 at credits_text_scroll_left
    show credits_text "Dan Salvato" as credits_text_1 at credits_text_scroll_left
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(16.95 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole ("os.remove(\"images/cg/n_cg1.webp\")", "n_cg1.webp успешно удалён.") from _call_updateconsole_1
    else:
        call updateconsole_clearall ("os.remove(\"images/cg/n_cg1.webp\")", "n_cg1.webp успешно удалён.") from _call_updateconsole_clearall
    show expression ("credits_cg2" + lockedtext) as credits_image_2 at credits_scroll_left
    show credits_header "Персонажи" as credits_header_2 at credits_text_scroll_right
    show credits_text "Satchely" as credits_text_2 at credits_text_scroll_right
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(26.05 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole ("os.remove(\"images/cg/n_cg2.webp\")", "n_cg2.webp успешно удалён.") from _call_updateconsole_2
    else:
        call updateconsole_clearall ("os.remove(\"images/cg/n_cg2.webp\")", "n_cg2.webp успешно удалён.") from _call_updateconsole_clearall_1
    show expression ("credits_cg3" + lockedtext) as credits_image_1 at credits_scroll_right
    show credits_header "Фоны" as credits_header_1 at credits_text_scroll_left
    show credits_text "Velinquent" as credits_text_1 at credits_text_scroll_left
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(35.15 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole ("os.remove(\"images/cg/y_cg1.webp\")", "y_cg1.webp успешно удалён.") from _call_updateconsole_3
    else:
        call updateconsole_clearall ("os.remove(\"images/cg/y_cg1.webp\")", "y_cg1.webp успешно удалён.") from _call_updateconsole_clearall_2
    show expression ("credits_cg4" + lockedtext) as credits_image_2 at credits_scroll_left
    show credits_header "Сценарий" as credits_header_2 at credits_text_scroll_right
    show credits_text "Dan Salvato" as credits_text_2 at credits_text_scroll_right
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(44.25 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole ("os.remove(\"images/cg/y_cg2.webp\")", "y_cg2.webp успешно удалён.") from _call_updateconsole_4
    else:
        call updateconsole_clearall ("os.remove(\"images/cg/y_cg2.webp\")", "y_cg2.webp успешно удалён.") from _call_updateconsole_clearall_3
    show expression ("credits_cg5" + lockedtext) as credits_image_1 at credits_scroll_right
    show credits_header "Музыка" as credits_header_1 at credits_text_scroll_left
    show credits_text "Dan Salvato" as credits_text_1 at credits_text_scroll_left
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(53.35 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole ("os.remove(\"images/cg/n_cg3.webp\")", "n_cg3.webp успешно удалён.") from _call_updateconsole_5
    else:
        call updateconsole_clearall ("os.remove(\"images/cg/n_cg3.webp\")", "n_cg3.webp успешно удалён.") from _call_updateconsole_clearall_4
    show expression ("credits_cg6" + lockedtext) as credits_image_2 at credits_scroll_left
    show credits_header "Вокал" as credits_header_2 at credits_text_scroll_right
    show credits_text "Jillian Ashcraft" as credits_text_2 at credits_text_scroll_right
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(62.45 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole ("os.remove(\"images/cg/y_cg3.webp\")", "y_cg3.webp успешно удалён.") from _call_updateconsole_6
    else:
        call updateconsole_clearall ("os.remove(\"images/cg/y_cg3.webp\")", "y_cg3.webp успешно удалён.") from _call_updateconsole_clearall_5
    show expression ("credits_cg7" + lockedtext) as credits_image_1 at credits_scroll_right
    show credits_header "Особая Благодарность\n\n\n\n\n" as credits_header_1 at credits_text_scroll_left
    show credits_text "Masha Gutin\nKagefumi\nDavid Evelyn\nCorey Shin\nAlecia Bardachino\nMatt Naples" as credits_text_1 at credits_text_scroll_left
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(71.55 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole ("os.remove(\"images/cg/s_cg1.webp\")", "s_cg1.webp успешно удалён.") from _call_updateconsole_7
    else:
        call updateconsole_clearall ("os.remove(\"images/cg/s_cg1.webp\")", "s_cg1.webp успешно удалён.") from _call_updateconsole_clearall_6
    show expression ("credits_cg8" + lockedtext) as credits_image_2 at credits_scroll_left
    show credits_header "Перевод на русский выполнен\n SUN-TEAM Studio\n\n\n\n\n" as credits_header_2 at credits_text_scroll_right
    show credits_text "MrSymon\niLight\nLorentain\nGMGamer\nStacy Martlet" as credits_text_2 at credits_text_scroll_right
    show s_sticker at credits_sticker_1
    show n_sticker at credits_sticker_2
    show y_sticker at credits_sticker_3
    show m_sticker at credits_sticker_4
    $ pause(80.60 - (datetime.datetime.now() - starttime).total_seconds())
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    if not persistent.clearall:
        call updateconsole ("os.remove(\"images/cg/s_cg2.webp\")", "s_cg2.webp успешно удалён.") from _call_updateconsole_8
    else:
        call updateconsole_clearall ("os.remove(\"images/cg/s_cg2.webp\")", "s_cg2.webp успешно удалён.") from _call_updateconsole_clearall_7
    $ pause(88.00 - (datetime.datetime.now() - starttime).total_seconds())
    show expression ("credits_cg9" + lockedtext) as credits_image_1 at credits_scroll_right
    show credits_header "Особая благодарность\n за помощь в переводе\n\n\n" as credits_header_1 at credits_text_scroll_left
    show credits_text "Aesthetic Dialectic\nRiaria" as credits_text_1 at credits_text_scroll_left
    show credits_header "Благодарность\n за порт на Android\n\n\n" as credits_header_1 at credits_text_scroll_left
    show credits_text "CuteRabbot (ex. Otorhin)\nBERGEN" as credits_text_1 at credits_text_scroll_left
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ pause(95.00 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole ("os.remove(\"images/cg/s_cg3.webp\")", "s_cg3.webp успешно удалён.") from _call_updateconsole_9
    else:
        call updateconsole_clearall ("os.remove(\"images/cg/s_cg3.webp\")", "s_cg3.webp успешно удалён.") from _call_updateconsole_clearall_8
    show expression ("credits_cg10" + lockedtext) as credits_image_2 at credits_scroll_left
    show credits_header "Особая Благодарность" as credits_header_2 at credits_text_scroll_right
    show credits_text "Моника\n[player]" as credits_text_2 at credits_text_scroll_right
    $ pause(104.10 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole ("os.remove(\"images/cg/m_cg1.webp\")", "m_cg1.webp успешно удалён.") from _call_updateconsole_10
    else:
        call updateconsole_clearall ("os.remove(\"images/cg/m_cg1.webp\")", "m_cg1.webp успешно удалён.") from _call_updateconsole_clearall_9

    call updateconsole ("os.remove(\"game/screens.rpy\")", "screens.rpy успешно удалён.") from _call_updateconsole_11
    call updateconsole ("os.remove(\"game/gui.rpy\")", "gui.rpy успешно удалён.") from _call_updateconsole_12
    call updateconsole ("os.remove(\"game/menu.rpy\")", "menu.rpy успешно удалён.") from _call_updateconsole_13
    call updateconsole ("os.remove(\"game/script.rpy\")", "script.rpy успешно удалён.") from _call_updateconsole_14
    $ pause(115.72 - (datetime.datetime.now() - starttime).total_seconds())
    call hideconsole from _call_hideconsole_1
    show credits_ts
    show credits_text "С любовью для вас":
        zoom 0.75 xalign 0.5 yalign 0.25 alpha 0 subpixel True
        linear 2.0 alpha 1
        4.5
        linear 2.0 alpha 0
    pause 9.3
    play sound page_turn
    show poem_end with Dissolve(1)
    label postcredits_loop:
        $ persistent.autoload = "postcredits_loop"
        $ config.keymap['game_menu'] = []
        $ config.keymap['hide_windows'] = []
        $ renpy.display.behavior.clear_keymap_cache()
        $ quick_menu = False
        $ config.skipping = False
        $ config.allow_skipping = False
        scene black
        show poem_end
        $ pause()
        call screen dialog(message="Ошибка: файл скрипта удалён или повреждён.\nПожалуйста, переустановите игру.", ok_action=Quit(confirm=False))
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
