"""
Program: dict_membership.py
Author: Jacob Sharpe
Last date modified: 6/24/2020

The purpose of this program is to return true or false if a key is in the dictionary
"""


def in_dict(the_dict, element):
    """ returns true if element is in the dictionary, false otherwise
    :param the_dict, the dictionary to be searched
    :param element, element being looked for
    :return true or false based on if element in the dictionary
     """
    return element in the_dict


if __name__ == '__main__':
    this_set = {'A': 1, 'B': 2, 'C': 3, 'D': 4}

    print(in_dict(this_set, 'A'))
    print(in_dict(this_set, 3))
    print(in_dict(this_set, 'Z'))
    print(this_set['A'])
