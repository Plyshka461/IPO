import requests
from bs4 import BeautifulSoup
import csv
url = 'https://www.priorbank.by/offers/services/currency-exchange'
r = requests.get(url)
print(r)
soup = BeautifulSoup(r.text,'html.parser')
print(soup)
items = soup.find_all('tr')
# print(items)
items.pop(-1)
# print(items)
courses = []
for item in items:
    _item = item.find_all("td")
    courses.append({
        'naim': _item[0].get_text(),
        'curAmount': _item[2].get_text(),
        'curs': _item[3].get_text().strip()
    })
print(courses)
with open('cursi.csv','w') as file:
    writer = csv.DictWriter(
        file,
        fieldnames = ['naim','curAmount','curs'],
        delimiter = ';',
        lineterminator = '\r',
        quoting = csv.QUOTE_MINIMAL
    )
    writer.writeheader();
    for elem in courses:
        writer.writerow(elem)