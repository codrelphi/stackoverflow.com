#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2019-11-15
# source: https://stackoverflow.com/questions/58858763/can-i-remove-multiple-indexes-from-a-string-with-a-for-loop
#=================================================================================

text = "Gvusaibdsz8audvbsauzdgsavuczisagbcsuzaicbhas"
text_list = list(text)
for index in range(0, 7):
    text_list.remove(text[index])

text = ''.join(text_list)
print(text)   # dsz8audvbsauzdgsavuczisagbcsuzaicbhas
