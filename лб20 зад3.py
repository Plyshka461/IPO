from urllib.parse import urlunparse

sborca = ('https', '//www.twitter.com', '/BrawlStars/status/1220908675218280453', '', '', '')
# Собираем URL обратно в строку
url = urlunparse(sborca)
print(url)