#! /usr/bin/env python3
# -*- coding: utf-8  -*-
import re, fileinput

field_pat = re.compile(r"\[(.+?)\]")
text = ''

nspace = {}
def replacement(match_obj):
	code = match_obj.group(1)
	try:
		return str(eval(code, nspace))
	except SyntaxError:
		exec(code, nspace)
		return ''

for line in fileinput.input():
	text += line

#print(text)

print(field_pat.sub(replacement, ''.join(text)))

