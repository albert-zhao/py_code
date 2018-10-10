#! /usr/bin/python3
from subprocess import Popen
from subprocess import PIPE

text = open('messy.html').read()
print(text)
print('----')

tidy = Popen('tidy', stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True)
(stdout_data, stderr_data) = tidy.communicate(input=text)
print(stdout_data)
print('----')
print(stderr_data)
print(tidy.pid)

f = open("nice_html.html", "wt")
f.write(stdout_data)
f.close()
