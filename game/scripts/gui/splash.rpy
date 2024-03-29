init python:
    menu_trans_time = 1
    splash_message_default = "Данная игра не предназначена для детей\nи впечатлительных особ."
    splash_messages = [
    "Ты мой лучик,\nМой единственный лучик.",
    "Я скучала по тебе.",
    "Поиграй со мной",
    "По большому счёту, это всего лишь игра.",
    "Данная игра не предназначена для детей\nи впечатлительных особ?",
    "sdfasdklfgsdfgsgoinrfoenlvbd",
    "null",
    "Детей я сдала в ад.",
    "ВП умерла за это.",
    "И это только частично твоя вина.",
    "Данная игра не предназначена для детей\nи расчленённых особ.",
    "Не забудь восстановить файл персонажа Моники."
    ]

image splash_warning = ParameterizedText(style="splash_text", xalign=0.5, yalign=0.5)

image menu_bg:
    topleft
    "gui/menu_bg.webp"
    menu_bg_move

image game_menu_bg:
    topleft
    "gui/menu_bg.webp"
    menu_bg_loop

image menu_fade:
    "white"
    menu_fadeout

image menu_art_y:
    subpixel True
    "gui/menu_art_y.webp"
    xcenter 600
    ycenter 335
    zoom 0.60
    menu_art_move(0.54, 600, 0.60)

image menu_art_n:
    subpixel True
    "gui/menu_art_n.webp"
    xcenter 750
    ycenter 385
    zoom 0.58
    menu_art_move(0.58, 750, 0.58)

image menu_art_s:
    subpixel True
    "gui/menu_art_s.webp"
    xcenter 510
    ycenter 500
    zoom 0.68
    menu_art_move(0.68, 510, 0.68)

image menu_art_m:
    subpixel True
    "gui/menu_art_m.webp"
    xcenter 1000
    ycenter 640
    zoom 1.00
    menu_art_move(1.00, 1000, 1.00)

image menu_art_y_ghost:
    subpixel True
    "gui/menu_art_y_ghost.webp"
    xcenter 600
    ycenter 335
    zoom 0.60
    menu_art_move(0.54, 600, 0.60)

image menu_art_n_ghost:
    subpixel True
    "gui/menu_art_n_ghost.webp"
    xcenter 750
    ycenter 385
    zoom 0.58
    menu_art_move(0.58, 750, 0.58)

image menu_art_s_ghost:
    subpixel True
    "gui/menu_art_s_ghost.webp"
    xcenter 510
    ycenter 500
    zoom 0.68
    menu_art_move(0.68, 510, 0.68)

image menu_art_m_ghost:
    subpixel True
    "gui/menu_art_m_ghost.webp"
    xcenter 1000
    ycenter 640
    zoom 1.00
    menu_art_move(1.00, 1000, 1.00)

image menu_art_s_glitch:
    subpixel True
    "gui/menu_art_s_break.webp"
    xcenter 470
    ycenter 600
    zoom 0.68
    menu_art_move(.8, 470, .8)

image menu_nav:
    "gui/overlay/main_menu.webp"
    menu_nav_move

image mods_menu_nav:
    "gui/overlay/main_menu.webp"

image menu_logo:
    "gui/logo.webp"
    subpixel True
    xcenter 240
    ycenter 120
    zoom 0.60
    menu_logo_move

image menu_particles:
    2.481
    xpos 224
    ypos 104
    ParticleBurst("gui/menu_particle.webp", explodeTime=0, numParticles=20, particleTime=2.0, particleXSpeed=6, particleYSpeed=4).sm
    particle_fadeout

transform particle_fadeout:
    easeout 1.5 alpha 0

transform menu_bg_move:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat
    parallel:
        ypos 0
        time 0.65
        ease_cubic 2.5 ypos -500

transform menu_bg_loop:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat

transform menu_logo_move:
    subpixel True
    yoffset -300
    time 1.925
    easein_bounce 1.5 yoffset 0

transform menu_nav_move:
    subpixel True
    xoffset -500
    time 1.5
    easein_quint 1 xoffset 0

transform menu_fadeout:
    easeout 0.75 alpha 0
    time 2.481
    alpha 0.4
    linear 0.5 alpha 0

transform menu_art_move(z, x, z2):
    subpixel True
    yoffset 0 + (1200 * z)
    xoffset (740 - x) * z * 0.5
    zoom z2 * 0.75
    time 1.0
    parallel:
        ease 1.75 yoffset 0
    parallel:
        pause 0.75
        ease 1.5 zoom z2 xoffset 0


image intro:
    truecenter
    "white"
    0.5
    "bg/splash.webp" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

image warning:
    truecenter
    "white"
    "splash_warning" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

image tos = "bg/warning.webp"
image tos2 = "bg/warning2.webp"


label splashscreen:

    python: # ОБНОВЛЯЕМ RPC
        try:
            rpc.update(state="В игре",details="Главное меню",large_image="ddlc",start=time.time())
        except AssertionError:
            pass


    python:
        process_list = []
        currentuser = ""
        if renpy.windows:
            try:
                process_list = subprocess.check_output("wmic process get Description", shell=True).lower().replace("\r", "").replace(" ", "").split("\n")
            except:
                pass
            try:
                for name in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
                    user = os.environ.get(name)
                    if user:
                        currentuser = user
            except:
                pass


    if persistent.s_kill_early:
        show black
        play music "bgm/s_kill_early.ogg"
        pause 1.0
        show end with dissolve_cg
        pause 3.0
        scene white
        show expression "images/cg/s_kill_early.webp":
            yalign -0.05
            xalign 0.25
            dizzy(1.0, 4.0, subpixel=False)
        show white as w2:
            choice:
                ease 0.25 alpha 0.1
            choice:
                ease 0.25 alpha 0.125
            choice:
                ease 0.25 alpha 0.15
            choice:
                ease 0.25 alpha 0.175
            choice:
                ease 0.25 alpha 0.2
            choice:
                ease 0.25 alpha 0.225
            choice:
                ease 0.25 alpha 0.25
            choice:
                ease 0.25 alpha 0.275
            choice:
                ease 0.25 alpha 0.3
            pass
            choice:
                pass
            choice:
                0.25
            choice:
                0.5
            choice:
                0.75
            repeat
        show noise:
            alpha 0.1
        with Dissolve(1.0)
        show expression Text("Теперь все будут счастливы.", style="sayori_text"):
            xalign 0.8
            yalign 0.5
            alpha 0.0
            30
            linear 60 alpha 0.5
        pause
        $ renpy.quit()

    if not persistent.first_run:
        $ persistent.monikachr = True
        $ persistent.sayorichr = True
        $ persistent.yurichr = True
        $ persistent.natsukichr = True
        $ quick_menu = False
        scene white
        pause 0.5
        scene tos
        with Dissolve(1.0)
        pause 1.0
        "Данная игра не предназначена для детей и впечатлительных особ."
        "Личности, подверженные нервным расстройствам или находящиеся в состоянии депрессии, могут пострадать в процессе игры. Прочесть предостережения можно на сайте: http://ddlc.moe/warning.html"
        menu:
            "Для того, чтобы начать играть в Доки-Доки Литературный клуб, подтвердите, что достигли возраста тринадцати лет и осознаёте, что используете стрессовый контент."
            "Подтверждаю.":
                pass
        $ persistent.first_run = True
        scene tos2
        with Dissolve(1.5)
        pause 1.0
        scene white


        if persistent.playthrough == 0:
            if persistent.sayorichr == False:
                $ persistent.s_kill_early = True

        if not persistent.s_kill_early:
            if persistent.playthrough <= 2 and persistent.playthrough != 0:
                $ persistent.monikachr = True
            if persistent.playthrough <= 1 or persistent.playthrough == 4:
                $ persistent.yurichr = True
                $ persistent.natsukichr = True
            if persistent.playthrough == 4:
                $ persistent.sayorichr = True

    if not persistent.special_poems:
        python hide:
            persistent.special_poems = [0,0,0]
            a = range(1,12)
            for i in range(3):
                b = renpy.random.choice(a)
                persistent.special_poems[i] = b
                a.remove(b)

    $ basedir = config.basedir.replace('\\', '/')



    if persistent.autoload:
        jump autoload



    $ config.allow_skipping = False

    if persistent.playthrough == 2 and not persistent.seen_ghost_menu and renpy.random.randint(0, 63) == 0:
        show black
        $ config.main_menu_music = audio.ghostmenu
        $ persistent.seen_ghost_menu = True
        $ persistent.ghost_menu = True
        $ renpy.music.play(config.main_menu_music)
        pause 1.0
        show end with dissolve_cg
        pause 3.0
        $ config.allow_skipping = True
        return

    show white
    $ persistent.ghost_menu = False
    $ splash_message = splash_message_default
    $ config.main_menu_music = audio.t1
    $ renpy.music.play(config.main_menu_music)
    show intro with Dissolve(0.5, alpha=True)
    pause 2.5
    hide intro with Dissolve(0.5, alpha=True)
    if persistent.playthrough == 2 and renpy.random.randint(0, 3) == 0:
        $ splash_message = renpy.random.choice(splash_messages)
    show splash_warning "[splash_message]" with Dissolve(0.5, alpha=True)
    pause 2.0
    hide splash_warning with Dissolve(0.5, alpha=True)
    $ config.allow_skipping = True
    return

label warningscreen:
    hide intro
    show warning
    pause 3.0

label after_load:
    if persistent.playthrough == 0:
        $ persistent.monikachr = True
        $ persistent.sayorichr = True
        $ persistent.yurichr = True
        $ persistent.natsukichr = True
    $ config.allow_skipping = allow_skipping
    $ _dismiss_pause = config.developer
    $ persistent.ghost_menu = False
    $ style.say_dialogue = style.normal

    if persistent.yuri_kill > 0 and persistent.autoload == "yuri_kill_2":
        if persistent.yuri_kill >= 1380:
            $ persistent.yuri_kill = 1440
        elif persistent.yuri_kill >= 1180:
            $ persistent.yuri_kill = 1380
        elif persistent.yuri_kill >= 1120:
            $ persistent.yuri_kill = 1180
        elif persistent.yuri_kill >= 920:
            $ persistent.yuri_kill = 1120
        elif persistent.yuri_kill >= 720:
            $ persistent.yuri_kill = 920
        elif persistent.yuri_kill >= 660:
            $ persistent.yuri_kill = 720
        elif persistent.yuri_kill >= 460:
            $ persistent.yuri_kill = 660
        elif persistent.yuri_kill >= 260:
            $ persistent.yuri_kill = 460
        elif persistent.yuri_kill >= 200:
            $ persistent.yuri_kill = 260
        else:
            $ persistent.yuri_kill = 200
        jump expression persistent.autoload

#    elif anticheat != persistent.anticheat:
#        stop music
#        scene black
#        "Не удалось загрузить сохрание."
#        "Пытаешься читерить?"
#        $ m_name = "Моника"
#        show monika 1 at t11
#        if persistent.playername == "":
#            m "Ты какой смешной."
#        else:
#            m "Ты такой смешной, [persistent.playername]."
#        $ renpy.utter_restart()
#    else:
        if persistent.playthrough == 0 and not persistent.first_load and not config.developer:
            $ persistent.first_load = True
            call screen dialog("Подсказка: Можете использовать кнопку \"Пропуск\",\nчтобы перемотать уже прочитанный текст.", ok_action=Return())
    return



label autoload:
    python:

        if "_old_game_menu_screen" in globals():
            _game_menu_screen = _old_game_menu_screen
            del _old_game_menu_screen
        if "_old_history" in globals():
            _history = _old_history
            del _old_history
        renpy.block_rollback()


        renpy.context()._menu = False
        renpy.context()._main_menu = False
        main_menu = False
        _in_replay = None

    if persistent.yuri_kill > 0 and persistent.autoload == "yuri_kill_2":
        $ persistent.yuri_kill += 200


    if renpy.get_return_stack():
        $ renpy.pop_call()
#    jump expression persistent.autoload

label autoload_yurikill:
    if persistent.yuri_kill >= 1380:
        $ persistent.yuri_kill = 1440
    elif persistent.yuri_kill >= 1180:
        $ persistent.yuri_kill = 1380
    elif persistent.yuri_kill >= 1120:
        $ persistent.yuri_kill = 1180
    elif persistent.yuri_kill >= 920:
        $ persistent.yuri_kill = 1120
    elif persistent.yuri_kill >= 720:
        $ persistent.yuri_kill = 920
    elif persistent.yuri_kill >= 660:
        $ persistent.yuri_kill = 720
    elif persistent.yuri_kill >= 460:
        $ persistent.yuri_kill = 660
    elif persistent.yuri_kill >= 260:
        $ persistent.yuri_kill = 460
    elif persistent.yuri_kill >= 200:
        $ persistent.yuri_kill = 260
    else:
        $ persistent.yuri_kill = 200
    jump expression persistent.autoload

label before_main_menu:
    $ config.main_menu_music = audio.t1
    return

label quit:
    if persistent.ghost_menu:
        hide screen main_menu
        scene white
        show expression "gui/menu_art_m_ghost.webp":
            xpos -100 ypos -100 zoom 3.5
        pause 0.01
    return

label readonly:
    scene black
    "Невозможно запустить игру.\nВы пытаетесь запустить игру из директории, предназначенной только для чтения."
    "Пожалуйста, скопируйте DDLC на рабочий стол или в любую другую доступную папку и попробуйте снова."
    $ renpy.quit()
    return
