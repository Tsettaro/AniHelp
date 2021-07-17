import time
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import re
a = []
lim = []
url = 'https://nyaki.ru/catalog/manga/?page=1'
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
goods = soup.findAll('div', class_='column column-cost')
for data in goods:
    a.append(data.text[:-11])
print(a)
# for i in range(len(a)):
#     if re.findall(r'1 том+$|1 книга+$', a[i]):
#         j = a[i].find('1')
#         if a[i][j+1] == ' ':
#             lim.append(a[i])
print(lim)
# import itertools
# s = "ABC"
# com_set = itertools.combinations(s, 2)
# for i in com_set:
#     print(i[1])
