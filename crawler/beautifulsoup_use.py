#! /usr/bin/env python3

from bs4 import BeautifulSoup

html = '<ul class = country><li>Area<li>Population</ul>'
soup = BeautifulSoup(html, 'html.parser') # html is markup, which can be string or file-like object, html or html.encode are all ok
fixed_html = soup.prettify()
print(fixed_html)
ul = soup.find('ul', attrs={'class': 'country'})
print(ul)
ul = soup.find('ul')
print(ul)
li = soup.find('li')
print(li)
li = soup.find_all('li')
print(li)
li = soup.find_all('li', limit=1)
print(li)