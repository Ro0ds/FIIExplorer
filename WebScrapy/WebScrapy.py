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
fii_current_price = soup.find(class_='headerTicker__content__price').find('p').getText()
fii_current_percent = soup.find(class_='headerTicker__content__price').find('span').getText().replace(',', '.')


lista = []
count = 0

for div in soup.find(class_='basicInformation__grid').find_all(class_='basicInformation__grid__box'):
    if count == 0:
        
        fii_title = div.b.getText()
    elif count == 4:
        fii_destinated_public = div.b.getText()
    elif count == 5:
        fii_segment = div.b.getText()
    elif count == 6:
        fii_type = div.b.getText()
    elif count == 7:
        fii_issued_shares = div.b.getText()
    elif count == 8:
        fii_number_of_shareholders = div.b.getText()
    count += 1

# fixing , and . on prices
fii_state = ''

if float(fii_current_percent.replace('%', '')) < 0:
    fii_state = 'BAIXA'
else:
    fii_state = 'ALTA'
    
# returning the result
# TODO: return the result as JSON, to use as an API later
print('RAZAO SOCIAL: {}' .format(fii_title))
print('SEGMENTO: {}' .format(fii_segment))
print('PUBLICO ALVO: {}' .format(fii_destinated_public))
print('MANDATO: {}' .format(fii_type))
print('COTAS EMITIDAS: {}' .format(fii_issued_shares))
print('N DE COTISTAS: {}\n' .format(fii_number_of_shareholders))

print('COTACAO ATUAL: {} | {} | {}' .format(fii_current_price, fii_state, fii_current_percent))
print('ULTIMO RENDIMENTO: ')
print('DIVIDEND YIELD: ')
print('RENTABILIDADE NO MES: ')
print('P/VP: \n')

print('>> ULTIMOS 5 MESES <<')
print('DATA DO PAGAMENTO: ')
print('COTACAO: ')
print('VALOR: ')
print('YIELD COTACAO: \n')

print('FII x POUPANCA: ')