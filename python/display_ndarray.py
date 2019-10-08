#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2019-10-08
# source: https://stackoverflow.com/questions/58289625/how-to-get-the-same-output-using-multidimensional-arrays/
#=================================================================================

while True:
    try:
        num_row = int(input("Number of rows: "))
        break
    except ValueError:
        print('Please enter an integer!')

while True:
    try:
        num_column = int(input('Number of columns: '))
        break
    except ValueError:
        print('Please enter an integer!')


# initialize the 2d array (tab) using a list-comprehension
# e.g.: for 3 cols and 2 rows, You will have
# tab = [[0, 0, 0], [0, 0, 0]]
tab = [[0 for c in range(num_column)] for r in range(num_row)]

# to create each value of the 2d array and print it at the same time
for rows in range(num_row):
    for columns in range(num_column):
        tab[rows][columns] = rows * columns
        print(tab[rows][columns], end= " ")
    print()
