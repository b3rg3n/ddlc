# DDLC MODLOADER DISCORD RPC
# by @b3rg3n
# since 2024

init python:
    from pypresence import DiscordNotFound # ИМПОРТИРУЕМ НУЖНУЮ ОШИБКУ ПИТОНА (ЛЕЖАТ В python-packages)
    from pypresence import Presence # ИМПОРТИРУЕМ НУЖНУЮ ФУНКЦИЮ ПИТОНА (ЛЕЖАТ В python-packages)
    import time # ИМПОРТИРУЕМ ВРЕМЯ ДЛЯ СЧЁТЧИКА

    rpc = Presence("1214596078721171456") # ID ХУЕТЫ
    try:
        rpc.connect() # ПОДКЛЮЧЕНИЕ К ДС
    except DiscordNotFound:
        pass

# КАК ЮЗАТЬ ЭТУ ПОЕБЕНЬ:
#
#    python: # ОБНОВЛЯЕМ RPC
#        try:
#            rpc.update(state="Акт I | Глава I",details="Поиски. Сайори",large_image="logogovna",start=time.time())
#        except AssertionError:
#            pass
#
# ЭТО ВСЁ ВСТАВИТЬ В НУЖНЫЙ ЛЕЙБЛ
# state - ВТОРАЯ СТРОКА
# details - ПЕРВАЯ СТРОКА
# large_image - КАРТИНКА АКТИВНОСТИ В ДС
