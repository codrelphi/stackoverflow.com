#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2019-11-04
# source: https://stackoverflow.com/questions/58653327/using-replace-function/
#=================================================================================
curseWords = ["crap", "butt", "fork"]
niceWords = ["poo", "buttox", "spoon"]
dirtySentence = "You crap, butt in fork"

def Censor(curseWords, niceWords, dirtySentence):
    for i in range(len(niceWords)):
        dirtySentence = dirtySentence.replace(curseWords[i], niceWords[i])

    return dirtySentence


dirtySentence = Censor(curseWords, niceWords, dirtySentence) # call the defined function
print(dirtySentence)

# Output: You poo, buttox in spoon
