#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2019-11-21
# source: https://stackoverflow.com/questions/58964513/splitting-and-appending-a-string-in-python
#=================================================================================

"""
I want to take the state number 01 the county number 001 and the tract 020100
and make a new string 01001020100. How do I achieve this in Python?
"""

# comment
# To achieve your goal, you can use a regular expression syntax.
# But, It seems you are a beginner, so I come here with a basic
# logic based on split method. Here is the code:

census = 'Census Tract 201, Autauga County, Alabama: Summary level: 140, state:01> county:001> tract:020100'

state = census.split('state:')[1].split('>')[0]
county = census.split('county:')[1].split('>')[0]
tract = census.split('tract:')[1].split('>')[0]
result = state + county + tract

print(result) # 01001020100
