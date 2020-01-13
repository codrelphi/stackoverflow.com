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
        clean_x = x.replace('.', "")
        clean_y = y.replace('.', "")
        clean_dic[clean_x] = clean_y
    return(clean_dic)

x = dot_be_gone({"No. of Pets":"1", "No Problem":"Okay..."})
print(x) # {'No of Pets': '1', 'No Problem': 'Okay'}
