#! /usr/bin/python


import itertools
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


max_errors = 5
num_errors = 0
if __name__ == '__main__':
    for page in itertools.count(1):
        url = 'http://example.webscraping.com/view/-%d' % page
        html = download(url)
        if html is None:  # 404 not found
            num_errors += 1
            if num_errors == max_errors:
                break
        else:
            # success - can scrape the result
            num_errors = 0
            print 'ok'


# log:
# Downloading: http://example.webscraping.com/view/-1
# ok
# Downloading: http://example.webscraping.com/view/-2
# ok
# Downloading: http://example.webscraping.com/view/-3
# ok
# Downloading: http://example.webscraping.com/view/-4
# ok
# Downloading: http://example.webscraping.com/view/-5
# ok
# Downloading: http://example.webscraping.com/view/-6
# ok
# Downloading: http://example.webscraping.com/view/-7
# ok
# Downloading: http://example.webscraping.com/view/-8
# ok
# Downloading: http://example.webscraping.com/view/-9
# ok
# Downloading: http://example.webscraping.com/view/-10
# ok
# Downloading: http://example.webscraping.com/view/-11
# ok
# Downloading: http://example.webscraping.com/view/-12
# Download error :  TOO MANY REQUESTS

# GET /view/-12 HTTP/1.1
# Accept-Encoding: identity
# Host: example.webscraping.com
# Connection: close
# User-Agent: wswp

# HTTP/1.1 429 TOO MANY REQUESTS
# Server: nginx
# Date: Mon, 15 Oct 2018 03:54:36 GMT
# Content-Type: text/html; charset=UTF-8
# Content-Length: 22
# Connection: close
# Set-Cookie: session_id_places=223.95.81.141-625269ad-fdc3-41b3-8a6d-bb0a00a123fe; httponly; Path=/

# IP temporarily blocked