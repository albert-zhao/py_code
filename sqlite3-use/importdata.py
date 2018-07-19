#! /usr/bin/env python

import sqlite3


def convert(var):
    if var.startswith('~'):
        return var.strip('~')
    if not var:
        var = '0'
    return float(var)


conn = sqlite3.connect('food.db')
curs = conn.cursor()
curs.execute('''
CREATE TABLE food (
id TEXT PRIMARY KEY,
desc TEXT,
water FLOAT,
kcal FLOAT,
protein FLOAT,
fat FLOAT,
ash FLOAT,
carbs FLOAT,
fiber FLOAT,
sugar FLOAT
)
''')
filed_cnt = 10
query = 'INSERT INTO food VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
for line in open('ABBREV.txt'):
    fields = line.split('^')
    vars = [convert(f) for f in fields[:filed_cnt]]
    curs.execute(query, vars)

conn.commit()
conn.close()
