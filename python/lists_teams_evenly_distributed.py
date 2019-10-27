#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2019-10-27
# source: https://stackoverflow.com/questions/58576153/assigning-values-of-one-list-to-another-list-with-even-distribution
#=================================================================================
import random

def list_by_team(aList, size):
    """ return a list for a team """
    list_for_a_team = []
    for i in range(0, size):
        nbr = random.choice(aList)
        aList.remove(nbr)
        list_for_a_team.append(nbr)

    return list_for_a_team

def main():

    Weeks= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
     21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
     40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]

    Teams=['alpha','beta','gamma','Lambda']

    results = {}

    lenTeams = len(Teams) # i.e. 4
    lenWeeks = len(Weeks) # i.e. 52
    weeksPerTeam = int(lenWeeks / lenTeams)
    for i in range(0, lenTeams):
        key = Teams[i]
        value = list_by_team(Weeks, weeksPerTeam)
        results[key] = value

    print(results)

main()

"""
    The function `list_by_team` returns a random evenly distributed weeks.Just to test:
    Weeks= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
     21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
     40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]
    w1, w2, w3, w4 = [list_by_team(Weeks) for i in range(0, 4)]
    result = set(w1) & set(w2) & set(w3) & set(w4)
    print(result) # display: set() => It means that no item is duplicated in four generated list for teams

"""
