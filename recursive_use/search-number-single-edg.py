#! /usr/bin/env python3
# -*- coding: utf-8 -*-
## [lowe, upper)
def search(seq, number, lower, upper):
    if (upper - lower) == 1 and seq[lower] == number:
        return seq[lower]

    middle = (lower + upper) // 2

    if  seq[lower] <= number < seq[middle]:
        return search(seq, number, lower, middle)
    elif seq[middle] <= number < seq[upper]:
        return search(seq, number, middle, upper)
    return -1

## [lowe, upper)
def searchnu(number, lower, upper):
    if (upper - lower) == 1 and lower == number:
        return lower

    middle = (lower + upper) // 2

    if  lower <= number < middle:
        return searchnu(number, lower, middle)
    else:
        return searchnu(number, middle, upper)

if __name__ == '__main__':
    number = 10
    print(searchnu(number, 1, 100))
    seq = list(range(0, 100))
    print(search(seq, number, 11, 100))
 