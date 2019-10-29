#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2019-10-29
# source:
#=================================================================================

def replaceWord(sep, word, sentence):
    """
        @param: sep is the separator
        @param: word is the work to replace
        @param: sentence is the sentence
    """
    len_word = len(word)
    replacer = sep * len_word
    print(sentence.replace(word, replacer))


if __name__ == "__main__":
    sentence = "what is tomorrow's date?"
    word = "what"
    sep = "-"
    replaceWord(sep, word, sentence)
    #print(help(replaceWord))
