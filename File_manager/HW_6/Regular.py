import re

# author: Kashapova Dilyara
pattern = "(((https)(:\/\/))?(www\.)?(((youtu\.be)[\/]([A-z0-9]*)?)|((youtube.com)[\/](watch\?)((v=)([A-z0-9]*)?))*)((-Jec)?([\?\&]?([t]|(start))[=][A-z0-9]*)*)*)"
youtube_link = str(input('Введите ссылку YT: '))
result = re.search(pattern, youtube_link)

if result.group(1) == youtube_link:
    print("Да, это ссылка YT")
else:
    print("Нет, это не ссылка YT")
