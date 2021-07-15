import time
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
url = "https://diskomir.ru/catalog/znachki/nabory_znachkov/?from_movie=bananovaya_ryba_banana_fish_rybka_bananka&from_movie=voleybol_haikyu_haikyuu_&from_movie=doktor_stoun_dr_stone_doctor_stone&from_movie=drakon_gornichnaya_kobayashi_kobayashi_san_chi_no_maid_dragon_miss_kobayashi_s_dragon_maid&from_movie=durochka_aho_girl_ahogaru_clueless_girl"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
goods = soup.findAll('a', class_='text_fader')
for e in goods:
    print(e.text[:-5])
t_pri = soup.findAll('div', class_='price')
for data in t_pri:
    print(data.text[:-5])

# import itertools
# s = "ABC"
# com_set = itertools.combinations(s, 2)
# for i in com_set:
#     print(i[1])
