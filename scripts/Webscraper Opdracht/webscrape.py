from email import header
from itertools import product
import requests
from bs4 import BeautifulSoup
from csv import writer

key =  '9b32bd97a1613ad18d264aabd5f5aa2e'
email = "info@samipuur.nl"
password = "Nuaym0640948374!"
loginurl = ("https://www.sanisupply.nl/account/loginPost/")





baseurl = 'https://www.sanisupply.nl'

headers = {
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36'
}

productlinks = []

for x in range (1, 6):
    r = requests.get(f'https://www.sanisupply.nl/collection/page{x}.html')
    soup = BeautifulSoup(r.content, 'lxml')


    productlist = soup.find_all('h3', class_="item-name")

    for item in productlist:
        for link in item.find_all('a', href=True):
            # print(link['href'])
            productlinks.append(link['href'])

# productlinks = "https://www.bescards.nl/sword-shield-5-premium-checklane-blister/"

with open('scrapeme.csv', 'w', encoding='utf-8-sig', newline='') as f:
    thewriter = writer(f)
    header = ['Title', 'Price']
    thewriter.writerow(header)
    for link in productlinks:
        r = requests.get(link)
        soup = BeautifulSoup(r.content, 'lxml')
        title = soup.find('h1',class_='product-name').text.strip()
        # price = soup.find('span', class_="product-price-amount").text.strip()


        productAtt = {
            # 'title' : title,
            # 'price' : price,
            'title' : title,
        }
        info = [title]
        thewriter.writerow(info)
        print("title ", title)







 