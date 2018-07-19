#! /usr/bin/env python3
# -*- coding: utf-8 -*-
## [lowe, upper]
def search(seq, number, lower, upper):
    middle = (lower + upper) // 2

    if seq[lower] == number:
        return seq[lower]
    if  seq[lower] < number < seq[middle]:
        return search(seq, number, lower, middle)
    elif seq[middle] == number:
        return seq[middle]
    elif seq[middle + 1] == number:
        return seq[number + 1]
    elif seq[middle + 1] < number < seq[upper]:
        return search(seq, number, middle + 1, upper)
    elif seq[upper] == number:
        return seq[upper]
    else:
        return -1

## [lowe, upper]
def searchnu(number, lower, upper):
    middle = (lower + upper) // 2

    if  lower == number:
        return lower
    elif lower < number < middle:
        return searchnu(number, lower, middle)
    elif middle == number:
        return middle
    elif (middle + 1) == number:
        return middle + 1
    elif middle  < number < upper:
        return searchnu(number, middle, upper)
    elif upper == number:
        return upper
    else:
        return -1

### errors: maximum recursion depth exceeded when (upper - lower) is two large
if __name__ == '__main__':
    number = 23
    print(searchnu(number, 1, 100))
    seq = list(range(0, 100))[1::2]
    print(search(seq, number, 10, 40))