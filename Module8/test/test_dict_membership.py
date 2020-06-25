import unittest
from more_fun_with_collections import dict_membership


class MyTestCase(unittest.TestCase):
    def test_in_dict_true(self):
        this_set = {'A': 1, 'B': 2, 'C': 3, 'D': 4}
        self.assertTrue(dict_membership.in_dict(this_set, 'C'))

    def test_in_dict_false(self):
        this_set = {'A': 1, 'B': 2, 'C': 3, 'D': 4}
        self.assertFalse(dict_membership.in_dict(this_set, 'Z'))


if __name__ == '__main__':
    unittest.main()
