#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2019-11-27
# source: https://stackoverflow.com/questions/59040973/how-do-i-update-an-initialized-variable-used-in-python-class/
#=================================================================================

class Whatever:
    def __init__(self, thing1):
        self.list=[]
        self.thing=thing1

    def list_append(self):
        df1=pd.read_csv('job.py')
        df2=pd.read_csv('home.py')

        self.list.append([df1,df2])
        return self.list

    def new_function(self):
        self.list_append() # to call the above method
        return self.list

function=Whatever(thing1)
function_output=function.new_function()
print(function_output)

# Let assume df1 = "hello", df2 = "world" and thing1 = "good".
# The above code will produce the result [['hello', 'world']].
