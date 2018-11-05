from bs4 import BeautifulSoup

html = '<ul class = country><li>Area<li>Population</ul>'
soup = BeautifulSoup(html, 'html.parser')
fixed_html = soup.prettify()
print(fixed_html)
soup.find() ## how to use find