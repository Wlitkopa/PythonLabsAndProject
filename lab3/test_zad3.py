
import unittest
from DeanerySystem.day import Day, nthDayFrom
from DeanerySystem.term import Term, DayToStr


class Test_comparison(unittest.TestCase):


    def test_earlierThan(self):
        term1 = Term(Day.MON, 10, 15)
        term2 = Term(Day.FRI, 12, 30)
        term3 = Term(Day.FRI, 12, 50)
        term4 = Term(Day.MON, 10, 15)
        self.assertEqual(term1.earlierThan(term2), True)
        self.assertEqual(term1.earlierThan(term3), True)
        self.assertEqual(term1.earlierThan(term4), False)
        self.assertEqual(term2.earlierThan(term3), True)

    def test_laterThan(self):
        term1 = Term(Day.MON, 10, 15)
        term2 = Term(Day.FRI, 12, 30)
        term3 = Term(Day.FRI, 12, 50)
        term4 = Term(Day.MON, 10, 15)
        self.assertEqual(term2.laterThan(term3), False)
        self.assertEqual(term2.laterThan(term1), True)
        self.assertEqual(term4.laterThan(term1), False)
        self.assertEqual(term3.laterThan(term2), True)

    def test_equals(self):
        term1 = Term(Day.MON, 10, 15)
        term2 = Term(Day.FRI, 12, 30)
        term4 = Term(Day.MON, 10, 15)
        self.assertEqual(term1.equals(term4), True)
        self.assertEqual(term1.equals(term2), False)

    def test_str(self):
        term1 = Term(Day.MON, 10, 15)
        self.assertEqual(term1.__str__(), "Poniedziałek 10:15 [90]")


if __name__ == '__main__':
    unittest.main()
