#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2019-11-03
# source: https://stackoverflow.com/questions/58683846/find-list-elements-that-do-not-contain-any-of-the-characters
#=================================================================================

# Problem
# Find list elements that do not contain any of the characters ( . - \ / )

book_list = ["book1", "book.2", "book/3", "book/\4", "book-5", "book(6", "book)7", "book(8)", "book10"]

for wo2 in book_list:
    if "/" not in wo2 and "\"" not in wo2 and "-" not in wo2 and "." not in wo2 and "(" not in wo2 and ")" not in wo2:
        print (wo2)

# Outputs
# book1
# book10
