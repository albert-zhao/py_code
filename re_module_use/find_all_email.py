#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import fileinput, re

addrs = set()
pattern = re.compile(r'[a-z\-\.]+@[a-z\-\.]+', re.IGNORECASE)

for line in fileinput.input():
	for addr in pattern.findall(line):
		addrs.add(addr)

for address in addrs:
	print(address)
   
	

