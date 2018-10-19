#! /usr/bin/env python3

from urllib.request import urlopen
from bs4 import BeautifulSoup

# text = urlopen('http://python.org/jobs').read().decode()
text = urlopen('http://python.org/jobs').read()

# Python的内置标准库html.parser 解析器 BeautifulSoup(markup, “html.parser”)
# lxml HTML 解析器 	BeautifulSoup(markup, “lxml”)
# lxml XML 解析器 	BeautifulSoup(markup, [“lxml”, “xml”])BeautifulSoup(markup, “xml”) 	
# html5lib 解析器	BeautifulSoup(markup, “html5lib”)
# lxml 解析器更加强大，速度更快，推荐安装。

# soup = BeautifulSoup(text, 'html.parser')# markup can be bytes or string or file-like objects
soup = BeautifulSoup(text, 'lxml')# markup can be bytes or string or file-like objects
jobs = set()
print(soup.name)
print(soup.attrs)
for job in soup.body.section('h2'): # soup.body.section('h2') is a list
    jobs.add('{} ({})'.format(job.a.string, job.a['href']))
print('\n'.join(sorted(jobs, key=str.lower))) # ascending order