#! /usr/bin/env python3

import cgi
import cgitb; cgitb.enable()

#form = cgi.FieldStorage()
#name = form['name'].value
form = cgi.FieldStorage()
name = form.getvalue('name', 'nonono')

print('Content-type: text/plain\n')
print('Hello, {}!'.format(name))

# 开启web服务器: python3 -m http.server --cgi
#
#
#log:
#http://127.0.0.1:8000/cgi-bin/parse_input.cgi?name=Gumby&age=42
#Hello, Gumby!
#
#
#http://127.0.0.1:8000/cgi-bin/parse_input.cgi
#Hello, nonono!
#
#>>> fo=urllib.request.urlopen('http://127.0.0.1:8000/cgi-bin/parse_input.cgi/?' + urllib.parse.urlencode({'age': '42', 'name': 'Gumby'}))
#>>> fo.read().decode()
#'Hello, Gumby!\n'

