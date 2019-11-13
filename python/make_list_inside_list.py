#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2019-11-13
# source: https://stackoverflow.com/questions/58844128/make-a-list-inside-of-a-list-using-loops
#=================================================================================

# Problem
# factorial_list(4) yields [[1], [1, 2], [1, 2, 3], [1, 2, 3, 4]]

def factorial_list(n):
    final_list = []
    for i in range(1, n+1):
        temp = [j for j in range(1, i+1)]
        final_list.append(temp)
    print(final_list)

factorial_list(4)  # [[1], [1, 2], [1, 2, 3], [1, 2, 3, 4]]
