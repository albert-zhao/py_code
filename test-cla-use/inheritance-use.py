#! /usr/bin/env python3
# -*- coding: utf-8 -*- 
class Filter:
    def init(self):
        self.blocked = []
    def filter(self, seq):
        return [x for x in seq if x not in self.blocked]

class SpamFilter(Filter):
    def init(self):
        self.blocked = ['SPAM']

f = SpamFilter()
f.init()
print(f.filter(['SPAM', 'SPAM', 'hello', 'world']))

print(issubclass(SpamFilter, Filter))

print(issubclass(Filter, SpamFilter))

print(SpamFilter.__bases__)
print(Filter.__bases__)

print(isinstance(f, SpamFilter))
print(isinstance(f, Filter))

print(f.__class__)
print(type(f))