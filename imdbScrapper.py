import requests
from bs4 import BeautifulSoup

URL = input("Enter imdb url :")

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:68.0) Gecko/20100101 Firefox/68.0'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.select('.title_wrapper h1')[0].get_text()

rating = soup.find('span', {'itemprop': 'ratingValue'}).get_text()

genere = []
generes = soup.select('.title_wrapper .subtext a')
for item in generes:
    genere.append(item.get_text())
del genere[-1]

summery = soup.select('.summary_text')[0].get_text().strip()

plot = soup.select('div.inline:nth-child(3) > p:nth-child(1) > span:nth-child(1)')[0].get_text().strip()

imageUrl = soup.select('.poster > a:nth-child(1) > img:nth-child(1)')[0]['src']

print("\nTitle :", title)
for i in genere:
    print(i, end=", ")
print("\nImdb Rating :", rating)
print("\nsummery")
print("---------------------")
print(summery)
print("\nStoryline")
print(".....................")
print (plot,'\n')
print("Poster :", imageUrl)

