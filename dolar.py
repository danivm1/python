import requests
from bs4 import BeautifulSoup

link = ("https://dolarhoje.com")
req = requests.get(link)
soup = BeautifulSoup(req.content,'html.parser')
#entrada
valor = float((input('Digite o valor em dolar à ser convertido: ')))


#programacao pesada
real = soup.find_all('input',{'id':'nacional'})

x=str(real)
x=x[41:45]
x=float(x.replace(',','.'))

r = valor * x

#frescura pra saida ficar bonita
r = str(r)
r = r.replace(".",",")
valor = str(valor)
valor = valor.replace(".",",")

#saida
print ("U$ 1,0 hoje vale R$", real[0]['value'])
print ("U$", valor, " hoje vale R$", r)
