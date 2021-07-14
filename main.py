import time
from selenium import webdriver
list=['a','b','c','d','e','f']
numbers=[1,2,3]
for n in sorted(numbers, reverse=True):
    del list[n]
print(list)
# driver = webdriver.Firefox(executable_path=r'A:\geckodriver.exe')
# driver.get("https://xlm.ru/search?search=%D0%A2%D0%BE%D0%BC+1&page=6")
# time.sleep(6)
#
# but = driver.find_elements_by_class_name("costs-value")
# a = []
# for e in but:
#     a.append(e.text)
# print(a)
# tag_list = driver.find_elements_by_class_name("product-name")
# b = []
# for e in tag_list:
#     b.append(e.text)
# print(len(b))
# print(a)
driver.quit()
# url = 'https://xlm.ru/search?search=%D0%A2%D0%BE%D0%BC+1&page=6'
# page = requests.get(url)
# time.sleep(2)
# soup = BeautifulSoup(page.text, "html.parser")
# goods = soup.findAll('a', class_='product-name')
# namae = []
# pri = []
# soup_p = soup.findAll('span', class_='costs-value')
# print(soup_p)
# for data in goods:
#     namae.append(data.text[7:-5])
# print(namae)
# for data in soup_p:
#     r = data
#     if 'Цена' in r.text:
#         dob = r.text[6:9]
#         pri.append(dob)
#     else:
#         s = r.text[1:-3].find('₽')
#         ik = r.text[s + 3:-3]
#         dob = re.sub('\s', '', ik)
#         pri.append(dob)
# print(pri)
# print(len(pri), len(namae))

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
