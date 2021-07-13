from bs4 import BeautifulSoup
import requests
import re
import time
url = 'https://xlm.ru/search?search=%D0%A2%D0%BE%D0%BC+1&page=6'
page = requests.get(url)
time.sleep(2)
soup = BeautifulSoup(page.text, "html.parser")
goods = soup.findAll('a', class_='product-name')
namae = []
pri = []
soup_p = soup.findAll('span', class_='costs-value')
print(soup_p)
for data in goods:
    namae.append(data.text[7:-5])
print(namae)
for data in soup_p:
    r = data
    if 'Цена' in r.text:
        dob = r.text[6:9]
        pri.append(dob)
    else:
        s = r.text[1:-3].find('₽')
        ik = r.text[s + 3:-3]
        dob = re.sub('\s', '', ik)
        pri.append(dob)
print(pri)
print(len(pri), len(namae))
# for data in soup_p:
#     namae.append(data)
# s = namae[0].text[1:-3].find('₽')
# ik = namae[0].text[s+3:-3]
# dob = re.sub('\s', '', ik)
# print(int(dob))


# import itertools
# s = "ABC"
# com_set = itertools.combinations(s, 2)
# for i in com_set:
#     print(i[1])
