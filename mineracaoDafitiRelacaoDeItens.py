import requests
from bs4 import BeautifulSoup

req = requests.get('https://www.dafiti.com.br/calcados-masculinos/')
soup = BeautifulSoup(req.content,'html.parser')

# print(soup)

valorItem = soup.find_all('span',{'class':'product-box-price-from'}) 
nomeItem = soup.find_all('div',{'class':'product-box-brand'})

tam=(len(valorItem))

for i in range(tam):
    print(nomeItem[i].text, ' = ',valorItem[i].text)
