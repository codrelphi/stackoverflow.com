#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2019-10-06
# source: https://stackoverflow.com/questions/58261217/error-inputting-array-element-into-recursive-function/
#=================================================================================

import numpy as np

rand_10 = np.random.randint(100,500,10, dtype=np.int64)

def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)

x = rand_10[0].item()   # method item() to convert the value into a native Python type
print(fact(x))
