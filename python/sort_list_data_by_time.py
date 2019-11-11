#! /usr/bin/python3
# -*- coding: utf-8 -*-
#=================================================================================
# author: Chancerel Codjovi (aka codrelphi)
# date: 2019-11-11
# source: https://stackoverflow.com/questions/58804838/is-there-an-obvious-way-to-sort-this-list-of-data-by-time-in-python
#=================================================================================
def conversion(t):
    """ convert time to minutes """
    if 'h' in t:
        hours = int(t.split('h')[0])
        minutes = int(t.split('h')[1].split('m')[0])
        minutes = hours * 60 + minutes
    else:
        minutes = int(t.split('m')[0])

    return minutes

def back_conversion(minutes):
    """ convert minutes to time """
    if minutes >= 60:
        hours = minutes // 60
        newminutes = minutes % 60
        if newminutes == 0:
            result = '{}h'.format(hours)
        else:
            result = '{}h{}m'.format(hours, newminutes)
    else:
        result = '{}m'.format(minutes)

    return result


if __name__ == "__main__":
    values = ['10m', '10m', '10m', '11h59m', '11m', '12m', '13h24m', '13m', '13m', '13m', '14m', '14m', '15m', '17m', '17m', '1h01m', '1h05m', '1h05m', '1h11m', '1h15m', '1h19m', '1h25m', '1h30m', '1h31m', '1h41m', '1h46m', '1h50m', '1h54m', '1m', '20m', '21m', '22m', '22m', '22m', '24m', '25m', '28m', '28m', '28m', '29m', '2h00m', '2h07m', '2h24m', '2h27m', '2h35m', '2h51m', '2h51m', '2m', '2m', '2m', '2m', '2m', '2m', '2m', '30m', '31m', '31m', '31m', '32m', '32m', '34m', '35m', '37m', '3h18m', '3h24m', '3h28m', '3h31m', '3h43m', '3h45m', '3h53m', '3m', '3m', '3m', '40m', '44m', '4h11m', '4h25m', '4h43m', '4h45m', '4h57m', '4m', '4m', '4m', '4m', '51m', '51m', '55m', '58m', '5h29m', '5h39m', '5h40m', '6h06m', '6h13m', '6h20m', '6m', '7h16m', '7h36m', '7h43m', '7m', '8h50m', '8m', '8m', '8m', '8m', '9h39m', '9m', '9m', '9m', '9m', '9m', '9m']
    sorted_values  = sorted([conversion(v) for v in values])
    final_results = [back_conversion(v) for v in sorted_values]
    print(final_results)
