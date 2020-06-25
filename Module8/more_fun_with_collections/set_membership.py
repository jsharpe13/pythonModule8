"""
Program: set_membership.py
Author: Jacob Sharpe
Last date modified: 6/24/2020

The purpose of this program is to return whether a specific element is within the set
"""


def in_set(the_set, element):
    """ returns true if element is in the set, false otherwise
          :param the_set, the set to be searched
          :param element, element being looked for
          :return true or false based on if element in the set
           """
    return element in the_set


if __name__ == '__main__':
    this_set = {1, 1, 2, 3, 4}

    print(in_set(this_set, 2))
    print(in_set(this_set, 7))
