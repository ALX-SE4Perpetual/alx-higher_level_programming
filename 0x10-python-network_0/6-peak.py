#!/usr/bin/python3
"""This is a function that finds "a peak" in a list of integers"""

def find_peak(list_of_integers):
    """Find "a peak" in a list_of_integers"""

    if len(list_of_integers) == 0:
        return None

    if len(list_of_integers) == 1:
        return list_of_integers[0]

    list_of_integers.sort()
    return list_of_integers[-1]
