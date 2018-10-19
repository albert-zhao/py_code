#! /usr/bin/python


import re
import urllib2


def link_crawler(seed_url, link_regex):
    """Crawl from the given seed URL following links matched by link_regex
    """
    crawl_queue = [seed_url]  # the queue of URL's to download
    while crawl_queue:
        url = crawl_queue.pop()
        html = download(url)
        # filter for links matching our regular expression
        for link in get_links(html):
            if re.match(link_regex, link):
                # add this link to the crawl queue
                crawl_queue.append(seed_url + link)


def get_links(html):
    """Return a list of links from html 
    """
    if html is None:
        return []
    # a regular expression to extract all links from the webpage
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    # list of all links from the webpage
    return webpage_regex.findall(html)


def download(url, numretries=2):
    print 'Downloading:', url
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print 'Download error : ', e.reason
        html = None
        if numretries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # recursively retry Sxx HTTP errors
                return download(url, numretries - 1)
    return html


if __name__ == '__main__':
    link_crawler('http://example.webscraping.com', '/places/default/(index|view)')


# urlib2 useragent ---> User-Agent: Python-urllib/2.7
