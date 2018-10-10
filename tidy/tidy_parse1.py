#! /usr/bin/python3
from subprocess import Popen
from subprocess import PIPE

text = open('messy.html').read()
print(text)
print('----')

tidy = Popen('tidy', stdin=PIPE, stdout=PIPE, stderr=PIPE)
(stdout_data, stderr_data) = tidy.communicate(input=text.encode())
print(stdout_data.decode())
print('----')
print(stderr_data.decode())
print(tidy.pid)
