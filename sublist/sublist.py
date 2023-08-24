"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def sublist(list_one, list_two):
    """
    Identifies the relations among lists
    """
    if list_one == list_two:
        return EQUAL
    invert = False
    if len(list_one) > len(list_two):
        list_one, list_two = list_two.copy(), list_one.copy()
        invert = True
    if any(
            list_one == list_two[index:index + len(list_one)]
            for index in range(len(list_two))
        ):
        if not invert:
            return SUBLIST
        return SUPERLIST
    return UNEQUAL
