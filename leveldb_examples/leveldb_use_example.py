#! /usr/bin/python3


import leveldb


db = leveldb.LevelDB('./DB')

db.Put('hello'.encode(), '3'.encode())
print(db.Get('hello'.encode()))

db.Delete('hello'.encode())

for i in range(10):
    db.Put(str(i).encode(), 'string_{}'.format(i).encode())

list(db.RangeIter(key_from='2'.encode(), key_to='5'.encode()))


for i in range(1000):
    db.Put(str(i).encode(), 'string_{}'.format(i).encode())

batch = leveldb.WriteBatch()
db.Write(batch, sync=True)

for i in range(2000):
    db.Put(str(i).encode(), 'string_{}'.format(i).encode())

db.Write(batch, sync=True)
