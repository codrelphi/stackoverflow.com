#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2020-01-07
# source: https://stackoverflow.com/questions/59624974/if-function-doesnt-return-anything-in-python
#=================================================================================
"""
Your function returns the year. So you have to print the result of the function calls.
To do that, just replace the following lines:

century(1601)
century(58)
century(356)

by these lines:

print(century(1601))   # 2
print(century(58))     # 1
print(century(356))    # 57
"""

def century(year):
    year = str(year)
    if len(year) == 4: # check if year is 4 digits
        if year[2:] == '00': # if year ends with 00
           year = (year[:2]) # return first 2 numbers out of year
           return year
        else:
           year = (int(year[2:]) + 1) # if year doesnt end with 00 add 1 to the first 2 digits
           return year
    elif len(year) == 3: # check if year is 3 digits
        if year[2:] == '00':
            year = (year[1:]) # if year ends with 00 return first digit
            return year
        else:
            year = (int(year[1:]) + 1) # return first digit plus 1
            return year
    else:
        year = 1 # return 1 if year is less than 2 digits
        return year


print(century(1601))    # 2
print(century(58))      # 1
print(century(356))     # 57
