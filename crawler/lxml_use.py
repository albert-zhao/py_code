#! /usr/bin/python3
import lxml.html


broken_html = '<ul class = country><li>Area<li>Population</ul>'
tree = lxml.html.fromstring(broken_html)  # from string to tree
print(tree)
print(broken_html)
fixed_html = lxml.html.tostring(tree, pretty_print=True)
print(fixed_html.decode())
