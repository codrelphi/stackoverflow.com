#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2019-11-02
# source: https://stackoverflow.com/questions/58675306/increasing-a-key-by-knowing-the-value-python-dictionary/
#=================================================================================

demand = {"bread":0,"butter":0,"cheese":0, "water":0,"ice cream":0}
# bread is the value and 0 is the key, which I want to increase every time

def bill(*buy_lst):  # see this line
    for item in buy_lst:
        demand[item] += 1  # see this line

bill("bread", "cheese") # The client buys the products `bread` and `cheese`
print(demand)
bill("bread", "cheese", "water", "butter")
print(demand)
