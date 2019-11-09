#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2019-11-09
# source: https://stackoverflow.com/questions/58780726/remove-elements-from-list-in-python-if-it-contains-in-other-lists
#=================================================================================

"""The elements in the main list should be removed if they are present in either of the other two lists.
Example:
s1 = [1,2,3,4,7]
s2 = [3,4,5,6,20]
mainlist = [6,7,8,9,10,11,12,13,14,15]
resultList = [8,9,10,11,12,13,14,15]
"""

s1 = [1,2,3,4,7]
s2 = [3,4,5,6,20]
mainlist = [6,7,8,9,10,11,12,13,14,15]

for i in mainlist:
    if i in s1 or i in s2:
        mainlist.remove(i)

print(mainlist)
