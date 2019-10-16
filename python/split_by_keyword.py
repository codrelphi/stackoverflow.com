#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2019-10-16
# source: https://stackoverflow.com/questions/58412309/how-can-i-split-the-second-line-when-the-keyword-match-two-lines-by-python/
#=================================================================================

# regular expression (i.e.: re module is powerful to do a such task).
# Here I give you another way to achieve your goal:

# contains the logs data (e.g: it is an example)
lines = [
            "19:07:57.166 [INFO]keyword = 3 ...",
            "19:08:13.664 [INFO]keyword = 2 ...",
            "19:14:27.062 [INFO]keyword = 3 ...",
            "19:14:43.061 [INFO]keyword = 2 ...",
]

results = [] # contains all the results

for line in lines:
    line_split = line.split("[INFO]")
    if line_split[1][10] == '2':
        results.append(line_split[0].strip())

print(results)

# Outputs:
# ['19:08:13.664', '19:14:43.061']
