define persistent.demo = False
define persistent.steam = False
define config.developer = False

python early:
    import singleton
    me = singleton.SingleInstance()

init python:
    renpy.music.register_channel("music_poem", mixer="music", tight=True)
    def get_pos(channel='music'):
        pos = renpy.music.get_pos(channel=channel)
        if pos: return pos
        return 0
    def delete_all_saves():
        for savegame in renpy.list_saved_games(fast=True):
            renpy.unlink_save(savegame)
    def delete_character(name):
        import os
        if renpy.android :
            try: os.remove(os.environ['ANDROID_PUBLIC'] + "/characters/" + name + ".chr")
            except: pass
        else :
            try: os.remove(config.basedir + "/characters/" + name + ".chr")
            except: pass
    def restore_character(names):
        import os
        if not isinstance(names, list):
            raise Exception("'names' parameter must be a list. Example: [\"monika\", \"sayori\"].")

        for x in names:
            if renpy.android:
                try: renpy.file(os.environ['ANDROID_PUBLIC'] + "/characters/" + x + ".chr")
                except: open(os.environ['ANDROID_PUBLIC'] + "/characters/" + x + ".chr", "wb").write(renpy.file("restore/" + x + ".chr").read())
            else:
                try: renpy.file(config.basedir + "/characters/" + x + ".chr")
                except: open(config.basedir + "/characters/" + x + ".chr", "wb").write(renpy.file("restore/" + x + ".chr").read())

    def restore_all_characters():
        if persistent.playthrough == 0:
            restore_character(["monika", "sayori", "natsuki", "yuri"])
        elif persistent.playthrough == 1 or persistent.playthrough == 2:
            restore_character(["monika", "natsuki", "yuri"])
        elif persistent.playthrough == 3:
            restore_character(["monika"])
        else:
            restore_character(["sayori", "natsuki", "yuri"])
    def pause(time=None):
        if not time:
            renpy.ui.saybehavior(afm=" ")
            renpy.ui.interact(mouse='pause', type='pause', roll_forward=None)
            return
        if time <= 0: return
        renpy.pause(time, hard = True)





define audio.t1 = "<loop 22.073>bgm/1.ogg"
define audio.t2 = "<loop 4.499>bgm/2.ogg"
define audio.t2g = "bgm/2g.ogg"
define audio.t2g2 = "<from 4.499 loop 4.499>bgm/2.ogg"
define audio.t2g3 = "<loop 4.492>bgm/2g2.ogg"
define audio.t3 = "<loop 4.618>bgm/3.ogg"
define audio.t3g = "<to 15.255>bgm/3g.ogg"
define audio.t3g2 = "<from 15.255 loop 4.618>bgm/3.ogg"
define audio.t3g3 = "<loop 4.618>bgm/3g2.ogg"
define audio.t3m = "<loop 4.618>bgm/3.ogg"
define audio.t4 = "<loop 19.451>bgm/4.ogg"
define audio.t4g = "<loop 1.000>bgm/4g.ogg"
define audio.t5 = "<loop 4.444>bgm/5.ogg"
define audio.t5b = "<loop 4.444>bgm/5.ogg"
define audio.t5c = "<loop 4.444>bgm/5.ogg"
define audio.t6 = "<loop 10.893>bgm/6.ogg"
define audio.t6g = "<loop 10.893>bgm/6g.ogg"
define audio.t6r = "<to 39.817 loop 0>bgm/6r.ogg"
define audio.t6s = "<loop 43.572>bgm/6s.ogg"
define audio.t7 = "<loop 2.291>bgm/7.ogg"
define audio.t7a = "<loop 4.316 to 12.453>bgm/7.ogg"
define audio.t7g = "<loop 31.880>bgm/7g.ogg"
define audio.t8 = "<loop 9.938>bgm/8.ogg"
define audio.t9 = "<loop 3.172>bgm/9.ogg"
define audio.t9g = "<loop 1.532>bgm/9g.ogg"
define audio.t10 = "<loop 5.861>bgm/10.ogg"
define audio.t10y = "<loop 0>bgm/10-yuri.ogg"
define audio.td = "<loop 36.782>bgm/d.ogg"

define audio.m1 = "<loop 0>bgm/m1.ogg"
define audio.mend = "<loop 6.424>bgm/monika-end.ogg"

define audio.ghostmenu = "<loop 0>bgm/ghostmenu.ogg"
define audio.g1 = "<loop 0>bgm/g1.ogg"
define audio.g2 = "<loop 0>bgm/g2.ogg"
define audio.hb = "<loop 0>bgm/heartbeat.ogg"

define audio.closet_open = "sfx/closet-open.ogg"
define audio.closet_close = "sfx/closet-close.ogg"
define audio.page_turn = "sfx/pageflip.ogg"
define audio.fall = "sfx/fall.ogg"


image black = "#000000"
image dark = "#000000e4"
image darkred = "#110000c8"
image white = "#ffffff"
image splash = "bg/splash.webp"
image end:
    truecenter
    "gui/end.webp"
image bg residential_day = "bg/residential.webp"
image bg class_day = "bg/class.webp"
image bg corridor = "bg/corridor.webp"
image bg club_day = "bg/club.webp"
image bg club_day2:
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg/club-skill.webp"
image bg closet = "bg/closet.webp"
image bg bedroom = "bg/bedroom.webp"
image bg sayori_bedroom = "bg/sayori_bedroom.webp"
image bg house = "bg/house.webp"
image bg kitchen = "bg/kitchen.webp"

image bg notebook = "bg/notebook.webp"
image bg notebook-glitch = "bg/notebook-glitch.webp"

image bg glitch = LiveTile("bg/glitch.webp")

image glitch_color:
    ytile 3
    zoom 2.5
    parallel:
        "bg/glitch-red.webp"
        0.1
        "bg/glitch-green.webp"
        0.1
        "bg/glitch-blue.webp"
        0.1
        repeat
    parallel:
        yoffset 720
        linear 0.5 yoffset 0
        repeat
    parallel:
        choice:
            xoffset 0
        choice:
            xoffset 10
        choice:
            xoffset 20
        choice:
            xoffset 35
        choice:
            xoffset -10
        choice:
            xoffset -20
        choice:
            xoffset -30
        0.01
        repeat
    parallel:
        alpha 0.6
        linear 0.15 alpha 0.1
        0.2
        alpha 0.6
        linear 0.15 alpha 0.1
        0.2
        alpha 0.7
        linear 0.45 alpha 0



image glitch_color2:
    ytile 3
    zoom 2.5
    parallel:
        "bg/glitch-red.webp"
        0.1
        "bg/glitch-green.webp"
        0.1
        "bg/glitch-blue.webp"
        0.1
        repeat
    parallel:
        yoffset 720
        linear 0.5 yoffset 0
        repeat
    parallel:
        choice:
            xoffset 0
        choice:
            xoffset 10
        choice:
            xoffset 20
        choice:
            xoffset 35
        choice:
            xoffset -10
        choice:
            xoffset -20
        choice:
            xoffset -30
        0.01
        repeat
    parallel:
        alpha 0.7
        linear 0.45 alpha 0




image sayori 1 = im.Composite((960, 960), (0, 0), "sayori/1l.webp", (0, 0), "sayori/1r.webp", (0, 0), "sayori/a.webp")
image sayori 1a = im.Composite((960, 960), (0, 0), "sayori/1l.webp", (0, 0), "sayori/1r.webp", (0, 0), "sayori/a.webp")
image sayori 1b = im.Composite((960, 960), (0, 0), "sayori/1l.webp", (0, 0), "sayori/1r.webp", (0, 0), "sayori/b.webp")
image sayori 1c = im.Composite((960, 960), (0, 0), "sayori/1l.webp", (0, 0), "sayori/1r.webp", (0, 0), "sayori/c.webp")
image sayori 1d = im.Composite((960, 960), (0, 0), "sayori/1l.webp", (0, 0), "sayori/1r.webp", (0, 0), "sayori/d.webp")
image sayori 1e = im.Composite((960, 960), (0, 0), "sayori/1l.webp", (0, 0), "sayori/1r.webp", (0, 0), "sayori/e.webp")
image sayori 1f = im.Composite((960, 960), (0, 0), "sayori/1l.webp", (0, 0), "sayori/1r.webp", (0, 0), "sayori/f.webp")
image sayori 1g = im.Composite((960, 960), (0, 0), "sayori/1l.webp", (0, 0), "sayori/1r.webp", (0, 0), "sayori/g.webp")
image sayori 1h = im.Composite((960, 960), (0, 0), "sayori/1l.webp", (0, 0), "sayori/1r.webp", (0, 0), "sayori/h.webp")
image sayori 1i = im.Composite((960, 960), (0, 0), "sayori/1l.webp", (0, 0), "sayori/1r.webp", (0, 0), "sayori/i.webp")
image sayori 1j = im.Composite((960, 960), (0, 0), "sayori/1l.webp", (0, 0), "sayori/1r.webp", (0, 0), "sayori/j.webp")
image sayori 1k = im.Composite((960, 960), (0, 0), "sayori/1l.webp", (0, 0), "sayori/1r.webp", (0, 0), "sayori/k.webp")
image sayori 1l = im.Composite((960, 960), (0, 0), "sayori/1l.webp", (0, 0), "sayori/1r.webp", (0, 0), "sayori/l.webp")
image sayori 1m = im.Composite((960, 960), (0, 0), "sayori/1l.webp", (0, 0), "sayori/1r.webp", (0, 0), "sayori/m.webp")
image sayori 1n = im.Composite((960, 960), (0, 0), "sayori/1l.webp", (0, 0), "sayori/1r.webp", (0, 0), "sayori/n.webp")
image sayori 1o = im.Composite((960, 960), (0, 0), "sayori/1l.webp", (0, 0), "sayori/1r.webp", (0, 0), "sayori/o.webp")
image sayori 1p = im.Composite((960, 960), (0, 0), "sayori/1l.webp", (0, 0), "sayori/1r.webp", (0, 0), "sayori/p.webp")
image sayori 1q = im.Composite((960, 960), (0, 0), "sayori/1l.webp", (0, 0), "sayori/1r.webp", (0, 0), "sayori/q.webp")
image sayori 1r = im.Composite((960, 960), (0, 0), "sayori/1l.webp", (0, 0), "sayori/1r.webp", (0, 0), "sayori/r.webp")
image sayori 1s = im.Composite((960, 960), (0, 0), "sayori/1l.webp", (0, 0), "sayori/1r.webp", (0, 0), "sayori/s.webp")
image sayori 1t = im.Composite((960, 960), (0, 0), "sayori/1l.webp", (0, 0), "sayori/1r.webp", (0, 0), "sayori/t.webp")
image sayori 1u = im.Composite((960, 960), (0, 0), "sayori/1l.webp", (0, 0), "sayori/1r.webp", (0, 0), "sayori/u.webp")
image sayori 1v = im.Composite((960, 960), (0, 0), "sayori/1l.webp", (0, 0), "sayori/1r.webp", (0, 0), "sayori/v.webp")
image sayori 1w = im.Composite((960, 960), (0, 0), "sayori/1l.webp", (0, 0), "sayori/1r.webp", (0, 0), "sayori/w.webp")
image sayori 1x = im.Composite((960, 960), (0, 0), "sayori/1l.webp", (0, 0), "sayori/1r.webp", (0, 0), "sayori/x.webp")
image sayori 1y = im.Composite((960, 960), (0, 0), "sayori/1l.webp", (0, 0), "sayori/1r.webp", (0, 0), "sayori/y.webp")

image sayori 2 = im.Composite((960, 960), (0, 0), "sayori/1l.webp", (0, 0), "sayori/2r.webp", (0, 0), "sayori/a.webp")
image sayori 2a = im.Composite((960, 960), (0, 0), "sayori/1l.webp", (0, 0), "sayori/2r.webp", (0, 0), "sayori/a.webp")
image sayori 2b = im.Composite((960, 960), (0, 0), "sayori/1l.webp", (0, 0), "sayori/2r.webp", (0, 0), "sayori/b.webp")
image sayori 2c = im.Composite((960, 960), (0, 0), "sayori/1l.webp", (0, 0), "sayori/2r.webp", (0, 0), "sayori/c.webp")
image sayori 2d = im.Composite((960, 960), (0, 0), "sayori/1l.webp", (0, 0), "sayori/2r.webp", (0, 0), "sayori/d.webp")
image sayori 2e = im.Composite((960, 960), (0, 0), "sayori/1l.webp", (0, 0), "sayori/2r.webp", (0, 0), "sayori/e.webp")
image sayori 2f = im.Composite((960, 960), (0, 0), "sayori/1l.webp", (0, 0), "sayori/2r.webp", (0, 0), "sayori/f.webp")
image sayori 2g = im.Composite((960, 960), (0, 0), "sayori/1l.webp", (0, 0), "sayori/2r.webp", (0, 0), "sayori/g.webp")
image sayori 2h = im.Composite((960, 960), (0, 0), "sayori/1l.webp", (0, 0), "sayori/2r.webp", (0, 0), "sayori/h.webp")
image sayori 2i = im.Composite((960, 960), (0, 0), "sayori/1l.webp", (0, 0), "sayori/2r.webp", (0, 0), "sayori/i.webp")
image sayori 2j = im.Composite((960, 960), (0, 0), "sayori/1l.webp", (0, 0), "sayori/2r.webp", (0, 0), "sayori/j.webp")
image sayori 2k = im.Composite((960, 960), (0, 0), "sayori/1l.webp", (0, 0), "sayori/2r.webp", (0, 0), "sayori/k.webp")
image sayori 2l = im.Composite((960, 960), (0, 0), "sayori/1l.webp", (0, 0), "sayori/2r.webp", (0, 0), "sayori/l.webp")
image sayori 2m = im.Composite((960, 960), (0, 0), "sayori/1l.webp", (0, 0), "sayori/2r.webp", (0, 0), "sayori/m.webp")
image sayori 2n = im.Composite((960, 960), (0, 0), "sayori/1l.webp", (0, 0), "sayori/2r.webp", (0, 0), "sayori/n.webp")
image sayori 2o = im.Composite((960, 960), (0, 0), "sayori/1l.webp", (0, 0), "sayori/2r.webp", (0, 0), "sayori/o.webp")
image sayori 2p = im.Composite((960, 960), (0, 0), "sayori/1l.webp", (0, 0), "sayori/2r.webp", (0, 0), "sayori/p.webp")
image sayori 2q = im.Composite((960, 960), (0, 0), "sayori/1l.webp", (0, 0), "sayori/2r.webp", (0, 0), "sayori/q.webp")
image sayori 2r = im.Composite((960, 960), (0, 0), "sayori/1l.webp", (0, 0), "sayori/2r.webp", (0, 0), "sayori/r.webp")
image sayori 2s = im.Composite((960, 960), (0, 0), "sayori/1l.webp", (0, 0), "sayori/2r.webp", (0, 0), "sayori/s.webp")
image sayori 2t = im.Composite((960, 960), (0, 0), "sayori/1l.webp", (0, 0), "sayori/2r.webp", (0, 0), "sayori/t.webp")
image sayori 2u = im.Composite((960, 960), (0, 0), "sayori/1l.webp", (0, 0), "sayori/2r.webp", (0, 0), "sayori/u.webp")
image sayori 2v = im.Composite((960, 960), (0, 0), "sayori/1l.webp", (0, 0), "sayori/2r.webp", (0, 0), "sayori/v.webp")
image sayori 2w = im.Composite((960, 960), (0, 0), "sayori/1l.webp", (0, 0), "sayori/2r.webp", (0, 0), "sayori/w.webp")
image sayori 2x = im.Composite((960, 960), (0, 0), "sayori/1l.webp", (0, 0), "sayori/2r.webp", (0, 0), "sayori/x.webp")
image sayori 2y = im.Composite((960, 960), (0, 0), "sayori/1l.webp", (0, 0), "sayori/2r.webp", (0, 0), "sayori/y.webp")

image sayori 3 = im.Composite((960, 960), (0, 0), "sayori/2l.webp", (0, 0), "sayori/1r.webp", (0, 0), "sayori/a.webp")
image sayori 3a = im.Composite((960, 960), (0, 0), "sayori/2l.webp", (0, 0), "sayori/1r.webp", (0, 0), "sayori/a.webp")
image sayori 3b = im.Composite((960, 960), (0, 0), "sayori/2l.webp", (0, 0), "sayori/1r.webp", (0, 0), "sayori/b.webp")
image sayori 3c = im.Composite((960, 960), (0, 0), "sayori/2l.webp", (0, 0), "sayori/1r.webp", (0, 0), "sayori/c.webp")
image sayori 3d = im.Composite((960, 960), (0, 0), "sayori/2l.webp", (0, 0), "sayori/1r.webp", (0, 0), "sayori/d.webp")
image sayori 3e = im.Composite((960, 960), (0, 0), "sayori/2l.webp", (0, 0), "sayori/1r.webp", (0, 0), "sayori/e.webp")
image sayori 3f = im.Composite((960, 960), (0, 0), "sayori/2l.webp", (0, 0), "sayori/1r.webp", (0, 0), "sayori/f.webp")
image sayori 3g = im.Composite((960, 960), (0, 0), "sayori/2l.webp", (0, 0), "sayori/1r.webp", (0, 0), "sayori/g.webp")
image sayori 3h = im.Composite((960, 960), (0, 0), "sayori/2l.webp", (0, 0), "sayori/1r.webp", (0, 0), "sayori/h.webp")
image sayori 3i = im.Composite((960, 960), (0, 0), "sayori/2l.webp", (0, 0), "sayori/1r.webp", (0, 0), "sayori/i.webp")
image sayori 3j = im.Composite((960, 960), (0, 0), "sayori/2l.webp", (0, 0), "sayori/1r.webp", (0, 0), "sayori/j.webp")
image sayori 3k = im.Composite((960, 960), (0, 0), "sayori/2l.webp", (0, 0), "sayori/1r.webp", (0, 0), "sayori/k.webp")
image sayori 3l = im.Composite((960, 960), (0, 0), "sayori/2l.webp", (0, 0), "sayori/1r.webp", (0, 0), "sayori/l.webp")
image sayori 3m = im.Composite((960, 960), (0, 0), "sayori/2l.webp", (0, 0), "sayori/1r.webp", (0, 0), "sayori/m.webp")
image sayori 3n = im.Composite((960, 960), (0, 0), "sayori/2l.webp", (0, 0), "sayori/1r.webp", (0, 0), "sayori/n.webp")
image sayori 3o = im.Composite((960, 960), (0, 0), "sayori/2l.webp", (0, 0), "sayori/1r.webp", (0, 0), "sayori/o.webp")
image sayori 3p = im.Composite((960, 960), (0, 0), "sayori/2l.webp", (0, 0), "sayori/1r.webp", (0, 0), "sayori/p.webp")
image sayori 3q = im.Composite((960, 960), (0, 0), "sayori/2l.webp", (0, 0), "sayori/1r.webp", (0, 0), "sayori/q.webp")
image sayori 3r = im.Composite((960, 960), (0, 0), "sayori/2l.webp", (0, 0), "sayori/1r.webp", (0, 0), "sayori/r.webp")
image sayori 3s = im.Composite((960, 960), (0, 0), "sayori/2l.webp", (0, 0), "sayori/1r.webp", (0, 0), "sayori/s.webp")
image sayori 3t = im.Composite((960, 960), (0, 0), "sayori/2l.webp", (0, 0), "sayori/1r.webp", (0, 0), "sayori/t.webp")
image sayori 3u = im.Composite((960, 960), (0, 0), "sayori/2l.webp", (0, 0), "sayori/1r.webp", (0, 0), "sayori/u.webp")
image sayori 3v = im.Composite((960, 960), (0, 0), "sayori/2l.webp", (0, 0), "sayori/1r.webp", (0, 0), "sayori/v.webp")
image sayori 3w = im.Composite((960, 960), (0, 0), "sayori/2l.webp", (0, 0), "sayori/1r.webp", (0, 0), "sayori/w.webp")
image sayori 3x = im.Composite((960, 960), (0, 0), "sayori/2l.webp", (0, 0), "sayori/1r.webp", (0, 0), "sayori/x.webp")
image sayori 3y = im.Composite((960, 960), (0, 0), "sayori/2l.webp", (0, 0), "sayori/1r.webp", (0, 0), "sayori/y.webp")

image sayori 4 = im.Composite((960, 960), (0, 0), "sayori/2l.webp", (0, 0), "sayori/2r.webp", (0, 0), "sayori/a.webp")
image sayori 4a = im.Composite((960, 960), (0, 0), "sayori/2l.webp", (0, 0), "sayori/2r.webp", (0, 0), "sayori/a.webp")
image sayori 4b = im.Composite((960, 960), (0, 0), "sayori/2l.webp", (0, 0), "sayori/2r.webp", (0, 0), "sayori/b.webp")
image sayori 4c = im.Composite((960, 960), (0, 0), "sayori/2l.webp", (0, 0), "sayori/2r.webp", (0, 0), "sayori/c.webp")
image sayori 4d = im.Composite((960, 960), (0, 0), "sayori/2l.webp", (0, 0), "sayori/2r.webp", (0, 0), "sayori/d.webp")
image sayori 4e = im.Composite((960, 960), (0, 0), "sayori/2l.webp", (0, 0), "sayori/2r.webp", (0, 0), "sayori/e.webp")
image sayori 4f = im.Composite((960, 960), (0, 0), "sayori/2l.webp", (0, 0), "sayori/2r.webp", (0, 0), "sayori/f.webp")
image sayori 4g = im.Composite((960, 960), (0, 0), "sayori/2l.webp", (0, 0), "sayori/2r.webp", (0, 0), "sayori/g.webp")
image sayori 4h = im.Composite((960, 960), (0, 0), "sayori/2l.webp", (0, 0), "sayori/2r.webp", (0, 0), "sayori/h.webp")
image sayori 4i = im.Composite((960, 960), (0, 0), "sayori/2l.webp", (0, 0), "sayori/2r.webp", (0, 0), "sayori/i.webp")
image sayori 4j = im.Composite((960, 960), (0, 0), "sayori/2l.webp", (0, 0), "sayori/2r.webp", (0, 0), "sayori/j.webp")
image sayori 4k = im.Composite((960, 960), (0, 0), "sayori/2l.webp", (0, 0), "sayori/2r.webp", (0, 0), "sayori/k.webp")
image sayori 4l = im.Composite((960, 960), (0, 0), "sayori/2l.webp", (0, 0), "sayori/2r.webp", (0, 0), "sayori/l.webp")
image sayori 4m = im.Composite((960, 960), (0, 0), "sayori/2l.webp", (0, 0), "sayori/2r.webp", (0, 0), "sayori/m.webp")
image sayori 4n = im.Composite((960, 960), (0, 0), "sayori/2l.webp", (0, 0), "sayori/2r.webp", (0, 0), "sayori/n.webp")
image sayori 4o = im.Composite((960, 960), (0, 0), "sayori/2l.webp", (0, 0), "sayori/2r.webp", (0, 0), "sayori/o.webp")
image sayori 4p = im.Composite((960, 960), (0, 0), "sayori/2l.webp", (0, 0), "sayori/2r.webp", (0, 0), "sayori/p.webp")
image sayori 4q = im.Composite((960, 960), (0, 0), "sayori/2l.webp", (0, 0), "sayori/2r.webp", (0, 0), "sayori/q.webp")
image sayori 4r = im.Composite((960, 960), (0, 0), "sayori/2l.webp", (0, 0), "sayori/2r.webp", (0, 0), "sayori/r.webp")
image sayori 4s = im.Composite((960, 960), (0, 0), "sayori/2l.webp", (0, 0), "sayori/2r.webp", (0, 0), "sayori/s.webp")
image sayori 4t = im.Composite((960, 960), (0, 0), "sayori/2l.webp", (0, 0), "sayori/2r.webp", (0, 0), "sayori/t.webp")
image sayori 4u = im.Composite((960, 960), (0, 0), "sayori/2l.webp", (0, 0), "sayori/2r.webp", (0, 0), "sayori/u.webp")
image sayori 4v = im.Composite((960, 960), (0, 0), "sayori/2l.webp", (0, 0), "sayori/2r.webp", (0, 0), "sayori/v.webp")
image sayori 4w = im.Composite((960, 960), (0, 0), "sayori/2l.webp", (0, 0), "sayori/2r.webp", (0, 0), "sayori/w.webp")
image sayori 4x = im.Composite((960, 960), (0, 0), "sayori/2l.webp", (0, 0), "sayori/2r.webp", (0, 0), "sayori/x.webp")
image sayori 4y = im.Composite((960, 960), (0, 0), "sayori/2l.webp", (0, 0), "sayori/2r.webp", (0, 0), "sayori/y.webp")

image sayori 5 = im.Composite((960, 960), (0, 0), "sayori/3a.webp")
image sayori 5a = im.Composite((960, 960), (0, 0), "sayori/3a.webp")
image sayori 5b = im.Composite((960, 960), (0, 0), "sayori/3b.webp")
image sayori 5c = im.Composite((960, 960), (0, 0), "sayori/3c.webp")
image sayori 5d = im.Composite((960, 960), (0, 0), "sayori/3d.webp")

image sayori 1ba = im.Composite((960, 960), (0, 0), "sayori/1bl.webp", (0, 0), "sayori/1br.webp", (0, 0), "sayori/a.webp")
image sayori 1bb = im.Composite((960, 960), (0, 0), "sayori/1bl.webp", (0, 0), "sayori/1br.webp", (0, 0), "sayori/b.webp")
image sayori 1bc = im.Composite((960, 960), (0, 0), "sayori/1bl.webp", (0, 0), "sayori/1br.webp", (0, 0), "sayori/c.webp")
image sayori 1bd = im.Composite((960, 960), (0, 0), "sayori/1bl.webp", (0, 0), "sayori/1br.webp", (0, 0), "sayori/d.webp")
image sayori 1be = im.Composite((960, 960), (0, 0), "sayori/1bl.webp", (0, 0), "sayori/1br.webp", (0, 0), "sayori/e.webp")
image sayori 1bf = im.Composite((960, 960), (0, 0), "sayori/1bl.webp", (0, 0), "sayori/1br.webp", (0, 0), "sayori/f.webp")
image sayori 1bg = im.Composite((960, 960), (0, 0), "sayori/1bl.webp", (0, 0), "sayori/1br.webp", (0, 0), "sayori/g.webp")
image sayori 1bh = im.Composite((960, 960), (0, 0), "sayori/1bl.webp", (0, 0), "sayori/1br.webp", (0, 0), "sayori/h.webp")
image sayori 1bi = im.Composite((960, 960), (0, 0), "sayori/1bl.webp", (0, 0), "sayori/1br.webp", (0, 0), "sayori/i.webp")
image sayori 1bj = im.Composite((960, 960), (0, 0), "sayori/1bl.webp", (0, 0), "sayori/1br.webp", (0, 0), "sayori/j.webp")
image sayori 1bk = im.Composite((960, 960), (0, 0), "sayori/1bl.webp", (0, 0), "sayori/1br.webp", (0, 0), "sayori/k.webp")
image sayori 1bl = im.Composite((960, 960), (0, 0), "sayori/1bl.webp", (0, 0), "sayori/1br.webp", (0, 0), "sayori/l.webp")
image sayori 1bm = im.Composite((960, 960), (0, 0), "sayori/1bl.webp", (0, 0), "sayori/1br.webp", (0, 0), "sayori/m.webp")
image sayori 1bn = im.Composite((960, 960), (0, 0), "sayori/1bl.webp", (0, 0), "sayori/1br.webp", (0, 0), "sayori/n.webp")
image sayori 1bo = im.Composite((960, 960), (0, 0), "sayori/1bl.webp", (0, 0), "sayori/1br.webp", (0, 0), "sayori/o.webp")
image sayori 1bp = im.Composite((960, 960), (0, 0), "sayori/1bl.webp", (0, 0), "sayori/1br.webp", (0, 0), "sayori/p.webp")
image sayori 1bq = im.Composite((960, 960), (0, 0), "sayori/1bl.webp", (0, 0), "sayori/1br.webp", (0, 0), "sayori/q.webp")
image sayori 1br = im.Composite((960, 960), (0, 0), "sayori/1bl.webp", (0, 0), "sayori/1br.webp", (0, 0), "sayori/r.webp")
image sayori 1bs = im.Composite((960, 960), (0, 0), "sayori/1bl.webp", (0, 0), "sayori/1br.webp", (0, 0), "sayori/s.webp")
image sayori 1bt = im.Composite((960, 960), (0, 0), "sayori/1bl.webp", (0, 0), "sayori/1br.webp", (0, 0), "sayori/t.webp")
image sayori 1bu = im.Composite((960, 960), (0, 0), "sayori/1bl.webp", (0, 0), "sayori/1br.webp", (0, 0), "sayori/u.webp")
image sayori 1bv = im.Composite((960, 960), (0, 0), "sayori/1bl.webp", (0, 0), "sayori/1br.webp", (0, 0), "sayori/v.webp")
image sayori 1bw = im.Composite((960, 960), (0, 0), "sayori/1bl.webp", (0, 0), "sayori/1br.webp", (0, 0), "sayori/w.webp")
image sayori 1bx = im.Composite((960, 960), (0, 0), "sayori/1bl.webp", (0, 0), "sayori/1br.webp", (0, 0), "sayori/x.webp")
image sayori 1by = im.Composite((960, 960), (0, 0), "sayori/1bl.webp", (0, 0), "sayori/1br.webp", (0, 0), "sayori/y.webp")

image sayori 2ba = im.Composite((960, 960), (0, 0), "sayori/1bl.webp", (0, 0), "sayori/2br.webp", (0, 0), "sayori/a.webp")
image sayori 2bb = im.Composite((960, 960), (0, 0), "sayori/1bl.webp", (0, 0), "sayori/2br.webp", (0, 0), "sayori/b.webp")
image sayori 2bc = im.Composite((960, 960), (0, 0), "sayori/1bl.webp", (0, 0), "sayori/2br.webp", (0, 0), "sayori/c.webp")
image sayori 2bd = im.Composite((960, 960), (0, 0), "sayori/1bl.webp", (0, 0), "sayori/2br.webp", (0, 0), "sayori/d.webp")
image sayori 2be = im.Composite((960, 960), (0, 0), "sayori/1bl.webp", (0, 0), "sayori/2br.webp", (0, 0), "sayori/e.webp")
image sayori 2bf = im.Composite((960, 960), (0, 0), "sayori/1bl.webp", (0, 0), "sayori/2br.webp", (0, 0), "sayori/f.webp")
image sayori 2bg = im.Composite((960, 960), (0, 0), "sayori/1bl.webp", (0, 0), "sayori/2br.webp", (0, 0), "sayori/g.webp")
image sayori 2bh = im.Composite((960, 960), (0, 0), "sayori/1bl.webp", (0, 0), "sayori/2br.webp", (0, 0), "sayori/h.webp")
image sayori 2bi = im.Composite((960, 960), (0, 0), "sayori/1bl.webp", (0, 0), "sayori/2br.webp", (0, 0), "sayori/i.webp")
image sayori 2bj = im.Composite((960, 960), (0, 0), "sayori/1bl.webp", (0, 0), "sayori/2br.webp", (0, 0), "sayori/j.webp")
image sayori 2bk = im.Composite((960, 960), (0, 0), "sayori/1bl.webp", (0, 0), "sayori/2br.webp", (0, 0), "sayori/k.webp")
image sayori 2bl = im.Composite((960, 960), (0, 0), "sayori/1bl.webp", (0, 0), "sayori/2br.webp", (0, 0), "sayori/l.webp")
image sayori 2bm = im.Composite((960, 960), (0, 0), "sayori/1bl.webp", (0, 0), "sayori/2br.webp", (0, 0), "sayori/m.webp")
image sayori 2bn = im.Composite((960, 960), (0, 0), "sayori/1bl.webp", (0, 0), "sayori/2br.webp", (0, 0), "sayori/n.webp")
image sayori 2bo = im.Composite((960, 960), (0, 0), "sayori/1bl.webp", (0, 0), "sayori/2br.webp", (0, 0), "sayori/o.webp")
image sayori 2bp = im.Composite((960, 960), (0, 0), "sayori/1bl.webp", (0, 0), "sayori/2br.webp", (0, 0), "sayori/p.webp")
image sayori 2bq = im.Composite((960, 960), (0, 0), "sayori/1bl.webp", (0, 0), "sayori/2br.webp", (0, 0), "sayori/q.webp")
image sayori 2br = im.Composite((960, 960), (0, 0), "sayori/1bl.webp", (0, 0), "sayori/2br.webp", (0, 0), "sayori/r.webp")
image sayori 2bs = im.Composite((960, 960), (0, 0), "sayori/1bl.webp", (0, 0), "sayori/2br.webp", (0, 0), "sayori/s.webp")
image sayori 2bt = im.Composite((960, 960), (0, 0), "sayori/1bl.webp", (0, 0), "sayori/2br.webp", (0, 0), "sayori/t.webp")
image sayori 2bu = im.Composite((960, 960), (0, 0), "sayori/1bl.webp", (0, 0), "sayori/2br.webp", (0, 0), "sayori/u.webp")
image sayori 2bv = im.Composite((960, 960), (0, 0), "sayori/1bl.webp", (0, 0), "sayori/2br.webp", (0, 0), "sayori/v.webp")
image sayori 2bw = im.Composite((960, 960), (0, 0), "sayori/1bl.webp", (0, 0), "sayori/2br.webp", (0, 0), "sayori/w.webp")
image sayori 2bx = im.Composite((960, 960), (0, 0), "sayori/1bl.webp", (0, 0), "sayori/2br.webp", (0, 0), "sayori/x.webp")
image sayori 2by = im.Composite((960, 960), (0, 0), "sayori/1bl.webp", (0, 0), "sayori/2br.webp", (0, 0), "sayori/y.webp")

image sayori 3ba = im.Composite((960, 960), (0, 0), "sayori/2bl.webp", (0, 0), "sayori/1br.webp", (0, 0), "sayori/a.webp")
image sayori 3bb = im.Composite((960, 960), (0, 0), "sayori/2bl.webp", (0, 0), "sayori/1br.webp", (0, 0), "sayori/b.webp")
image sayori 3bc = im.Composite((960, 960), (0, 0), "sayori/2bl.webp", (0, 0), "sayori/1br.webp", (0, 0), "sayori/c.webp")
image sayori 3bd = im.Composite((960, 960), (0, 0), "sayori/2bl.webp", (0, 0), "sayori/1br.webp", (0, 0), "sayori/d.webp")
image sayori 3be = im.Composite((960, 960), (0, 0), "sayori/2bl.webp", (0, 0), "sayori/1br.webp", (0, 0), "sayori/e.webp")
image sayori 3bf = im.Composite((960, 960), (0, 0), "sayori/2bl.webp", (0, 0), "sayori/1br.webp", (0, 0), "sayori/f.webp")
image sayori 3bg = im.Composite((960, 960), (0, 0), "sayori/2bl.webp", (0, 0), "sayori/1br.webp", (0, 0), "sayori/g.webp")
image sayori 3bh = im.Composite((960, 960), (0, 0), "sayori/2bl.webp", (0, 0), "sayori/1br.webp", (0, 0), "sayori/h.webp")
image sayori 3bi = im.Composite((960, 960), (0, 0), "sayori/2bl.webp", (0, 0), "sayori/1br.webp", (0, 0), "sayori/i.webp")
image sayori 3bj = im.Composite((960, 960), (0, 0), "sayori/2bl.webp", (0, 0), "sayori/1br.webp", (0, 0), "sayori/j.webp")
image sayori 3bk = im.Composite((960, 960), (0, 0), "sayori/2bl.webp", (0, 0), "sayori/1br.webp", (0, 0), "sayori/k.webp")
image sayori 3bl = im.Composite((960, 960), (0, 0), "sayori/2bl.webp", (0, 0), "sayori/1br.webp", (0, 0), "sayori/l.webp")
image sayori 3bm = im.Composite((960, 960), (0, 0), "sayori/2bl.webp", (0, 0), "sayori/1br.webp", (0, 0), "sayori/m.webp")
image sayori 3bn = im.Composite((960, 960), (0, 0), "sayori/2bl.webp", (0, 0), "sayori/1br.webp", (0, 0), "sayori/n.webp")
image sayori 3bo = im.Composite((960, 960), (0, 0), "sayori/2bl.webp", (0, 0), "sayori/1br.webp", (0, 0), "sayori/o.webp")
image sayori 3bp = im.Composite((960, 960), (0, 0), "sayori/2bl.webp", (0, 0), "sayori/1br.webp", (0, 0), "sayori/p.webp")
image sayori 3bq = im.Composite((960, 960), (0, 0), "sayori/2bl.webp", (0, 0), "sayori/1br.webp", (0, 0), "sayori/q.webp")
image sayori 3br = im.Composite((960, 960), (0, 0), "sayori/2bl.webp", (0, 0), "sayori/1br.webp", (0, 0), "sayori/r.webp")
image sayori 3bs = im.Composite((960, 960), (0, 0), "sayori/2bl.webp", (0, 0), "sayori/1br.webp", (0, 0), "sayori/s.webp")
image sayori 3bt = im.Composite((960, 960), (0, 0), "sayori/2bl.webp", (0, 0), "sayori/1br.webp", (0, 0), "sayori/t.webp")
image sayori 3bu = im.Composite((960, 960), (0, 0), "sayori/2bl.webp", (0, 0), "sayori/1br.webp", (0, 0), "sayori/u.webp")
image sayori 3bv = im.Composite((960, 960), (0, 0), "sayori/2bl.webp", (0, 0), "sayori/1br.webp", (0, 0), "sayori/v.webp")
image sayori 3bw = im.Composite((960, 960), (0, 0), "sayori/2bl.webp", (0, 0), "sayori/1br.webp", (0, 0), "sayori/w.webp")
image sayori 3bx = im.Composite((960, 960), (0, 0), "sayori/2bl.webp", (0, 0), "sayori/1br.webp", (0, 0), "sayori/x.webp")
image sayori 3by = im.Composite((960, 960), (0, 0), "sayori/2bl.webp", (0, 0), "sayori/1br.webp", (0, 0), "sayori/y.webp")

image sayori 4ba = im.Composite((960, 960), (0, 0), "sayori/2bl.webp", (0, 0), "sayori/2br.webp", (0, 0), "sayori/a.webp")
image sayori 4bb = im.Composite((960, 960), (0, 0), "sayori/2bl.webp", (0, 0), "sayori/2br.webp", (0, 0), "sayori/b.webp")
image sayori 4bc = im.Composite((960, 960), (0, 0), "sayori/2bl.webp", (0, 0), "sayori/2br.webp", (0, 0), "sayori/c.webp")
image sayori 4bd = im.Composite((960, 960), (0, 0), "sayori/2bl.webp", (0, 0), "sayori/2br.webp", (0, 0), "sayori/d.webp")
image sayori 4be = im.Composite((960, 960), (0, 0), "sayori/2bl.webp", (0, 0), "sayori/2br.webp", (0, 0), "sayori/e.webp")
image sayori 4bf = im.Composite((960, 960), (0, 0), "sayori/2bl.webp", (0, 0), "sayori/2br.webp", (0, 0), "sayori/f.webp")
image sayori 4bg = im.Composite((960, 960), (0, 0), "sayori/2bl.webp", (0, 0), "sayori/2br.webp", (0, 0), "sayori/g.webp")
image sayori 4bh = im.Composite((960, 960), (0, 0), "sayori/2bl.webp", (0, 0), "sayori/2br.webp", (0, 0), "sayori/h.webp")
image sayori 4bi = im.Composite((960, 960), (0, 0), "sayori/2bl.webp", (0, 0), "sayori/2br.webp", (0, 0), "sayori/i.webp")
image sayori 4bj = im.Composite((960, 960), (0, 0), "sayori/2bl.webp", (0, 0), "sayori/2br.webp", (0, 0), "sayori/j.webp")
image sayori 4bk = im.Composite((960, 960), (0, 0), "sayori/2bl.webp", (0, 0), "sayori/2br.webp", (0, 0), "sayori/k.webp")
image sayori 4bl = im.Composite((960, 960), (0, 0), "sayori/2bl.webp", (0, 0), "sayori/2br.webp", (0, 0), "sayori/l.webp")
image sayori 4bm = im.Composite((960, 960), (0, 0), "sayori/2bl.webp", (0, 0), "sayori/2br.webp", (0, 0), "sayori/m.webp")
image sayori 4bn = im.Composite((960, 960), (0, 0), "sayori/2bl.webp", (0, 0), "sayori/2br.webp", (0, 0), "sayori/n.webp")
image sayori 4bo = im.Composite((960, 960), (0, 0), "sayori/2bl.webp", (0, 0), "sayori/2br.webp", (0, 0), "sayori/o.webp")
image sayori 4bp = im.Composite((960, 960), (0, 0), "sayori/2bl.webp", (0, 0), "sayori/2br.webp", (0, 0), "sayori/p.webp")
image sayori 4bq = im.Composite((960, 960), (0, 0), "sayori/2bl.webp", (0, 0), "sayori/2br.webp", (0, 0), "sayori/q.webp")
image sayori 4br = im.Composite((960, 960), (0, 0), "sayori/2bl.webp", (0, 0), "sayori/2br.webp", (0, 0), "sayori/r.webp")
image sayori 4bs = im.Composite((960, 960), (0, 0), "sayori/2bl.webp", (0, 0), "sayori/2br.webp", (0, 0), "sayori/s.webp")
image sayori 4bt = im.Composite((960, 960), (0, 0), "sayori/2bl.webp", (0, 0), "sayori/2br.webp", (0, 0), "sayori/t.webp")
image sayori 4bu = im.Composite((960, 960), (0, 0), "sayori/2bl.webp", (0, 0), "sayori/2br.webp", (0, 0), "sayori/u.webp")
image sayori 4bv = im.Composite((960, 960), (0, 0), "sayori/2bl.webp", (0, 0), "sayori/2br.webp", (0, 0), "sayori/v.webp")
image sayori 4bw = im.Composite((960, 960), (0, 0), "sayori/2bl.webp", (0, 0), "sayori/2br.webp", (0, 0), "sayori/w.webp")
image sayori 4bx = im.Composite((960, 960), (0, 0), "sayori/2bl.webp", (0, 0), "sayori/2br.webp", (0, 0), "sayori/x.webp")
image sayori 4by = im.Composite((960, 960), (0, 0), "sayori/2bl.webp", (0, 0), "sayori/2br.webp", (0, 0), "sayori/y.webp")

image sayori glitch:
    "sayori/glitch1.webp"
    pause 0.01666
    "sayori/glitch2.webp"
    pause 0.01666
    repeat


image natsuki 11 = im.Composite((960, 960), (0, 0), "natsuki/1l.webp", (0, 0), "natsuki/1r.webp", (0, 0), "natsuki/1t.webp")
image natsuki 1a = im.Composite((960, 960), (0, 0), "natsuki/1l.webp", (0, 0), "natsuki/1r.webp", (0, 0), "natsuki/a.webp")
image natsuki 1b = im.Composite((960, 960), (0, 0), "natsuki/1l.webp", (0, 0), "natsuki/1r.webp", (0, 0), "natsuki/b.webp")
image natsuki 1c = im.Composite((960, 960), (0, 0), "natsuki/1l.webp", (0, 0), "natsuki/1r.webp", (0, 0), "natsuki/c.webp")
image natsuki 1d = im.Composite((960, 960), (0, 0), "natsuki/1l.webp", (0, 0), "natsuki/1r.webp", (0, 0), "natsuki/d.webp")
image natsuki 1e = im.Composite((960, 960), (0, 0), "natsuki/1l.webp", (0, 0), "natsuki/1r.webp", (0, 0), "natsuki/e.webp")
image natsuki 1f = im.Composite((960, 960), (0, 0), "natsuki/1l.webp", (0, 0), "natsuki/1r.webp", (0, 0), "natsuki/f.webp")
image natsuki 1g = im.Composite((960, 960), (0, 0), "natsuki/1l.webp", (0, 0), "natsuki/1r.webp", (0, 0), "natsuki/g.webp")
image natsuki 1h = im.Composite((960, 960), (0, 0), "natsuki/1l.webp", (0, 0), "natsuki/1r.webp", (0, 0), "natsuki/h.webp")
image natsuki 1i = im.Composite((960, 960), (0, 0), "natsuki/1l.webp", (0, 0), "natsuki/1r.webp", (0, 0), "natsuki/i.webp")
image natsuki 1j = im.Composite((960, 960), (0, 0), "natsuki/1l.webp", (0, 0), "natsuki/1r.webp", (0, 0), "natsuki/j.webp")
image natsuki 1k = im.Composite((960, 960), (0, 0), "natsuki/1l.webp", (0, 0), "natsuki/1r.webp", (0, 0), "natsuki/k.webp")
image natsuki 1l = im.Composite((960, 960), (0, 0), "natsuki/1l.webp", (0, 0), "natsuki/1r.webp", (0, 0), "natsuki/l.webp")
image natsuki 1m = im.Composite((960, 960), (0, 0), "natsuki/1l.webp", (0, 0), "natsuki/1r.webp", (0, 0), "natsuki/m.webp")
image natsuki 1n = im.Composite((960, 960), (0, 0), "natsuki/1l.webp", (0, 0), "natsuki/1r.webp", (0, 0), "natsuki/n.webp")
image natsuki 1o = im.Composite((960, 960), (0, 0), "natsuki/1l.webp", (0, 0), "natsuki/1r.webp", (0, 0), "natsuki/o.webp")
image natsuki 1p = im.Composite((960, 960), (0, 0), "natsuki/1l.webp", (0, 0), "natsuki/1r.webp", (0, 0), "natsuki/p.webp")
image natsuki 1q = im.Composite((960, 960), (0, 0), "natsuki/1l.webp", (0, 0), "natsuki/1r.webp", (0, 0), "natsuki/q.webp")
image natsuki 1r = im.Composite((960, 960), (0, 0), "natsuki/1l.webp", (0, 0), "natsuki/1r.webp", (0, 0), "natsuki/r.webp")
image natsuki 1s = im.Composite((960, 960), (0, 0), "natsuki/1l.webp", (0, 0), "natsuki/1r.webp", (0, 0), "natsuki/s.webp")
image natsuki 1t = im.Composite((960, 960), (0, 0), "natsuki/1l.webp", (0, 0), "natsuki/1r.webp", (0, 0), "natsuki/t.webp")
image natsuki 1u = im.Composite((960, 960), (0, 0), "natsuki/1l.webp", (0, 0), "natsuki/1r.webp", (0, 0), "natsuki/u.webp")
image natsuki 1v = im.Composite((960, 960), (0, 0), "natsuki/1l.webp", (0, 0), "natsuki/1r.webp", (0, 0), "natsuki/v.webp")
image natsuki 1w = im.Composite((960, 960), (0, 0), "natsuki/1l.webp", (0, 0), "natsuki/1r.webp", (0, 0), "natsuki/w.webp")
image natsuki 1x = im.Composite((960, 960), (0, 0), "natsuki/1l.webp", (0, 0), "natsuki/1r.webp", (0, 0), "natsuki/x.webp")
image natsuki 1y = im.Composite((960, 960), (0, 0), "natsuki/1l.webp", (0, 0), "natsuki/1r.webp", (0, 0), "natsuki/y.webp")
image natsuki 1z = im.Composite((960, 960), (0, 0), "natsuki/1l.webp", (0, 0), "natsuki/1r.webp", (0, 0), "natsuki/z.webp")

image natsuki 21 = im.Composite((960, 960), (0, 0), "natsuki/1l.webp", (0, 0), "natsuki/2r.webp", (0, 0), "natsuki/1t.webp")
image natsuki 2a = im.Composite((960, 960), (0, 0), "natsuki/1l.webp", (0, 0), "natsuki/2r.webp", (0, 0), "natsuki/a.webp")
image natsuki 2b = im.Composite((960, 960), (0, 0), "natsuki/1l.webp", (0, 0), "natsuki/2r.webp", (0, 0), "natsuki/b.webp")
image natsuki 2c = im.Composite((960, 960), (0, 0), "natsuki/1l.webp", (0, 0), "natsuki/2r.webp", (0, 0), "natsuki/c.webp")
image natsuki 2d = im.Composite((960, 960), (0, 0), "natsuki/1l.webp", (0, 0), "natsuki/2r.webp", (0, 0), "natsuki/d.webp")
image natsuki 2e = im.Composite((960, 960), (0, 0), "natsuki/1l.webp", (0, 0), "natsuki/2r.webp", (0, 0), "natsuki/e.webp")
image natsuki 2f = im.Composite((960, 960), (0, 0), "natsuki/1l.webp", (0, 0), "natsuki/2r.webp", (0, 0), "natsuki/f.webp")
image natsuki 2g = im.Composite((960, 960), (0, 0), "natsuki/1l.webp", (0, 0), "natsuki/2r.webp", (0, 0), "natsuki/g.webp")
image natsuki 2h = im.Composite((960, 960), (0, 0), "natsuki/1l.webp", (0, 0), "natsuki/2r.webp", (0, 0), "natsuki/h.webp")
image natsuki 2i = im.Composite((960, 960), (0, 0), "natsuki/1l.webp", (0, 0), "natsuki/2r.webp", (0, 0), "natsuki/i.webp")
image natsuki 2j = im.Composite((960, 960), (0, 0), "natsuki/1l.webp", (0, 0), "natsuki/2r.webp", (0, 0), "natsuki/j.webp")
image natsuki 2k = im.Composite((960, 960), (0, 0), "natsuki/1l.webp", (0, 0), "natsuki/2r.webp", (0, 0), "natsuki/k.webp")
image natsuki 2l = im.Composite((960, 960), (0, 0), "natsuki/1l.webp", (0, 0), "natsuki/2r.webp", (0, 0), "natsuki/l.webp")
image natsuki 2m = im.Composite((960, 960), (0, 0), "natsuki/1l.webp", (0, 0), "natsuki/2r.webp", (0, 0), "natsuki/m.webp")
image natsuki 2n = im.Composite((960, 960), (0, 0), "natsuki/1l.webp", (0, 0), "natsuki/2r.webp", (0, 0), "natsuki/n.webp")
image natsuki 2o = im.Composite((960, 960), (0, 0), "natsuki/1l.webp", (0, 0), "natsuki/2r.webp", (0, 0), "natsuki/o.webp")
image natsuki 2p = im.Composite((960, 960), (0, 0), "natsuki/1l.webp", (0, 0), "natsuki/2r.webp", (0, 0), "natsuki/p.webp")
image natsuki 2q = im.Composite((960, 960), (0, 0), "natsuki/1l.webp", (0, 0), "natsuki/2r.webp", (0, 0), "natsuki/q.webp")
image natsuki 2r = im.Composite((960, 960), (0, 0), "natsuki/1l.webp", (0, 0), "natsuki/2r.webp", (0, 0), "natsuki/r.webp")
image natsuki 2s = im.Composite((960, 960), (0, 0), "natsuki/1l.webp", (0, 0), "natsuki/2r.webp", (0, 0), "natsuki/s.webp")
image natsuki 2t = im.Composite((960, 960), (0, 0), "natsuki/1l.webp", (0, 0), "natsuki/2r.webp", (0, 0), "natsuki/t.webp")
image natsuki 2u = im.Composite((960, 960), (0, 0), "natsuki/1l.webp", (0, 0), "natsuki/2r.webp", (0, 0), "natsuki/u.webp")
image natsuki 2v = im.Composite((960, 960), (0, 0), "natsuki/1l.webp", (0, 0), "natsuki/2r.webp", (0, 0), "natsuki/v.webp")
image natsuki 2w = im.Composite((960, 960), (0, 0), "natsuki/1l.webp", (0, 0), "natsuki/2r.webp", (0, 0), "natsuki/w.webp")
image natsuki 2x = im.Composite((960, 960), (0, 0), "natsuki/1l.webp", (0, 0), "natsuki/2r.webp", (0, 0), "natsuki/x.webp")
image natsuki 2y = im.Composite((960, 960), (0, 0), "natsuki/1l.webp", (0, 0), "natsuki/2r.webp", (0, 0), "natsuki/y.webp")
image natsuki 2z = im.Composite((960, 960), (0, 0), "natsuki/1l.webp", (0, 0), "natsuki/2r.webp", (0, 0), "natsuki/z.webp")

image natsuki 31 = im.Composite((960, 960), (0, 0), "natsuki/2l.webp", (0, 0), "natsuki/1r.webp", (0, 0), "natsuki/1t.webp")
image natsuki 3a = im.Composite((960, 960), (0, 0), "natsuki/2l.webp", (0, 0), "natsuki/1r.webp", (0, 0), "natsuki/a.webp")
image natsuki 3b = im.Composite((960, 960), (0, 0), "natsuki/2l.webp", (0, 0), "natsuki/1r.webp", (0, 0), "natsuki/b.webp")
image natsuki 3c = im.Composite((960, 960), (0, 0), "natsuki/2l.webp", (0, 0), "natsuki/1r.webp", (0, 0), "natsuki/c.webp")
image natsuki 3d = im.Composite((960, 960), (0, 0), "natsuki/2l.webp", (0, 0), "natsuki/1r.webp", (0, 0), "natsuki/d.webp")
image natsuki 3e = im.Composite((960, 960), (0, 0), "natsuki/2l.webp", (0, 0), "natsuki/1r.webp", (0, 0), "natsuki/e.webp")
image natsuki 3f = im.Composite((960, 960), (0, 0), "natsuki/2l.webp", (0, 0), "natsuki/1r.webp", (0, 0), "natsuki/f.webp")
image natsuki 3g = im.Composite((960, 960), (0, 0), "natsuki/2l.webp", (0, 0), "natsuki/1r.webp", (0, 0), "natsuki/g.webp")
image natsuki 3h = im.Composite((960, 960), (0, 0), "natsuki/2l.webp", (0, 0), "natsuki/1r.webp", (0, 0), "natsuki/h.webp")
image natsuki 3i = im.Composite((960, 960), (0, 0), "natsuki/2l.webp", (0, 0), "natsuki/1r.webp", (0, 0), "natsuki/i.webp")
image natsuki 3j = im.Composite((960, 960), (0, 0), "natsuki/2l.webp", (0, 0), "natsuki/1r.webp", (0, 0), "natsuki/j.webp")
image natsuki 3k = im.Composite((960, 960), (0, 0), "natsuki/2l.webp", (0, 0), "natsuki/1r.webp", (0, 0), "natsuki/k.webp")
image natsuki 3l = im.Composite((960, 960), (0, 0), "natsuki/2l.webp", (0, 0), "natsuki/1r.webp", (0, 0), "natsuki/l.webp")
image natsuki 3m = im.Composite((960, 960), (0, 0), "natsuki/2l.webp", (0, 0), "natsuki/1r.webp", (0, 0), "natsuki/m.webp")
image natsuki 3n = im.Composite((960, 960), (0, 0), "natsuki/2l.webp", (0, 0), "natsuki/1r.webp", (0, 0), "natsuki/n.webp")
image natsuki 3o = im.Composite((960, 960), (0, 0), "natsuki/2l.webp", (0, 0), "natsuki/1r.webp", (0, 0), "natsuki/o.webp")
image natsuki 3p = im.Composite((960, 960), (0, 0), "natsuki/2l.webp", (0, 0), "natsuki/1r.webp", (0, 0), "natsuki/p.webp")
image natsuki 3q = im.Composite((960, 960), (0, 0), "natsuki/2l.webp", (0, 0), "natsuki/1r.webp", (0, 0), "natsuki/q.webp")
image natsuki 3r = im.Composite((960, 960), (0, 0), "natsuki/2l.webp", (0, 0), "natsuki/1r.webp", (0, 0), "natsuki/r.webp")
image natsuki 3s = im.Composite((960, 960), (0, 0), "natsuki/2l.webp", (0, 0), "natsuki/1r.webp", (0, 0), "natsuki/s.webp")
image natsuki 3t = im.Composite((960, 960), (0, 0), "natsuki/2l.webp", (0, 0), "natsuki/1r.webp", (0, 0), "natsuki/t.webp")
image natsuki 3u = im.Composite((960, 960), (0, 0), "natsuki/2l.webp", (0, 0), "natsuki/1r.webp", (0, 0), "natsuki/u.webp")
image natsuki 3v = im.Composite((960, 960), (0, 0), "natsuki/2l.webp", (0, 0), "natsuki/1r.webp", (0, 0), "natsuki/v.webp")
image natsuki 3w = im.Composite((960, 960), (0, 0), "natsuki/2l.webp", (0, 0), "natsuki/1r.webp", (0, 0), "natsuki/w.webp")
image natsuki 3x = im.Composite((960, 960), (0, 0), "natsuki/2l.webp", (0, 0), "natsuki/1r.webp", (0, 0), "natsuki/x.webp")
image natsuki 3y = im.Composite((960, 960), (0, 0), "natsuki/2l.webp", (0, 0), "natsuki/1r.webp", (0, 0), "natsuki/y.webp")
image natsuki 3z = im.Composite((960, 960), (0, 0), "natsuki/2l.webp", (0, 0), "natsuki/1r.webp", (0, 0), "natsuki/z.webp")

image natsuki 41 = im.Composite((960, 960), (0, 0), "natsuki/2l.webp", (0, 0), "natsuki/2r.webp", (0, 0), "natsuki/1t.webp")
image natsuki 4a = im.Composite((960, 960), (0, 0), "natsuki/2l.webp", (0, 0), "natsuki/2r.webp", (0, 0), "natsuki/a.webp")
image natsuki 4b = im.Composite((960, 960), (0, 0), "natsuki/2l.webp", (0, 0), "natsuki/2r.webp", (0, 0), "natsuki/b.webp")
image natsuki 4c = im.Composite((960, 960), (0, 0), "natsuki/2l.webp", (0, 0), "natsuki/2r.webp", (0, 0), "natsuki/c.webp")
image natsuki 4d = im.Composite((960, 960), (0, 0), "natsuki/2l.webp", (0, 0), "natsuki/2r.webp", (0, 0), "natsuki/d.webp")
image natsuki 4e = im.Composite((960, 960), (0, 0), "natsuki/2l.webp", (0, 0), "natsuki/2r.webp", (0, 0), "natsuki/e.webp")
image natsuki 4f = im.Composite((960, 960), (0, 0), "natsuki/2l.webp", (0, 0), "natsuki/2r.webp", (0, 0), "natsuki/f.webp")
image natsuki 4g = im.Composite((960, 960), (0, 0), "natsuki/2l.webp", (0, 0), "natsuki/2r.webp", (0, 0), "natsuki/g.webp")
image natsuki 4h = im.Composite((960, 960), (0, 0), "natsuki/2l.webp", (0, 0), "natsuki/2r.webp", (0, 0), "natsuki/h.webp")
image natsuki 4i = im.Composite((960, 960), (0, 0), "natsuki/2l.webp", (0, 0), "natsuki/2r.webp", (0, 0), "natsuki/i.webp")
image natsuki 4j = im.Composite((960, 960), (0, 0), "natsuki/2l.webp", (0, 0), "natsuki/2r.webp", (0, 0), "natsuki/j.webp")
image natsuki 4k = im.Composite((960, 960), (0, 0), "natsuki/2l.webp", (0, 0), "natsuki/2r.webp", (0, 0), "natsuki/k.webp")
image natsuki 4l = im.Composite((960, 960), (0, 0), "natsuki/2l.webp", (0, 0), "natsuki/2r.webp", (0, 0), "natsuki/l.webp")
image natsuki 4m = im.Composite((960, 960), (0, 0), "natsuki/2l.webp", (0, 0), "natsuki/2r.webp", (0, 0), "natsuki/m.webp")
image natsuki 4n = im.Composite((960, 960), (0, 0), "natsuki/2l.webp", (0, 0), "natsuki/2r.webp", (0, 0), "natsuki/n.webp")
image natsuki 4o = im.Composite((960, 960), (0, 0), "natsuki/2l.webp", (0, 0), "natsuki/2r.webp", (0, 0), "natsuki/o.webp")
image natsuki 4p = im.Composite((960, 960), (0, 0), "natsuki/2l.webp", (0, 0), "natsuki/2r.webp", (0, 0), "natsuki/p.webp")
image natsuki 4q = im.Composite((960, 960), (0, 0), "natsuki/2l.webp", (0, 0), "natsuki/2r.webp", (0, 0), "natsuki/q.webp")
image natsuki 4r = im.Composite((960, 960), (0, 0), "natsuki/2l.webp", (0, 0), "natsuki/2r.webp", (0, 0), "natsuki/r.webp")
image natsuki 4s = im.Composite((960, 960), (0, 0), "natsuki/2l.webp", (0, 0), "natsuki/2r.webp", (0, 0), "natsuki/s.webp")
image natsuki 4t = im.Composite((960, 960), (0, 0), "natsuki/2l.webp", (0, 0), "natsuki/2r.webp", (0, 0), "natsuki/t.webp")
image natsuki 4u = im.Composite((960, 960), (0, 0), "natsuki/2l.webp", (0, 0), "natsuki/2r.webp", (0, 0), "natsuki/u.webp")
image natsuki 4v = im.Composite((960, 960), (0, 0), "natsuki/2l.webp", (0, 0), "natsuki/2r.webp", (0, 0), "natsuki/v.webp")
image natsuki 4w = im.Composite((960, 960), (0, 0), "natsuki/2l.webp", (0, 0), "natsuki/2r.webp", (0, 0), "natsuki/w.webp")
image natsuki 4x = im.Composite((960, 960), (0, 0), "natsuki/2l.webp", (0, 0), "natsuki/2r.webp", (0, 0), "natsuki/x.webp")
image natsuki 4y = im.Composite((960, 960), (0, 0), "natsuki/2l.webp", (0, 0), "natsuki/2r.webp", (0, 0), "natsuki/y.webp")
image natsuki 4z = im.Composite((960, 960), (0, 0), "natsuki/2l.webp", (0, 0), "natsuki/2r.webp", (0, 0), "natsuki/z.webp")

image natsuki 12 = im.Composite((960, 960), (0, 0), "natsuki/1l.webp", (0, 0), "natsuki/1r.webp", (0, 0), "natsuki/2t.webp")
image natsuki 12a = im.Composite((960, 960), (0, 0), "natsuki/1l.webp", (0, 0), "natsuki/1r.webp", (0, 0), "natsuki/2ta.webp")
image natsuki 12b = im.Composite((960, 960), (0, 0), "natsuki/1l.webp", (0, 0), "natsuki/1r.webp", (0, 0), "natsuki/2tb.webp")
image natsuki 12c = im.Composite((960, 960), (0, 0), "natsuki/1l.webp", (0, 0), "natsuki/1r.webp", (0, 0), "natsuki/2tc.webp")
image natsuki 12d = im.Composite((960, 960), (0, 0), "natsuki/1l.webp", (0, 0), "natsuki/1r.webp", (0, 0), "natsuki/2td.webp")
image natsuki 12e = im.Composite((960, 960), (0, 0), "natsuki/1l.webp", (0, 0), "natsuki/1r.webp", (0, 0), "natsuki/2te.webp")
image natsuki 12f = im.Composite((960, 960), (0, 0), "natsuki/1l.webp", (0, 0), "natsuki/1r.webp", (0, 0), "natsuki/2tf.webp")
image natsuki 12g = im.Composite((960, 960), (0, 0), "natsuki/1l.webp", (0, 0), "natsuki/1r.webp", (0, 0), "natsuki/2tg.webp")
image natsuki 12h = im.Composite((960, 960), (0, 0), "natsuki/1l.webp", (0, 0), "natsuki/1r.webp", (0, 0), "natsuki/2th.webp")
image natsuki 12i = im.Composite((960, 960), (0, 0), "natsuki/1l.webp", (0, 0), "natsuki/1r.webp", (0, 0), "natsuki/2ti.webp")

image natsuki 42 = im.Composite((960, 960), (0, 0), "natsuki/2l.webp", (0, 0), "natsuki/2r.webp", (0, 0), "natsuki/2t.webp")
image natsuki 42a = im.Composite((960, 960), (0, 0), "natsuki/2l.webp", (0, 0), "natsuki/2r.webp", (0, 0), "natsuki/2ta.webp")
image natsuki 42b = im.Composite((960, 960), (0, 0), "natsuki/2l.webp", (0, 0), "natsuki/2r.webp", (0, 0), "natsuki/2tb.webp")
image natsuki 42c = im.Composite((960, 960), (0, 0), "natsuki/2l.webp", (0, 0), "natsuki/2r.webp", (0, 0), "natsuki/2tc.webp")
image natsuki 42d = im.Composite((960, 960), (0, 0), "natsuki/2l.webp", (0, 0), "natsuki/2r.webp", (0, 0), "natsuki/2td.webp")
image natsuki 42e = im.Composite((960, 960), (0, 0), "natsuki/2l.webp", (0, 0), "natsuki/2r.webp", (0, 0), "natsuki/2te.webp")
image natsuki 42f = im.Composite((960, 960), (0, 0), "natsuki/2l.webp", (0, 0), "natsuki/2r.webp", (0, 0), "natsuki/2tf.webp")
image natsuki 42g = im.Composite((960, 960), (0, 0), "natsuki/2l.webp", (0, 0), "natsuki/2r.webp", (0, 0), "natsuki/2tg.webp")
image natsuki 42h = im.Composite((960, 960), (0, 0), "natsuki/2l.webp", (0, 0), "natsuki/2r.webp", (0, 0), "natsuki/2th.webp")
image natsuki 42i = im.Composite((960, 960), (0, 0), "natsuki/2l.webp", (0, 0), "natsuki/2r.webp", (0, 0), "natsuki/2ti.webp")

image natsuki 51 = im.Composite((960, 960), (18, 22), "natsuki/1t.webp", (0, 0), "natsuki/3.webp")
image natsuki 5a = im.Composite((960, 960), (18, 22), "natsuki/a.webp", (0, 0), "natsuki/3.webp")
image natsuki 5b = im.Composite((960, 960), (18, 22), "natsuki/b.webp", (0, 0), "natsuki/3.webp")
image natsuki 5c = im.Composite((960, 960), (18, 22), "natsuki/c.webp", (0, 0), "natsuki/3.webp")
image natsuki 5d = im.Composite((960, 960), (18, 22), "natsuki/d.webp", (0, 0), "natsuki/3.webp")
image natsuki 5e = im.Composite((960, 960), (18, 22), "natsuki/e.webp", (0, 0), "natsuki/3.webp")
image natsuki 5f = im.Composite((960, 960), (18, 22), "natsuki/f.webp", (0, 0), "natsuki/3.webp")
image natsuki 5g = im.Composite((960, 960), (18, 22), "natsuki/g.webp", (0, 0), "natsuki/3.webp")
image natsuki 5h = im.Composite((960, 960), (18, 22), "natsuki/h.webp", (0, 0), "natsuki/3.webp")
image natsuki 5i = im.Composite((960, 960), (18, 22), "natsuki/i.webp", (0, 0), "natsuki/3.webp")
image natsuki 5j = im.Composite((960, 960), (18, 22), "natsuki/j.webp", (0, 0), "natsuki/3.webp")
image natsuki 5k = im.Composite((960, 960), (18, 22), "natsuki/k.webp", (0, 0), "natsuki/3.webp")
image natsuki 5l = im.Composite((960, 960), (18, 22), "natsuki/l.webp", (0, 0), "natsuki/3.webp")
image natsuki 5m = im.Composite((960, 960), (18, 22), "natsuki/m.webp", (0, 0), "natsuki/3.webp")
image natsuki 5n = im.Composite((960, 960), (18, 22), "natsuki/n.webp", (0, 0), "natsuki/3.webp")
image natsuki 5o = im.Composite((960, 960), (18, 22), "natsuki/o.webp", (0, 0), "natsuki/3.webp")
image natsuki 5p = im.Composite((960, 960), (18, 22), "natsuki/p.webp", (0, 0), "natsuki/3.webp")
image natsuki 5q = im.Composite((960, 960), (18, 22), "natsuki/q.webp", (0, 0), "natsuki/3.webp")
image natsuki 5r = im.Composite((960, 960), (18, 22), "natsuki/r.webp", (0, 0), "natsuki/3.webp")
image natsuki 5s = im.Composite((960, 960), (18, 22), "natsuki/s.webp", (0, 0), "natsuki/3.webp")
image natsuki 5t = im.Composite((960, 960), (18, 22), "natsuki/t.webp", (0, 0), "natsuki/3.webp")
image natsuki 5u = im.Composite((960, 960), (18, 22), "natsuki/u.webp", (0, 0), "natsuki/3.webp")
image natsuki 5v = im.Composite((960, 960), (18, 22), "natsuki/v.webp", (0, 0), "natsuki/3.webp")
image natsuki 5w = im.Composite((960, 960), (18, 22), "natsuki/w.webp", (0, 0), "natsuki/3.webp")
image natsuki 5x = im.Composite((960, 960), (18, 22), "natsuki/x.webp", (0, 0), "natsuki/3.webp")
image natsuki 5y = im.Composite((960, 960), (18, 22), "natsuki/y.webp", (0, 0), "natsuki/3.webp")
image natsuki 5z = im.Composite((960, 960), (18, 22), "natsuki/z.webp", (0, 0), "natsuki/3.webp")



image natsuki 1ba = im.Composite((960, 960), (0, 0), "natsuki/1bl.webp", (0, 0), "natsuki/1br.webp", (0, 0), "natsuki/a.webp")
image natsuki 1bb = im.Composite((960, 960), (0, 0), "natsuki/1bl.webp", (0, 0), "natsuki/1br.webp", (0, 0), "natsuki/b.webp")
image natsuki 1bc = im.Composite((960, 960), (0, 0), "natsuki/1bl.webp", (0, 0), "natsuki/1br.webp", (0, 0), "natsuki/c.webp")
image natsuki 1bd = im.Composite((960, 960), (0, 0), "natsuki/1bl.webp", (0, 0), "natsuki/1br.webp", (0, 0), "natsuki/d.webp")
image natsuki 1be = im.Composite((960, 960), (0, 0), "natsuki/1bl.webp", (0, 0), "natsuki/1br.webp", (0, 0), "natsuki/e.webp")
image natsuki 1bf = im.Composite((960, 960), (0, 0), "natsuki/1bl.webp", (0, 0), "natsuki/1br.webp", (0, 0), "natsuki/f.webp")
image natsuki 1bg = im.Composite((960, 960), (0, 0), "natsuki/1bl.webp", (0, 0), "natsuki/1br.webp", (0, 0), "natsuki/g.webp")
image natsuki 1bh = im.Composite((960, 960), (0, 0), "natsuki/1bl.webp", (0, 0), "natsuki/1br.webp", (0, 0), "natsuki/h.webp")
image natsuki 1bi = im.Composite((960, 960), (0, 0), "natsuki/1bl.webp", (0, 0), "natsuki/1br.webp", (0, 0), "natsuki/i.webp")
image natsuki 1bj = im.Composite((960, 960), (0, 0), "natsuki/1bl.webp", (0, 0), "natsuki/1br.webp", (0, 0), "natsuki/j.webp")
image natsuki 1bk = im.Composite((960, 960), (0, 0), "natsuki/1bl.webp", (0, 0), "natsuki/1br.webp", (0, 0), "natsuki/k.webp")
image natsuki 1bl = im.Composite((960, 960), (0, 0), "natsuki/1bl.webp", (0, 0), "natsuki/1br.webp", (0, 0), "natsuki/l.webp")
image natsuki 1bm = im.Composite((960, 960), (0, 0), "natsuki/1bl.webp", (0, 0), "natsuki/1br.webp", (0, 0), "natsuki/m.webp")
image natsuki 1bn = im.Composite((960, 960), (0, 0), "natsuki/1bl.webp", (0, 0), "natsuki/1br.webp", (0, 0), "natsuki/n.webp")
image natsuki 1bo = im.Composite((960, 960), (0, 0), "natsuki/1bl.webp", (0, 0), "natsuki/1br.webp", (0, 0), "natsuki/o.webp")
image natsuki 1bp = im.Composite((960, 960), (0, 0), "natsuki/1bl.webp", (0, 0), "natsuki/1br.webp", (0, 0), "natsuki/p.webp")
image natsuki 1bq = im.Composite((960, 960), (0, 0), "natsuki/1bl.webp", (0, 0), "natsuki/1br.webp", (0, 0), "natsuki/q.webp")
image natsuki 1br = im.Composite((960, 960), (0, 0), "natsuki/1bl.webp", (0, 0), "natsuki/1br.webp", (0, 0), "natsuki/r.webp")
image natsuki 1bs = im.Composite((960, 960), (0, 0), "natsuki/1bl.webp", (0, 0), "natsuki/1br.webp", (0, 0), "natsuki/s.webp")
image natsuki 1bt = im.Composite((960, 960), (0, 0), "natsuki/1bl.webp", (0, 0), "natsuki/1br.webp", (0, 0), "natsuki/t.webp")
image natsuki 1bu = im.Composite((960, 960), (0, 0), "natsuki/1bl.webp", (0, 0), "natsuki/1br.webp", (0, 0), "natsuki/u.webp")
image natsuki 1bv = im.Composite((960, 960), (0, 0), "natsuki/1bl.webp", (0, 0), "natsuki/1br.webp", (0, 0), "natsuki/v.webp")
image natsuki 1bw = im.Composite((960, 960), (0, 0), "natsuki/1bl.webp", (0, 0), "natsuki/1br.webp", (0, 0), "natsuki/w.webp")
image natsuki 1bx = im.Composite((960, 960), (0, 0), "natsuki/1bl.webp", (0, 0), "natsuki/1br.webp", (0, 0), "natsuki/x.webp")
image natsuki 1by = im.Composite((960, 960), (0, 0), "natsuki/1bl.webp", (0, 0), "natsuki/1br.webp", (0, 0), "natsuki/y.webp")
image natsuki 1bz = im.Composite((960, 960), (0, 0), "natsuki/1bl.webp", (0, 0), "natsuki/1br.webp", (0, 0), "natsuki/z.webp")

image natsuki 2ba = im.Composite((960, 960), (0, 0), "natsuki/1bl.webp", (0, 0), "natsuki/2br.webp", (0, 0), "natsuki/a.webp")
image natsuki 2bb = im.Composite((960, 960), (0, 0), "natsuki/1bl.webp", (0, 0), "natsuki/2br.webp", (0, 0), "natsuki/b.webp")
image natsuki 2bc = im.Composite((960, 960), (0, 0), "natsuki/1bl.webp", (0, 0), "natsuki/2br.webp", (0, 0), "natsuki/c.webp")
image natsuki 2bd = im.Composite((960, 960), (0, 0), "natsuki/1bl.webp", (0, 0), "natsuki/2br.webp", (0, 0), "natsuki/d.webp")
image natsuki 2be = im.Composite((960, 960), (0, 0), "natsuki/1bl.webp", (0, 0), "natsuki/2br.webp", (0, 0), "natsuki/e.webp")
image natsuki 2bf = im.Composite((960, 960), (0, 0), "natsuki/1bl.webp", (0, 0), "natsuki/2br.webp", (0, 0), "natsuki/f.webp")
image natsuki 2bg = im.Composite((960, 960), (0, 0), "natsuki/1bl.webp", (0, 0), "natsuki/2br.webp", (0, 0), "natsuki/g.webp")
image natsuki 2bh = im.Composite((960, 960), (0, 0), "natsuki/1bl.webp", (0, 0), "natsuki/2br.webp", (0, 0), "natsuki/h.webp")
image natsuki 2bi = im.Composite((960, 960), (0, 0), "natsuki/1bl.webp", (0, 0), "natsuki/2br.webp", (0, 0), "natsuki/i.webp")
image natsuki 2bj = im.Composite((960, 960), (0, 0), "natsuki/1bl.webp", (0, 0), "natsuki/2br.webp", (0, 0), "natsuki/j.webp")
image natsuki 2bk = im.Composite((960, 960), (0, 0), "natsuki/1bl.webp", (0, 0), "natsuki/2br.webp", (0, 0), "natsuki/k.webp")
image natsuki 2bl = im.Composite((960, 960), (0, 0), "natsuki/1bl.webp", (0, 0), "natsuki/2br.webp", (0, 0), "natsuki/l.webp")
image natsuki 2bm = im.Composite((960, 960), (0, 0), "natsuki/1bl.webp", (0, 0), "natsuki/2br.webp", (0, 0), "natsuki/m.webp")
image natsuki 2bn = im.Composite((960, 960), (0, 0), "natsuki/1bl.webp", (0, 0), "natsuki/2br.webp", (0, 0), "natsuki/n.webp")
image natsuki 2bo = im.Composite((960, 960), (0, 0), "natsuki/1bl.webp", (0, 0), "natsuki/2br.webp", (0, 0), "natsuki/o.webp")
image natsuki 2bp = im.Composite((960, 960), (0, 0), "natsuki/1bl.webp", (0, 0), "natsuki/2br.webp", (0, 0), "natsuki/p.webp")
image natsuki 2bq = im.Composite((960, 960), (0, 0), "natsuki/1bl.webp", (0, 0), "natsuki/2br.webp", (0, 0), "natsuki/q.webp")
image natsuki 2br = im.Composite((960, 960), (0, 0), "natsuki/1bl.webp", (0, 0), "natsuki/2br.webp", (0, 0), "natsuki/r.webp")
image natsuki 2bs = im.Composite((960, 960), (0, 0), "natsuki/1bl.webp", (0, 0), "natsuki/2br.webp", (0, 0), "natsuki/s.webp")
image natsuki 2bt = im.Composite((960, 960), (0, 0), "natsuki/1bl.webp", (0, 0), "natsuki/2br.webp", (0, 0), "natsuki/t.webp")
image natsuki 2bu = im.Composite((960, 960), (0, 0), "natsuki/1bl.webp", (0, 0), "natsuki/2br.webp", (0, 0), "natsuki/u.webp")
image natsuki 2bv = im.Composite((960, 960), (0, 0), "natsuki/1bl.webp", (0, 0), "natsuki/2br.webp", (0, 0), "natsuki/v.webp")
image natsuki 2bw = im.Composite((960, 960), (0, 0), "natsuki/1bl.webp", (0, 0), "natsuki/2br.webp", (0, 0), "natsuki/w.webp")
image natsuki 2bx = im.Composite((960, 960), (0, 0), "natsuki/1bl.webp", (0, 0), "natsuki/2br.webp", (0, 0), "natsuki/x.webp")
image natsuki 2by = im.Composite((960, 960), (0, 0), "natsuki/1bl.webp", (0, 0), "natsuki/2br.webp", (0, 0), "natsuki/y.webp")
image natsuki 2bz = im.Composite((960, 960), (0, 0), "natsuki/1bl.webp", (0, 0), "natsuki/2br.webp", (0, 0), "natsuki/z.webp")

image natsuki 3ba = im.Composite((960, 960), (0, 0), "natsuki/2bl.webp", (0, 0), "natsuki/1br.webp", (0, 0), "natsuki/a.webp")
image natsuki 3bb = im.Composite((960, 960), (0, 0), "natsuki/2bl.webp", (0, 0), "natsuki/1br.webp", (0, 0), "natsuki/b.webp")
image natsuki 3bc = im.Composite((960, 960), (0, 0), "natsuki/2bl.webp", (0, 0), "natsuki/1br.webp", (0, 0), "natsuki/c.webp")
image natsuki 3bd = im.Composite((960, 960), (0, 0), "natsuki/2bl.webp", (0, 0), "natsuki/1br.webp", (0, 0), "natsuki/d.webp")
image natsuki 3be = im.Composite((960, 960), (0, 0), "natsuki/2bl.webp", (0, 0), "natsuki/1br.webp", (0, 0), "natsuki/e.webp")
image natsuki 3bf = im.Composite((960, 960), (0, 0), "natsuki/2bl.webp", (0, 0), "natsuki/1br.webp", (0, 0), "natsuki/f.webp")
image natsuki 3bg = im.Composite((960, 960), (0, 0), "natsuki/2bl.webp", (0, 0), "natsuki/1br.webp", (0, 0), "natsuki/g.webp")
image natsuki 3bh = im.Composite((960, 960), (0, 0), "natsuki/2bl.webp", (0, 0), "natsuki/1br.webp", (0, 0), "natsuki/h.webp")
image natsuki 3bi = im.Composite((960, 960), (0, 0), "natsuki/2bl.webp", (0, 0), "natsuki/1br.webp", (0, 0), "natsuki/i.webp")
image natsuki 3bj = im.Composite((960, 960), (0, 0), "natsuki/2bl.webp", (0, 0), "natsuki/1br.webp", (0, 0), "natsuki/j.webp")
image natsuki 3bk = im.Composite((960, 960), (0, 0), "natsuki/2bl.webp", (0, 0), "natsuki/1br.webp", (0, 0), "natsuki/k.webp")
image natsuki 3bl = im.Composite((960, 960), (0, 0), "natsuki/2bl.webp", (0, 0), "natsuki/1br.webp", (0, 0), "natsuki/l.webp")
image natsuki 3bm = im.Composite((960, 960), (0, 0), "natsuki/2bl.webp", (0, 0), "natsuki/1br.webp", (0, 0), "natsuki/m.webp")
image natsuki 3bn = im.Composite((960, 960), (0, 0), "natsuki/2bl.webp", (0, 0), "natsuki/1br.webp", (0, 0), "natsuki/n.webp")
image natsuki 3bo = im.Composite((960, 960), (0, 0), "natsuki/2bl.webp", (0, 0), "natsuki/1br.webp", (0, 0), "natsuki/o.webp")
image natsuki 3bp = im.Composite((960, 960), (0, 0), "natsuki/2bl.webp", (0, 0), "natsuki/1br.webp", (0, 0), "natsuki/p.webp")
image natsuki 3bq = im.Composite((960, 960), (0, 0), "natsuki/2bl.webp", (0, 0), "natsuki/1br.webp", (0, 0), "natsuki/q.webp")
image natsuki 3br = im.Composite((960, 960), (0, 0), "natsuki/2bl.webp", (0, 0), "natsuki/1br.webp", (0, 0), "natsuki/r.webp")
image natsuki 3bs = im.Composite((960, 960), (0, 0), "natsuki/2bl.webp", (0, 0), "natsuki/1br.webp", (0, 0), "natsuki/s.webp")
image natsuki 3bt = im.Composite((960, 960), (0, 0), "natsuki/2bl.webp", (0, 0), "natsuki/1br.webp", (0, 0), "natsuki/t.webp")
image natsuki 3bu = im.Composite((960, 960), (0, 0), "natsuki/2bl.webp", (0, 0), "natsuki/1br.webp", (0, 0), "natsuki/u.webp")
image natsuki 3bv = im.Composite((960, 960), (0, 0), "natsuki/2bl.webp", (0, 0), "natsuki/1br.webp", (0, 0), "natsuki/v.webp")
image natsuki 3bw = im.Composite((960, 960), (0, 0), "natsuki/2bl.webp", (0, 0), "natsuki/1br.webp", (0, 0), "natsuki/w.webp")
image natsuki 3bx = im.Composite((960, 960), (0, 0), "natsuki/2bl.webp", (0, 0), "natsuki/1br.webp", (0, 0), "natsuki/x.webp")
image natsuki 3by = im.Composite((960, 960), (0, 0), "natsuki/2bl.webp", (0, 0), "natsuki/1br.webp", (0, 0), "natsuki/y.webp")
image natsuki 3bz = im.Composite((960, 960), (0, 0), "natsuki/2bl.webp", (0, 0), "natsuki/1br.webp", (0, 0), "natsuki/z.webp")

image natsuki 4ba = im.Composite((960, 960), (0, 0), "natsuki/2bl.webp", (0, 0), "natsuki/2br.webp", (0, 0), "natsuki/a.webp")
image natsuki 4bb = im.Composite((960, 960), (0, 0), "natsuki/2bl.webp", (0, 0), "natsuki/2br.webp", (0, 0), "natsuki/b.webp")
image natsuki 4bc = im.Composite((960, 960), (0, 0), "natsuki/2bl.webp", (0, 0), "natsuki/2br.webp", (0, 0), "natsuki/c.webp")
image natsuki 4bd = im.Composite((960, 960), (0, 0), "natsuki/2bl.webp", (0, 0), "natsuki/2br.webp", (0, 0), "natsuki/d.webp")
image natsuki 4be = im.Composite((960, 960), (0, 0), "natsuki/2bl.webp", (0, 0), "natsuki/2br.webp", (0, 0), "natsuki/e.webp")
image natsuki 4bf = im.Composite((960, 960), (0, 0), "natsuki/2bl.webp", (0, 0), "natsuki/2br.webp", (0, 0), "natsuki/f.webp")
image natsuki 4bg = im.Composite((960, 960), (0, 0), "natsuki/2bl.webp", (0, 0), "natsuki/2br.webp", (0, 0), "natsuki/g.webp")
image natsuki 4bh = im.Composite((960, 960), (0, 0), "natsuki/2bl.webp", (0, 0), "natsuki/2br.webp", (0, 0), "natsuki/h.webp")
image natsuki 4bi = im.Composite((960, 960), (0, 0), "natsuki/2bl.webp", (0, 0), "natsuki/2br.webp", (0, 0), "natsuki/i.webp")
image natsuki 4bj = im.Composite((960, 960), (0, 0), "natsuki/2bl.webp", (0, 0), "natsuki/2br.webp", (0, 0), "natsuki/j.webp")
image natsuki 4bk = im.Composite((960, 960), (0, 0), "natsuki/2bl.webp", (0, 0), "natsuki/2br.webp", (0, 0), "natsuki/k.webp")
image natsuki 4bl = im.Composite((960, 960), (0, 0), "natsuki/2bl.webp", (0, 0), "natsuki/2br.webp", (0, 0), "natsuki/l.webp")
image natsuki 4bm = im.Composite((960, 960), (0, 0), "natsuki/2bl.webp", (0, 0), "natsuki/2br.webp", (0, 0), "natsuki/m.webp")
image natsuki 4bn = im.Composite((960, 960), (0, 0), "natsuki/2bl.webp", (0, 0), "natsuki/2br.webp", (0, 0), "natsuki/n.webp")
image natsuki 4bo = im.Composite((960, 960), (0, 0), "natsuki/2bl.webp", (0, 0), "natsuki/2br.webp", (0, 0), "natsuki/o.webp")
image natsuki 4bp = im.Composite((960, 960), (0, 0), "natsuki/2bl.webp", (0, 0), "natsuki/2br.webp", (0, 0), "natsuki/p.webp")
image natsuki 4bq = im.Composite((960, 960), (0, 0), "natsuki/2bl.webp", (0, 0), "natsuki/2br.webp", (0, 0), "natsuki/q.webp")
image natsuki 4br = im.Composite((960, 960), (0, 0), "natsuki/2bl.webp", (0, 0), "natsuki/2br.webp", (0, 0), "natsuki/r.webp")
image natsuki 4bs = im.Composite((960, 960), (0, 0), "natsuki/2bl.webp", (0, 0), "natsuki/2br.webp", (0, 0), "natsuki/s.webp")
image natsuki 4bt = im.Composite((960, 960), (0, 0), "natsuki/2bl.webp", (0, 0), "natsuki/2br.webp", (0, 0), "natsuki/t.webp")
image natsuki 4bu = im.Composite((960, 960), (0, 0), "natsuki/2bl.webp", (0, 0), "natsuki/2br.webp", (0, 0), "natsuki/u.webp")
image natsuki 4bv = im.Composite((960, 960), (0, 0), "natsuki/2bl.webp", (0, 0), "natsuki/2br.webp", (0, 0), "natsuki/v.webp")
image natsuki 4bw = im.Composite((960, 960), (0, 0), "natsuki/2bl.webp", (0, 0), "natsuki/2br.webp", (0, 0), "natsuki/w.webp")
image natsuki 4bx = im.Composite((960, 960), (0, 0), "natsuki/2bl.webp", (0, 0), "natsuki/2br.webp", (0, 0), "natsuki/x.webp")
image natsuki 4by = im.Composite((960, 960), (0, 0), "natsuki/2bl.webp", (0, 0), "natsuki/2br.webp", (0, 0), "natsuki/y.webp")
image natsuki 4bz = im.Composite((960, 960), (0, 0), "natsuki/2bl.webp", (0, 0), "natsuki/2br.webp", (0, 0), "natsuki/z.webp")

image natsuki 12ba = im.Composite((960, 960), (0, 0), "natsuki/1bl.webp", (0, 0), "natsuki/1br.webp", (0, 0), "natsuki/2bta.webp")
image natsuki 12bb = im.Composite((960, 960), (0, 0), "natsuki/1bl.webp", (0, 0), "natsuki/1br.webp", (0, 0), "natsuki/2btb.webp")
image natsuki 12bc = im.Composite((960, 960), (0, 0), "natsuki/1bl.webp", (0, 0), "natsuki/1br.webp", (0, 0), "natsuki/2btc.webp")
image natsuki 12bd = im.Composite((960, 960), (0, 0), "natsuki/1bl.webp", (0, 0), "natsuki/1br.webp", (0, 0), "natsuki/2btd.webp")
image natsuki 12be = im.Composite((960, 960), (0, 0), "natsuki/1bl.webp", (0, 0), "natsuki/1br.webp", (0, 0), "natsuki/2bte.webp")
image natsuki 12bf = im.Composite((960, 960), (0, 0), "natsuki/1bl.webp", (0, 0), "natsuki/1br.webp", (0, 0), "natsuki/2btf.webp")
image natsuki 12bg = im.Composite((960, 960), (0, 0), "natsuki/1bl.webp", (0, 0), "natsuki/1br.webp", (0, 0), "natsuki/2btg.webp")
image natsuki 12bh = im.Composite((960, 960), (0, 0), "natsuki/1bl.webp", (0, 0), "natsuki/1br.webp", (0, 0), "natsuki/2bth.webp")
image natsuki 12bi = im.Composite((960, 960), (0, 0), "natsuki/1bl.webp", (0, 0), "natsuki/1br.webp", (0, 0), "natsuki/2bti.webp")

image natsuki 42ba = im.Composite((960, 960), (0, 0), "natsuki/2bl.webp", (0, 0), "natsuki/2br.webp", (0, 0), "natsuki/2bta.webp")
image natsuki 42bb = im.Composite((960, 960), (0, 0), "natsuki/2bl.webp", (0, 0), "natsuki/2br.webp", (0, 0), "natsuki/2btb.webp")
image natsuki 42bc = im.Composite((960, 960), (0, 0), "natsuki/2bl.webp", (0, 0), "natsuki/2br.webp", (0, 0), "natsuki/2btc.webp")
image natsuki 42bd = im.Composite((960, 960), (0, 0), "natsuki/2bl.webp", (0, 0), "natsuki/2br.webp", (0, 0), "natsuki/2btd.webp")
image natsuki 42be = im.Composite((960, 960), (0, 0), "natsuki/2bl.webp", (0, 0), "natsuki/2br.webp", (0, 0), "natsuki/2bte.webp")
image natsuki 42bf = im.Composite((960, 960), (0, 0), "natsuki/2bl.webp", (0, 0), "natsuki/2br.webp", (0, 0), "natsuki/2btf.webp")
image natsuki 42bg = im.Composite((960, 960), (0, 0), "natsuki/2bl.webp", (0, 0), "natsuki/2br.webp", (0, 0), "natsuki/2btg.webp")
image natsuki 42bh = im.Composite((960, 960), (0, 0), "natsuki/2bl.webp", (0, 0), "natsuki/2br.webp", (0, 0), "natsuki/2bth.webp")
image natsuki 42bi = im.Composite((960, 960), (0, 0), "natsuki/2bl.webp", (0, 0), "natsuki/2br.webp", (0, 0), "natsuki/2bti.webp")

image natsuki 5ba = im.Composite((960, 960), (18, 22), "natsuki/a.webp", (0, 0), "natsuki/3b.webp")
image natsuki 5bb = im.Composite((960, 960), (18, 22), "natsuki/b.webp", (0, 0), "natsuki/3b.webp")
image natsuki 5bc = im.Composite((960, 960), (18, 22), "natsuki/c.webp", (0, 0), "natsuki/3b.webp")
image natsuki 5bd = im.Composite((960, 960), (18, 22), "natsuki/d.webp", (0, 0), "natsuki/3b.webp")
image natsuki 5be = im.Composite((960, 960), (18, 22), "natsuki/e.webp", (0, 0), "natsuki/3b.webp")
image natsuki 5bf = im.Composite((960, 960), (18, 22), "natsuki/f.webp", (0, 0), "natsuki/3b.webp")
image natsuki 5bg = im.Composite((960, 960), (18, 22), "natsuki/g.webp", (0, 0), "natsuki/3b.webp")
image natsuki 5bh = im.Composite((960, 960), (18, 22), "natsuki/h.webp", (0, 0), "natsuki/3b.webp")
image natsuki 5bi = im.Composite((960, 960), (18, 22), "natsuki/i.webp", (0, 0), "natsuki/3b.webp")
image natsuki 5bj = im.Composite((960, 960), (18, 22), "natsuki/j.webp", (0, 0), "natsuki/3b.webp")
image natsuki 5bk = im.Composite((960, 960), (18, 22), "natsuki/k.webp", (0, 0), "natsuki/3b.webp")
image natsuki 5bl = im.Composite((960, 960), (18, 22), "natsuki/l.webp", (0, 0), "natsuki/3b.webp")
image natsuki 5bm = im.Composite((960, 960), (18, 22), "natsuki/m.webp", (0, 0), "natsuki/3b.webp")
image natsuki 5bn = im.Composite((960, 960), (18, 22), "natsuki/n.webp", (0, 0), "natsuki/3b.webp")
image natsuki 5bo = im.Composite((960, 960), (18, 22), "natsuki/o.webp", (0, 0), "natsuki/3b.webp")
image natsuki 5bp = im.Composite((960, 960), (18, 22), "natsuki/p.webp", (0, 0), "natsuki/3b.webp")
image natsuki 5bq = im.Composite((960, 960), (18, 22), "natsuki/q.webp", (0, 0), "natsuki/3b.webp")
image natsuki 5br = im.Composite((960, 960), (18, 22), "natsuki/r.webp", (0, 0), "natsuki/3b.webp")
image natsuki 5bs = im.Composite((960, 960), (18, 22), "natsuki/s.webp", (0, 0), "natsuki/3b.webp")
image natsuki 5bt = im.Composite((960, 960), (18, 22), "natsuki/t.webp", (0, 0), "natsuki/3b.webp")
image natsuki 5bu = im.Composite((960, 960), (18, 22), "natsuki/u.webp", (0, 0), "natsuki/3b.webp")
image natsuki 5bv = im.Composite((960, 960), (18, 22), "natsuki/v.webp", (0, 0), "natsuki/3b.webp")
image natsuki 5bw = im.Composite((960, 960), (18, 22), "natsuki/w.webp", (0, 0), "natsuki/3b.webp")
image natsuki 5bx = im.Composite((960, 960), (18, 22), "natsuki/x.webp", (0, 0), "natsuki/3b.webp")
image natsuki 5by = im.Composite((960, 960), (18, 22), "natsuki/y.webp", (0, 0), "natsuki/3b.webp")
image natsuki 5bz = im.Composite((960, 960), (18, 22), "natsuki/z.webp", (0, 0), "natsuki/3b.webp")


image natsuki 1 = im.Composite((960, 960), (0, 0), "natsuki/1l.webp", (0, 0), "natsuki/1r.webp", (0, 0), "natsuki/1t.webp")
image natsuki 2 = im.Composite((960, 960), (0, 0), "natsuki/1l.webp", (0, 0), "natsuki/2r.webp", (0, 0), "natsuki/1t.webp")
image natsuki 3 = im.Composite((960, 960), (0, 0), "natsuki/2l.webp", (0, 0), "natsuki/1r.webp", (0, 0), "natsuki/1t.webp")
image natsuki 4 = im.Composite((960, 960), (0, 0), "natsuki/2l.webp", (0, 0), "natsuki/2r.webp", (0, 0), "natsuki/1t.webp")
image natsuki 5 = im.Composite((960, 960), (18, 22), "natsuki/1t.webp", (0, 0), "natsuki/3.webp")

image natsuki mouth = LiveComposite((960, 960), (0, 0), "natsuki/0.webp", (390, 340), "n_rects_mouth", (480, 334), "n_rects_mouth")

image n_rects_mouth:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    size (20, 25)

image n_moving_mouth:
    "images/natsuki/mouth.webp"
    pos (615, 305)
    xanchor 0.5 yanchor 0.5
    parallel:
        choice:
            ease 0.10 yzoom 0.2
        choice:
            ease 0.05 yzoom 0.2
        choice:
            ease 0.075 yzoom 0.2
        pass
        choice:
            0.02
        choice:
            0.04
        choice:
            0.06
        choice:
            0.08
        pass
        choice:
            ease 0.10 yzoom 1
        choice:
            ease 0.05 yzoom 1
        choice:
            ease 0.075 yzoom 1
        pass
        choice:
            0.02
        choice:
            0.04
        choice:
            0.06
        choice:
            0.08
        repeat
    parallel:
        choice:
            0.2
        choice:
            0.4
        choice:
            0.6
        ease 0.2 xzoom 0.4
        ease 0.2 xzoom 0.8
        repeat

image natsuki_ghost_blood:
    "#00000000"
    "natsuki/ghost_blood.webp" with ImageDissolve("images/menu/wipedown.webp", 80.0, ramplen=4, alpha=True)
    pos (620,320) zoom 0.80

image natsuki ghost_base:
    "natsuki/ghost1.webp"
image natsuki ghost1:
    "natsuki 11"
    "natsuki ghost_base" with Dissolve(20.0, alpha=True)
image natsuki ghost2 = Image("natsuki/ghost2.webp")
image natsuki ghost3 = Image("natsuki/ghost3.webp")
image natsuki ghost4:
    "natsuki ghost3"
    parallel:
        easeout 0.25 zoom 4.5 yoffset 1200
    parallel:
        ease 0.025 xoffset -20
        ease 0.025 xoffset 20
        repeat
    0.25
    "black"
image natsuki glitch1:
    "natsuki/glitch1.webp"
    zoom 1.25
    block:
        yoffset 300 xoffset 100 ytile 2
        linear 0.15 yoffset 200
        repeat
    time 0.75
    yoffset 0 zoom 1 xoffset 0 ytile 1
    "natsuki 4e"

image natsuki scream = im.Composite((960, 960), (0, 0), "natsuki/1l.webp", (0, 0), "natsuki/1r.webp", (0, 0), "natsuki/scream.webp")
image natsuki vomit = "natsuki/vomit.webp"

image n_blackeyes = "images/natsuki/blackeyes.webp"
image n_eye = "images/natsuki/eye.webp"


image yuri 1 = im.Composite((960, 960), (0, 0), "yuri/1l.webp", (0, 0), "yuri/1r.webp", (0, 0), "yuri/a.webp")
image yuri 2 = im.Composite((960, 960), (0, 0), "yuri/1l.webp", (0, 0), "yuri/2r.webp", (0, 0), "yuri/a.webp")
image yuri 3 = im.Composite((960, 960), (0, 0), "yuri/2l.webp", (0, 0), "yuri/2r.webp", (0, 0), "yuri/a.webp")
image yuri 4 = im.Composite((960, 960), (0, 0), "yuri/3.webp", (0, 0), "yuri/a2.webp")

image yuri 1a = im.Composite((960, 960), (0, 0), "yuri/1l.webp", (0, 0), "yuri/1r.webp", (0, 0), "yuri/a.webp")
image yuri 1b = im.Composite((960, 960), (0, 0), "yuri/1l.webp", (0, 0), "yuri/1r.webp", (0, 0), "yuri/b.webp")
image yuri 1c = im.Composite((960, 960), (0, 0), "yuri/1l.webp", (0, 0), "yuri/1r.webp", (0, 0), "yuri/c.webp")
image yuri 1d = im.Composite((960, 960), (0, 0), "yuri/1l.webp", (0, 0), "yuri/1r.webp", (0, 0), "yuri/d.webp")
image yuri 1e = im.Composite((960, 960), (0, 0), "yuri/1l.webp", (0, 0), "yuri/1r.webp", (0, 0), "yuri/e.webp")
image yuri 1f = im.Composite((960, 960), (0, 0), "yuri/1l.webp", (0, 0), "yuri/1r.webp", (0, 0), "yuri/f.webp")
image yuri 1g = im.Composite((960, 960), (0, 0), "yuri/1l.webp", (0, 0), "yuri/1r.webp", (0, 0), "yuri/g.webp")
image yuri 1h = im.Composite((960, 960), (0, 0), "yuri/1l.webp", (0, 0), "yuri/1r.webp", (0, 0), "yuri/h.webp")
image yuri 1i = im.Composite((960, 960), (0, 0), "yuri/1l.webp", (0, 0), "yuri/1r.webp", (0, 0), "yuri/i.webp")
image yuri 1j = im.Composite((960, 960), (0, 0), "yuri/1l.webp", (0, 0), "yuri/1r.webp", (0, 0), "yuri/j.webp")
image yuri 1k = im.Composite((960, 960), (0, 0), "yuri/1l.webp", (0, 0), "yuri/1r.webp", (0, 0), "yuri/k.webp")
image yuri 1l = im.Composite((960, 960), (0, 0), "yuri/1l.webp", (0, 0), "yuri/1r.webp", (0, 0), "yuri/l.webp")
image yuri 1m = im.Composite((960, 960), (0, 0), "yuri/1l.webp", (0, 0), "yuri/1r.webp", (0, 0), "yuri/m.webp")
image yuri 1n = im.Composite((960, 960), (0, 0), "yuri/1l.webp", (0, 0), "yuri/1r.webp", (0, 0), "yuri/n.webp")
image yuri 1o = im.Composite((960, 960), (0, 0), "yuri/1l.webp", (0, 0), "yuri/1r.webp", (0, 0), "yuri/o.webp")
image yuri 1p = im.Composite((960, 960), (0, 0), "yuri/1l.webp", (0, 0), "yuri/1r.webp", (0, 0), "yuri/p.webp")
image yuri 1q = im.Composite((960, 960), (0, 0), "yuri/1l.webp", (0, 0), "yuri/1r.webp", (0, 0), "yuri/q.webp")
image yuri 1r = im.Composite((960, 960), (0, 0), "yuri/1l.webp", (0, 0), "yuri/1r.webp", (0, 0), "yuri/r.webp")
image yuri 1s = im.Composite((960, 960), (0, 0), "yuri/1l.webp", (0, 0), "yuri/1r.webp", (0, 0), "yuri/s.webp")
image yuri 1t = im.Composite((960, 960), (0, 0), "yuri/1l.webp", (0, 0), "yuri/1r.webp", (0, 0), "yuri/t.webp")
image yuri 1u = im.Composite((960, 960), (0, 0), "yuri/1l.webp", (0, 0), "yuri/1r.webp", (0, 0), "yuri/u.webp")
image yuri 1v = im.Composite((960, 960), (0, 0), "yuri/1l.webp", (0, 0), "yuri/1r.webp", (0, 0), "yuri/v.webp")
image yuri 1w = im.Composite((960, 960), (0, 0), "yuri/1l.webp", (0, 0), "yuri/1r.webp", (0, 0), "yuri/w.webp")

image yuri 1y1 = im.Composite((960, 960), (0, 0), "yuri/1l.webp", (0, 0), "yuri/1r.webp", (0, 0), "yuri/y1.webp")
image yuri 1y2 = im.Composite((960, 960), (0, 0), "yuri/1l.webp", (0, 0), "yuri/1r.webp", (0, 0), "yuri/y2.webp")
image yuri 1y3 = im.Composite((960, 960), (0, 0), "yuri/1l.webp", (0, 0), "yuri/1r.webp", (0, 0), "yuri/y3.webp")
image yuri 1y4 = im.Composite((960, 960), (0, 0), "yuri/1l.webp", (0, 0), "yuri/1r.webp", (0, 0), "yuri/y4.webp")
image yuri 1y5 = im.Composite((960, 960), (0, 0), "yuri/1l.webp", (0, 0), "yuri/1r.webp", (0, 0), "yuri/y5.webp")
image yuri 1y6 = im.Composite((960, 960), (0, 0), "yuri/1l.webp", (0, 0), "yuri/1r.webp", (0, 0), "yuri/y6.webp")
image yuri 1y7 = im.Composite((960, 960), (0, 0), "yuri/1l.webp", (0, 0), "yuri/1r.webp", (0, 0), "yuri/y7.webp")

image yuri 2a = im.Composite((960, 960), (0, 0), "yuri/1l.webp", (0, 0), "yuri/2r.webp", (0, 0), "yuri/a.webp")
image yuri 2b = im.Composite((960, 960), (0, 0), "yuri/1l.webp", (0, 0), "yuri/2r.webp", (0, 0), "yuri/b.webp")
image yuri 2c = im.Composite((960, 960), (0, 0), "yuri/1l.webp", (0, 0), "yuri/2r.webp", (0, 0), "yuri/c.webp")
image yuri 2d = im.Composite((960, 960), (0, 0), "yuri/1l.webp", (0, 0), "yuri/2r.webp", (0, 0), "yuri/d.webp")
image yuri 2e = im.Composite((960, 960), (0, 0), "yuri/1l.webp", (0, 0), "yuri/2r.webp", (0, 0), "yuri/e.webp")
image yuri 2f = im.Composite((960, 960), (0, 0), "yuri/1l.webp", (0, 0), "yuri/2r.webp", (0, 0), "yuri/f.webp")
image yuri 2g = im.Composite((960, 960), (0, 0), "yuri/1l.webp", (0, 0), "yuri/2r.webp", (0, 0), "yuri/g.webp")
image yuri 2h = im.Composite((960, 960), (0, 0), "yuri/1l.webp", (0, 0), "yuri/2r.webp", (0, 0), "yuri/h.webp")
image yuri 2i = im.Composite((960, 960), (0, 0), "yuri/1l.webp", (0, 0), "yuri/2r.webp", (0, 0), "yuri/i.webp")
image yuri 2j = im.Composite((960, 960), (0, 0), "yuri/1l.webp", (0, 0), "yuri/2r.webp", (0, 0), "yuri/j.webp")
image yuri 2k = im.Composite((960, 960), (0, 0), "yuri/1l.webp", (0, 0), "yuri/2r.webp", (0, 0), "yuri/k.webp")
image yuri 2l = im.Composite((960, 960), (0, 0), "yuri/1l.webp", (0, 0), "yuri/2r.webp", (0, 0), "yuri/l.webp")
image yuri 2m = im.Composite((960, 960), (0, 0), "yuri/1l.webp", (0, 0), "yuri/2r.webp", (0, 0), "yuri/m.webp")
image yuri 2n = im.Composite((960, 960), (0, 0), "yuri/1l.webp", (0, 0), "yuri/2r.webp", (0, 0), "yuri/n.webp")
image yuri 2o = im.Composite((960, 960), (0, 0), "yuri/1l.webp", (0, 0), "yuri/2r.webp", (0, 0), "yuri/o.webp")
image yuri 2p = im.Composite((960, 960), (0, 0), "yuri/1l.webp", (0, 0), "yuri/2r.webp", (0, 0), "yuri/p.webp")
image yuri 2q = im.Composite((960, 960), (0, 0), "yuri/1l.webp", (0, 0), "yuri/2r.webp", (0, 0), "yuri/q.webp")
image yuri 2r = im.Composite((960, 960), (0, 0), "yuri/1l.webp", (0, 0), "yuri/2r.webp", (0, 0), "yuri/r.webp")
image yuri 2s = im.Composite((960, 960), (0, 0), "yuri/1l.webp", (0, 0), "yuri/2r.webp", (0, 0), "yuri/s.webp")
image yuri 2t = im.Composite((960, 960), (0, 0), "yuri/1l.webp", (0, 0), "yuri/2r.webp", (0, 0), "yuri/t.webp")
image yuri 2u = im.Composite((960, 960), (0, 0), "yuri/1l.webp", (0, 0), "yuri/2r.webp", (0, 0), "yuri/u.webp")
image yuri 2v = im.Composite((960, 960), (0, 0), "yuri/1l.webp", (0, 0), "yuri/2r.webp", (0, 0), "yuri/v.webp")
image yuri 2w = im.Composite((960, 960), (0, 0), "yuri/1l.webp", (0, 0), "yuri/2r.webp", (0, 0), "yuri/w.webp")

image yuri 2y1 = im.Composite((960, 960), (0, 0), "yuri/1l.webp", (0, 0), "yuri/2r.webp", (0, 0), "yuri/y1.webp")
image yuri 2y2 = im.Composite((960, 960), (0, 0), "yuri/1l.webp", (0, 0), "yuri/2r.webp", (0, 0), "yuri/y2.webp")
image yuri 2y3 = im.Composite((960, 960), (0, 0), "yuri/1l.webp", (0, 0), "yuri/2r.webp", (0, 0), "yuri/y3.webp")
image yuri 2y4 = im.Composite((960, 960), (0, 0), "yuri/1l.webp", (0, 0), "yuri/2r.webp", (0, 0), "yuri/y4.webp")
image yuri 2y5 = im.Composite((960, 960), (0, 0), "yuri/1l.webp", (0, 0), "yuri/2r.webp", (0, 0), "yuri/y5.webp")
image yuri 2y6 = im.Composite((960, 960), (0, 0), "yuri/1l.webp", (0, 0), "yuri/2r.webp", (0, 0), "yuri/y6.webp")
image yuri 2y7 = im.Composite((960, 960), (0, 0), "yuri/1l.webp", (0, 0), "yuri/2r.webp", (0, 0), "yuri/y7.webp")

image yuri 3a = im.Composite((960, 960), (0, 0), "yuri/2l.webp", (0, 0), "yuri/2r.webp", (0, 0), "yuri/a.webp")
image yuri 3b = im.Composite((960, 960), (0, 0), "yuri/2l.webp", (0, 0), "yuri/2r.webp", (0, 0), "yuri/b.webp")
image yuri 3c = im.Composite((960, 960), (0, 0), "yuri/2l.webp", (0, 0), "yuri/2r.webp", (0, 0), "yuri/c.webp")
image yuri 3d = im.Composite((960, 960), (0, 0), "yuri/2l.webp", (0, 0), "yuri/2r.webp", (0, 0), "yuri/d.webp")
image yuri 3e = im.Composite((960, 960), (0, 0), "yuri/2l.webp", (0, 0), "yuri/2r.webp", (0, 0), "yuri/e.webp")
image yuri 3f = im.Composite((960, 960), (0, 0), "yuri/2l.webp", (0, 0), "yuri/2r.webp", (0, 0), "yuri/f.webp")
image yuri 3g = im.Composite((960, 960), (0, 0), "yuri/2l.webp", (0, 0), "yuri/2r.webp", (0, 0), "yuri/g.webp")
image yuri 3h = im.Composite((960, 960), (0, 0), "yuri/2l.webp", (0, 0), "yuri/2r.webp", (0, 0), "yuri/h.webp")
image yuri 3i = im.Composite((960, 960), (0, 0), "yuri/2l.webp", (0, 0), "yuri/2r.webp", (0, 0), "yuri/i.webp")
image yuri 3j = im.Composite((960, 960), (0, 0), "yuri/2l.webp", (0, 0), "yuri/2r.webp", (0, 0), "yuri/j.webp")
image yuri 3k = im.Composite((960, 960), (0, 0), "yuri/2l.webp", (0, 0), "yuri/2r.webp", (0, 0), "yuri/k.webp")
image yuri 3l = im.Composite((960, 960), (0, 0), "yuri/2l.webp", (0, 0), "yuri/2r.webp", (0, 0), "yuri/l.webp")
image yuri 3m = im.Composite((960, 960), (0, 0), "yuri/2l.webp", (0, 0), "yuri/2r.webp", (0, 0), "yuri/m.webp")
image yuri 3n = im.Composite((960, 960), (0, 0), "yuri/2l.webp", (0, 0), "yuri/2r.webp", (0, 0), "yuri/n.webp")
image yuri 3o = im.Composite((960, 960), (0, 0), "yuri/2l.webp", (0, 0), "yuri/2r.webp", (0, 0), "yuri/o.webp")
image yuri 3p = im.Composite((960, 960), (0, 0), "yuri/2l.webp", (0, 0), "yuri/2r.webp", (0, 0), "yuri/p.webp")
image yuri 3q = im.Composite((960, 960), (0, 0), "yuri/2l.webp", (0, 0), "yuri/2r.webp", (0, 0), "yuri/q.webp")
image yuri 3r = im.Composite((960, 960), (0, 0), "yuri/2l.webp", (0, 0), "yuri/2r.webp", (0, 0), "yuri/r.webp")
image yuri 3s = im.Composite((960, 960), (0, 0), "yuri/2l.webp", (0, 0), "yuri/2r.webp", (0, 0), "yuri/s.webp")
image yuri 3t = im.Composite((960, 960), (0, 0), "yuri/2l.webp", (0, 0), "yuri/2r.webp", (0, 0), "yuri/t.webp")
image yuri 3u = im.Composite((960, 960), (0, 0), "yuri/2l.webp", (0, 0), "yuri/2r.webp", (0, 0), "yuri/u.webp")
image yuri 3v = im.Composite((960, 960), (0, 0), "yuri/2l.webp", (0, 0), "yuri/2r.webp", (0, 0), "yuri/v.webp")
image yuri 3w = im.Composite((960, 960), (0, 0), "yuri/2l.webp", (0, 0), "yuri/2r.webp", (0, 0), "yuri/w.webp")

image yuri 3y1 = im.Composite((960, 960), (0, 0), "yuri/2l.webp", (0, 0), "yuri/2r.webp", (0, 0), "yuri/y1.webp")
image yuri 3y2 = im.Composite((960, 960), (0, 0), "yuri/2l.webp", (0, 0), "yuri/2r.webp", (0, 0), "yuri/y2.webp")
image yuri 3y3 = im.Composite((960, 960), (0, 0), "yuri/2l.webp", (0, 0), "yuri/2r.webp", (0, 0), "yuri/y3.webp")
image yuri 3y4 = im.Composite((960, 960), (0, 0), "yuri/2l.webp", (0, 0), "yuri/2r.webp", (0, 0), "yuri/y4.webp")
image yuri 3y5 = im.Composite((960, 960), (0, 0), "yuri/2l.webp", (0, 0), "yuri/2r.webp", (0, 0), "yuri/y5.webp")
image yuri 3y6 = im.Composite((960, 960), (0, 0), "yuri/2l.webp", (0, 0), "yuri/2r.webp", (0, 0), "yuri/y6.webp")
image yuri 3y7 = im.Composite((960, 960), (0, 0), "yuri/2l.webp", (0, 0), "yuri/2r.webp", (0, 0), "yuri/y7.webp")

image yuri 4a = im.Composite((960, 960), (0, 0), "yuri/3.webp", (0, 0), "yuri/a2.webp")
image yuri 4b = im.Composite((960, 960), (0, 0), "yuri/3.webp", (0, 0), "yuri/b2.webp")
image yuri 4c = im.Composite((960, 960), (0, 0), "yuri/3.webp", (0, 0), "yuri/c2.webp")
image yuri 4d = im.Composite((960, 960), (0, 0), "yuri/3.webp", (0, 0), "yuri/d2.webp")
image yuri 4e = im.Composite((960, 960), (0, 0), "yuri/3.webp", (0, 0), "yuri/e2.webp")

image yuri 1ba = im.Composite((960, 960), (0, 0), "yuri/a.webp", (0, 0), "yuri/1bl.webp", (0, 0), "yuri/1br.webp")
image yuri 1bb = im.Composite((960, 960), (0, 0), "yuri/b.webp", (0, 0), "yuri/1bl.webp", (0, 0), "yuri/1br.webp")
image yuri 1bc = im.Composite((960, 960), (0, 0), "yuri/c.webp", (0, 0), "yuri/1bl.webp", (0, 0), "yuri/1br.webp")
image yuri 1bd = im.Composite((960, 960), (0, 0), "yuri/d.webp", (0, 0), "yuri/1bl.webp", (0, 0), "yuri/1br.webp")
image yuri 1be = im.Composite((960, 960), (0, 0), "yuri/e.webp", (0, 0), "yuri/1bl.webp", (0, 0), "yuri/1br.webp")
image yuri 1bf = im.Composite((960, 960), (0, 0), "yuri/f.webp", (0, 0), "yuri/1bl.webp", (0, 0), "yuri/1br.webp")
image yuri 1bg = im.Composite((960, 960), (0, 0), "yuri/g.webp", (0, 0), "yuri/1bl.webp", (0, 0), "yuri/1br.webp")
image yuri 1bh = im.Composite((960, 960), (0, 0), "yuri/h.webp", (0, 0), "yuri/1bl.webp", (0, 0), "yuri/1br.webp")
image yuri 1bi = im.Composite((960, 960), (0, 0), "yuri/i.webp", (0, 0), "yuri/1bl.webp", (0, 0), "yuri/1br.webp")
image yuri 1bj = im.Composite((960, 960), (0, 0), "yuri/j.webp", (0, 0), "yuri/1bl.webp", (0, 0), "yuri/1br.webp")
image yuri 1bk = im.Composite((960, 960), (0, 0), "yuri/k.webp", (0, 0), "yuri/1bl.webp", (0, 0), "yuri/1br.webp")
image yuri 1bl = im.Composite((960, 960), (0, 0), "yuri/l.webp", (0, 0), "yuri/1bl.webp", (0, 0), "yuri/1br.webp")
image yuri 1bm = im.Composite((960, 960), (0, 0), "yuri/m.webp", (0, 0), "yuri/1bl.webp", (0, 0), "yuri/1br.webp")
image yuri 1bn = im.Composite((960, 960), (0, 0), "yuri/n.webp", (0, 0), "yuri/1bl.webp", (0, 0), "yuri/1br.webp")
image yuri 1bo = im.Composite((960, 960), (0, 0), "yuri/o.webp", (0, 0), "yuri/1bl.webp", (0, 0), "yuri/1br.webp")
image yuri 1bp = im.Composite((960, 960), (0, 0), "yuri/p.webp", (0, 0), "yuri/1bl.webp", (0, 0), "yuri/1br.webp")
image yuri 1bq = im.Composite((960, 960), (0, 0), "yuri/q.webp", (0, 0), "yuri/1bl.webp", (0, 0), "yuri/1br.webp")
image yuri 1br = im.Composite((960, 960), (0, 0), "yuri/r.webp", (0, 0), "yuri/1bl.webp", (0, 0), "yuri/1br.webp")
image yuri 1bs = im.Composite((960, 960), (0, 0), "yuri/s.webp", (0, 0), "yuri/1bl.webp", (0, 0), "yuri/1br.webp")
image yuri 1bt = im.Composite((960, 960), (0, 0), "yuri/t.webp", (0, 0), "yuri/1bl.webp", (0, 0), "yuri/1br.webp")
image yuri 1bu = im.Composite((960, 960), (0, 0), "yuri/u.webp", (0, 0), "yuri/1bl.webp", (0, 0), "yuri/1br.webp")
image yuri 1bv = im.Composite((960, 960), (0, 0), "yuri/v.webp", (0, 0), "yuri/1bl.webp", (0, 0), "yuri/1br.webp")
image yuri 1bw = im.Composite((960, 960), (0, 0), "yuri/w.webp", (0, 0), "yuri/1bl.webp", (0, 0), "yuri/1br.webp")

image yuri 2ba = im.Composite((960, 960), (0, 0), "yuri/a.webp", (0, 0), "yuri/1bl.webp", (0, 0), "yuri/2br.webp")
image yuri 2bb = im.Composite((960, 960), (0, 0), "yuri/b.webp", (0, 0), "yuri/1bl.webp", (0, 0), "yuri/2br.webp")
image yuri 2bc = im.Composite((960, 960), (0, 0), "yuri/c.webp", (0, 0), "yuri/1bl.webp", (0, 0), "yuri/2br.webp")
image yuri 2bd = im.Composite((960, 960), (0, 0), "yuri/d.webp", (0, 0), "yuri/1bl.webp", (0, 0), "yuri/2br.webp")
image yuri 2be = im.Composite((960, 960), (0, 0), "yuri/e.webp", (0, 0), "yuri/1bl.webp", (0, 0), "yuri/2br.webp")
image yuri 2bf = im.Composite((960, 960), (0, 0), "yuri/f.webp", (0, 0), "yuri/1bl.webp", (0, 0), "yuri/2br.webp")
image yuri 2bg = im.Composite((960, 960), (0, 0), "yuri/g.webp", (0, 0), "yuri/1bl.webp", (0, 0), "yuri/2br.webp")
image yuri 2bh = im.Composite((960, 960), (0, 0), "yuri/h.webp", (0, 0), "yuri/1bl.webp", (0, 0), "yuri/2br.webp")
image yuri 2bi = im.Composite((960, 960), (0, 0), "yuri/i.webp", (0, 0), "yuri/1bl.webp", (0, 0), "yuri/2br.webp")
image yuri 2bj = im.Composite((960, 960), (0, 0), "yuri/j.webp", (0, 0), "yuri/1bl.webp", (0, 0), "yuri/2br.webp")
image yuri 2bk = im.Composite((960, 960), (0, 0), "yuri/k.webp", (0, 0), "yuri/1bl.webp", (0, 0), "yuri/2br.webp")
image yuri 2bl = im.Composite((960, 960), (0, 0), "yuri/l.webp", (0, 0), "yuri/1bl.webp", (0, 0), "yuri/2br.webp")
image yuri 2bm = im.Composite((960, 960), (0, 0), "yuri/m.webp", (0, 0), "yuri/1bl.webp", (0, 0), "yuri/2br.webp")
image yuri 2bn = im.Composite((960, 960), (0, 0), "yuri/n.webp", (0, 0), "yuri/1bl.webp", (0, 0), "yuri/2br.webp")
image yuri 2bo = im.Composite((960, 960), (0, 0), "yuri/o.webp", (0, 0), "yuri/1bl.webp", (0, 0), "yuri/2br.webp")
image yuri 2bp = im.Composite((960, 960), (0, 0), "yuri/p.webp", (0, 0), "yuri/1bl.webp", (0, 0), "yuri/2br.webp")
image yuri 2bq = im.Composite((960, 960), (0, 0), "yuri/q.webp", (0, 0), "yuri/1bl.webp", (0, 0), "yuri/2br.webp")
image yuri 2br = im.Composite((960, 960), (0, 0), "yuri/r.webp", (0, 0), "yuri/1bl.webp", (0, 0), "yuri/2br.webp")
image yuri 2bs = im.Composite((960, 960), (0, 0), "yuri/s.webp", (0, 0), "yuri/1bl.webp", (0, 0), "yuri/2br.webp")
image yuri 2bt = im.Composite((960, 960), (0, 0), "yuri/t.webp", (0, 0), "yuri/1bl.webp", (0, 0), "yuri/2br.webp")
image yuri 2bu = im.Composite((960, 960), (0, 0), "yuri/u.webp", (0, 0), "yuri/1bl.webp", (0, 0), "yuri/2br.webp")
image yuri 2bv = im.Composite((960, 960), (0, 0), "yuri/v.webp", (0, 0), "yuri/1bl.webp", (0, 0), "yuri/2br.webp")
image yuri 2bw = im.Composite((960, 960), (0, 0), "yuri/w.webp", (0, 0), "yuri/1bl.webp", (0, 0), "yuri/2br.webp")

image yuri 3ba = im.Composite((960, 960), (0, 0), "yuri/a.webp", (0, 0), "yuri/2bl.webp", (0, 0), "yuri/2br.webp")
image yuri 3bb = im.Composite((960, 960), (0, 0), "yuri/b.webp", (0, 0), "yuri/2bl.webp", (0, 0), "yuri/2br.webp")
image yuri 3bc = im.Composite((960, 960), (0, 0), "yuri/c.webp", (0, 0), "yuri/2bl.webp", (0, 0), "yuri/2br.webp")
image yuri 3bd = im.Composite((960, 960), (0, 0), "yuri/d.webp", (0, 0), "yuri/2bl.webp", (0, 0), "yuri/2br.webp")
image yuri 3be = im.Composite((960, 960), (0, 0), "yuri/e.webp", (0, 0), "yuri/2bl.webp", (0, 0), "yuri/2br.webp")
image yuri 3bf = im.Composite((960, 960), (0, 0), "yuri/f.webp", (0, 0), "yuri/2bl.webp", (0, 0), "yuri/2br.webp")
image yuri 3bg = im.Composite((960, 960), (0, 0), "yuri/g.webp", (0, 0), "yuri/2bl.webp", (0, 0), "yuri/2br.webp")
image yuri 3bh = im.Composite((960, 960), (0, 0), "yuri/h.webp", (0, 0), "yuri/2bl.webp", (0, 0), "yuri/2br.webp")
image yuri 3bi = im.Composite((960, 960), (0, 0), "yuri/i.webp", (0, 0), "yuri/2bl.webp", (0, 0), "yuri/2br.webp")
image yuri 3bj = im.Composite((960, 960), (0, 0), "yuri/j.webp", (0, 0), "yuri/2bl.webp", (0, 0), "yuri/2br.webp")
image yuri 3bk = im.Composite((960, 960), (0, 0), "yuri/k.webp", (0, 0), "yuri/2bl.webp", (0, 0), "yuri/2br.webp")
image yuri 3bl = im.Composite((960, 960), (0, 0), "yuri/l.webp", (0, 0), "yuri/2bl.webp", (0, 0), "yuri/2br.webp")
image yuri 3bm = im.Composite((960, 960), (0, 0), "yuri/m.webp", (0, 0), "yuri/2bl.webp", (0, 0), "yuri/2br.webp")
image yuri 3bn = im.Composite((960, 960), (0, 0), "yuri/n.webp", (0, 0), "yuri/2bl.webp", (0, 0), "yuri/2br.webp")
image yuri 3bo = im.Composite((960, 960), (0, 0), "yuri/o.webp", (0, 0), "yuri/2bl.webp", (0, 0), "yuri/2br.webp")
image yuri 3bp = im.Composite((960, 960), (0, 0), "yuri/p.webp", (0, 0), "yuri/2bl.webp", (0, 0), "yuri/2br.webp")
image yuri 3bq = im.Composite((960, 960), (0, 0), "yuri/q.webp", (0, 0), "yuri/2bl.webp", (0, 0), "yuri/2br.webp")
image yuri 3br = im.Composite((960, 960), (0, 0), "yuri/r.webp", (0, 0), "yuri/2bl.webp", (0, 0), "yuri/2br.webp")
image yuri 3bs = im.Composite((960, 960), (0, 0), "yuri/s.webp", (0, 0), "yuri/2bl.webp", (0, 0), "yuri/2br.webp")
image yuri 3bt = im.Composite((960, 960), (0, 0), "yuri/t.webp", (0, 0), "yuri/2bl.webp", (0, 0), "yuri/2br.webp")
image yuri 3bu = im.Composite((960, 960), (0, 0), "yuri/u.webp", (0, 0), "yuri/2bl.webp", (0, 0), "yuri/2br.webp")
image yuri 3bv = im.Composite((960, 960), (0, 0), "yuri/v.webp", (0, 0), "yuri/2bl.webp", (0, 0), "yuri/2br.webp")
image yuri 3bw = im.Composite((960, 960), (0, 0), "yuri/w.webp", (0, 0), "yuri/2bl.webp", (0, 0), "yuri/2br.webp")

image yuri 4ba = im.Composite((960, 960), (0, 0), "yuri/a2.webp", (0, 0), "yuri/3b.webp")
image yuri 4bb = im.Composite((960, 960), (0, 0), "yuri/b2.webp", (0, 0), "yuri/3b.webp")
image yuri 4bc = im.Composite((960, 960), (0, 0), "yuri/c2.webp", (0, 0), "yuri/3b.webp")
image yuri 4bd = im.Composite((960, 960), (0, 0), "yuri/d2.webp", (0, 0), "yuri/3b.webp")
image yuri 4be = im.Composite((960, 960), (0, 0), "yuri/e2.webp", (0, 0), "yuri/3b.webp")

image y_glitch_head:
    "images/yuri/za.webp"
    0.15
    "images/yuri/zb.webp"
    0.15
    "images/yuri/zc.webp"
    0.15
    "images/yuri/zd.webp"
    0.15
    repeat

image yuri stab_1 = "yuri/stab/1.webp"
image yuri stab_2 = "yuri/stab/2.webp"
image yuri stab_3 = "yuri/stab/3.webp"
image yuri stab_4 = "yuri/stab/4.webp"
image yuri stab_5 = "yuri/stab/5.webp"
image yuri stab_6 = LiveComposite((960,960), (0, 0), "yuri/stab/6-mask.webp", (0, 0), "yuri stab_6_eyes", (0, 0), "yuri/stab/6.webp")

image yuri stab_6_eyes:
    "yuri/stab/6-eyes.webp"
    subpixel True
    parallel:
        choice:
            xoffset 0.5
        choice:
            xoffset 0
        choice:
            xoffset -0.5
        0.2
        repeat
    parallel:
        choice:
            yoffset 0.5
        choice:
            yoffset 0
        choice:
            yoffset -0.5
        0.2
        repeat
    parallel:
        2.05
        easeout 1.0 yoffset -15
        linear 10 yoffset -15


image yuri oneeye = LiveComposite((960, 960), (0, 0), "yuri/1l.webp", (0, 0), "yuri/1r.webp", (0, 0), "yuri/oneeye.webp", (0, 0), "yuri oneeye2")
image yuri oneeye2:
    "yuri/oneeye2.webp"
    subpixel True
    pause 5.0
    linear 60 xoffset -50 yoffset 20

image yuri glitch:
    "yuri/glitch1.webp"
    pause 0.1
    "yuri/glitch2.webp"
    pause 0.1
    "yuri/glitch3.webp"
    pause 0.1
    "yuri/glitch4.webp"
    pause 0.1
    "yuri/glitch5.webp"
    pause 0.1
    repeat
image yuri glitch2:
    "yuri/0a.webp"
    pause 0.1
    "yuri/0b.webp"
    pause 0.5
    "yuri/0a.webp"
    pause 0.3
    "yuri/0b.webp"
    pause 0.3
    "yuri 1"

image yuri eyes = LiveComposite((1280, 720), (0, 0), "yuri/eyes1.webp", (0, 0), "yuripupils")

image yuri eyes_base = "yuri/eyes1.webp"

image yuripupils:
    "yuri/eyes2.webp"
    yuripupils_move

image yuri cuts = "yuri/cuts.webp"

image yuri dragon:
    "yuri 3"
    0.25
    parallel:
        "yuri/dragon1.webp"
        0.01
        "yuri/dragon2.webp"
        0.01
        repeat
    parallel:
        0.01
        choice:
            xoffset -1
            xoffset -2
            xoffset -5
            xoffset -6
            xoffset -9
            xoffset -10
        0.01
        xoffset 0
        repeat
    time 0.55
    xoffset 0
    "yuri 3"


image monika 1 = im.Composite((960, 960), (0, 0), "monika/1l.webp", (0, 0), "monika/1r.webp", (0, 0), "monika/a.webp")
image monika 2 = im.Composite((960, 960), (0, 0), "monika/1l.webp", (0, 0), "monika/2r.webp", (0, 0), "monika/a.webp")
image monika 3 = im.Composite((960, 960), (0, 0), "monika/2l.webp", (0, 0), "monika/1r.webp", (0, 0), "monika/a.webp")
image monika 4 = im.Composite((960, 960), (0, 0), "monika/2l.webp", (0, 0), "monika/2r.webp", (0, 0), "monika/a.webp")
image monika 5 = im.Composite((960, 960), (0, 0), "monika/3a.webp")

image monika 1a = im.Composite((960, 960), (0, 0), "monika/1l.webp", (0, 0), "monika/1r.webp", (0, 0), "monika/a.webp")
image monika 1b = im.Composite((960, 960), (0, 0), "monika/1l.webp", (0, 0), "monika/1r.webp", (0, 0), "monika/b.webp")
image monika 1c = im.Composite((960, 960), (0, 0), "monika/1l.webp", (0, 0), "monika/1r.webp", (0, 0), "monika/c.webp")
image monika 1d = im.Composite((960, 960), (0, 0), "monika/1l.webp", (0, 0), "monika/1r.webp", (0, 0), "monika/d.webp")
image monika 1e = im.Composite((960, 960), (0, 0), "monika/1l.webp", (0, 0), "monika/1r.webp", (0, 0), "monika/e.webp")
image monika 1f = im.Composite((960, 960), (0, 0), "monika/1l.webp", (0, 0), "monika/1r.webp", (0, 0), "monika/f.webp")
image monika 1g = im.Composite((960, 960), (0, 0), "monika/1l.webp", (0, 0), "monika/1r.webp", (0, 0), "monika/g.webp")
image monika 1h = im.Composite((960, 960), (0, 0), "monika/1l.webp", (0, 0), "monika/1r.webp", (0, 0), "monika/h.webp")
image monika 1i = im.Composite((960, 960), (0, 0), "monika/1l.webp", (0, 0), "monika/1r.webp", (0, 0), "monika/i.webp")
image monika 1j = im.Composite((960, 960), (0, 0), "monika/1l.webp", (0, 0), "monika/1r.webp", (0, 0), "monika/j.webp")
image monika 1k = im.Composite((960, 960), (0, 0), "monika/1l.webp", (0, 0), "monika/1r.webp", (0, 0), "monika/k.webp")
image monika 1l = im.Composite((960, 960), (0, 0), "monika/1l.webp", (0, 0), "monika/1r.webp", (0, 0), "monika/l.webp")
image monika 1m = im.Composite((960, 960), (0, 0), "monika/1l.webp", (0, 0), "monika/1r.webp", (0, 0), "monika/m.webp")
image monika 1n = im.Composite((960, 960), (0, 0), "monika/1l.webp", (0, 0), "monika/1r.webp", (0, 0), "monika/n.webp")
image monika 1o = im.Composite((960, 960), (0, 0), "monika/1l.webp", (0, 0), "monika/1r.webp", (0, 0), "monika/o.webp")
image monika 1p = im.Composite((960, 960), (0, 0), "monika/1l.webp", (0, 0), "monika/1r.webp", (0, 0), "monika/p.webp")
image monika 1q = im.Composite((960, 960), (0, 0), "monika/1l.webp", (0, 0), "monika/1r.webp", (0, 0), "monika/q.webp")
image monika 1r = im.Composite((960, 960), (0, 0), "monika/1l.webp", (0, 0), "monika/1r.webp", (0, 0), "monika/r.webp")

image monika 2a = im.Composite((960, 960), (0, 0), "monika/1l.webp", (0, 0), "monika/2r.webp", (0, 0), "monika/a.webp")
image monika 2b = im.Composite((960, 960), (0, 0), "monika/1l.webp", (0, 0), "monika/2r.webp", (0, 0), "monika/b.webp")
image monika 2c = im.Composite((960, 960), (0, 0), "monika/1l.webp", (0, 0), "monika/2r.webp", (0, 0), "monika/c.webp")
image monika 2d = im.Composite((960, 960), (0, 0), "monika/1l.webp", (0, 0), "monika/2r.webp", (0, 0), "monika/d.webp")
image monika 2e = im.Composite((960, 960), (0, 0), "monika/1l.webp", (0, 0), "monika/2r.webp", (0, 0), "monika/e.webp")
image monika 2f = im.Composite((960, 960), (0, 0), "monika/1l.webp", (0, 0), "monika/2r.webp", (0, 0), "monika/f.webp")
image monika 2g = im.Composite((960, 960), (0, 0), "monika/1l.webp", (0, 0), "monika/2r.webp", (0, 0), "monika/g.webp")
image monika 2h = im.Composite((960, 960), (0, 0), "monika/1l.webp", (0, 0), "monika/2r.webp", (0, 0), "monika/h.webp")
image monika 2i = im.Composite((960, 960), (0, 0), "monika/1l.webp", (0, 0), "monika/2r.webp", (0, 0), "monika/i.webp")
image monika 2j = im.Composite((960, 960), (0, 0), "monika/1l.webp", (0, 0), "monika/2r.webp", (0, 0), "monika/j.webp")
image monika 2k = im.Composite((960, 960), (0, 0), "monika/1l.webp", (0, 0), "monika/2r.webp", (0, 0), "monika/k.webp")
image monika 2l = im.Composite((960, 960), (0, 0), "monika/1l.webp", (0, 0), "monika/2r.webp", (0, 0), "monika/l.webp")
image monika 2m = im.Composite((960, 960), (0, 0), "monika/1l.webp", (0, 0), "monika/2r.webp", (0, 0), "monika/m.webp")
image monika 2n = im.Composite((960, 960), (0, 0), "monika/1l.webp", (0, 0), "monika/2r.webp", (0, 0), "monika/n.webp")
image monika 2o = im.Composite((960, 960), (0, 0), "monika/1l.webp", (0, 0), "monika/2r.webp", (0, 0), "monika/o.webp")
image monika 2p = im.Composite((960, 960), (0, 0), "monika/1l.webp", (0, 0), "monika/2r.webp", (0, 0), "monika/p.webp")
image monika 2q = im.Composite((960, 960), (0, 0), "monika/1l.webp", (0, 0), "monika/2r.webp", (0, 0), "monika/q.webp")
image monika 2r = im.Composite((960, 960), (0, 0), "monika/1l.webp", (0, 0), "monika/2r.webp", (0, 0), "monika/r.webp")

image monika 3a = im.Composite((960, 960), (0, 0), "monika/2l.webp", (0, 0), "monika/1r.webp", (0, 0), "monika/a.webp")
image monika 3b = im.Composite((960, 960), (0, 0), "monika/2l.webp", (0, 0), "monika/1r.webp", (0, 0), "monika/b.webp")
image monika 3c = im.Composite((960, 960), (0, 0), "monika/2l.webp", (0, 0), "monika/1r.webp", (0, 0), "monika/c.webp")
image monika 3d = im.Composite((960, 960), (0, 0), "monika/2l.webp", (0, 0), "monika/1r.webp", (0, 0), "monika/d.webp")
image monika 3e = im.Composite((960, 960), (0, 0), "monika/2l.webp", (0, 0), "monika/1r.webp", (0, 0), "monika/e.webp")
image monika 3f = im.Composite((960, 960), (0, 0), "monika/2l.webp", (0, 0), "monika/1r.webp", (0, 0), "monika/f.webp")
image monika 3g = im.Composite((960, 960), (0, 0), "monika/2l.webp", (0, 0), "monika/1r.webp", (0, 0), "monika/g.webp")
image monika 3h = im.Composite((960, 960), (0, 0), "monika/2l.webp", (0, 0), "monika/1r.webp", (0, 0), "monika/h.webp")
image monika 3i = im.Composite((960, 960), (0, 0), "monika/2l.webp", (0, 0), "monika/1r.webp", (0, 0), "monika/i.webp")
image monika 3j = im.Composite((960, 960), (0, 0), "monika/2l.webp", (0, 0), "monika/1r.webp", (0, 0), "monika/j.webp")
image monika 3k = im.Composite((960, 960), (0, 0), "monika/2l.webp", (0, 0), "monika/1r.webp", (0, 0), "monika/k.webp")
image monika 3l = im.Composite((960, 960), (0, 0), "monika/2l.webp", (0, 0), "monika/1r.webp", (0, 0), "monika/l.webp")
image monika 3m = im.Composite((960, 960), (0, 0), "monika/2l.webp", (0, 0), "monika/1r.webp", (0, 0), "monika/m.webp")
image monika 3n = im.Composite((960, 960), (0, 0), "monika/2l.webp", (0, 0), "monika/1r.webp", (0, 0), "monika/n.webp")
image monika 3o = im.Composite((960, 960), (0, 0), "monika/2l.webp", (0, 0), "monika/1r.webp", (0, 0), "monika/o.webp")
image monika 3p = im.Composite((960, 960), (0, 0), "monika/2l.webp", (0, 0), "monika/1r.webp", (0, 0), "monika/p.webp")
image monika 3q = im.Composite((960, 960), (0, 0), "monika/2l.webp", (0, 0), "monika/1r.webp", (0, 0), "monika/q.webp")
image monika 3r = im.Composite((960, 960), (0, 0), "monika/2l.webp", (0, 0), "monika/1r.webp", (0, 0), "monika/r.webp")

image monika 4a = im.Composite((960, 960), (0, 0), "monika/2l.webp", (0, 0), "monika/2r.webp", (0, 0), "monika/a.webp")
image monika 4b = im.Composite((960, 960), (0, 0), "monika/2l.webp", (0, 0), "monika/2r.webp", (0, 0), "monika/b.webp")
image monika 4c = im.Composite((960, 960), (0, 0), "monika/2l.webp", (0, 0), "monika/2r.webp", (0, 0), "monika/c.webp")
image monika 4d = im.Composite((960, 960), (0, 0), "monika/2l.webp", (0, 0), "monika/2r.webp", (0, 0), "monika/d.webp")
image monika 4e = im.Composite((960, 960), (0, 0), "monika/2l.webp", (0, 0), "monika/2r.webp", (0, 0), "monika/e.webp")
image monika 4f = im.Composite((960, 960), (0, 0), "monika/2l.webp", (0, 0), "monika/2r.webp", (0, 0), "monika/f.webp")
image monika 4g = im.Composite((960, 960), (0, 0), "monika/2l.webp", (0, 0), "monika/2r.webp", (0, 0), "monika/g.webp")
image monika 4h = im.Composite((960, 960), (0, 0), "monika/2l.webp", (0, 0), "monika/2r.webp", (0, 0), "monika/h.webp")
image monika 4i = im.Composite((960, 960), (0, 0), "monika/2l.webp", (0, 0), "monika/2r.webp", (0, 0), "monika/i.webp")
image monika 4j = im.Composite((960, 960), (0, 0), "monika/2l.webp", (0, 0), "monika/2r.webp", (0, 0), "monika/j.webp")
image monika 4k = im.Composite((960, 960), (0, 0), "monika/2l.webp", (0, 0), "monika/2r.webp", (0, 0), "monika/k.webp")
image monika 4l = im.Composite((960, 960), (0, 0), "monika/2l.webp", (0, 0), "monika/2r.webp", (0, 0), "monika/l.webp")
image monika 4m = im.Composite((960, 960), (0, 0), "monika/2l.webp", (0, 0), "monika/2r.webp", (0, 0), "monika/m.webp")
image monika 4n = im.Composite((960, 960), (0, 0), "monika/2l.webp", (0, 0), "monika/2r.webp", (0, 0), "monika/n.webp")
image monika 4o = im.Composite((960, 960), (0, 0), "monika/2l.webp", (0, 0), "monika/2r.webp", (0, 0), "monika/o.webp")
image monika 4p = im.Composite((960, 960), (0, 0), "monika/2l.webp", (0, 0), "monika/2r.webp", (0, 0), "monika/p.webp")
image monika 4q = im.Composite((960, 960), (0, 0), "monika/2l.webp", (0, 0), "monika/2r.webp", (0, 0), "monika/q.webp")
image monika 4r = im.Composite((960, 960), (0, 0), "monika/2l.webp", (0, 0), "monika/2r.webp", (0, 0), "monika/r.webp")

image monika 5a = im.Composite((960, 960), (0, 0), "monika/3a.webp")
image monika 5b = im.Composite((960, 960), (0, 0), "monika/3b.webp")

image monika g1:
    "monika/g1.webp"
    xoffset 35 yoffset 55
    parallel:
        zoom 1.00
        linear 0.10 zoom 1.03
        repeat
    parallel:
        xoffset 35
        0.20
        xoffset 0
        0.05
        xoffset -10
        0.05
        xoffset 0
        0.05
        xoffset -80
        0.05
        repeat
    time 1.25
    xoffset 0 yoffset 0 zoom 1.00
    "monika 3"

image monika g2:
    block:
        choice:
            "monika/g2.webp"
        choice:
            "monika/g3.webp"
        choice:
            "monika/g4.webp"
    block:
        choice:
            pause 0.05
        choice:
            pause 0.1
        choice:
            pause 0.15
        choice:
            pause 0.2
    repeat


define narrator = Character(ctc="ctc", ctc_position="fixed")
define mc = DynamicCharacter('player', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define s = DynamicCharacter('s_name', image='sayori', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define m = DynamicCharacter('m_name', image='monika', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define n = DynamicCharacter('n_name', image='natsuki', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define y = DynamicCharacter('y_name', image='yuri', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define ny = Character('Нацуки и Юри', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")

define _dismiss_pause = config.developer

default persistent.playername = ""
default player = persistent.playername
default persistent.playthrough = 0
default persistent.yuri_kill = 0
default persistent.seen_eyes = None
default persistent.seen_sticker = None
default persistent.ghost_menu = None
default persistent.seen_ghost_menu = None
default seen_eyes_this_chapter = False
default persistent.anticheat = 0
default persistent.clear = [False, False, False, False, False, False, False, False, False, False]
default persistent.special_poems = None
default persistent.clearall = None
default persistent.menu_bg_m = None
default persistent.first_load = None
default persistent.first_poem = None
default persistent.seen_colors_poem = None
default persistent.monika_back = None
default in_sayori_kill = None
default in_yuri_kill = None
default anticheat = 0
define config.mouse = None
default allow_skipping = True
default basedir = config.basedir
default chapter = 0
default currentpos = 0
default faint_effect = None

default persistent.sayoriname = "Саёри"
default s_name = "[persistent.sayoriname]"
default m_name = "Моника"
default n_name = "Нацуки"
default y_name = "Юри"



default n_poemappeal = [0, 0, 0]
default s_poemappeal = [0, 0, 0]
default y_poemappeal = [0, 0, 0]
default m_poemappeal = [0, 0, 0]


default poemwinner = ['sayori', 'sayori', 'sayori']


default s_readpoem = False
default n_readpoem = False
default y_readpoem = False
default m_readpoem = False


default poemsread = 0



default n_appeal = 0
default s_appeal = 0
default y_appeal = 0
default m_appeal = 0



default n_exclusivewatched = False
default y_exclusivewatched = False


default y_gave = False
default y_ranaway = False


default ch1_choice = "sayori"


default help_sayori = None
default help_monika = None


default ch4_scene = "yuri"
default ch4_name = "Юри"
default sayori_confess = True


default natsuki_23 = None

label menuchr:
    scene tos
    menu:
        "Удалить monika.chr":
            $ delete_character("monika")
        "Удалить sayori.chr":
            $ delete_character("sayori")
        "Удалить yuri.chr":
            $ delete_character("yuri")
        "Удалить natsuki.chr":
            $ delete_character("natsuki")
        "Вернуться":
            return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
