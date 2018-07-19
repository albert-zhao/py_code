#! /usr/bin/env python3


from xmlrpc.client import ServerProxy
# If the target part and the slash preceding it are both omitted,
# "/RPC2" is assumed
# http://localhost:8000 equal to http://localhost:8000/RPC2
s = ServerProxy('http://localhost:8000/RPC1')
print(s.pow(2, 3))
print(s.add(2, 3))
# print(s.div(5, 2))

print(s.system.listMethods())