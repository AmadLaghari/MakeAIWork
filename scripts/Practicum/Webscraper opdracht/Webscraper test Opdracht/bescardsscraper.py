from email import header
from itertools import product
import requests
from bs4 import BeautifulSoup
from csv import writer



baseurl = 'https://www.bescards.nl/'

headers = {
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36'
}

productlinks = []

for x in range (1, 3):
    r = requests.get(f'https://www.bescards.nl/pokemon-blister/page/{x}')
    soup = BeautifulSoup(r.content, 'lxml')

    productlist = soup.find_all('h3', class_='wd-entities-title')


    for item in productlist:
        for link in item.find_all('a', href=True):
            # print(link['href'])
            productlinks.append(link['href'])
        
        
# testlink = "https://wereldkruiden.com/home/395-1021-draaigember-tea.html#/37-hoeveelheid-100_gram"
with open('bescardswc1.csv', 'w', encoding='utf-8-sig', newline='') as f:
    thewriter = writer(f)
    header = ['Title', 'oldPrice' 'newprice', 'category']
    thewriter.writerow(header)
    for link in productlinks:
        r = requests.get(link)
        soup = BeautifulSoup(r.content, 'lxml')
        try: 
            title = soup.find('h1', class_="product_title entry-title wd-entities-title").text.strip()
        except:
            title = soup.find('h1', class_="product_title entry-title wd-entities-title").text.strip()
        price = soup.find('span', class_="price").text.strip()
        category = "Pokémon Blister"
        # description = soup.find('div', class_="product-description-short").text.strip()
        # longDescription = soup.find('div', class_="product-description").text.strip()
        # img = soup.find('img', class_='js-qv-product-cover')
        # theekruiden = {
        #     'title' : title,
        #     'price' : price,
        #     'description' : description,
        #     'longDescription' : longDescription,
        #     'img': img
        # }
        info = [title, price, category]
        thewriter.writerow(info)
        print(title)