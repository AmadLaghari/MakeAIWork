from bs4 import BeautifulSoup

import requests
baseurl = 'www.bol.com'
productlinks = []

for x in range (1, 500):
    r = requests.get(f'https://www.bol.com/nl/nl/l/muziek-op-cd-s/54479/?page={x}')
    soup = BeautifulSoup(r.content, 'lxml')
    productlist = soup.find_all('div', class_="product-item__content")
    for item in productlist:
        for link in item.find_all('a', href=True):
            productlinks.append(baseurl + link['href'])

print(productlinks)
            



# def getdata(url):
#     r = requests.get(url)
#     return r.text

# htmldata = getdata(url)
# soup = BeautifulSoup(htmldata, 'html.parser')

# imgdata = []
# for i in soup.find_all('img', itemprop="image" ):
#     imgdata.append(i['src']) # made a change here so its appendig to the list
#     print(imgdata)


# #Pillow
# #matplotlib-venn
# #numpy
# #ptpython
# #scipy
# #SimPyLC == 3.10.0
# #sonar

# #pillow
# #pandas
# #matplotlip



