#! /usr/bin/python3

from urllib.request import urlopen
import re


def scrape(html):
    #area = re.findall('<tr id="places_area__row">.*?<td\s*class=["\']w2p_fw["\']>(.*?)</td>', html)
    area = re.findall('<td\s*class=["\']w2p_fw["\']>(.*?)</td>', html)[1]
    return area


if __name__ == '__main__':
    html = urlopen('http://example.webscraping.com/places/default/view/United-Kingdom-239').read().decode()
    # print(html)
    print(scrape(html))
