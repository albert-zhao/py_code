#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import fileinput, re

pattern = re.compile('From: (.*) <.*?>$')
for line in fileinput.input():
	m = pattern.match(line)
	if m:
		print(m.group(1))
	

