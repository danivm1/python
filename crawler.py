import requests
from bs4 import BeautifulSoup

link = 'https://www.dafiti.com.br/roupas-femininas/'
req = requests.get(link)
soup = BeautifulSoup(req.content,'html.parser')

item = soup.find_all('div',{'class':'product-box-brand'})

for i in item:
	print(i.text)