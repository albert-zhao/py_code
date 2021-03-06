#! /usr/bin/python

import re
import urlparse
import urllib2
import time
from datetime import datetime
import robotparser
import Queue


def download(url, user_agent='wswp', proxy=None, num_retries = 2):
    print 'Downloading:', url
    headers = {'User-agent': user_agent}
    request = urllib2.Request(url, headers=headers)
    opener = urllib2.build_opener()
    if proxy:
        proxy_params = {urlparse.urlparse(url).scheme: proxy}
        opener.add_handler(urllib2.ProxyHandler(proxy_params))
    try:
        html = opener.open(request).read()
    except urllib2.URLError as e:
        print 'Download error:', e.reason
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # retry SXX HTTP errors
                html = download(url, user_agent, proxy, num_retries - 1)

    return html


if __name__ == '__main__':
    html = download('http://example.webscraping.com', proxy='http://www.baidu.com')
