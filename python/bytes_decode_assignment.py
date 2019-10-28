#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2019-10-20
# source: https://stackoverflow.com/questions/58477936/importing-arduino-byte-data-into-python3-using-readline-want-to-assign-data-t
#=================================================================================

while True:
    data = ser.readline()
    data = data.strip().decode('utf-8') # to decode byte to unicode
    data = data.split(',') # you get something like ['10.1', '20.2', '30.3']
    a = float(data[0]) # transform '10.1' to 10.1
    b = float(data[1]) # transform '20.2' to 20.2
    c = float(data[2]) # transform '30.3' to 30.3
    print(a) # display 10.1
    print(b) # display 20.2
    print(c) # display 30.2
