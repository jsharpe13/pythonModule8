import unittest
from more_fun_with_collections import assign_average


class MyTestCase(unittest.TestCase):
    def test_average_A(self):
        case = 'A'
        result = assign_average.switch_average(case)
        self.assertEqual(result, 95)

    def test_average_B(self):
        case = 'B'
        result = assign_average.switch_average(case)
        self.assertEqual(result, 85)

    def test_average_C(self):
        case = 'C'
        result = assign_average.switch_average(case)
        self.assertEqual(result, 75)

    def test_average_D(self):
        case = 'D'
        result = assign_average.switch_average(case)
        self.assertEqual(result, 65)

    def test_average_F(self):
        case = 'F'
        result = assign_average.switch_average(case)
        self.assertEqual(result, 50)

    def test_average_E_Invalid(self):
        case = 'E'
        result = assign_average.switch_average(case)
        self.assertEqual(result, 'Invalid Input default case')


if __name__ == '__main__':
    unittest.main()
