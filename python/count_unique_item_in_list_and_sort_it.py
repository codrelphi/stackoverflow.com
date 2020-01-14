#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2020-01-14
# source: the post is deleted
#=================================================================================
the_list = ['Antonia', 'Sara', 'Nick', 'Deppy', 'Antonia', 'Deppy', 'Antonia']

# count unique item in the list 'the_list'
for item in set(the_list):
    print(item, ':', the_list.count(item))

# an ordered new list containing unique item of 'the_list'
new_list = sorted([item for item in set(the_list)])
print(new_list)
"""
> **Outputs:**

    Nick : 1
    Antonia : 3
    Sara : 1
    Deppy : 2

    ['Antonia', 'Deppy', 'Nick', 'Sara']

"""
