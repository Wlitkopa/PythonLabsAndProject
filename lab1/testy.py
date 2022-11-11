import main
import unittest
import cmath
from fractions import Fraction


class Test_TestSum(unittest.TestCase):
    def test_sum_integer_integer(self):
        self.assertEqual(main.sum(2, 2), 4)

    def test_sum_integer_float(self):
        self.assertEqual(main.sum(2, 1.5), 3.5)

    def test_sum_integer_string(self):
       self.assertEqual(main.sum(2, '2'), 4)

    def test_sum_string_string(self):
        self.assertEqual(main.sum('2.1', '2.0'), 4.1)

    def test_sum_integer_wrong_number_in_string(self):
        self.assertEqual(main.sum(2, 'Ala ma kota123'), 2)

    def test_sum_tablica_zamiast_int(self):
        self.assertEqual(main.sum(2, [1, 2]), 2)

    def test_sum_fraction_fraction(self):
        self.assertEqual(main.sum(Fraction('5/7'), Fraction('3/4')), Fraction(41, 28))

    def test_sum_complex_complex(self):
        self.assertEqual(main.sum(complex(1, 3), complex(2, -1)), complex(3, 2))

    def non_num_non_str(self):
        self.assertEqual(main.sum(1, [1, 2]), 4)

    # def test_raised_exception_ValueError(self):
    #     with self.assertRaises(ValueError):
    #         main.sum(2, 'Ala ma kota123')


if __name__ == '__main__':
    unittest.main()
