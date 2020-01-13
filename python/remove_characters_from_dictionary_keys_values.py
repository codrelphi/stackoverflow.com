#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2020-01-13
# source: https://stackoverflow.com/questions/59723285/removing-characters-from-both-a-dictionarys-keys-and-values
#=================================================================================
def dot_be_gone(dirty_dic):
    return {k.replace('.', '') : v.replace('.', '') for k, v in dirty_dic.items()}

x = dot_be_gone({"No. of Pets":"1", "No Problem":"Okay..."})
print(x) # {'No of Pets': '1', 'No Problem': 'Okay'}
