
import sys
from typing import List
sys.path.append("/home/przemek/PycharmProjects/ps")
# import day
from lab3_4.DeanerySystem.day import Day, nthDayFrom, Action
# import term
from lab3_4.DeanerySystem.term import Term, DayToStr
# sys.path.append("/home/przemek/PycharmProjects/ps")
from lab3_4.lesson import Lesson


class Break:

    def __init__(self, term):
        self.term = term
        # print(f"self.term.day: {self.term.day}")

    def __str__(self):
        return "---"

    def getTerm(self):
        return self.term


