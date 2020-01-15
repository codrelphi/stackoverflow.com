#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2020-01-14
# source: https://stackoverflow.com/questions/59739081/making-a-function-to-change-a-variable
#=================================================================================

# Method 1: based on your code.
def check(output_name):
    if ".pdf" not in output_name:
        output_name += ".pdf"
    return output_name


output_name = "sample"
result = check(output_name)
print(result) # sample.pdf

# Method 2: base on the string method endswith
def check(output_name):
    if not output_name.endswith('.pdf'):
        output_name = output_name + ".pdf"
    return output_name

output_name = "sample"
result = check(output_name)
print(result) # sample.pdf
