#! /usr/bin/env python3


import urllib.request
import lxml.html


def scrape(html):
    tree = lxml.html.fromstring(html)
    td = tree.cssselect('tr#places_area__row > td.w2p_fw')  # tr id = "places_area__row", td.w2pfw for td class = "w2p_fw", > 代表td.w2p_fw的父标签是 tr#places_neighbours_row
    td1 = td[0]
    print(td)
    print(td1)
    print(type(td))
    print(type(td1))
    area = td1.text_content()
    return area


if __name__ == '__main__':
    html = urllib.request.urlopen('http://example.webscraping.com/places/default/view/United-Kingdom-239').read()
    print(scrape(html))

# <tr id="places_area__row">
#  <td class="w2p_fl">
#   <label class="readonly" for="places_area" id="places_area__label">
#    Area:
#   </label>
#  </td>
#  <td class="w2p_fw">
#   244,820 square kilometres
#  </td>
#  <td class="w2p_fc">
#  </td>
# </tr>
