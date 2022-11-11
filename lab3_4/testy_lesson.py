
import unittest
from DeanerySystem import day
from DeanerySystem.day import Day, nthDayFrom, Action
from DeanerySystem import term
from DeanerySystem.term import Term, DayToStr
from enum import Enum, IntEnum
import lesson
from lesson import Lesson, yeartoString, sctoStrign
from DeanerySystem.TimetableWithoutBreaks import TimetableWithoutBreaks
from lab3_4.DeanerySystem.BasicTimetable import BasicTimetable, NoRecordError


class Test_TestAll(unittest.TestCase):

    def test_print_zero(self):
        with self.assertRaises(NoRecordError):
            timetable = TimetableWithoutBreaks()
            print(timetable)

    def test_input(self):
        with self.assertRaises(TypeError):
            term1 = Term(Day.MON, 8, 0)
            lesson100 = Lesson("kot", term1, "Podstawy programowania", "Stanisław Polak", 2)
        with self.assertRaises(TypeError):
            timetable = TimetableWithoutBreaks()
            lesson100 = Lesson(timetable, "kot", "Podstawy programowania", "Stanisław Polak", 2)
        with self.assertRaises(TypeError):
            term1 = Term(Day.MON, 8, 0)
            timetable = TimetableWithoutBreaks()
            lesson100 = Lesson(timetable, term1, "Podstawy programowania", "Stanisław Polak", 10)
        with self.assertRaises(ValueError   ):
            term1 = Term(Day.MON, 8, 0)
            timetable = TimetableWithoutBreaks()
            lesson100 = Lesson(timetable, term1, "Podstawy programowania", "Stanisław Polak", "kot")

    timetable = TimetableWithoutBreaks()
    term1 = Term(Day.MON, 8, 0)
    lesson1 = Lesson(timetable, term1, "Podstawy programowania", "Stanisław Polak", 2)
    term2 = Term(Day.TUE, 8, 0)
    lesson2 = Lesson(timetable, term2, "Podstawy programowania", "Stanisław Polak", 2)
    term3 = Term(Day.MON, 9, 30)
    lesson3 = Lesson(timetable, term3, "Fizyka", "prof Zakrzewska", 2)
    term4 = Term(Day.FRI, 17, 00)
    lesson4 = Lesson(timetable, term4, "Biologia", "prof Łodyga", 2, False)
    term5 = Term(Day.FRI, 14, 00)
    lesson5 = Lesson(timetable, term5, "Kosmologia", "prof Neptun", 2)
    term6 = Term(Day.SUN, 17, 00)
    lesson6 = Lesson(timetable, term6, "Anatomia", "prof Palec", 2, False)
    term7 = Term(Day.SAT, 18, 30)
    lesson7 = Lesson(timetable, term7, "Geografia", "prof Morze", 2, False)
    term8 = Term(Day.WED, 18, 30)
    lesson8 = Lesson(timetable, term8, "Chemia", "prof Cząstka", 2)
    term9 = Term(Day.THU, 9, 30)
    lesson9 = Lesson(timetable, term9, "wf", "prof Wycisk", 2)

    def test_put(self): # SKORO DODAJĘ LEKCJE Z WYKORZYSTANIEM METODY "put", TO ZNACZY ŻE DZIAŁA JEŻELI CHODZI O POMYŚLNE DODAWANIE

        with self.assertRaises(ValueError):
            term_temp = Term(Day.THU, 9, 30)
            lesson_temp = Lesson(Test_TestAll.timetable, term_temp, "taniec", "prof Jive", 2)  # bo wtedy występuje kolizja z wf

        # self.assertEqual(Test_TestAll.timetable.put(lesson_temp), False)  # bo wtedy występuje kolizja z wf

    def test_get(self):
        term_temp = Term(Day.THU, 9, 30)
        self.assertEqual(Test_TestAll.timetable.get(term_temp), Test_TestAll.lesson9)  # bo wtedy są zajęcia z wf
        term_temp = Term(Day.THU, 12, 30)
        self.assertEqual(Test_TestAll.timetable.get(term_temp), None)  # bo wtedy nic nie ma

    def test_print(self):
        self.assertEqual(Test_TestAll.timetable.__str__(), """               * Poniedziałek            * Wtorek                 * Środa                  * Czwartek               * Piątek                 * Sobota                 * Niedziela              *
************************************************************************************************************************************************************************************************
8:00 - 9:30    * Podstawy programowania  * Podstawy programowania *                        *                        *                        *                        *                        *
************************************************************************************************************************************************************************************************
9:30 - 11:00   * Fizyka                  *                        *                        * wf                     *                        *                        *                        *
************************************************************************************************************************************************************************************************
11:00 - 12:30  *                         *                        *                        *                        *                        *                        *                        *
************************************************************************************************************************************************************************************************
12:30 - 14:00  *                         *                        *                        *                        *                        *                        *                        *
************************************************************************************************************************************************************************************************
14:00 - 15:30  *                         *                        *                        *                        * Kosmologia             *                        *                        *
************************************************************************************************************************************************************************************************
15:30 - 17:00  *                         *                        *                        *                        *                        *                        *                        *
************************************************************************************************************************************************************************************************
17:00 - 18:30  *                         *                        *                        *                        * Biologia               *                        * Anatomia               *
************************************************************************************************************************************************************************************************
18:30 - 20:00  *                         *                        * Chemia                 *                        *                        * Geografia              *                        *
************************************************************************************************************************************************************************************************""")

    def test_earlierDay(self):
        term1_2 = Term(Day.SUN, 8, 0)
        self.assertEqual(Test_TestAll.timetable.can_be_transferred_to(term1_2, Test_TestAll.lesson1.fulltime), False)  # bo wtedy nie ma przedziału czasowego dla fulltime (Podstawy programowania)
        term1_2 = Term(Day.THU, 17, 0)
        self.assertEqual(Test_TestAll.timetable.can_be_transferred_to(term1_2, Test_TestAll.lesson4.fulltime), False)  # bo wtedy nie ma przedziału czasowego dla parttime (Biologia)
        term1_2 = Term(Day.THU, 18, 30)
        self.assertEqual(Test_TestAll.timetable.can_be_transferred_to(term1_2, Test_TestAll.lesson8.fulltime), True)  # fulltime (Chemia)
        term1_2 = Term(Day.SUN, 18, 30)
        self.assertEqual(Test_TestAll.timetable.can_be_transferred_to(term1_2, Test_TestAll.lesson7.fulltime), True)  # parttime (Geografia)

    def test_laterDay(self):
        term1_2 = Term(Day.SAT, 14, 0)
        self.assertEqual(Test_TestAll.timetable.can_be_transferred_to(term1_2, Test_TestAll.lesson5.fulltime), False)  # bo wtedy nie ma przedziału czasowego dla fulltime (Podstawy programowania)
        term1_2 = Term(Day.MON, 17, 0)
        self.assertEqual(Test_TestAll.timetable.can_be_transferred_to(term1_2, Test_TestAll.lesson6.fulltime), False)  # bo wtedy nie ma przedziału czasowego dla parttime (Anatomia)
        term1_2 = Term(Day.THU, 18, 30)
        self.assertEqual(Test_TestAll.timetable.can_be_transferred_to(term1_2, Test_TestAll.lesson8.fulltime), True)  # fulltime (Chemia)
        term1_2 = Term(Day.SUN, 18, 30)
        self.assertEqual(Test_TestAll.timetable.can_be_transferred_to(term1_2, Test_TestAll.lesson7.fulltime), True)  # parttime (Geografia)

    def test_earlierTime(self):
        term1_2 = Term(Day.MON, 6, 30)
        self.assertEqual(Test_TestAll.timetable.can_be_transferred_to(term1_2, Test_TestAll.lesson1.fulltime), False)  # bo wtedy nie ma przedziału czasowego dla parttime (Geografia)
        term1_2 = Term(Day.MON, 8, 0)
        self.assertEqual(Test_TestAll.timetable.can_be_transferred_to(term1_2, Test_TestAll.lesson3.fulltime), False)  # bo wtedy są zajęcia z Programowania skryptowego (Fizyka)
        term1_2 = Term(Day.WED, 17, 00)
        self.assertEqual(Test_TestAll.timetable.can_be_transferred_to(term1_2, Test_TestAll.lesson8.fulltime), True)  # można przesunąć Chemię (fulltime)
        term1_2 = Term(Day.SAT, 17, 0)
        self.assertEqual(Test_TestAll.timetable.can_be_transferred_to(term1_2, Test_TestAll.lesson7.fulltime), True)  # można przesunąć Geografia (parttime)

    def test_laterTime(self):
        term1_2 = Term(Day.MON, 9, 30)
        self.assertEqual(Test_TestAll.timetable.can_be_transferred_to(term1_2, Test_TestAll.lesson1.fulltime), False)  # bo wtedy są zajęcia z fizyki (Podstawy programowania)
        term1_2 = Term(Day.MON, 20, 00)
        self.assertEqual(Test_TestAll.timetable.can_be_transferred_to(term1_2, Test_TestAll.lesson7.fulltime), False)  # bo wtedy nie ma przedziału czasowego dla parttime (Geografia)
        term1_2 = Term(Day.TUE, 9, 30)
        self.assertEqual(Test_TestAll.timetable.can_be_transferred_to(term1_2, Test_TestAll.lesson2.fulltime), True)  # mogę przesunąć wtorkowe Podstawy Programowania
        term1_2 = Term(Day.SUN, 18, 30)
        self.assertEqual(Test_TestAll.timetable.can_be_transferred_to(term1_2, Test_TestAll.lesson6.fulltime), True)  # można przesunąć Anatomię (parttime)

    def test_parse(self):
        lista = "d+ t- d- t+"
        lista = lista.split(' ')
        self.assertEqual(Test_TestAll.timetable.parse(lista), [1, 2, 0, 3])

        with self.assertRaises(ValueError) as context:
            lista = "d+ t- d- t+ Ala ma kota"
            lista = lista.split(' ')
            Test_TestAll.timetable.parse(lista)

        # self.assertTrue('This is broken' in context.exception)

    def test_perform(self):
        lista = "d+ t- t- t+ d+ d+ t- d-"
        lista = lista.split(' ')
        moves = Test_TestAll.timetable.parse(lista)
        Test_TestAll.timetable.perform(moves)
        # print(Test_TestAll.timetable)
        self.assertEqual(Test_TestAll.lesson1.termin.day, Test_TestAll.term1.day)  # lesson1 nie mogła się przesunąć, bo termin wychodzi poza fulltime
        self.assertEqual(Test_TestAll.lesson2.termin.hour, Test_TestAll.term2.hour)
        self.assertEqual(Test_TestAll.lesson2.termin.minute, Test_TestAll.term2.minute)  # lesson2 nie mogła się przesunąć, bo termin wychodzi poza fulltime
        self.assertEqual(Test_TestAll.lesson3.termin, Test_TestAll.term3)  # lesson3 nie mogła się przesunąć, bo wtedy jest lesson1
        term1_2 = Term(Day.FRI, 18, 30)
        self.assertEqual(Test_TestAll.lesson4.termin, term1_2)  # lesson4 mogła się przesunąć o termin do przodu
        term1_2 = Term(Day.SAT, 14, 00)
        self.assertEqual(Test_TestAll.lesson5.termin.day, Test_TestAll.term5.day)  # lesson5 się nie mogła przesunąć, bo wtedy nie ma przedziału czasowego dla fulltime
        self.assertEqual(Test_TestAll.lesson6.termin, Test_TestAll.term6)  # bo wtedy nie ma przedziału czasowego dla parttime, więc nie mogła się przesunąć
        term1_2 = Term(Day.SAT, 17, 00)
        self.assertEqual(Test_TestAll.lesson7.termin.day, term1_2.day)
        self.assertEqual(Test_TestAll.lesson7.termin.hour, term1_2.hour)
        self.assertEqual(Test_TestAll.lesson7.termin.minute, term1_2.minute)  # lesson7 mogła się przesunąć o termin do tyłu
        term1_2 = Term(Day.TUE, 18, 30)
        # print(Test_TestAll.timetable)
        # print(f"\nTERAZ JEST LESSON8\n\n{Test_TestAll.lesson8}\n\n")
        # print("Actions: ", moves)
        self.assertEqual(Test_TestAll.lesson8.termin.day, term1_2.day)
        self.assertEqual(Test_TestAll.lesson8.termin.hour, term1_2.hour)
        self.assertEqual(Test_TestAll.lesson8.termin.minute, term1_2.minute)  # lesson8 mogła się przesunąć o dzień w tył
        lista = "d+ t- t- t- d+ d+ t+ d+"
        lista = lista.split(' ')
        moves = Test_TestAll.timetable.parse(lista)
        Test_TestAll.timetable.perform(moves)


if __name__ == '__main__':
    unittest.main()
