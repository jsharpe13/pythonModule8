"""
Program: dict_membership.py
Author: Jacob Sharpe
Last date modified: 6/25/2020

the purpose of this program is to use dictionaries to substitute for switch statements
"""
def one():
    return 95
def two():
    return 85
def three():
    return 75
def four():
    return 65
def five():
    return 50
def default():
    return 'Invalid Input default case'


def switch_average(case):
    """ gets which funtion to call
           :return call to function
            """
    switch = {
        'A': one,
        'B': two,
        'C': three,
        'D': four,
        'F': five
    }
    functionToCall = switch.get(case, default)
    return functionToCall()


if __name__ == '__main__':
    result = switch_average('A')
    result2 = switch_average('E')
    print(result)
    print(result2)
