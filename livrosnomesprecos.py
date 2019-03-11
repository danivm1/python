import requests
from bs4 import BeautifulSoup
'''
for a in range(0,2):
    if (a==0):
        link = ('https://busca.saraiva.com.br/busca?q=python&page=1')
    else:
        link = ('https://busca.saraiva.com.br/busca?q=python&page=2')'''

req = requests.get('https://busca.saraiva.com.br/busca?q=python&page=1')
soup = BeautifulSoup(req.content,'html.parser')


nomeLivro = soup.find_all('a',{'class':'details'}) 
valorLivro = soup.find_all('div',{'class':'nm-price-value'})

tam=(len(valorLivro))

for i in range(tam):
    print(nomeLivro[i].text, ' = ',valorLivro[i].text)
