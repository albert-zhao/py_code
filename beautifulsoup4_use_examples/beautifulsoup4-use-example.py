#! /usr/bin/env python3

from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html, 'lxml')
print(soup.a) # 不需要是soup的子也可是孙子，纯孙子
print('------\n')

# contents 和 .children 属性仅包含tag的直接子节点，
# .descendants 属性可以对所有tag的子孙节点进行递归循环，和 children类似，我们也需要遍历获取其中的内容。
print(soup.head.contents)
print('------\n')
print(soup.head.contents[0])
print('------\n')
print(soup.head.children)
print('------\n')


for child in soup.body.children:
    print(child)
    print('------')

for child in soup.descendants:
    print(child)
    print('=====')

print(soup.body.p('b'))