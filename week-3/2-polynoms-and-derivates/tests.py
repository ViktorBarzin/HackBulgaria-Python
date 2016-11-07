import unittest
from one_liner import get_first_derivative


class OneLinerTest(unittest.TestCase):
    def test_monomial_without_coeff(self):
        self.assertEqual('2*x', get_first_derivative('x^2', 'x'))

    def test_monomial_on_first_power(self):
        self.assertEqual('1', get_first_derivative('x^1', 'x'))

    def test_full_equation_with_all_cases(self):
        self.assertEqual('1+3*y^2+6*y^2+6*y+24*y^3', get_first_derivative('1 + y + y^3 + 2*y^3 + 3*y^2 + 6*y^4', 'y'))

    def test_single_monomial(self):
        self.assertEqual('6*y^2', get_first_derivative('2*y^3', 'y'))

    def test_single_integer(self):
        self.assertEqual('0', get_first_derivative('1', 'x'))

    def test_variable_only(self):
        self.assertEqual('1', get_first_derivative('x', 'x'))
        
    # print(get_first_derivative('x^4 + 10*x^3', 'x'))
    # print(get_first_derivative('x^2 + 1', 'x'))
    # print(get_first_derivative('3*x^2', 'x'))

if __name__ == '__main__':
    unittest.main()

'''
$ python3 solution.py '2x^3+x'
Derivative of f(x) = 2*x^3 + x is:
f'(x) = 6*x^2 + 1

$ python3 solution.py '1'
The derivative of f(x) = 1 is:
f'(x) = 0

$ python3 solution.py 'x^4+10x^3'
The derivative of f(x) = x^4 + 10*x^3 is:
f'(x) = 4*x^3 + 30*x^2

$ python3 solution.py '1+x^2'
The derivative of f(x) = x^2 + 1 is:
f'(x) = 2x

$ python3 solution.py '3x^2'
The derivative of f(x) = 3x^2 is:
f'(x) = 6x
'''

