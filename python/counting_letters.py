#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2019-10-25
# source: https://stackoverflow.com/questions/58550800/adding-the-amount-of-letters-there-are-in-a-string-in-python
#=================================================================================

# Method 3: using a list comprehensions
def countingletters(st):
    return len([i for i in st if i.isalpha()])

# test
print(countingletters("a12a")) # display 2

"""
# Method 2: using a counter
def countingletters(st):
    cpt = 0 # the counter
    for i in st:
        if i.isalpha():
            cpt += 1
    return cpt


# test
print(countingletters("a12a")) # display 2
"""

"""
# Method 1: using a list
def countingletters(st):
    empty = []
    for i in st:
        if i.isalpha():
             empty += str(i)

    return len(empty)

# test
print(countingletters("a12a")) # display 2
"""
