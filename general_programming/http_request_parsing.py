import requests
from bs4 import BeautifulSoup

url= 'https://quotes.toscrape.com/'
data= requests.get(url)
import pdb;pdb.set_trace()

no_line=len(data.content)
soup = BeautifulSoup(data.content, 'html5lib')

result = soup.findAll('div',  attrs={'class':'quote'})
quotes=[]
authors=[]
for i in result:
    quotes.append(i.find('span',attrs={'class':'text'}).text)
    authors.append(i.find('small',attrs={'class':'author'}).text)

print (quotes)
print ('+++++++++++++++++++++++++')
print (authors)
print ('+++++++++++++++++++++++++')


tags= soup.findAll('div', attrs={'class':'col-md-4 tags-box'})
tags=tags[0].findAll('a', attrs={'class':'tag'})
top_10_tags=[]
for i in tags:
    top_10_tags.append(i.text)
print (top_10_tags)
print ('+++++++++++++++++++++++++')

pdb.set_trace()
unique_author = set()
for i in range(1,11):
    pages = url+'/page/'+str(i)+'/'
    page_data = requests.get(pages)
    data = BeautifulSoup(page_data.content, 'html5lib')
    result = data.findAll('div',  attrs={'class':'quote'})
    for x in result:
        unique_author.add(x.find('small',attrs={'class':'author'}).text)

print (unique_author)
