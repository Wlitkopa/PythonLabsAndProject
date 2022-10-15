
from zad2 import recognize
import unittest


class Testrecognize(unittest.TestCase):

    def test_single_num(self):
        self.assertEqual(recognize('123'), '  Liczba: 123')

    def test_single_word(self):
        self.assertEqual(recognize('alamakota'), '  Wyraz: alamakota')

    def test_word_and_num(self):
        self.assertEqual(recognize('ala1ma34kotów5'), '''  Wyraz: ala
  Liczba: 1\n  Wyraz: ma\n  Liczba: 34\n  Wyraz: kotów\n  Liczba: 5''')

    def test_raised_exception_ValueError(self):
        with self.assertRaises(ValueError):
            recognize(2, 'Ala ma kota123')


if __name__ == '__main__':
    unittest.main()
