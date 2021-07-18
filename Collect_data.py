from bs4 import BeautifulSoup
import requests
from itertools import combinations
import re
import pandas as pd
import time
from selenium import webdriver

def get_n(soup, id, shop):
    if shop == 'discomir':
        goods = soup.findAll('a', class_='text_fader')
    elif shop == 'XL':
        driver = webdriver.Firefox(executable_path=r'A:\geckodriver.exe')
        driver.get(soup)
        time.sleep(6)
    elif shop == 'Nyaki':
        goods = soup.findAll('div', class_='product-name')
    namae = []
    if shop == 'discomir':
        for data in goods:
            namae.append(data.text)
    elif shop == "XL":
        tag_list = driver.find_elements_by_class_name("product-name")
        for e in tag_list:
            namae.append(e.text)
    elif shop == 'Nyaki':
        for data in goods:
            namae.append(data.text)
    lim = []
    lim_pr = []
    if id == 'manga' and shop == 'discomir':
        goods.clear()
        for i in range(len(namae)):
            if re.findall(r'Ранобэ',namae[i]):
                lim.append(i)
        namae = [x for ind,x in enumerate(namae) if ind+1 not in lim]
        lim.clear()
        for i in range(len(namae)):
            if re.findall(r'Том 1+$|Книга 1+$|Vol. 1+$',namae[i]):
                lim.append(namae[i])
        namae.clear()
        return lim
    elif id == 'manga' and shop == 'XL':
        but = driver.find_elements_by_class_name("button")
        for e in but:
            lim.append(e.text)
        del lim[0]
        for e in range(len(lim)):
            if lim[e] != 'Купить':
                lim_pr.append(e)
        for n in sorted(lim_pr, reverse=True):
            del namae[n]
        but.clear()
        lim.clear()
        for i in range(len(namae)):
            if re.findall(r'Том 1+$|Книга 1+$|Vol. 1+$|Том 1.+$', namae[i]):
                lim.append(namae[i])
        driver.quit()
        return lim
    elif id == 'manga' and shop == 'Nyaki':
        for i in range(len(namae)):
            if re.findall(r'1 том+$|1 книга+$', namae[i]):
                j = namae[i].find('1')
                if namae[i][j + 1] == ' ':
                    lim.append(namae[i])
        return lim
    elif id == 'figure' and shop == 'XL':
        but = driver.find_elements_by_class_name("button")
        for e in but:
            lim.append(e.text)
        del lim[0]
        for e in range(len(lim)):
            if lim[e] != 'Купить':
                lim_pr.append(e)
        for n in sorted(lim_pr, reverse=True):
            del namae[n]
        but.clear()
        lim.clear()
        driver.quit()
        return namae
    elif id == 'figure' and shop == 'discomir':
        for i in range(len(namae)):
            if re.findall(r'Копия', namae[i]) or re.findall(r'Pokemon', namae[i]) or re.findall(r'One Piece', namae[i]):
                lim.append(i)

        namae = [x for ind,x in enumerate(namae) if ind+1 not in lim]
        lim.clear()
        return namae
    elif id == 'znachok' and shop == 'discomir':
        for i in range(len(namae)):
            namae[i] = namae[i][:-5]
        return namae
    elif id == 'napitki' and shop == 'Nyaki':
        return namae

def get_p(soup, id, shop):
    if shop == 'discomir':
        goods = soup.findAll('a', class_='text_fader')
        t_pri = soup.findAll('div', class_='price')
    elif shop == 'XL':
        driver = webdriver.Firefox(executable_path=r'A:\geckodriver.exe')
        driver.get(soup)
        time.sleep(6)
    elif shop == 'Nyaki':
        goods = soup.findAll('div', class_='product-name')
        t_pri = soup.findAll('div', class_='column column-cost')
    namae = []
    pri = []
    if shop == 'discomir':
        for data in goods:
            namae.append(data.text)
        for data in t_pri:
            pri.append(data.text[:-5])
    elif shop == 'XL':
        tag_list = driver.find_elements_by_class_name("product-name")
        for e in tag_list:
            namae.append(e.text)
        but = driver.find_elements_by_class_name("costs-value")
        m = []
        for e in but:
            m.append(e.text)
        for data in m:
            r = data
            if 'Цена' in r:
                s = r[1:-3].find('а')
                dob = r[s+3:-1]
                dob = re.sub('\s', '', dob)
                pri.append(dob)
            else:
                s = r[1:-3].find('₽')
                ik = r[s + 3:-2]
                dob = re.sub('\s', '', ik)
                pri.append(dob)
    elif shop == 'Nyaki':
        for data in goods:
            namae.append(data.text)
        for data in t_pri:
            pri.append(data.text[:-11])
    lim = []
    lim_pr = []

    if id == 'manga' and shop == 'discomir':
        goods.clear()
        t_pri.clear()
        for i in range(len(namae)):
            if re.findall(r'Ранобэ', namae[i]):
                lim.append(i)
                lim_pr.append(i)

        namae = [x for ind, x in enumerate(namae) if ind + 1 not in lim]
        pri = [x for ind, x in enumerate(pri) if ind + 1 not in lim_pr]
        lim.clear()
        lim_pr.clear()
        for i in range(len(namae)):
            if re.findall(r'Том 1+$|Книга 1+$|Vol. 1+$', namae[i]):
                lim.append(namae[i])
                lim_pr.append(pri[i])
        namae.clear()
        pri.clear()
        return lim_pr
    elif id == 'manga' and shop == 'XL':
        but = driver.find_elements_by_class_name("button")
        for e in but:
            lim.append(e.text)
        del lim[0]
        for e in range(len(lim)):
            if lim[e] != 'Купить':
                lim_pr.append(e)
        for n in sorted(lim_pr, reverse=True):
            del namae[n]
            del pri[n]
        but.clear()
        lim.clear()
        lim_pr.clear()
        for i in range(len(namae)):
            if re.findall(r'Том 1+$|Книга 1+$|Vol. 1+$|Том 1.+$', namae[i]):
                lim.append(namae[i])
                lim_pr.append(pri[i])
        driver.quit()
        return lim_pr
    elif id == 'manga' and shop == 'Nyaki':
        for i in range(len(namae)):
            if re.findall(r'1 том+$|1 книга+$', namae[i]):
                j = namae[i].find('1')
                if namae[i][j + 1] == ' ':
                    lim_pr.append(pri[i])
        return lim_pr
    elif id == 'figure' and shop == 'XL':
        but = driver.find_elements_by_class_name("button")
        for e in but:
            lim.append(e.text)
        del lim[0]
        for e in range(len(lim)):
            if lim[e] != 'Купить':
                lim_pr.append(e)
        for n in sorted(lim_pr, reverse=True):
            del namae[n]
            del pri[n]
        but.clear()
        lim.clear()
        lim_pr.clear()
        driver.quit()
        return pri
    elif id == 'figure' and shop == 'discomir':
        for i in range(len(namae)):
            if re.findall(r'Копия', namae[i]) or re.findall(r'Pokemon', namae[i]) or re.findall(r'One Piece', namae[i]):
                lim_pr.append(i)

        pri = [x for ind, x in enumerate(pri) if ind + 1 not in lim_pr]
        lim_pr.clear()
        return pri
    elif id == 'znachok' and shop == 'discomir':
        return pri
    elif id == 'napitki' and shop == 'Nyaki':
        return pri
df = pd.read_excel('output.xlsx')
df.pop('Unnamed: 0')
namae = []
price = []

# Discomir (znachki)
# url = "https://diskomir.ru/catalog/znachki/nabory_znachkov/?from_movie=bananovaya_ryba_banana_fish_rybka_bananka&from_movie=voleybol_haikyu_haikyuu_&from_movie=doktor_stoun_dr_stone_doctor_stone&from_movie=drakon_gornichnaya_kobayashi_kobayashi_san_chi_no_maid_dragon_miss_kobayashi_s_dragon_maid&from_movie=durochka_aho_girl_ahogaru_clueless_girl"
# page = requests.get(url)
# soup = BeautifulSoup(page.text, "html.parser")
# namae = namae + get_n(soup, 'znachok', 'discomir')
# price = price + get_p(soup, 'znachok', 'discomir')
# for i in range(len(namae)):
#     if price[i].isdigit()==True:
#         _df = pd.DataFrame([[namae[i], int(price[i]), 'Discomir', 'Pins']], columns=['name', 'price', 'shop', 'category'])
#         df = df.append(_df, ignore_index=True)

# Old collect data

# Diskomir (manga)
# url = 'https://diskomir.ru/catalog/manga/manga/?arrFilter_ff%5BNAME%5D=&arrFilter_pf%5BNALICHIE%5D=86&arrFilter_pf%5BFROM_MOVIE%5D=&arrFilter_pf%5BMADE_BY%5D=&set_filter=%CD%E0%E9%F2%E8'
# page = requests.get(url)
# soup = BeautifulSoup(page.text, "html.parser")
# namae = namae + get_n(soup, 'manga', 'discomir')
# price = price + get_p(soup, 'manga', 'discomir')
# for k in range(2, 13):
#     url = 'https://diskomir.ru/catalog/manga/manga/?arrFilter_ff%5BNAME%5D=&arrFilter_pf%5BNALICHIE%5D=86&arrFilter_pf%5BFROM_MOVIE%5D=&arrFilter_pf%5BMADE_BY%5D=&set_filter=%CD%E0%E9%F2%E8&PAGEN_1=' + str(k)
#     page = requests.get(url)
#     soup = BeautifulSoup(page.text, "html.parser")
#     namae = namae + get_n(soup, 'manga', 'discomir')
#     price = price + get_p(soup, 'manga', 'discomir')
# del price[96]
# del namae[96]
#
# df = pd.DataFrame(columns=['name', 'price', 'shop', 'category'])
# for i in range(len(namae)):
#     if price[i].isdigit() == True:
#         _df = pd.DataFrame([[namae[i], int(price[i]), 'Discomir', 'Manga']], columns=['name', 'price', 'shop', 'category'])
#         df = df.append(_df, ignore_index=True)
# namae.clear()
# price.clear()

# Discomir (figurki)

# url = 'https://diskomir.ru/catalog/animefigurki/malenkie_kitayskie_figurki/?arrFilter_ff%5BNAME%5D=&arrFilter_pf%5BNALICHIE%5D=86&arrFilter_pf%5BFROM_MOVIE%5D=&arrFilter_pf%5BMADE_BY%5D=&set_filter=%CD%E0%E9%F2%E8'
# page = requests.get(url)
# soup = BeautifulSoup(page.text, "html.parser")
# namae = namae + get_n(soup, 'figure', 'discomir')
# price = price + get_p(soup, 'figure', 'discomir')
# url = 'https://diskomir.ru/catalog/animefigurki/malenkie_kitayskie_figurki/?arrFilter_ff%5BNAME%5D=&arrFilter_pf%5BNALICHIE%5D=86&arrFilter_pf%5BFROM_MOVIE%5D=&arrFilter_pf%5BMADE_BY%5D=&set_filter=%CD%E0%E9%F2%E8&PAGEN_1=2'
# page = requests.get(url)
# soup = BeautifulSoup(page.text, "html.parser")
# namae = namae + get_n(soup, 'figure', 'discomir')
# price = price + get_p(soup, 'figure', 'discomir')
# del namae[len(namae)-1]
# del price[len(namae)-1]
# for i in range(len(namae)):
#     if price[i].isdigit()==True:
#         _df = pd.DataFrame([[namae[i], int(price[i]), 'Discomir', 'Figure']], columns=['name', 'price', 'shop', 'category'])
#         df = df.append(_df, ignore_index=True)
#
# namae.clear()
# price.clear()

# XL (the end 224) (figurki)
#
# for k in range(2, 5):
#     url = 'https://xlm.ru/nendoroid?by=popular&page='+str(k)
#     namae = namae + get_n(url, 'figure', 'XL')
#     price = price + get_p(url, 'figure', 'XL')
# for i in range(len(namae)):
#     if price[i].isdigit() == True:
#         _df = pd.DataFrame([[namae[i], int(price[i]), 'XL Media', 'Figure']], columns=['name', 'price', 'shop', 'category'])
#         df = df.append(_df, ignore_index=True)
#
# namae.clear()
# price.clear()

# XL (manga)

# url = 'https://xlm.ru/manga?by=popular'
# namae = namae + get_n(url, 'manga', 'XL')
# price = price + get_p(url, 'manga', 'XL')
# for i in range(len(namae)):
#     if price[i].isdigit() == True:
#         _df = pd.DataFrame([[namae[i], int(price[i]), 'XL Media', 'Manga']], columns=['name', 'price', 'shop', 'category'])
#         df = df.append(_df, ignore_index=True)
#
# namae.clear()
# price.clear()
#
# for k in range(2, 19):
#     url = 'https://xlm.ru/manga?by=popular&page='+str(k)
#     namae = namae + get_n(url, 'manga', 'XL')
#     price = price + get_p(url, 'manga', 'XL')
#
# for i in range(len(namae)):
#     if price[i].isdigit() == True:
#         _df = pd.DataFrame([[namae[i], int(price[i]), 'XL Media', 'Manga']], columns=['name', 'price', 'shop', 'category'])
#         df = df.append(_df, ignore_index=True)

# Nyaki (manga)
# for i in range(1, 9):
#     url = 'https://nyaki.ru/catalog/manga/?page='+str(i)
#     page = requests.get(url)
#     soup = BeautifulSoup(page.text, "html.parser")
#     namae = namae + get_n(soup, 'manga', 'Nyaki')
#     price = price + get_p(soup, 'manga', 'Nyaki')
# for i in range(len(namae)):
#     if price[i].isdigit() == True:
#         _df = pd.DataFrame([[namae[i], int(price[i]), 'Nyaki', 'Manga']], columns=['name', 'price', 'shop', 'category'])
#         df = df.append(_df, ignore_index=True)

# url = 'https://nyaki.ru/catalog/napitki/'
# page = requests.get(url)
# soup = BeautifulSoup(page.text, "html.parser")
# namae = namae + get_n(soup, 'napitki', 'Nyaki')
# price = price + get_p(soup, 'napitki', 'Nyaki')
# for i in range(len(namae)):
#     if price[i].isdigit() == True:
#         _df = pd.DataFrame([[namae[i], int(price[i]), 'Nyaki', 'Soda']], columns=['name', 'price', 'shop', 'category'])
#         df = df.append(_df, ignore_index=True)

a = []
for i in range(307):
    a.append(i)
data = list(combinations(a, 3))
a.clear()
i = 0
for k in range(len(data)):
    if df.iloc[data[k][0]]['category'] != df.iloc[data[k][1]]['category'] and df.iloc[data[k][0]]['category'] != df.iloc[data[k][2]]['category'] and df.iloc[data[k][1]]['category'] != df.iloc[data[k][2]]['category']:
        a.append(data[k])
        i = i + 1
        print('Now – '+str(k))
        print('Real – '+str(i))
print(a)
# if df.iloc[0]['shop'] == df.iloc[1]['shop']:
#     print('YAY')

# i = df.iloc[0]['price']
# i = i + 1
# print(i)
# df.to_excel('output.xlsx')
