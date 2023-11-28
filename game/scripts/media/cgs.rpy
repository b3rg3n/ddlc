image y_cg2_bg:
    "images/cg/y_cg2_bg1.webp"
    6.0
    "images/cg/y_cg2_bg2.webp" with Dissolve(1)
    2
    "images/cg/y_cg2_bg1.webp" with Dissolve(1)
    1
    repeat
image y_cg2_base:
    "images/cg/y_cg2_base.webp"
image y_cg2_nochoc:
    "images/cg/y_cg2_nochoc.webp"
    on hide:
        linear 0.5 alpha 0
image y_cg2_details:
    "images/cg/y_cg2_details.webp"
    alpha 1.00
    6.0
    linear 1.0 alpha 0.35
    1.0
    linear 1.0 alpha 1.0
    repeat

image y_cg2_exp2:
    "images/cg/y_cg2_exp2.webp"
    alpha 0
    linear 0.5 alpha 1
    on hide:
        linear 0.5 alpha 0
image y_cg2_exp3:
    "images/cg/y_cg2_exp3.webp"
    alpha 0
    linear 0.5 alpha 1
    on hide:
        linear 0.5 alpha 0

image y_cg2_dust1:
    "images/cg/y_cg2_dust1.webp"
    subpixel True
    parallel:
        alpha 1.00
        6.0
        linear 1.0 alpha 0.35
        1.0
        linear 1.0 alpha 1.0
        repeat
    parallel:
        alpha 0
        linear 2.0 alpha 1.0
        10.0
        linear 2.0 alpha 0
        repeat
    parallel:
        xoffset 100 yoffset -100
        linear 14.0 xoffset -100 yoffset 100
        repeat
image y_cg2_dust2:
    "images/cg/y_cg2_dust2.webp"
    subpixel True
    parallel:
        alpha 1.00
        6.0
        linear 1.0 alpha 0.35
        1.0
        linear 1.0 alpha 1.0
        repeat
    parallel:
        alpha 0
        linear 2.0 alpha 1.0
        28.0
        linear 2.0 alpha 0
        repeat
    parallel:
        xoffset 100 yoffset -100
        linear 32.0 xoffset -100 yoffset 100
        repeat
image y_cg2_dust3:
    "images/cg/y_cg2_dust3.webp"
    subpixel True
    parallel:
        alpha 1.00
        6.0
        linear 1.0 alpha 0.35
        1.0
        linear 1.0 alpha 1.0
        repeat
    parallel:
        alpha 0
        linear 2.0 alpha 1.0
        13.0
        linear 2.0 alpha 0
        repeat
    parallel:
        xoffset 100 yoffset -100
        linear 17.0 xoffset -100 yoffset 100
        repeat

image y_cg2_dust4:
    "images/cg/y_cg2_dust4.webp"
    subpixel True
    parallel:
        alpha 1.00
        6.0
        linear 1.0 alpha 0.35
        1.0
        linear 1.0 alpha 1.0
        repeat
    parallel:
        alpha 0
        linear 2.0 alpha 1.0
        15.0
        linear 2.0 alpha 0
        repeat
    parallel:
        xoffset 100 yoffset -100
        linear 19.0 xoffset -100 yoffset 100
        repeat

image n_cg1_bg:
    "images/cg/n_cg1_bg.webp"
image n_cg1_base:
    "images/cg/n_cg1_base.webp"

image n_cg1_exp1:
    "images/cg/n_cg1_exp1.webp"
image n_cg1_exp2:
    "images/cg/n_cg1_exp2.webp"
image n_cg1_exp3:
    "images/cg/n_cg1_exp3.webp"
image n_cg1_exp4:
    "images/cg/n_cg1_exp4.webp"
image n_cg1_exp5:
    "images/cg/n_cg1_exp5.webp"

image n_cg1b = LiveComposite((1280,720), (0,0), "images/cg/n_cg1b.webp", (882,325), "n_rects1", (732,400), "n_rects2", (850,475), "n_rects3")

image n_rects1:
    RectCluster(Solid("#000"), 12, 30, 30).sm
    pos (899, 350)
    size (34, 34)

image n_rects2:
    RectCluster(Solid("#000"), 12, 30, 24).sm
    pos (749, 430)
    size (34, 34)

image n_rects3:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (764, 490)
    size (30, 20)

image n_cg2_bg:
    "images/cg/n_cg2_bg.webp"
image n_cg2_base:
    "images/cg/n_cg2_base.webp"
image n_cg2_exp1:
    "images/cg/n_cg2_exp1.webp"
image n_cg2_exp2:
    "images/cg/n_cg2_exp2.webp"

image n_cg3_base:
    "images/cg/n_cg3_base.webp"
image n_cg3_cake:
    "images/cg/n_cg3_cake.webp"
image n_cg3_exp1:
    "images/cg/n_cg3_exp1.webp"
image n_cg3_exp2:
    "images/cg/n_cg3_exp2.webp"

image y_cg1_base:
    "images/cg/y_cg1_base.webp"
image y_cg1_exp1:
    "images/cg/y_cg1_exp1.webp"
image y_cg1_exp2:
    "images/cg/y_cg1_exp2.webp"
image y_cg1_exp3:
    "images/cg/y_cg1_exp3.webp"

image y_cg3_base:
    "images/cg/y_cg3_base.webp"
image y_cg3_exp1:
    "images/cg/y_cg3_exp1.webp"

image s_cg1:
    "images/cg/s_cg1.webp"

image s_cg2_base1:
    "images/cg/s_cg2_base1.webp"
image s_cg2_base2:
    "images/cg/s_cg2_base2.webp"
image s_cg2_exp1:
    "images/cg/s_cg2_exp1.webp"
image s_cg2_exp2:
    "images/cg/s_cg2_exp2.webp"
image s_cg2_exp3:
    "images/cg/s_cg2_exp3.webp"

image s_cg3:
    "images/cg/s_cg3.webp"

image s_kill_bg:
    subpixel True
    "images/cg/s_kill_bg.webp"

image s_kill:
    subpixel True
    "images/cg/s_kill.webp"

image s_kill_bg2:
    subpixel True
    "images/cg/s_kill_bg2.webp"

image s_kill2:
    subpixel True
    "images/cg/s_kill2.webp"

image y_kill = ConditionSwitch(
    "persistent.yuri_kill >= 1380", "images/cg/y_kill/3a.webp",
    "persistent.yuri_kill >= 1180", "images/cg/y_kill/3c.webp",
    "persistent.yuri_kill >= 1120", "images/cg/y_kill/3b.webp",
    "persistent.yuri_kill >= 920", "images/cg/y_kill/3a.webp",
    "persistent.yuri_kill >= 720", "images/cg/y_kill/2c.webp",
    "persistent.yuri_kill >= 660", "images/cg/y_kill/2b.webp",
    "persistent.yuri_kill >= 460", "images/cg/y_kill/2a.webp",
    "persistent.yuri_kill >= 260", "images/cg/y_kill/1c.webp",
    "persistent.yuri_kill >= 200", "images/cg/y_kill/1b.webp",
    "True", "images/cg/y_kill/1a.webp",

    )

transform s_kill_bg_start:
    truecenter
    zoom 1.10
    linear 4 zoom 1.00

transform s_kill_start:
    truecenter
    xalign 0.3 yalign 0.25 zoom 0.8
    linear 4 zoom 0.75 xalign 0.315 yoffset 10

image s_kill_bg_zoom:
    contains:
        "s_kill_bg"
        xalign 0.2 yalign 0.3 zoom 2.0
    dizzy(0.25, 1.0)

transform dizzy(m, t, subpixel=True):
    subpixel subpixel
    parallel:
        xoffset 0
        ease 0.75 * t xoffset 10 * m
        ease 0.75 * t xoffset 5 * m
        ease 0.75 * t xoffset -5 * m
        ease 0.75 * t xoffset -3 * m
        ease 0.75 * t xoffset -10 * m
        ease 0.75 * t xoffset 0
        ease 0.75 * t xoffset 5 * m
        ease 0.75 * t xoffset 0
        repeat
    parallel:
        yoffset 0
        ease 1.0 * t yoffset 5 * m
        ease 2.0 * t yoffset -5 * m
        easein 1.0 * t yoffset 0
        repeat

image s_kill_zoom:
    contains:
        "s_kill"
        truecenter
        zoom 2.0 xalign 0.5 yalign 0.05
    dizzy(1, 1.0)

image s_kill_bg2_zoom:
    contains:
        "s_kill_bg2"
        xalign 0.2 yalign 0.3 zoom 2.0
    parallel:
        dizzy(0.25, 1.0)
    parallel:
        alpha 0.2
        linear 0.25 alpha 0.2
        linear 0.25 alpha 0.25
        linear 0.25 alpha 0.2
        linear 0.25 alpha 0.3
        linear 0.25 alpha 0.25
        linear 0.25 alpha 0.35
        linear 0.25 alpha 0.3
        linear 0.25 alpha 0.35
        linear 0.25 alpha 0.2
        repeat

image s_kill2_zoom:
    contains:
        "s_kill2"
        truecenter
        zoom 2.0 xalign 0.5 yalign 0.05
    parallel:
        dizzy(1, 1.0)
    parallel:
        alpha 0.3
        linear 0.25 alpha 0.3
        linear 0.25 alpha 0.4
        linear 0.25 alpha 0.3
        linear 0.25 alpha 0.5
        linear 0.25 alpha 0.4
        linear 0.25 alpha 0.6
        linear 0.25 alpha 0.5
        linear 0.25 alpha 0.6
        linear 0.25 alpha 0.4
        repeat
