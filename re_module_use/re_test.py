#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import fileinput

for line in fileinput.input(files=("data_test_fileinput.txt",)):
	print(type(line))
	print(len(line))    
	if not line.isspace():
		print(line.strip())
