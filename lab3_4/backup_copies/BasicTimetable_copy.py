
from abc import ABC, abstractmethod
from typing import List
import sys
sys.path.append("/home/przemek/PycharmProjects/ps")
from lab3_4.DeanerySystem.term import Term, DayToStr
from lab3_4.lesson import Lesson
from lab3_4.DeanerySystem.day import Day, nthDayFrom, Action


class NoRecordError(Exception):
    def __init__(self):
        message = "There are no lessons rocorded"
        self.message = message
        super().__init__(self.message)


class BasicTimetable(ABC):

    def __init__(self):
        self.timetable = []
        self.secret = 10

    def busy(self, term: Term) -> bool:

        # print("Potencjalny termin: ", term)

        t_min_start = term.hour * 60 + term.minute  # godzina rozpoczęcia terminu w minutach
        t_min_end = t_min_start + term.duration  # godzina zakończenia terminu w minutach

        for lesson in self.timetable:
            # print("lesson: ", lesson)
            if term.day == lesson.termin.day:
                # print("t_min_start: ", t_min_start)
                # print("t_min_end: ", t_min_end)
                l_min_start = lesson.termin.hour * 60 + lesson.termin.minute  # godzina rozpoczęcia lekcji w minutach
                l_min_end = l_min_start + lesson.termin.duration  # godzina zakończenia lekcji w minutach
                # print("l_min_start: ", l_min_start)
                # print("l_min_end: ", l_min_end)
                if t_min_start < l_min_start or t_min_start >= l_min_end:
                    if t_min_end <= l_min_start or t_min_end > l_min_end:
                        if not (t_min_start < l_min_start and t_min_end > l_min_end):
                            pass
                        else:
                            # print(f"Termin jest zajęty. Kolizja z {lesson}")
                            return False
                        pass
                    else:
                        # print(f"Termin jest zajęty. Kolizja z {lesson}")
                        return False
                else:
                    # print(f"Termin jest zajęty. Kolizja z {lesson}")
                    return False
        # print("Termin jest wolny")
        return True
##########################################################

    @abstractmethod
    def get(self, term: Term) -> Lesson:
        pass
##########################################################

    def parse(self, actions: List[str]) -> List[Action]:

        moves = []
        for i in actions:
            if i == "d-":
                moves.append(Action.DAY_EARLIER)
            elif i == "d+":
                moves.append(Action.DAY_LATER)
            elif i == "t-":
                moves.append(Action.TIME_EARLIER)
            elif i == "t+":
                moves.append(Action.TIME_LATER)
            else:
                raise ValueError(f"Translation {i} is incorrect")
                pass
        return moves
##########################################################

    def perform(self, actions: List[Action]):

        all_les = len(self.timetable)

        for i in range(len(actions)):
            # print("\ncur_action: ", actions[i])
            les_i = i % all_les
            # print("i: ", i)
            # print("Rozpatrywana lekcja: ", self.timetable[les_i])
            if actions[i].value == 0:
                # print("============== Zachodzi earlier.Day =================")
                Lesson.earlierDay(self.timetable[les_i])
            elif actions[i].value == 1:
                # print("============== Zachodzi later.Day =================")
                Lesson.laterDay(self.timetable[les_i])
            elif actions[i].value == 2:
                # print("============== Zachodzi earlier.Time =================")
                Lesson.earlierTime(self.timetable[les_i])
            elif actions[i].value == 3:
                # print("============== Zachodzi later.Time =================")
                Lesson.laterTime(self.timetable[les_i])
##########################################################

    @abstractmethod
    def put(self, lesson: Lesson) -> bool:
        pass


# class Timetable(BasicTimetable):
#
#     #                                              hours for friday
#     ft_limit = [Day.MON, Day.THU, [8, 0], [20, 0], [8, 0], [17, 0]]
#     pt_limit = [Day.SAT, Day.SUN, [8, 0], [20, 0], [17, 0], [20, 0]]
#
#     def __init__(self):
#         self.timetable = []
#     def parse(self, actions):
#
#         moves = []
#         for i in actions:
#             if i == "d-":
#                 moves.append(Action.DAY_EARLIER)
#             elif i == "d+":
#                 moves.append(Action.DAY_LATER)
#             elif i == "t-":
#                 moves.append(Action.TIME_EARLIER)
#             elif i == "t+":
#                 moves.append(Action.TIME_LATER)
#             else:
#                 pass
#         return moves
#
#     def perform(self, actions):
#
#         all_les = len(self.timetable)
#
#         for i in range(len(actions)):
#             print("\ncur_action: ", actions[i])
#             les_i = i % all_les
#             print("i: ", i)
#             print("Rozpatrywana lekcja: ", self.timetable[les_i])
#             if actions[i].value == 0:
#                 print("============== Zachodzi earlier.Day =================")
#                 Lesson.earlierDay(self.timetable[les_i])
#             elif actions[i].value == 1:
#                 print("============== Zachodzi later.Day =================")
#                 Lesson.laterDay(self.timetable[les_i])
#             elif actions[i].value == 2:
#                 print("============== Zachodzi earlier.Time =================")
#                 Lesson.earlierTime(self.timetable[les_i])
#             elif actions[i].value == 3:
#                 print("============== Zachodzi later.Time =================")
#                 Lesson.laterTime(self.timetable[les_i])
#
#     def busy(self, term):
#
#         print("Potencjalny termin: ", term)
#
#         t_min_start = term.hour * 60 + term.minute  # godzina rozpoczęcia terminu w minutach
#         t_min_end = t_min_start + term.duration  # godzina zakończenia terminu w minutach
#
#         for lesson in self.timetable:
#             # print("lesson: ", lesson)
#             if term.day == lesson.termin.day:
#                 # print("t_min_start: ", t_min_start)
#                 # print("t_min_end: ", t_min_end)
#                 l_min_start = lesson.termin.hour * 60 + lesson.termin.minute  # godzina rozpoczęcia lekcji w minutach
#                 l_min_end = l_min_start + lesson.termin.duration  # godzina zakończenia lekcji w minutach
#                 # print("l_min_start: ", l_min_start)
#                 # print("l_min_end: ", l_min_end)
#                 if t_min_start < l_min_start or t_min_start >= l_min_end:
#                     if t_min_end <= l_min_start or t_min_end > l_min_end:
#                         if not (t_min_start < l_min_start and t_min_end > l_min_end):
#                             pass
#                         else:
#                             print(f"Termin jest zajęty. Kolizja z {lesson}")
#                             return False
#                         pass
#                     else:
#                         print(f"Termin jest zajęty. Kolizja z {lesson}")
#                         return False
#                 else:
#                     print(f"Termin jest zajęty. Kolizja z {lesson}")
#                     return False
#         print("Termin jest wolny")
#         return True
#
#     def put(self, lesson: Lesson) -> bool:
#
#         print("kot")
#         #
#         # if Timetable.can_be_transferred_to(self, lesson.termin, lesson.fulltime):
#         #     self.timetable.append(lesson)
#         #     return True
#         # else:
#         #     print("Lesson couldn't be added. Timetable slot is already occupied "
#         #           "or this lesson term do not fit in the fulltime/parttime scheme")
#         #     return False


# Sprawdź, czy można tworzyć instancję klasy abstrakcyjnej — 'BasicTimetable'
# timeTable = BasicTimetable()

# Sprawdź, czy można tworzyć instancję klasy pochodnej — 'Timetable'
# timeTable = Timetable()

# Wywołujemy metodę, która NIE JEST zdefiniowana w klasie 'Timetable', a w klasie 'BasicTimetable'

# term1 = Term(Day.MON, 8, 0)
# timeTable.get(term1)
