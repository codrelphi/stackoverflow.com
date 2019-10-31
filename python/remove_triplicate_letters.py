#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2019-10-26
# source: https://stackoverflow.com/questions/58565315/how-to-remove-triplicate-letters-in-python/
#=================================================================================
def removeTriplicateLetters(sentence):
    """
        :param sentence: The sentence to transform
        :param words: The words in the sentence
        :param new_words: List of the final words of the new sentence

    """
    words = sentence.split(" ") # split the sentence into words
    new_words = []
    for word in words:  # loop through words of the sentence
        new_word = []
        for char in word:   # loop through characters in a word
            position = word.index(char)
            if word.count(char) >= 3:
                new_word = [i for i in word if i != char]
                new_word.insert(position, char)
        new_words.append(''.join(new_word))

    return ' '.join(new_words)


def main():
    print(removeTriplicateLetters('byeee mmmy friiiennd'))


main()

# output: 'bye my friennd'
