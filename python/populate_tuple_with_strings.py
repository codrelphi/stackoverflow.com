#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2019-10-31
# source: https://stackoverflow.com/questions/58643815/populating-a-python-tuple-with-strings-stored-in-different-keys-across-multiple
#=================================================================================

""" The problem:

Suppose I have the following data structures:

x = {'name': 'x', 'alias': ['test']}
y = {'name': 'y', 'alias': ['run', 'log']}
z = (x, y)
And now I would like to populate a tuple with all of the name and alias strings, like so:

result = ('x', 'y', 'test', 'run', 'log')

"""
