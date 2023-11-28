init python:
    build.archive("scripts", "all")
    build.archive("images", "all")
    build.archive("audio", "all")
    build.archive("fonts", "all")
    build.archive("video", "all")

    build.classify("game/**.jpg", "images")
    build.classify("game/**.png", "images")
    build.classify("game/**.webp", "images")

    build.classify("game/**.rpyc", "scripts")
    build.classify("game/**.txt", "scripts")
    build.classify("game/**.chr", "scripts")

    build.classify("game/**.wav", "audio")
    build.classify("game/**.mp3", "audio")
    build.classify("game/**.ogg", "audio")


    build.classify("game/**.otf", "fonts")
    build.classify("game/**.ttf", "fonts")

    build.classify("game/**.webm", "video")
    build.classify("game/**.ogv", "video")

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**.rpy', None)
    build.classify('**.psd', None)
    build.classify('**.sublime-project', None)
    build.classify('**.sublime-workspace', None)
    build.classify('/music/*.*', None)
    build.classify('script-regex.txt', None)
    build.classify('/game/10', None)
    build.classify('**.rar', None)
    build.classify('**.zip', None)
    build.classify('**.7z', None)
    build.classify('**.md', None)
    build.classify('game/scripts/.vscode/**', None)
    build.classify('game/cache/**', None)
    build.classify('game/tl/**', None)

    build.documentation('*.html')
    build.documentation('*.txt')

    build.include_old_themes = False

define build.itch_project = "teamsalvato/ddlc"
