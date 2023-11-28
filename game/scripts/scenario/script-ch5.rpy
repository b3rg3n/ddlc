image exception_bg = "#dadada"
image fake_exception = Text("Произошла ошибка.", size=40, style="_default")
image fake_exception2 = Text("File \"game/script-ch5.rpy\", line 307\nSee traceback.txt for details.", size=20, style="_default")

image splash_glitch:
    subpixel True
    "images/bg/splash-glitch.webp"
    alpha 0.0
    pause 0.5
    linear 0.5 alpha 1.0
    pause 2.5
    linear 0.5 alpha 0.0
    "gui/menu_bg.webp"
    topleft
    alpha 0.0
    parallel:
        xoffset 0 yoffset 0
        linear 0.25 xoffset -100 yoffset -100
        repeat
    parallel:
        linear 0.5 alpha 1.0
    parallel:
        ypos 0
        pause 1.0
        easeout 1.0 ypos -500
image splash_glitch2:
    subpixel True
    "gui/menu_bg.webp"
    topleft
    block:
        xoffset 0 yoffset 0
        linear 0.05 xoffset -100 yoffset -100
        repeat

image splash_glitch_m:
    subpixel True
    "gui/menu_art_m.webp"
    zoom 0.5
    xpos 0.5 ypos 0.5
    pause 0.1
    parallel:
        xpos 0.3 ypos 1.2
        linear 0.08 ypos 0.1
        repeat
    parallel:
        pause 0.5
        alpha 0.0

image splash_glitch_n:
    subpixel True
    "gui/menu_art_n.webp"
    zoom 0.5
    pause 0.2
    xpos 0.8 ypos 0.8
    pause 0.05
    xpos 0.2 ypos 0.7
    pause 0.05
    xpos 0.4 ypos 0.2
    pause 0.05
    xpos 0.7 ypos 1.2
    pause 0.05
    xpos 0.1 ypos 1.0
    pause 0.05
    xpos 0.2 ypos 0.6
    pause 0.05
    xpos 0.9 ypos 0.4
    pause 0.05
    alpha 0.0

image splash_glitch_y:
    subpixel True
    "gui/menu_art_y.webp"
    zoom 0.5
    ypos 1.3
    block:
        xpos 0.85
        pause 0.02
        xpos 0.81
        pause 0.02
        repeat


label ch5_main:
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full

    "А вот и день фестиваля."
    "Именно сегодня я надеялся, что пойду в школу вместе с [persistent.sayoriname]."
    "Но [persistent.sayoriname] не брала трубку."
    "Я подумал было зайти за ней и разбудить её, но решил, что это немного слишком."
    "Между тем подготовка к мероприятию должна была быть почти завершена."
    if ch4_scene == "natsuki":
        "Я умудрился сам донести все кексы, аккуратно разложив их на двух подносах."
        "Мой телефон уже разрывался от сообщений Нацуки, но я не мог ответить из-за отсутствия свободных рук."
    else:
        "Плакат, который я рисовал с Юри, уже высох, и я осторожно свернул его, чтобы взять с собой."
        "Она прислала мне приятное сообщение, в котором напомнила ничего не забыть, и я успокоил её."
    "Забавно, но я, кажется, испытываю насчёт этого мероприятия те же чувства, что и Нацуки."
    "Меня крайне радует, что подготовка закончилась, и я могу спокойно провести время с [persistent.sayoriname] и [ch4_name] на фестивале."
    "Но зная Монику, уверен, что и само мероприятие будет на высоте."

    scene bg club_day with wipeleft_scene
    show monika 5 zorder 2 at t11
    m "[player]!"
    m "Ты сегодня первый."
    m "Спасибо, что пришёл пораньше!"
    mc "Прикольно. Я думал, что как минимум Юри уже будет здесь."
    "Моника раскладывала по партам небольшие буклеты."
    "Это, наверное, те программки, где написаны все стихи, с которыми мы будем выступать."
    "Я в итоге нашёл в интернете какое-то стихотворение, которое, как мне показалось, понравится Монике, и отдал ей."
    "Его я и буду читать."
    m 1d "Я удивлена, что ты пришёл без [persistent.sayoriname]."
    mc "Да она снова проспала..."
    mc "Вот дурочка."
    mc "Хотя бы в такой важный день могла бы и подсуетиться..."
    "Сказал я, но тут же вспомнил, что мне вчера рассказала [persistent.sayoriname]..."
    "И почувствовал себя ужасно, понимая, что для неё это не так просто."
    "Я высказался подобным образом, потому что привык так думать."
    "Но..."
    "Может, всё-таки нужно было зайти и разбудить её?"
    m 1k "А-ха-ха."
    m 4b "Ты должен теперь следить за ней, [player]!"
    m "Особенно после того, что произошло между вами вчера..."
    m "Ты что-то оставил её в подвешенном состоянии сегодня утром, понимаешь?"
    show monika 4a
    mc "Произошло между нами?.."
    mc "Моника... Ты знаешь?!"
    m 2a "Конечно же знаю."
    m "Я же президент клуба, как-никак."
    mc "Но!.."
    "Я смутился и начал заикаться."
    "Неужели [persistent.sayoriname] уже всё рассказала ей?"
    if sayori_confess:
        "О том... что мы теперь вместе?"
        "Я пока что не планировал никому рассказывать об этом..."
    else:
        "О том, что я отверг её чувства?"
        "Я, наверное, выгляжу из-за этого редкой сволочью..."
        "Но я ведь знаю, как лучше для неё, так ведь?"
    mc "Боже..."
    mc "Ты просто не знаешь всего, так что..."
    m 2j "Не волнуйся."
    m "Я, скорее всего, знаю намного больше, чем ты думаешь."
    mc "А?.."
    "Моника вела себя дружелюбно, как и всегда, но от этих слов по моей спине почему-то пробежался холодок."
    m 5 "Эй, не хочешь посмотреть буклетик?"
    m "Они очень хорошо получились!"
    mc "Угу, конечно."
    "Я взял один из буклетов, разложенных на партах."
    mc "Да, они и вправду хороши."
    mc "Такие штуки определённо заставят людей воспринимать клуб более серьёзно."
    m "Да, я тоже так подумала!"
    show monika zorder 1 at thide
    hide monika
    "Я стал листать программку."
    "Стихотворение каждого участника клуба было аккуратно напечатано на собственной странице, отдавая чувством профессионализма."
    "Я узнал стихи Нацуки и Юри, которые они зачитывали во время нашей тренировки."
    mc "Что... это?.."
    "Я открыл стихотворение [persistent.sayoriname]."
    "Оно отличалось от того, с которым она выступала."
    "Этот стих я никогда не видел..."
    call showpoem (poem_s3, music=False) from _call_showpoem_21
    mc "А..."
    "Что это?.."
    "От этого стиха мои внутренности ухнули в чёрную дыру."
    show monika 1d zorder 2 at t11
    m "[player]?"
    m "Что случилось?"
    mc "A, ничего..."
    "Это стихотворение крайне сильно отличается от всего, что до этого писала [persistent.sayoriname]."
    "И более того..."
    mc "Я... Я передумал!"
    mc "Я схожу за [persistent.sayoriname], так что..."
    m "А-а-а..."
    m 1b "Ну хорошо!"
    m "Только сильно не задерживайся, ладно?"
    scene bg corridor with wipeleft
    "Я выскочил из класса."
    m "Не перенапряга-а-айся-а-а!"
    "Прокричала мне в спину Моника."
    "Я ускорил шаг."

    scene bg residential_day with wipeleft_scene
    "О чём я только думал?"
    "Мог бы хоть немного позаботиться о [persistent.sayoriname]."
    "Не перетрудился бы подождать хотя бы или разбудить."
    "Даже когда я просто провожаю её до школы, она уже радуется как ребёнок."
    "Кроме того..."
    "Вчера я сказал ей, что всё будет как прежде."
    "Это всё, что ей нужно, и что я хочу ей дать."

    scene bg house with wipeleft
    "Я добрался до дома [persistent.sayoriname] и постучался."
    "Впрочем, ответа я не ждал, так как она до сих пор не поднимала трубку."
    "Как и вчера, я открыл дверь и зашёл."
    scene black with wipeleft
    mc "[persistent.sayoriname]?"
    "Она и правда та ещё соня..."
    "Я сглотнул."
    "Не могу поверить, что всё-таки дошло до такого."
    "Будить её в её же доме..."
    if sayori_confess:
        "Я же её парень, так что всё в порядке вещей."
    else:
        "Я не её парень, чтобы это было в порядке вещей."
    "Но в любом случае..."
    "Я чувствую, что это будет правильно."

    "Я постучался в дверь её комнаты."
    mc "[persistent.sayoriname]?"
    mc "Просыпайся, дурочка..."
    "Нет ответа."
    "Я правда не хотел без спроса врываться к ней в комнату..."
    "Разве это не нарушение личного пространства?"
    "Но она действительно не оставила мне выбора."
    "Я осторожно открыл дверь."
    mc "{cps=30}Саё...........{/cps}{nw}"
    $ persistent.playthrough = 1
    $ persistent.anticheat = renpy.random.randint(100000, 999999)
    $ delete_character("sayori")
    $ in_sayori_kill = True
    window hide(None)
    window auto
    play music td
    show s_kill_bg2
    show s_kill2
    show s_kill_bg as s_kill_bg at s_kill_bg_start
    show s_kill as s_kill at s_kill_start
    pause 3.75
    show s_kill_bg2 as s_kill_bg
    show s_kill2 as s_kill
    pause 0.01
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    stop sound
    hide screen tear
    hide s_kill_bg
    hide s_kill
    show s_kill_bg_zoom zorder 1
    show s_kill_bg2_zoom zorder 1
    show s_kill_zoom zorder 3
    show s_kill2_zoom zorder 3
    show s_kill as s_kill_zoom_trans zorder 3:
        truecenter
        alpha 0.5
        zoom 2.0 xalign 0.5 yalign 0.05
        pause 0.5
        dizzy(1, 1.0)
    pause 2.0
    show noise zorder 3:
        alpha 0.0
        linear 3.0 alpha 0.25
    show vignette zorder 3:
        alpha 0.0
        linear 3.0 alpha 0.75
    pause 1.5
    show white zorder 2
    show splash_glitch zorder 2
    pause 1.5
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.2
    stop sound
    hide screen tear
    pause 4.0
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.2
    stop sound
    hide screen tear
    hide splash_glitch
    show splash_glitch2 zorder 2
    show splash_glitch_m zorder 2
    show splash_glitch_n zorder 2
    show splash_glitch_y zorder 2
    pause 0.75
    hide white
    hide splash_glitch2
    hide splash_glitch_m
    hide splash_glitch_n
    hide splash_glitch_y
    show exception_bg zorder 2
    show fake_exception zorder 2:
        xpos 0.1 ypos 0.05
    show fake_exception2 zorder 2:
        xpos 0.1 ypos 0.15
    python:
        try: sys.modules['renpy.error'].report_exception("О чёрт... Я же ничего не сломала, нет? Погоди секунду, я, наверное, могу это исправить... Думаю...\nХотя знаешь, что? По-моему, будет намного проще просто удалить её. Это она тут всё усложнила. А-ха-ха! Ну, вот и всё.", False)
        except: pass
    pause 6.0


    "..."
    hide fake_exception
    hide fake_exception2
    hide exception_bg
    "Что за чёрт?.."
    "{i}Что за чёрт???{/i}"
    "Это кошмар?"
    "Да... наверное он."
    "Это не реально."
    "Это не может быть реальным."
    "[persistent.sayoriname] этого бы не сделала."
    "Всё было хорошо до последних дней."
    "Поэтому я не могу поверить своим глазам!.."
    scene black with dissolve_cg
    "Я сдерживаю рвоту."
    "Ещё вчера..."
    "Я сказал [persistent.sayoriname], что буду с ней."
    "Я сказал ей, что знаю, как будет лучше, и что всё будет хорошо."
    "Тогда почему?.."
    "Почему она это сделала?.."
    "Как я мог оказаться таким беспомощным?"
    "Что я сделал не так?"
    if sayori_confess:
        "Признался ей..."
        "Не стоило признаваться."
        "Это совершенно не было нужно [persistent.sayoriname]."
        "Она же рассказывала, как сильно её тяготит забота окружающих."
        "Тогда зачем я признался и сделал ей только хуже?"
    else:
        "Отверг её чувства..."
        "Это, скорее всего, и подтолкнуло к такому поступку."
        "Её мучительный крик до сих пор эхом отдаётся в моих ушах."
        "Почему я так поступил, когда она нуждалась во мне больше всего?"
    "Почему я был таким эгоистом?"
    "Это моя вина!.."
    "Мои мысли продолжали нашёптывать мне способы, которыми я мог предотвратить это."
    "Если бы я только проводил с ней больше времени."
    "Провожал до школы."
    if sayori_confess:
        "И остался бы ей другом, как всегда и было..."
    else:
        "И дал бы ей то, чего она хотела от наших отношений..."
    "...Тогда я бы смог предотвратить это."
    "Я знаю, что смог бы!"
    "К чёрту Литературный Клуб."
    "К чёрту фестиваль."
    "Я... только что потерял своего лучшего друга."
    "Ту, с кем рос."
    "Она ушла навсегда."
    "Я ничего не могу сделать, чтобы вернуть её."
    "Это же не какая-то игра, где можно перезагрузиться и попробовать что-то другое."
    "У меня был только один шанс, и я оказался недостаточно осторожен."
    "И теперь эта вина будет грызть меня до самой смерти."
    "Её жизнь — самое ценное, что было в моей."
    "Но я всё равно не смог сделать то, чего она от меня хотела."
    "И теперь..."
    "Я никогда не верну всё назад."
    "Никогда."
    "Никогда."
    "Никогда."
    "Никогда."
    "Никогда..."
    $ in_sayori_kill = False


    return
