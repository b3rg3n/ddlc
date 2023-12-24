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
    define config.developer = True
    define config.variants = [ "large", "pc", "touch", None ]
    define config.hw_video = False
    $ number_of_options = 13
    $ bergenmods = False
    $ modistalled = False