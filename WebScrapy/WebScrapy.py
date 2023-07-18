# Imports and Modules
import requests

from os import system
from bs4 import BeautifulSoup
from Filters import html_tags

# Main Program
print('>> Verificador simples de FIIs <<\n')

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600'
    }

fii_name = input('Nome do FII (exemplo: hglg11): ')

# Getting all infos from fundsexplorer.com based on users fii choice
url = 'https://www.fundsexplorer.com.br/funds/' + fii_name.lower()
req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'html.parser')

system('cls')

# Grouping relevant infos
title = str(soup.title)

fii_current_price = soup.find(class_='headerTicker__content__price').find('p').getText()

fii_current_percent = soup.find(class_='headerTicker__content__price').find('span').getText().replace(',', '.')


# fixing , and . on prices
fii_state = ''

if float(fii_current_percent.replace('%', '')) < 0:
    fii_state = 'Baixa'
else:
    fii_state = 'Alta'
    
# returning the result
# TODO: return the result as JSON, to use as an API later
print('FII: {}' .format(html_tags.remove_html_tags(title, 'title')))
print('Preco atual: {} em {} de {}\n' .format(fii_current_price, fii_state, fii_current_percent))
