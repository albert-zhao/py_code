#! /usr/bin/env python3

import cgitb; cgitb.enable()


print('Content-type: text/plain')
print(1/0)
print('Hello, world!')
