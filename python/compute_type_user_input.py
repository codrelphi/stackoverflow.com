#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2019-10-23
# source: https://stackoverflow.com/questions/58530668/how-to-find-type-of-user-input-and-print-different-values-depending-on-the-type/
#=================================================================================

def findt():
    userin = input("Input: ")

    if userin.isnumeric():
        # userin is numeric
        result = float(userin) ** 2
        print(result)

    else:
        try:
            # userin is a float
            result = float(userin) ** 2
            print(result)
        except ValueError:
            # userin is a string
            print("Sorry Dave, I'm afraid I can't do that")
            return 0.0


findt()
