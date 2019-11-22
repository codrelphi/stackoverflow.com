#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2019-11-22
# source: https://stackoverflow.com/questions/58902138/gather-all-data-for-same-day-into-one-row/
#=================================================================================

# I assume the file data.txt contains your data

"""
Date;Temp
2019-06-20 00:00:00;18.44
2019-06-20 01:00:00;18.28
2019-06-20 07:00:00;18.23
2019-06-20 13:00:00;18.20
2019-06-21 02:00:00;18.48
2019-06-21 08:00:00;18.45
2019-06-21 14:00:00;18.36
2019-06-21 21:00:00;18.24
2019-06-22 01:00:00;18.15
2019-06-22 05:00:00;18.12
2019-06-22 12:00:00;18.06
2019-06-22 19:00:00;17.99
2019-06-23 00:00:00;17.35
2019-06-23 03:00:00;17.34
2019-06-23 08:00:00;17.31
2019-06-23 23:00:00;17.24
"""

data = {}
with open("data.txt") as f:
    for line in f:
        if 'Date' not in line or 'Temp' not in line:
            k, v = line.split()
            temperature = v.split(';')[1]
            if k not in data:
                data[k] = [temperature]
            else:
                data[k].append(temperature)


for k, v in data.items():
    print("{} ;{}".format(k, ";".join(v)))
