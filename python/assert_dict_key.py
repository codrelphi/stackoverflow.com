#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2019-10-20
# source: https://stackoverflow.com/questions/58475838/check-a-dict-key-using-assert-from-unit-test
#=================================================================================

d1 = {'success': 'success', 'return message': 'return_msg', 'debug_data': 'debug_data'}
d2 =  {'success': 'validation', 'return message': 'return_msg', 'debug_data': 'debug_data'}

# If the values are not the same, you will get the exception AssertionError.
assert d1['success'] == d2['success']
