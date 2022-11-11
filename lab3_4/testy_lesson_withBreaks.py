
import unittest
from DeanerySystem import day
from DeanerySystem.day import Day, nthDayFrom, Action
from DeanerySystem import term
from DeanerySystem.term import Term, DayToStr, BasicTerm
from enum import Enum, IntEnum
import lesson
from lesson import Lesson, yeartoString, sctoStrign
import DeanerySystem.TimetableWithBreaks
from DeanerySystem.TimetableWithBreaks import TimetableWithBreaks
from DeanerySystem.Break import Break
from lab3_4.DeanerySystem.BasicTimetable import BasicTimetable, NoRecordError


class Test_TestAll(unittest.TestCase):

    term1 = BasicTerm(9, 30, 10)
    term2 = BasicTerm(11, 10, 10)
    term3 = BasicTerm(12, 50, 10)
    term4 = BasicTerm(14, 30, 10)
    term5 = BasicTerm(16, 10, 10)
    term6 = BasicTerm(17, 50, 10)
    term7 = BasicTerm(19, 30, 10)
    term8 = BasicTerm(11, 30, 10)
    term9 = BasicTerm(16, 20, 10)

    break1 = Break(term1)
    break2 = Break(term2)
    break3 = Break(term3)
    break4 = Break(term4)
    break5 = Break(term5)
    break6 = Break(term6)
    break7 = Break(term7)
    break8 = Break(term8)
    break9 = Break(term9)
    break10 = 10000000

    def test_print_zero(self):
        with self.assertRaises(NoRecordError):
            timetable = TimetableWithBreaks()
            print(timetable)

    def test_break(self):
        with self.assertRaises(TypeError):
            breaks = [Test_TestAll.break1, Test_TestAll.break2, Test_TestAll.break3, Test_TestAll.break10]
            timetable = TimetableWithBreaks(False, breaks)

    def test_getTerm(self):
        self.assertEqual(Test_TestAll.break1.getTerm(), Test_TestAll.break1.term)

    def test_str_break(self):
        self.assertEqual(Test_TestAll.break1.__str__(), "---")

    def test_put(self): # SKORO DODAJĘ LEKCJE Z WYKORZYSTANIEM METODY "put", TO ZNACZY ŻE DZIAŁA JEŻELI CHODZI O POMYŚLNE DODAWANIE

        break_list = [Test_TestAll.break1, Test_TestAll.break2, Test_TestAll.break3, Test_TestAll.break4, Test_TestAll.break5, Test_TestAll.break6, Test_TestAll.break7]
        timetable = TimetableWithBreaks(True, break_list)
        term1 = Term(Day.MON, 11, 20)
        lesson1 = Lesson(timetable, term1, "WDZC - CWP", "mgr Golizda", 2)

        with self.assertRaises(ValueError):
            term2 = Term(Day.MON, 11, 20)
            lesson_temp1 = Lesson(timetable, term2, "Fizyka", "dr Lewińska", 2)  # Wtedy występuje kolizja z "WDZC - CWP"

        with self.assertRaises(ValueError):
            term3 = Term(Day.MON, 18, 20)
            lesson_temp2 = Lesson(timetable, term3, "Prog skryp - wykl", "dr Stanisław Polak", 2)  # Wtedy zajęcia kolidują z przerwą

        # self.assertEqual(timetable.put(lesson_temp1), False)  # Wtedy są zajęcia "WDZC - CWP"
        # self.assertEqual(timetable.put(lesson_temp2), False)  # Zajęcia nachodzą na przerwę

    def test_skipBreaks_False(self):

        break_list = [Test_TestAll.break1, Test_TestAll.break2, Test_TestAll.break3]
        timetable = TimetableWithBreaks(False, break_list)
        term1 = Term(Day.MON, 11, 20)
        lesson1 = Lesson(timetable, term1, "WDZC - CWP", "mgr Golizda", 2)
        term2 = Term(Day.MON, 16, 20)
        lesson2 = Lesson(timetable, term2, "Analiza", "dr Cichacz", 2)

        self.assertEqual(lesson1.earlierTime(), False)  # Nie można przenieść wstecz, bo jest przerwa
        self.assertEqual(lesson1.laterTime(), False)  # Nie można przenieść w przód, bo jest przerwa
        self.assertEqual(lesson2.earlierTime(), True)  # Mogę przenieść tę lekcję wcześniej, bo mam tylko 3 poranne przerwy w timetable
        self.assertEqual(lesson2.laterTime(), True)  # Mogę przenieść tę lekcję później, bo mam tylko 3 poranne przerwy w timetable

        term3 = Term(Day.MON, 17, 50)
        lesson3 = Lesson(timetable, term3, "Kosmologia", "dr Ziemia", 2)

        # print(timetable)

        self.assertEqual(lesson2.laterTime(), False)  # o 17:50 jest Kosmologia, zatem nie można przesunąć tej lekcji na później wykorzystując pomijanie przerw
        self.assertEqual(lesson2.termin.hour, 16)
        self.assertEqual(lesson2.termin.minute, 20)

        term4 = Term(Day.MON, 14, 50)
        lesson4 = Lesson(timetable, term4, "Anatomia", "dr Ręka", 2)

        self.assertEqual(lesson2.earlierTime(), False)  # o 14:50 jest Anatomia, zatem nie można przesunąć tej lekcji na wcześniej wykorzystując pomijanie przerw
        self.assertEqual(lesson2.termin.hour, 16)
        self.assertEqual(lesson2.termin.minute, 20)

    def test_skipBreaks_True(self):

        break_list = [Test_TestAll.break1, Test_TestAll.break2, Test_TestAll.break3, Test_TestAll.break4, Test_TestAll.break5, Test_TestAll.break6, Test_TestAll.break7, Test_TestAll.break8, Test_TestAll.break9]
        timetable = TimetableWithBreaks(True, break_list)
        term1 = Term(Day.MON, 8, 0)
        lesson1 = Lesson(timetable, term1, "WDZC - CWP", "mgr Golizda", 2)
        term2 = Term(Day.TUE, 13, 0)
        lesson2 = Lesson(timetable, term2, "Analiza", "dr Cichacz", 2)

        print(timetable)
        for key in timetable.dictionary:
            print(f"key: {key}")
        print("1 hash terminu lekcji: ", hash(lesson2.termin))
        self.assertEqual(lesson2.earlierTime(), True)  # earlierTime pomija wszystkie przerwy wcześniej, zatem lekcja wyląduje nie o 11:20 tylko dopiero o 9:40
        self.assertEqual(lesson2.termin.hour, 9)
        self.assertEqual(lesson2.termin.minute, 40)
        print(timetable)
        for key in timetable.dictionary:
            print(f"key: {key}")
        print("2 hash terminu lekcji (po zmianie terminu): ", hash(lesson2.termin))

        self.assertEqual(lesson2.laterTime(), True)  # laterTime pomija wszystkie przerwy później, zatem lekcja wyląduje nie o 11:20 tylko dopiero z powrotem będzie o 13:00
        self.assertEqual(lesson2.termin.hour, 13)
        self.assertEqual(lesson2.termin.minute, 0)
        print(timetable)
        for key in timetable.dictionary:
            print(f"key: {key}")
        print("3 hash terminu lekcji (po ponownej próbie zmiany terminu): ", hash(lesson2.termin))
        print("===============================")

        term3 = Term(Day.TUE, 14, 40)
        lesson3 = Lesson(timetable, term3, "Kosmologia", "dr Ziemia", 2)

        self.assertEqual(lesson2.laterTime(), False)  # o 14:40 jest Kosmologia, zatem nie można przesunąć tej lekcji na później wykorzystując pomijanie przerw
        self.assertEqual(lesson2.termin.hour, 13)
        self.assertEqual(lesson2.termin.minute, 0)

        term4 = Term(Day.TUE, 9, 40)
        lesson4 = Lesson(timetable, term4, "Anatomia", "dr Ręka", 2)

        self.assertEqual(lesson2.earlierTime(), False)  # o 9:40 jest Anatomia, zatem nie można przesunąć tej lekcji na wcześniej wykorzystując pomijanie przerw
        self.assertEqual(lesson2.termin.hour, 13)
        self.assertEqual(lesson2.termin.minute, 0)

    def test_print(self):
        break_list = [Test_TestAll.break1, Test_TestAll.break2, Test_TestAll.break3, Test_TestAll.break4, Test_TestAll.break5, Test_TestAll.break6, Test_TestAll.break7]
        timetable = TimetableWithBreaks(True, break_list)

        # Odchaczyłem te lekcje, które nachodzą na czas przerwy

        term1 = Term(Day.MON, 11, 20)
        lesson1 = Lesson(timetable, term1, "WDZC - CWP", "mgr Golizda", 2)
        # term2 = Term(Day.MON, 18, 20)
        # lesson2 = Lesson(timetable, term2, "Prog skryp - wykl", "dr Stanisław Polak", 2)
        term3 = Term(Day.TUE, 9, 40)
        lesson3 = Lesson(timetable, term3, "Krypto - wykl", "dr Paweł Topa", 2)
        term4 = Term(Day.TUE, 14, 40)
        lesson4 = Lesson(timetable, term4, "blsk - CWL", "mgr Rząsa", 2)
        term5 = Term(Day.TUE, 16, 20)
        lesson5 = Lesson(timetable, term5, "Fizyka - CWL", "dr Dyndał", 2)
        term6 = Term(Day.WED, 9, 40)
        lesson6 = Lesson(timetable, term6, "Krypto - CWP", "dr Paweł Topa", 2)
        term7 = Term(Day.WED, 11, 20)
        lesson7 = Lesson(timetable, term7, "Prog skryp - CWA", "dr Stanisław Polak", 2)
        term8 = Term(Day.WED, 13, 0)
        lesson8 = Lesson(timetable, term8, "Fizyka - CWA", "dr Gabriela Lewińska", 2)
        # term9 = Term(Day.WED, 18, 20)
        # lesson9 = Lesson(timetable, term9, "Inf Sl - CWL/P", "mgr Kamil Jurczyk", 2)
        term10 = Term(Day.THU, 11, 20)
        lesson10 = Lesson(timetable, term10, "WDZC - CWL", "mgr Golizda", 2)
        term11 = Term(Day.THU, 13, 0)
        lesson11 = Lesson(timetable, term11, "Fizyka - wykl", "prof Katarzyna Zakrzewska", 2)
        # term12 = Term(Day.THU, 16, 40)
        # lesson12 = Lesson(timetable, term12, "InfSl/WDZC - wykl", "dr Faber/mgr Golizda", 2)
        # term13 = Term(Day.THU, 18, 20)
        # lesson13 = Lesson(timetable, term13, "Sysopy - wykl", "dr Krzysztof Rzecki ", 2)
        term14 = Term(Day.FRI, 8, 0)
        lesson14 = Lesson(timetable, term14, "blsk - wykl", "dr Mirosław Kantor", 2)
        term15 = Term(Day.FRI, 11, 20)
        lesson15 = Lesson(timetable, term15, "sysopy - CWL", "dr Krzysztof Rzecki", 2)

        # moves = ["t-", "d-", "d+"]
        # actions = timetable.parse(moves)
        # timetable.perform(actions)

        self.assertEqual(timetable.__str__(), """               * Poniedziałek            * Wtorek                 * Środa                  * Czwartek               * Piątek                 * Sobota                 * Niedziela              *
************************************************************************************************************************************************************************************************
8:00 - 9:30    *                         *                        *                        *                        * blsk - wykl            *                        *                        *
************************************************************************************************************************************************************************************************
9:30 - 9:40     ---
************************************************************************************************************************************************************************************************
9:40 - 11:10   *                         * Krypto - wykl          * Krypto - CWP           *                        *                        *                        *                        *
************************************************************************************************************************************************************************************************
11:10 - 11:20   ---
************************************************************************************************************************************************************************************************
11:20 - 12:50  * WDZC - CWP              *                        * Prog skryp - CWA       * WDZC - CWL             * sysopy - CWL           *                        *                        *
************************************************************************************************************************************************************************************************
12:50 - 13:00   ---
************************************************************************************************************************************************************************************************
13:00 - 14:30  *                         *                        * Fizyka - CWA           * Fizyka - wykl          *                        *                        *                        *
************************************************************************************************************************************************************************************************
14:30 - 14:40   ---
************************************************************************************************************************************************************************************************
14:40 - 16:10  *                         * blsk - CWL             *                        *                        *                        *                        *                        *
************************************************************************************************************************************************************************************************
16:10 - 16:20   ---
************************************************************************************************************************************************************************************************
16:20 - 17:50  *                         * Fizyka - CWL           *                        *                        *                        *                        *                        *
************************************************************************************************************************************************************************************************
17:50 - 18:00   ---
************************************************************************************************************************************************************************************************
18:00 - 19:30  *                         *                        *                        *                        *                        *                        *                        *
************************************************************************************************************************************************************************************************
19:30 - 19:40   ---
************************************************************************************************************************************************************************************************
19:40 - 21:10  *                         *                        *                        *                        *                        *                        *                        *
************************************************************************************************************************************************************************************************""")


if __name__ == '__main__':
    unittest.main()
