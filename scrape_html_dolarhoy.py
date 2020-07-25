import requests
from bs4 import BeautifulSoup
import pprint # solo para presentar la info del dictionary resultado en el terminal

# resDolarHoy = requests.get('https://www.dolarhoy.com/')
resDolarOficial = requests.get('https://www.dolarhoy.com/cotizaciondolaroficial')
resDolarBlue = requests.get('https://www.dolarhoy.com/cotizaciondolarblue')

# soupDolarHoy = BeautifulSoup(resDolarHoy.text, 'html.parser')
soupDolarOficial = BeautifulSoup(resDolarOficial.text, 'html.parser')
soupDolarBlue = BeautifulSoup(resDolarBlue.text, 'html.parser')

print('***** Dolar Oficial *****')
for info in soupDolarOficial.select('.pull-left'):
    print(info.text)
print('***** Dolar Blue *****')
for info in soupDolarBlue.select('.pull-left'):
    print(info.text)

