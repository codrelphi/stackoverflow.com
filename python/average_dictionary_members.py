#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2020-01-13
# source: https://stackoverflow.com/questions/59705517/attempting-to-get-the-average-from-numbers-in-a-dictionary
#=================================================================================

def get_average(numbers):
    """compute the average of the dictionary members."""
    val = 0
    for v in numbers.values():
        val += v
    avg = val / len(numbers)
    return avg

if __name__ == '__main__':
    numbers = {
        'one': 1,
        'two': 2
    }

    print(get_average(numbers)) # 1.5
