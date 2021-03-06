#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2019-11-10
# source: https://stackoverflow.com/questions/58789668/how-to-create-a-matrix-from-a-given-text-file/
#=================================================================================

""" matrix.txt
xxxxx
xS--x
xx-Fx
xxxxx
"""
# desired output
# print(matrix[1][1])
# S

txt = open('matrix.txt')
matrix = []
for line in txt:
    line_list = [l for l in list(line) if l != '\n']
    matrix.append(line_list)

print(matrix)
print(matrix[1][1])

# outputs
# [['x', 'x', 'x', 'x', 'x'], ['x', 'S', '-', '-', 'x'], ['x', 'x', '-', 'F', 'x'], ['x', 'x', 'x', 'x', 'x']]
# S
