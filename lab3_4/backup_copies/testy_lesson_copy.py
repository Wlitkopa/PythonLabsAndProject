
import unittest
import sys
sys.path.append("/home/przemek/PycharmProjects/ps")
from lab3_4.DeanerySystem import day
from lab3_4.DeanerySystem.day import Day, nthDayFrom, Action
from lab3_4.DeanerySystem import term
from lab3_4.DeanerySystem.term import Term, DayToStr
from enum import Enum, IntEnum
import lesson_copy
from lesson_copy import Lesson, yeartoString, sctoStrign
from lab3_4.DeanerySystem.TimetableWithoutBreaks import TimetableWithoutBreaks


class Test_TestDay(unittest.TestCase):

    timetable = TimetableWithoutBreaks()
    term1 = Term(Day.MON, 8, 0)
    lesson1 = Lesson(term1, "Podstawy programowania", "Stanisław Polak", 2)
    term2 = Term(Day.MON, 10, 0)
    lesson2 = Lesson(term2, "Algebra", "Lech Adamus", 2)
    term3 = Term(Day.TUE, 8, 00)
    lesson3 = Lesson(term3, "Fizyka", "prof Zakrzewska", 2)
    term4 = Term(Day.FRI, 15, 00)
    lesson4 = Lesson(term4, "Biologia", "prof Łodyga", 2)
    term5 = Term(Day.TUE, 9, 00)
    lesson5 = Lesson(term5, "Kosmologia", "prof Ziemia", 2)
    term6 = Term(Day.FRI, 17, 00)
    lesson6 = Lesson(term6, "Anatomia", "prof Głowa", 2, False)
    term7 = Term(Day.SAT, 17, 00)
    lesson7 = Lesson(term7, "Anatomia", "prof Ręka", 2, False)
    term8 = Term(Day.SUN, 14, 00)
    lesson8 = Lesson(term8, "Anatomia", "prof Noga", 2, False)
    term9 = Term(Day.SUN, 10, 00)
    lesson9 = Lesson(term9, "Anatomia", "prof Stopa", 2, False)
    term10 = Term(Day.FRI, 12, 00)
    lesson10 = Lesson(term9, "Anatomia", "prof Ucho", 2)
    term11 = Term(Day.FRI, 19, 00)
    lesson11 = Lesson(term11, "Anatomia", "prof Palec", 2, False)
    term12 = Term(Day.TUE, 12, 00)
    lesson12 = Lesson(term12, "Kosmologia", "prof Mars", 2)
    term13 = Term(Day.SAT, 20, 00)
    lesson13 = Lesson(term13, "Anatomia", "prof Głos", 2, False)
    term14 = Term(Day.FRI, 16, 00)
    lesson14 = Lesson(term14, "Kosmologia", "prof Neptun", 2)
    term15 = Term(Day.SUN, 18, 30)
    lesson15 = Lesson(term15, "Anatomia", "prof Nos", 2, False)
    term16 = Term(Day.SUN, 9, 30)
    lesson16 = Lesson(term16, "Anatomia", "prof Kot", 2, False)

    def test_earlierDay(self):
        self.assertEqual(Test_TestDay.lesson1.earlierDay(), False)  # bo wtedy nie ma przedziału czasowego dla fulltime
        self.assertEqual(Test_TestDay.lesson6.earlierDay(), False)  # bo wtedy nie ma przedziału czasowego dla parttime
        self.assertEqual(Test_TestDay.lesson3.earlierDay(), False)  # bo wtedy termin jest zajęty (fulltime)
        self.assertEqual(Test_TestDay.lesson7.earlierDay(), False)  # bo wtedy termin jest zajęty (parttime)
        self.assertEqual(Test_TestDay.lesson4.earlierDay(), True)  # dla fulltime
        self.assertEqual(Test_TestDay.lesson8.earlierDay(), True)  # dla parttime
        self.assertEqual(Test_TestDay.lesson4.termin._Term__day, Day.THU)
        self.assertEqual(Test_TestDay.lesson4.termin.hour, 15)
        self.assertEqual(Test_TestDay.lesson4.termin.minute, 0)
        self.assertEqual(Test_TestDay.lesson4.name, "Biologia")
        self.assertEqual(Test_TestDay.lesson4.teacherName, "prof Łodyga")
        self.assertEqual(Test_TestDay.lesson4.fulltime, True)

    def test_laterDay(self):
        self.assertEqual(Test_TestDay.lesson10.laterDay(), False)  # bo wtedy nie ma przedziału czasowego dla fulltime
        self.assertEqual(Test_TestDay.lesson9.laterDay(), False)  # bo wtedy nie ma przedziału czasowego dla parttime
        self.assertEqual(Test_TestDay.lesson2.laterDay(), False)  # bo wtedy termin jest zajęty (fulltime)
        self.assertEqual(Test_TestDay.lesson6.laterDay(), False)  # bo wtedy termin jest zajęty (parttime)
        self.assertEqual(Test_TestDay.lesson3.laterDay(), True)  # dla fulltime
        self.assertEqual(Test_TestDay.lesson7.laterDay(), True)  # dla parttime
        self.assertEqual(Test_TestDay.lesson7.termin.hour, 17)
        self.assertEqual(Test_TestDay.lesson7.termin.minute, 0)
        self.assertEqual(Test_TestDay.lesson7.name, "Anatomia")
        self.assertEqual(Test_TestDay.lesson7.teacherName, "prof Ręka")
        self.assertEqual(Test_TestDay.lesson7.fulltime, False)

    def test_earlierTime(self):
        self.assertEqual(Test_TestDay.lesson6.earlierTime(), False)  # bo wtedy nie ma przedziału czasowego dla fulltime
        self.assertEqual(Test_TestDay.lesson6.earlierTime(), False)  # bo wtedy nie ma przedziału czasowego dla parttime
        self.assertEqual(Test_TestDay.lesson2.earlierTime(), False)  # bo wtedy termin jest zajęty (fulltime)
        self.assertEqual(Test_TestDay.lesson11.earlierTime(), False)  # bo wtedy termin jest zajęty (parttime)
        self.assertEqual(Test_TestDay.lesson12.earlierTime(), True)  # dla fulltime
        self.assertEqual(Test_TestDay.lesson13.earlierTime(), True)  # dla parttime
        self.assertEqual(Test_TestDay.lesson12.termin.hour, 10)
        self.assertEqual(Test_TestDay.lesson12.termin.minute, 30)
        self.assertEqual(Test_TestDay.lesson12.name, "Kosmologia")
        self.assertEqual(Test_TestDay.lesson12.teacherName, "prof Mars")
        self.assertEqual(Test_TestDay.lesson12.fulltime, True)

    def test_laterTime(self):
        self.assertEqual(Test_TestDay.lesson14.laterTime(), False)  # bo wtedy nie ma przedziału czasowego dla fulltime
        self.assertEqual(Test_TestDay.lesson15.laterTime(), False)  # bo wtedy nie ma przedziału czasowego dla parttime
        self.assertEqual(Test_TestDay.lesson1.laterTime(), False)  # bo wtedy termin jest zajęty (fulltime)
        self.assertEqual(Test_TestDay.lesson16.laterTime(), False)  # bo wtedy termin jest zajęty (parttime)
        self.assertEqual(Test_TestDay.lesson12.laterTime(), True)  # dla fulltime
        self.assertEqual(Test_TestDay.lesson8.laterTime(), True)  # dla parttime
        self.assertEqual(Test_TestDay.lesson12.termin.hour, 12)
        self.assertEqual(Test_TestDay.lesson12.termin.minute, 0)
        self.assertEqual(Test_TestDay.lesson12.name, "Kosmologia")
        self.assertEqual(Test_TestDay.lesson12.teacherName, "prof Mars")
        self.assertEqual(Test_TestDay.lesson12.fulltime, True)


if __name__ == '__main__':
    unittest.main()
