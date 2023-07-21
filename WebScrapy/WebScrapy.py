# Imports and Modules
import requests

from os import system
from bs4 import BeautifulSoup
from Entities import ScrapInfo
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
fii_current_price = soup.find(class_='headerTicker__content__price').find('p').getText()
fii_current_percent = soup.find(class_='headerTicker__content__price').find('span').getText().replace(',', '.')

basic_information = ScrapInfo.FundInformation()
indicator_information = ScrapInfo.FundInformation()

fii_basic_information = basic_information.get_information_from_web(soup.find(class_='basicInformation__grid').find_all(class_='basicInformation__grid__box'))
fii_indicator_information = indicator_information.get_information_from_web(soup.find(class_='indicators historic', id='indicators').find_all(class_='indicators__box'))

# fixing , and . on prices
fii_state = ''

if float(fii_current_percent.replace('%', '')) < 0:
    fii_state = 'BAIXA'
else:
    fii_state = 'ALTA'
    
# returning the result
# TODO: return the result as JSON, to use as an API later
print('COTACAO ATUAL: {} | {} | {}\n' .format(fii_current_price.replace(' ', ''), fii_state, fii_current_percent))

for information_value in fii_basic_information:
    for information_name in information_value:
        print('{}: {}' .format(information_name, information_value[information_name]))

print('\n>> ULTIMOS 5 MESES <<')
print('DATA DO PAGAMENTO: ')
print('COTACAO: ')
print('VALOR: ')
print('YIELD COTACAO: \n')

print('FII x POUPANCA: ')