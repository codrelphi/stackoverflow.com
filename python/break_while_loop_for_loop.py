#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2019-12-03
# source: https://stackoverflow.com/questions/59148762/how-can-i-properly-use-while-loop-and-not-have-it-repeat-on-break
#=================================================================================

# break will exit from the for loop
# you need a flag to exit from the while loop

looper = True # the flag
while looper:
profile_name = input("\nEnter Profile Name (Case Sensitive): ")
    if len(profile_name) == 0:
        print("Profile cannot be blank!\n")
        pass
    for profile in prof_collection.find({"name": profile_name}):
        if profile_name in profile["name"]:
            print("%s has been found." % profile_name)
            looper = False # flag changes
            break
        else:
            print("%s was not found. Please enter a valid Profile." % profile_name)
            pass
