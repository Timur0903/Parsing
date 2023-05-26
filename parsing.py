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