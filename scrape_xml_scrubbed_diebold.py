import requests
from bs4 import BeautifulSoup
import pprint

with open('scrubbed_diebold.XML') as xmlfile:
    xmlstring = xmlfile.read()
soup = BeautifulSoup(xmlstring, 'xml')
print(soup.select('TotalDeductionAmt'))

