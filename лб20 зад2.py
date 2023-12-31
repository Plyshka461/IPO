from urllib.parse import urlparse

url=urlparse ('//www.twitter.com/BrawlStars/status/1220908675218280453')
url._replace(scheme='https')#здесь мы должны были добавить протокол, но он не выводится, так же как и на лекции не работает
print(url)