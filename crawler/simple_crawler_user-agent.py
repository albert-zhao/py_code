#! /usr/bin/python

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


if __name__ == '__main__':
    download('http://www.meetup.com')