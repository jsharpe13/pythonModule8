"""
Program: date_time.py
Author: Jacob Sharpe
Last date modified: 6/27/2020

the purpose of this program is to calculate six months from a given birthday
"""
import datetime


def half_birthday(d):
    """ calculates six months from a birthday
            :param d the birthday date
           :return six month date
            """
    six_months = d + datetime.timedelta(days=(365 / 2))
    return six_months


if __name__ == '__main__':
    Birthday = datetime.datetime(2020, 1, 23)
    result = half_birthday(Birthday)
    print(result)
