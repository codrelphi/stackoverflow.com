#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2019-10-21
# source: https://stackoverflow.com/questions/58494338/swap-first-and-last-digits-of-a-number-using-loops
#=================================================================================

def swap(numbers):
    """ Swap the first and the last digit of a number using loop """
    numbersList = []
    for number in str(numbers):
        numbersList.append(number)
    numbersList[0], numbersList[-1] = numbersList[-1], numbersList[0]
    return int(''.join(numbersList))


print(2665, " => ", swap(2665)) # display 2665 => 5662
