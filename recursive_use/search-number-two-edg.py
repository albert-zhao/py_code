#! /usr/bin/env python3
# -*- coding: utf-8 -*-
## [lowe, upper]
def search(seq, number, lower, upper):
    if (upper == lower) and (number == seq[lower]):
        return seq[lower]

    middle = (lower + upper) // 2

    if  seq[lower] <= number <= seq[middle]:
        return search(seq, number, lower, middle)
    elif seq[middle + 1] <= number <= seq[upper]:
        return search(seq, number, middle + 1, upper)
    return -1

## [lowe, upper]
def searchnu(number, lower, upper):
    if (upper == lower) and (lower == number):
        return lower

    middle = (lower + upper) // 2

    if  lower <= number <= middle:
        return searchnu(number, lower, middle)
    elif (middle + 1) <= number <= upper:
        return searchnu(number, middle + 1, upper)
    else:
        return -1

if __name__ == '__main__':
    number = 10
    print(searchnu(number, 1, 100))
    seq = list(range(0, 100))
    print(search(seq, number, 9, 100))