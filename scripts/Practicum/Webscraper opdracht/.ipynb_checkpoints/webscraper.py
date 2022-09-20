from email import header
from itertools import product
from unicodedata import category
import requests
from bs4 import BeautifulSoup
from csv import writer
from urllib.request import urlopen

# loginurl = ('https://www.sanisupply.nl/account/login/')
# secureurl = ('https://www.sanisupply.nl/collection/page{x}.html')
# payload = {
#         "email":  "davincitegels@gmail.com",
#         "password": "arnhemarnhem"
# }


# with requests.session() as s:
#     s.post('login', data=payload)
#     r = s.get(secureurl)




headers = {
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36'
}

productlinks = []

for x in range (1, 47):
    r = requests.get(f'https://www.sanisupply.nl/collection/page{x}.html')
    soup = BeautifulSoup(r.content, 'lxml')


    productlist = soup.find_all('h3', class_='item-name')

    for item in productlist:
        for link in item.find_all('a', href=True):
            # print(link['href'])
            productlinks.append(link['href'])
print(len(productlinks))
  
# # productlinks = "https://www.sanisupply.nl/aktieset-badmeubel-pl-greeploos-60-hoogglans-wit.html"

# with open('titl.csv', 'w', encoding='utf-8-sig', newline='') as f:
#     thewriter = writer(f)
#     header = ['title', 'code', 'image_url1,' 'image_url', 'specs']
#     thewriter.writerow(header)
#     for link in productlinks:
#         r = requests.get(link)
#         soup = BeautifulSoup(r.content, 'lxml')

#         title = soup.find('span', itemprop='name').text.strip()
#         code = soup.find('div', class_="code").text.strip()
#         cat = soup.find('ul', class_="breadcrumb").text.strip()

#         specs = []
#         spec = soup.find('ul', class_="product-details-list")
#         for sp in spec:
#             specs.append(sp.text.strip())

#         htmldata = urlopen(link)
#         soup = BeautifulSoup(htmldata, 'html.parser')




#         images = soup.find_all('a', class_='fancybox-thumb')
#         image_url = []
#         for item in images:
#             # print(item['href'])
#             image_url.append(item['href'])

#         image_main = images = soup.find_all('img', class_="img-responsive featured")
#         image_url1 = []
#         for item in images:
#             img = item['src']
#             image_url1.append(img)



#         productAtt = {
#             'title' : title,
#             'code': code,
#             'image_url1' : image_url1,
#             'image_url' : image_url,
#             'specs': specs
#         }
#         info = [title, code, image_url1, image_url, specs]
#         thewriter.writerow(info)
#         print(title)







 