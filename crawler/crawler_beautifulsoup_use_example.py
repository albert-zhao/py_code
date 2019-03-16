#! /usr/bin/env python3

# -*- coding: utf-8 -*-

import urllib
from bs4 import BeautifulSoup


def scrape(html):
    soup = BeautifulSoup(html, 'html.parser')
    print(type(soup))
    tr = soup.find(attrs={'id': 'places_area__row'})  # locate the area row
    print(type(tr))
    print('tr:')
    print(tr.prettify())
    # 'class' is a special python attribute so instead 'class_' is used
    td = tr.find(attrs={'class': 'w2p_fw'})  # locate the area tag
    print(type(td))
    print('td:')
    print(td.prettify())
    area = td.text  # extract the area contents from this tag
    print(type(area), area)
    name = td.name
    print(type(name), name)
    attrs = td.attrs
    print(type(attrs), td.attrs)
    return area


if __name__ == '__main__':
    html = urllib.request.urlopen('http://example.webscraping.com/places/default/view/United-Kingdom-239').read()
    print(scrape(html))
