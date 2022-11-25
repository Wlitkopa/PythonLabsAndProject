import zadanie1
from zadanie1 import Operacje
import unittest
from unittest.mock import patch
import io
import sys


def test_sum_print1():
    op = Operacje()
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    op.suma(1, 2, 3)
    sys.stdout = sys.__stdout__
    if capturedOutput.getvalue() == "1 + 2 + 3 = 6\n":
        print("test_sum_print1 passed")
    else:
        print(f"ERROR:\n'{capturedOutput.getvalue()}' does not equal with '1 + 2 + 3 = 6\n'")


def test_sum_print2():
    op = Operacje()
    capturedOutput = io.StringIO()  # Create StringIO object
    sys.stdout = capturedOutput  # and redirect stdout.
    op.suma(1, 2)  # Call unchanged function.
    sys.stdout = sys.__stdout__
    if capturedOutput.getvalue() == "1 + 2 + 4 = 7\n":
        print("test_sum_print2 passed")
    else:
        print(f"ERROR:\n'{capturedOutput.getvalue()}' does not equal with '1 + 2 + 4 = 7\n'")


def test_sum_print3():
    op = Operacje()
    capturedOutput = io.StringIO()  # Create StringIO object
    sys.stdout = capturedOutput  # and redirect stdout.
    op.suma(1)  # Call unchanged function.
    sys.stdout = sys.__stdout__
    if capturedOutput.getvalue() == "1 + 4 + 5 = 10\n":
        print("test_sum_print3 passed")
    else:
        print(f"ERROR:\n'{capturedOutput.getvalue()}' does not equal with '1 + 4 + 5 = 10\n'")


def test_dif_print1():
    op = Operacje()
    capturedOutput = io.StringIO()  # Create StringIO object
    sys.stdout = capturedOutput  # and redirect stdout.
    op.roznica(2, 1)  # Call unchanged function.
    sys.stdout = sys.__stdout__
    if capturedOutput.getvalue() == "2 - 1 = 1\n":
        print("test_dif_print1 passed")
    else:
        print(f"ERROR:\n'{capturedOutput.getvalue()}' does not equal with '2 - 1 = -1\n'")


def test_dif_print2():
    op = Operacje()
    capturedOutput = io.StringIO()  # Create StringIO object
    sys.stdout = capturedOutput  # and redirect stdout.
    op.roznica(2)  # Call unchanged function.
    sys.stdout = sys.__stdout__
    if capturedOutput.getvalue() == "2 - 4 = -2\n":
        print("test_dif_print2 passed")
    else:
        print(f"ERROR:\n'{capturedOutput.getvalue()}' does not equal with '2 - 4 = -2\n'")


def test_sum_ch_print1():
    op = Operacje()
    op['suma'] = [1, 2]
    op['roznica'] = [1, 2, 3]
    capturedOutput = io.StringIO()  # Create StringIO object
    sys.stdout = capturedOutput  # and redirect stdout.
    op.suma(1, 2)  # Call unchanged function.
    sys.stdout = sys.__stdout__
    if capturedOutput.getvalue() == "1 + 2 + 1 = 4\n":
        print("test_sum_ch_print1 passed")
    else:
        print(f"ERROR:\n'{capturedOutput.getvalue()}' does not equal with '1 + 2 + 1 = 4\n'")


def test_sum_ch_print2():
    op = Operacje()
    op['suma'] = [1, 2]
    op['roznica'] = [1, 2, 3]
    capturedOutput = io.StringIO()  # Create StringIO object
    sys.stdout = capturedOutput  # and redirect stdout.
    op.suma(1)  # Call unchanged function.
    sys.stdout = sys.__stdout__
    if capturedOutput.getvalue() == "1 + 1 + 2 = 4\n":
        print("test_sum_ch_print1 passed")
    else:
        print(f"ERROR:\n'{capturedOutput.getvalue()}' does not equal with '1 + 1 + 2 = 4\n'")


def test_dif_ch_print1():
    op = Operacje()
    op['suma'] = [1, 2]
    op['roznica'] = [1, 2, 3]
    capturedOutput = io.StringIO()  # Create StringIO object
    sys.stdout = capturedOutput  # and redirect stdout.
    op.roznica(5)  # Call unchanged function.
    sys.stdout = sys.__stdout__
    if capturedOutput.getvalue() == "5 - 1 = 4\n":
        print("test_sum_ch_print1 passed")
    else:
        print(f"ERROR:\n'{capturedOutput.getvalue()}' does not equal with '5 - 1 = 4\n'")


def Custom_Tests():

    test_sum_print1()
    test_sum_print2()
    test_sum_print3()
    test_dif_print1()
    test_dif_print2()
    print("\nPo zmianach list sumy i różnicy:\n")
    test_sum_ch_print1()
    test_sum_ch_print2()
    test_dif_ch_print1()


class Test_TestDecorators(unittest.TestCase):
    op = Operacje()

    def test_wynik(self):

        # print(f"Test_TestDecorators.op.argumentySuma: {Test_TestDecorators.op.argumentySuma}")
        Test_TestDecorators.op['suma'] = [4, 5]
        Test_TestDecorators.op['roznica'] = [4, 5, 6]

        self.assertEqual(Test_TestDecorators.op.suma(1, 2, 3), 4)
        self.assertEqual(Test_TestDecorators.op.suma(1, 2), 5)
        self.assertEqual(Test_TestDecorators.op.suma(1), "All used")

        Test_TestDecorators.op['suma'] = [1, 2]
        Test_TestDecorators.op['roznica'] = [1, 2, 3]

        self.assertEqual(Test_TestDecorators.op.roznica(2, 1), 1)
        self.assertEqual(Test_TestDecorators.op.roznica(2), 2)
        self.assertEqual(Test_TestDecorators.op.roznica(), 3)

    def test_exceptions(self):

        with self.assertRaises(TypeError):
            Test_TestDecorators.op.suma()


if __name__ == '__main__':
    Custom_Tests()
    unittest.main()
