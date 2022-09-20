        
from email import header
from itertools import product
import requests
from bs4 import BeautifulSoup
from csv import writer
from urllib.request import urlopen




productlinks = []

for x in range (1, 7):
    r = requests.get(f'https://www.spellenrijk.nl/categorie/83/trading-cards.html?ft11=Pokemon&page=1{x}')
    soup = BeautifulSoup(r.content, 'lxml')

    productlist = soup.find_all('h3', class_='productlist-title gtm-product-impression')


    for item in productlist:
        for link in item.find_all('a', href=True):
            # print(link['href'])
            productlinks.append(link['href'])     


        
    with open('scrapeimg-notenenchocola.csv', 'w', encoding='utf-8-sig', newline='') as f:
        thewriter = writer(f)
        header = ['img']
        thewriter.writerow(header)
        for item in productlist:
            for link in item.find_all('a', href=True):
                # print(link['href'])
                productlinks.append(link['href'])
                

            
                htmldata = urlopen(link['href'])
                soup = BeautifulSoup(htmldata, 'html.parser')
                images = soup.find_all('img', itemprop="image") 

                


                for item in images:
                    img = item['data-src']
                    info = [img]
                    thewriter.writerow(info)
                    print(len(img))
