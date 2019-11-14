#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2019-11-14
# source: https://stackoverflow.com/questions/58860125/is-there-a-way-to-count-the-occurrence-of-a-character-in-each-word-of-a-string-i/
#=================================================================================

def count_char(text, char):
    text = text.lower()
    char = char.lower()
    words = text.split()
    return [word.count(char) for word in words]


if __name__ == '__main__':
    print(count_char("Welcome to this world", "w")) # [1, 0, 0, 1]
