#! /usr/bin/python3

from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)


parser = MyHTMLParser()
parser.feed('<html><head><title>Test</title></head>'
            '<body><h1>Parse me!</h1></body></html>')

# log:
# zxl@pc-zxl:~/Work/py_code/html_parse$ ./html_parse_simple.py 
# Encountered a start tag: html
# Encountered a start tag: head
# Encountered a start tag: title
# Encountered some data  : Test
# Encountered an end tag : title
# Encountered an end tag : head
# Encountered a start tag: body
# Encountered a start tag: h1
# Encountered some data  : Parse me!
# Encountered an end tag : h1
# Encountered an end tag : body
# Encountered an end tag : html
# zxl@pc-zxl:~/Work/py_code/html_parse$ 