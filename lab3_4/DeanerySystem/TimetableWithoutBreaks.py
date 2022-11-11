
import sys
from typing import List
sys.path.append("/home/przemek/PycharmProjects/ps")
# import day
from lab3_4.DeanerySystem.day import Day, nthDayFrom, Action
# import term
from lab3_4.DeanerySystem.term import Term, DayToStr
# sys.path.append("/home/przemek/PycharmProjects/ps")
from lab3_4.lesson import Lesson
from lab3_4.DeanerySystem.BasicTimetable import BasicTimetable, NoRecordError


class TimetableWithoutBreaks(BasicTimetable):
    """ Class containing a set of operations to manage the timetable """

    #                                              hours for friday
    ft_limit = [Day.MON, Day.THU, [8, 0], [20, 0], [8, 0], [17, 0]]
    pt_limit = [Day.SAT, Day.SUN, [8, 0], [20, 0], [17, 0], [20, 0]]

    def __init__(self):
        super().__init__()

    def can_be_transferred_to(self, term: Term, fullTime: bool, earlierTime=None) -> bool:

        limit = []
        if fullTime:
            limit = Lesson.ft_limit
        else:
            limit = Lesson.pt_limit
        t_min_start = term.hour * 60 + term.minute  # godzina rozpoczęcia terminu w minutach
        t_min_end = t_min_start + term.duration  # godzina zakończenia terminu w minutach
        # print("\n\nLesson.ft_limit[0].value (czyli monday): ", limit[0].value)
        # print("termin._Term__day: ", term.day)
        # print("Lesson.ft_limit[0].value: ", limit[0].value)
        # print("Lesson.ft_limit[1].value: ", limit[1].value)
        # print("\n\n")

        if limit[0].value <= term.day <= limit[1].value:
            # print("Zaszedł if")
            z_min_start = limit[2][0] * 60 + limit[2][1]  # godzina rozpoczęcia zajęć pn-czw w minutach
            z_min_end = limit[3][0] * 60 + limit[3][1]  # godzina zakończenia zajęć pn-czw w minutach
            if z_min_start <= t_min_start < z_min_end and z_min_start < t_min_end <= z_min_end and self.busy(term):
                return True
        elif term.day == Day.FRI.value:
            # print("Zaszedł elif")
            z_min_start = limit[4][0] * 60 + limit[4][1]  # godzina rozpoczęcia zajęć pt w minutach
            z_min_end = limit[5][0] * 60 + limit[5][1]  # godzina zakończenia zajęć pt w minutach
            if z_min_start <= t_min_start < z_min_end and z_min_start < t_min_end <= z_min_end and self.busy(term):
                return True
        return False

    def put(self, lesson: Lesson) -> bool:

        if TimetableWithoutBreaks.can_be_transferred_to(self, lesson.termin, lesson.fulltime):
            self.timetable.append(lesson)
            self.dictionary[lesson.termin] = lesson
            return True
        else:
            raise ValueError("Lesson couldn't be added. Timetable slot is already occupied "
                             "or this lesson term do not fit in the fulltime/parttime scheme")
            # print("Lesson couldn't be added. Timetable slot is already occupied "
            #       "or this lesson term do not fit in the fulltime/parttime scheme")
            # return False

    def get(self, term: Term) -> Lesson:

        # if isinstance(term, Term):
        #     pass
        # else:
        #     print(type(term))
        #     raise TypeError("term should be class Term object")

        t_min_start = term.hour * 60 + term.minute  # godzina rozpoczęcia terminu w minutach
        t_min_end = t_min_start + term.duration  # godzina zakończenia terminu w minutach

        # print(f"term.Day: {term.day}\nterm.hour: {term.hour}\nterm.minute: {term.minute}\n")

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
                        if not (t_min_start <= l_min_start and t_min_end >= l_min_end):
                            pass
                        else:
                            return lesson
                        pass
                    else:
                        return lesson
                else:
                    return lesson
        return None

    def __str__(self):

        if len(self.timetable) == 0:
            raise NoRecordError()

        output = str()
        star = "*"
        space = " "

        output = f'               * Poniedziałek            * Wtorek                 * Środa                  * Czwartek               * Piątek                 * Sobota                 * Niedziela              *'
        defa_len = len(output)
        cell_len = len("Podstawy programowania  ")
        # print("cell_len: ", cell_len)
        output += f'\n{star*defa_len}'

        for i in range(8):

            output += "\n"
            minutes = 90 * i
            new_min = int(minutes % 60)
            hours = int(8 + (int(minutes) - new_min)/60)

            if i % 2 == 0:
                new_set = str(f"{hours}:00 - {hours + 1}:30")
                output += f"{new_set:15}"
            else:
                new_set = str(f"{hours}:30 - {hours + 2}:00")
                output += f"{new_set:15}"
            # print(f"\n\nhours: {hours}\nnew_min: {new_min}\n\n")
            for j in range(7):
                cur_term = Term(j, hours, new_min)
                pot_lesson = self.get(cur_term)
                # print("pot_lesson: ", pot_lesson)
                if pot_lesson is not None and j == 0:
                    output += f"* {pot_lesson.name:{cell_len}}*"
                elif pot_lesson is not None and j < 7:
                    output += f" {pot_lesson.name:{cell_len - 1}}*"
                elif j == 0:
                    output += f"*{space*int(cell_len + 1)}*"
                else:
                    output += f"{space*int(cell_len)}*"
            output += f"\n{star*defa_len}"
        f = open("tabela.txt", "w")
        f.write(output)
        f.close()
        return output


# timetable = TimetableWithoutBreaks()
# print(timetable)
# print("TimetableWithoutBreaks.list: ", timetable.timetable)

