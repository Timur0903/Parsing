"----------------------------------------------PARSING-----------------------------------------------------"
# парсинг - процесс автомотического сбора данных 

# Библиотеки.
# requests - отправляет запрос на сайт и в итоге получает html код страницы
# Beautiful Soap - помогает извлечь информацию из html Помогает обращатся к определенным тегами и вытаскиать информацию
# Lxml - вступает в роле парсера для BS(разбивает информацию на мелкие части и анализирует данные )


# python3 -m venv venv-создание виртуального окружения

# source venv/bin/activate - активировали виртуальнок окружение

# pip install -r requirements.txt



# import requests
# from bs4 import BeautifulSoup
# import csv


# URL = 'https://enter.kg/computers/noutbuki_bishkek'

# def write_to_csv(data):
#     with open('data.csv','a')as file:
#         writer = csv.writer(file)
#         writer.writerow([data['title'],data['price'],data['image']])

# def get_html(url):
#     response = requests.get(url)
#     return response.text

# def get_data(html):
#     soup = BeautifulSoup(html,'lxml')
#     list_comp = soup.find_all('div',class_ = 'row' )
#     dict_={}
#     for comp in list_comp:
#         title = comp.find('span',class_ = 'prouct_name').text
#         price = comp.find('span',class_ = 'price').text
#         image = 'https://enter.kg' + comp.find('img').get('src')
#         dict_ = {'title':title,'price':price,'image':image}
    
#         write_to_csv(dict_)

# print(get_data(get_html(URL)))











"----------------------------------------------TASKI-----------------------------------------------------"

# Нужно получить статус запроса доступа к странице:
# https://stackoverflow.com/questions
# В начале, получите статус запроса и присвойте результат запроса к переменной source.
# Затем выведите эту переменную в консоль.
# Примерный вывод в консоли:
# 200 
# функцию создавать не нужно, весь код прописывайте сразу в терминале


# import requests
# URL = 'https://stackoverflow.com/questions'
# source = requests.get(URL).status_code
# print(source)



"--------------------------------------------------------------------------------------------------"


# Спарсите тэги h1, p и ссылку с тэга a из веб-страницы:
# http://www.example.com/
# и выведите результат в консоль в таком виде

# import requests
# from bs4 import BeautifulSoup

# source = requests.get('http://www.example.com/').text 
# my_page = BeautifulSoup(source, 'lxml')
# print('h1:'+my_page.h1.text)
# print('p:'+my_page.p.text)
# print('a:'+my_page.a.get('href'))

"--------------------------------------------------------------------------------------------------"


# Выведите с главной страницы википедии:
# https://www.wikipedia.org/
# сколько всего статей есть немецком языке.
# Вывод в консоль должен быть таким:
# Deutsch
# 2 590 000+ Artikel 



# import requests
# from bs4 import BeautifulSoup

# source = requests.get('https://www.wikipedia.org/').text 
# my_page = BeautifulSoup(source, 'lxml')
# vlog = my_page.find('div', class_ = 'central-featured-lang lang4') 
# print(vlog.text)


"--------------------------------------------------------------------------------------------------"

# Напишите программу которая проверяет имеет ли страница заголовок(тэг h1) или нет.

# Для этого напишите функцию getTitle() которая будет принимать url страницы и возвращать заголовок если он есть, если же его нет то будет возвращать "Title could not be found"

#  print(getTitle('http://www.example.com/'))
# Output:

#  <h1>Example Domain</h1>


# import requests
# from bs4 import BeautifulSoup

# URL = 'http://www.example.com/'

# def getTitle(url):
#     response = requests.get(url).text
    

#     soup = BeautifulSoup(response,'lxml')
#     list_comp = soup.find('h1') 
#     if list_comp:
#         return list_comp
#     else:
#         return "Title could not be found"

# print(getTitle('http://www.example.com/'))


"--------------------------------------------------------------------------------------------------"


# пишите код который сохраняет все названия категорий со страницы:
# https://enter.kg/
# в список category_list.
# После, напишите функцию которая имеет два параметра - список категорий - categories и ключевое слово - keyword.
# Функция должна производить поиск по ключевому слову в списке заголовков category_list и возвращать список заголовков которые содержат данное слово (независимо от регистра).
# К примеру:
# print(find_category(category_list, 'Ноутбуки')) 
# Вывод будет:
# ['Ноутбуки, Ультрабуки, Гот. решения (1281)', 'Ноутбуки (1235)', 'Ноутбуки, Ультрабуки, Гот. решения(1281)', 'Ноутбуки и ультрабуки'] 



# import requests
# from bs4 import BeautifulSoup
# import csv


# URL = 'https://enter.kg/'


# def find_category(categories:list,keyword:str):
#     result = []
#     for category in categories:
#         if keyword.lower() in category.lower():
#             result.append(category)
#     response = requests.get(url)
#     return response.text

# def get_data(html):
#     soup = BeautifulSoup(html,'lxml')
#     list_comp = soup.find_all('div',class_ = 'row' )
#     dict_={}
#     for comp in list_comp:
#         title = comp.find('span',class_ = 'prouct_name').text
#         price = comp.find('span',class_ = 'price').text
#         image = 'https://enter.kg' + comp.find('img').get('src')
#         dict_ = {'title':title,'price':price,'image':image}
    
#         write_to_csv(dict_)

# print(get_data(get_html(URL)))







# import requests from bs4 import BeautifulSoup as BS def find_category(categories: list, keyword: str): result = [] for category in categories: if keyword.lower() in category.lower(): result.append(category) return result category_list = [] URL = 'https://enter.kg/' response = requests.get(URL) soup = BS(response.text, 'html.parser') categories = soup.find_all('li', {'class': 'VmClose'}) for category in categories: title = category.find('a').text category_list.append(title) categories = soup.find_all("span", {"class": "category-product-count"}) for category in categories: title = category.text.strip() category_list.append(title) print(find_category(category_list, 'Ноутбуки'))



"--------------------------------------------------------------------------------------------------"

# Напишите программу которая будет парсить топ 250 фильмов с сайта IMBD:
# https://www.imdb.com/chart/top
# Затем напишите функцию get_link, которая будет принимать в аргументы список фильмов - title_list и строку - name. Функция должна производить поиск в списке по строке и возвращать ссылку на фильм. Вы должны вернуть только первое совпадение в списке.
# Например:
# get_link(title_list, 'shawshank') 
# Вернет вам:
# https://www.imdb.com/title/tt0111161/ 



























"---------------------------------------CLASSROOM-----------------------------------------------------------"



# import requests
# from bs4 import BeautifulSoup
# import csv
# count = 0
# url = 'https://vesti.kg/'
# news_titles = []

# for page in range(100):
#     url = f'https://vesti.kg/itemlist.html?start={count}'
#     response = requests.get(url)
#     htmltext = response.text
#     soup = BeautifulSoup(htmltext, 'lxml')
#     news_items = soup.find_all('div', class_='itemBody')
#     for i in news_items:
#         news_titles.append(i.h2.text.strip())

#     count+=30


# with open('vesti_news.csv', 'w') as csvfile:
#     writer = csv.writer(csvfile)
#     for i in news_titles:
#         writer.writerow([i])
    
'------------------------------------------PARSING------------------------------------------------------'


import requests
from bs4 import BeautifulSoup
import csv
count = 0
url = 'http://kenesh.kg/ru/news/all/list'
news_titles = []


def write_to_csv(data):
    with open('data1.csv','a')as file:
        writer = csv.writer(file)
        writer.writerow([data['title'],data['date'],data['image']])

for page in range(20):
    url = f'http://kenesh.kg/ru/news/all/list?page={count}'
    response = requests.get(url)
    htmltext = response.text
    soup = BeautifulSoup(htmltext, 'lxml')
    news_items = soup.find_all('div','news__item news__item__3')
    for i in news_items:
        title = i.find('a', class_ = 'news__item__title__link').text
        date = i.find('div','news__item__date').text
        image = 'http://kenesh.kg'+i.find('img').get('src') if i.find('img') != None else 'NONE'
        dict_ = {'title':title,'date':date,'image':image}
    
        write_to_csv(dict_)
        
    count+=1




    























# source = requests.get('http://www.example.com/').text 
# my_page = BeautifulSoup(source, 'lxml')
# print('h1:'+my_page.h1.text)
# print('p:'+my_page.p.text)
# print('a:'+my_page.a.get('href'))










# URL = 'https://enter.kg/computers/noutbuki_bishkek'

# def write_to_csv(data):
#     with open('data.csv','a')as file:
#         writer = csv.writer(file)
#         writer.writerow([data['title'],data['price'],data['image']])

# def get_html(url):
#     response = requests.get(url)
#     return response.text

# def get_data(html):
#     soup = BeautifulSoup(html,'lxml')
#     list_comp = soup.find_all('div',class_ = 'row' )
#     dict_={}
#     for comp in list_comp:
#         title = comp.find('span',class_ = 'prouct_name').text
#         price = comp.find('span',class_ = 'price').text
#         image = 'https://enter.kg' + comp.find('img').get('src')
#         dict_ = {'title':title,'price':price,'image':image}
    
#         write_to_csv(dict_)

# print(get_data(get_html(URL)))