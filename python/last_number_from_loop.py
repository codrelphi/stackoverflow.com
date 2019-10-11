#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2019-10-11
# source: https://stackoverflow.com/questions/58342215/getting-the-last-number-from-a-for-loop/58342301
#=================================================================================

# use a list
def LCM(minN,maxN):
    count = 1
    results = []
    for i in range(count,(maxN*count)+1):
        results.append(minN*count)
        count = count + 1
    print(results[-1]) # print the last elements of the list.


LCM(5, 7) # print 35.
