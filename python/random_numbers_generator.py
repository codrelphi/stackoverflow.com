#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2019-12-01
# source: https://stackoverflow.com/questions/59128392/random-numbers-exercise
#=================================================================================

import random

def rolldies(n):
    result = []
    for i in range(n):
        number = random.randrange(1, 6)
        result.append(number)
    return sorted(result)


print(rolldies(3)) # display [3, 4, 5] for example
