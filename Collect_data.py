from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
def get_n(soup, id):
    goods = soup.findAll('a', class_='text_fader')
    namae = []
    for data in goods:
        namae.append(data.text)
    lim = []
    goods.clear()
    if id == 'manga':
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
    elif id == 'figure':
        for i in range(len(namae)):
            if re.findall(r'Копия', namae[i]) or re.findall(r'Pokemon', namae[i]) or re.findall(r'One Piece', namae[i]):
                lim.append(i)

        namae = [x for ind,x in enumerate(namae) if ind+1 not in lim]
        lim.clear()
        return namae

def get_p(soup, id):
    goods = soup.findAll('a', class_='text_fader')
    t_pri = soup.findAll('div', class_='price')
    namae = []
    pri = []
    for data in goods:
        namae.append(data.text)
    for data in t_pri:
        pri.append(data.text[:-5])
    lim = []
    lim_pr = []
    goods.clear()
    t_pri.clear()
    if id == 'manga':
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
    elif id == 'figure':
        for i in range(len(namae)):
            if re.findall(r'Копия', namae[i]) or re.findall(r'Pokemon', namae[i]) or re.findall(r'One Piece', namae[i]):
                lim_pr.append(i)

        pri = [x for ind, x in enumerate(pri) if ind + 1 not in lim_pr]
        lim_pr.clear()
        return pri

namae = []
price = []
url = 'https://diskomir.ru/catalog/manga/manga/?arrFilter_ff%5BNAME%5D=&arrFilter_pf%5BNALICHIE%5D=86&arrFilter_pf%5BFROM_MOVIE%5D=&arrFilter_pf%5BMADE_BY%5D=&set_filter=%CD%E0%E9%F2%E8'
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
namae = namae + get_n(soup, 'manga')
price = price + get_p(soup, 'manga')
for k in range(2, 13):
    url = 'https://diskomir.ru/catalog/manga/manga/?arrFilter_ff%5BNAME%5D=&arrFilter_pf%5BNALICHIE%5D=86&arrFilter_pf%5BFROM_MOVIE%5D=&arrFilter_pf%5BMADE_BY%5D=&set_filter=%CD%E0%E9%F2%E8&PAGEN_1=' + str(k)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    namae = namae + get_n(soup, 'manga')
    price = price + get_p(soup, 'manga')
del price[96]
del namae[96]

df = pd.DataFrame(columns=['name', 'price', 'shop', 'category'])
for i in range(len(namae)):
    _df = pd.DataFrame([[namae[i], int(price[i]), 'Discomir', 'Manga']], columns=['name', 'price', 'shop', 'category'])
    df = df.append(_df, ignore_index=True)
namae.clear()
price.clear()
url = 'https://diskomir.ru/catalog/animefigurki/malenkie_kitayskie_figurki/?arrFilter_ff%5BNAME%5D=&arrFilter_pf%5BNALICHIE%5D=86&arrFilter_pf%5BFROM_MOVIE%5D=&arrFilter_pf%5BMADE_BY%5D=&set_filter=%CD%E0%E9%F2%E8'
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
namae = namae + get_n(soup, 'figure')
price = price + get_p(soup, 'figure')
url = 'https://diskomir.ru/catalog/animefigurki/malenkie_kitayskie_figurki/?arrFilter_ff%5BNAME%5D=&arrFilter_pf%5BNALICHIE%5D=86&arrFilter_pf%5BFROM_MOVIE%5D=&arrFilter_pf%5BMADE_BY%5D=&set_filter=%CD%E0%E9%F2%E8&PAGEN_1=2'
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
namae = namae + get_n(soup, 'figure')
price = price + get_p(soup, 'figure')
del namae[len(namae)-1]
del price[len(namae)-1]
for i in range(len(namae)):
    _df = pd.DataFrame([[namae[i], int(price[i]), 'Discomir', 'Figure']], columns=['name', 'price', 'shop', 'category'])
    df = df.append(_df, ignore_index=True)
print(df)
df.to_excel('output.xlsx')