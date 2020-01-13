#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2020-01-13
# source: https://stackoverflow.com/questions/59723285/removing-characters-from-both-a-dictionarys-keys-and-values
#=================================================================================
def dot_be_gone(dirty_dic):
    clean_dic = {}
    for x, y in dirty_dic.items():
        clean_x = x
        clean_y = y
        if '.' in x:
            x_items = x.split('.')
            clean_x = x_items[0] + x_items[1]
        if '.' in y:
            y_items = y.split('.')
            clean_y = y_items[0] + y_items[1]
        clean_dic[clean_x] = clean_y
    return(clean_dic)

x = dot_be_gone({"No. of Pets":"1", "No Problem":"Okay..."})
print(x) # {'No of Pets': '1', 'No Problem': 'Okay'}
