import requests
from bs4 import BeautifulSoup
import pprint # solo para presentar la info del dictionary resultado en el terminal

res = requests.get('https://news.ycombinator.com/news/')
# agrego una pagina (website paginado) y cuantas quiera solos las concateno al final y envio toda la data junta
res2 = requests.get('https://news.ycombinator.com/news?p=2') 

# from website, take html as a text or string and parse it.
# en este caso es un html pero la librery tambien cuenta con xml parser
# doc: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')
# print(soup.body.contents)
# puedo filtrar las tags div y los devuelve en una lista de tags (todos los divs)
# print(soup.find_all('div'))
# tambien puedo filtrar por el atriuto id por ejemplo
# print(soup.find(id='score_23821648'))
# soup como (css selectors) que permite obtener la data de un tipo o clase css
# por ejemplo tomo todas las span class="score":
# print(soup.select('.score'))
# tomo el primer elemento de los articulos de la pagina
# print(soup.select('.storylink')[0])
links = soup.select('.storylink')
subtext = soup.select('.subtext')

links2 = soup2.select('.storylink')
subtext2 = soup2.select('.subtext')

mega_links = links + links2
mega_subtext = subtext + subtext2

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key= lambda k:k['votes'], reverse=True)

def create_custom_hn(links, subtext):
    hn = [] # hacker news
    for idx, item in enumerate(links): #enumerate para tener ambos, links y subtexts
        title = item.getText()
        href = item.get('href')
        vote = subtext[idx].select('.score')
        if len(vote):
            #points = votes[idx].getText()
            points = int(vote[0].getText().replace(' points', ''))
            # print(points)
            if points > 99:
                #genera un dictionary con la data q quiero.
                hn.append({'title': title, 'link': href, 'votes': points}) 
    return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(mega_links,mega_subtext))
