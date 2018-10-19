#! /usr/bin/python

import urllib2


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
    download('http://httpstat.us/500')