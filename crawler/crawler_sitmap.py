#! /usr/bin/python


import re
import urllib2

def download(url, useragent='wswp', numretries=2):
    print 'Downloading:', url
    headers = {'User-agent': useragent}
    request = urllib2.Request(url, headers=headers)
    try:
        html = urllib2.urlopen(request).read()
    except urllib2.URLError as e:
        print 'Download error : ', e.reason
        html = None
        if numretries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # recursively retry Sxx HTTP errors
                return download(url, useragent, numretries - 1)
    return html


def crawlsitemap(url):
    # download the sitemap file
    sitemap = download(url)
    # print 'sitemap:', sitemap
    # extract the sitemap links
    links = re.findall('<loc>(.*?)</loc>', sitemap)
    # print 'links: ', links
    # download each link
    for link in links:
        print 'site:', link
        html = download(link)
        # scrape html here
        # ...



if __name__ == '__main__':
    crawlsitemap('http://example.webscraping.com/sitemap.xml')


# site is like that 'http://example.webscraping.com/places/default/view/Afghanistan-1'