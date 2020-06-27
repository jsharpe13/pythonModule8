"""
Program: dict_membership.py
Author: Jacob Sharpe
Last date modified: 6/25/2020

the purpose of this program is to find the average in a dictionary of numbers
"""


def get_test_scores():
    """ gets the user input and creates the score_dict
       :return score_dict dictionary
        """
    scores_dict = dict()
    isValid = False
    while not isValid:
        try:
            num_scores = int(input("how many test scores are there? "))
            isValid = True
        except ValueError:
            print("something went wrong please try again")

    for x in range(num_scores):
        isValid = False
        while not isValid:
            try:
                score = int(input("what is the test score "))
                scores_dict.update({x: score})
                isValid = True
            except ValueError:
                print("something went wrong please try again")

    return scores_dict


def average_scores(scores_dict):
    """ calculates the average number
       :param scores_dict, dictionary passed in
       :return average_num the average
        """
    num_score = len(scores_dict)
    sum_num = 0

    for x in range(len(scores_dict)):
        sum_num = sum_num + scores_dict[x]

    average_num = sum_num / num_score

    return average_num


if __name__ == '__main__':
    dictionary = get_test_scores()
    results = average_scores(dictionary)

    print("%.2f" % results)