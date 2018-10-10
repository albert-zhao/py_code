#! /usr/bin/python3
from subprocess import Popen
from subprocess import PIPE

text = open('messy.html').read()
print(text)
print('----')

tidy = Popen('tidy', stdin=PIPE, stdout=PIPE, stderr=PIPE)
# if universal_newlines is False the file objects stdin, stdout and stderr
# will be opened as binary streams, and no line ending conversion is done.
print(tidy.stdin.write(text.encode()))  # must be text.encode(),cause universal_newlines=False
tidy.stdin.close()

print('----')
print(tidy.stdout.read().decode())
# print(tidy.stdout.read())
tidy.stdout.close()

print('----')
print(tidy.stderr.read().decode())
tidy.stderr.close()
