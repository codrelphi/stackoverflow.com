#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2019-11-20
# source: https://stackoverflow.com/questions/58924586/exception-handling-easy-python
#=================================================================================

def is_perfect(n):
    total = 0
    for x in range(1, n):
        if n % x == 0:
            total = total + x
    return total == n


if __name__ == '__main__':
    try:
        user_input = int(input("Enter your number: "))
        print(is_perfect(user_input))
    except ValueError:
        print("Error: enter a number")

# Output
# Enter your number: 6
# True
