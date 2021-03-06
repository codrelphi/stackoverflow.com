#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2019-11-02
# source: https://stackoverflow.com/questions/58675306/increasing-a-key-by-knowing-the-value-python-dictionary/
#=================================================================================

def bill(*buy_lst):  # see this line
    for item in buy_lst:
        demand[item] += 1  # see this line

if __name__ == "__main__":
    demand = {"bread":0,"butter":0,"cheese":0, "water":0,"ice cream":0}
    # bread is the value and 0 is the key, which I want to increase every time

    bill("bread", "cheese") # The client buys the products `bread` and `cheese`
    print(demand)
    bill("bread", "cheese", "water", "butter")
    print(demand)

# Outputs
# {'bread': 1, 'butter': 0, 'cheese': 1, 'water': 0, 'ice cream': 0}
# {'bread': 2, 'butter': 1, 'cheese': 2, 'water': 1, 'ice cream': 0}
