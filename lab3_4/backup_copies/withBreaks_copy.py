
import sys
from typing import List
sys.path.append("/home/przemek/PycharmProjects/ps")
# import day
from lab3_4.DeanerySystem.day import Day, nthDayFrom, Action
# import term
from lab3_4.DeanerySystem.term import Term, DayToStr
# import Break
from lab3_4.DeanerySystem.Break import Break
# sys.path.append("/home/przemek/PycharmProjects/ps")
from lab3_4.lesson import Lesson


class TimetableWithBreaks:
    """ Class containing a set of operations to manage the timetable """

    #                                              hours for friday
    ft_limit = [Day.MON, Day.THU, [8, 0], [20, 0], [8, 0], [17, 0]]
    pt_limit = [Day.SAT, Day.SUN, [8, 0], [20, 0], [17, 0], [20, 0]]

    def __init__(self, skipBreaks=False, breaks=None):
        self.timetable = []
        self.breaks = breaks
        self.skipBreaks = skipBreaks

    def can_be_transferred_to(self, term: Term, fullTime: bool, laterTime=None, put=False) -> bool:

        if not put:

            if laterTime:

                while True:

                    cnt = 0
                    t_min_start = term.hour * 60 + term.minute  # godzina rozpoczęcia terminu w minutach
                    t_min_end = t_min_start + term.duration  # godzina zakończenia terminu w minutach

                    for pot_break in self.breaks:
                        cnt += 1
                        break_min_start = 60 * pot_break.term.hour + pot_break.term.minute
                        break_min_end = break_min_start + pot_break.term.duration

                        if t_min_start <= break_min_start < t_min_end or t_min_start < break_min_end <= t_min_end:
                            print("Potencjalny termini nowej lekcji nachodzi na przerwę")
                            if not self.skipBreaks:
                                print("skipBreaks ma wartość False. Nie można pomijać przerw")
                                return False

                            else:
                                break_minutes = int(break_min_end % 60)
                                break_hours = int(int(break_min_end - break_minutes)/60)
                                term.hour = break_hours
                                term.minute = break_minutes
                                cnt = 0
                                break

                    if cnt == len(self.breaks):
                        break
            else:

                while True:

                    cnt = 0
                    t_min_start = term.hour * 60 + term.minute  # godzina rozpoczęcia terminu w minutach
                    t_min_end = t_min_start + term.duration  # godzina zakończenia terminu w minutach

                    for pot_break in self.breaks:
                        cnt += 1
                        break_min_start = 60 * pot_break.term.hour + pot_break.term.minute
                        break_min_end = break_min_start + pot_break.term.duration

                        if t_min_start <= break_min_start < t_min_end or t_min_start < break_min_end <= t_min_end:
                            print("Potencjalny termini nowej lekcji nachodzi na przerwę")
                            if not self.skipBreaks:
                                print("skipBreaks ma wartość False. Nie można pomijać przerw")
                                return False

                            else:

                                t_min_start -= pot_break.term.duration
                                new_start_min = int(t_min_start % 60)
                                new_start_hour = int(int(t_min_start - new_start_min) / 60)
                                term.hour = new_start_hour
                                term.minute = new_start_min
                                cnt = 0
                                break

                    if cnt == len(self.breaks):
                        break

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
                            print(f"Termin jest zajęty. Kolizja z {lesson}")
                            return False
                        pass
                    else:
                        print(f"Termin jest zajęty. Kolizja z {lesson}")
                        return False
                else:
                    print(f"Termin jest zajęty. Kolizja z {lesson}")
                    return False
        print("Termin jest wolny")
        return True

    def put(self, lesson: Lesson) -> bool:

        lesson_min_start = 60*lesson.termin.hour + lesson.termin.minute
        lesson_min_end = lesson_min_start + lesson.termin.duration

        if TimetableWithBreaks.can_be_transferred_to(self, lesson.termin, lesson.fulltime, None, True):

            for pot_break in self.breaks:
                # print("Sprawdzam przerwę: ", pot_break.getTerm())
                # print("Dla lekcji: ", lesson)
                # print("\n\n")
                break_min_start = 60*pot_break.term.hour + pot_break.term.minute
                break_min_end = break_min_start + pot_break.term.duration

                if lesson_min_start <= break_min_start < lesson_min_end or lesson_min_start < break_min_end <= lesson_min_end:
                    print("Lekcja nachodzi na przerwę")
                    return False

            self.timetable.append(lesson)
            return True
        else:
            print("Lesson couldn't be added. Timetable slot is already occupied "
                  "or this lesson term do not fit in the fulltime/parttime scheme")
            return False

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
                pass
        return moves

    def perform(self, actions: List[Action]):

        all_les = len(self.timetable)

        for i in range(len(actions)):
            print("\ncur_action: ", actions[i])
            les_i = i % all_les
            print("i: ", i)
            print("Rozpatrywana lekcja: ", self.timetable[les_i])
            if actions[i].value == 0:
                print("============== Zachodzi earlier.Day =================")
                Lesson.earlierDay(self.timetable[les_i])
            elif actions[i].value == 1:
                print("============== Zachodzi later.Day =================")
                Lesson.laterDay(self.timetable[les_i])
            elif actions[i].value == 2:
                print("============== Zachodzi earlier.Time =================")
                Lesson.earlierTime(self.timetable[les_i])
            elif actions[i].value == 3:
                print("============== Zachodzi later.Time =================")
                Lesson.laterTime(self.timetable[les_i])

    def get(self, term: Term, new_hour=None, new_min=None) -> Lesson:
        t_min_start = term.hour * 60 + term.minute  # godzina rozpoczęcia terminu w minutach

        if new_hour is None:
            t_min_end = t_min_start + term.duration  # godzina zakończenia terminu w minutach
        else:
            t_min_end = 60*new_hour + new_min

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
        output = ""
        basic_hour = 8
        basic_min = 0
        basic_minutes = int(60*basic_hour + basic_min)

        star = "*"
        space = " "

        output = f'               * Poniedziałek            * Wtorek                 * Środa                  * Czwartek               * Piątek                 * Sobota                 * Niedziela              *'
        defa_len = len(output)
        cell_len = len("Podstawy programowania  ")
        # print("cell_len: ", cell_len)
        output += f'\n{star*defa_len}'

        # for i in range(8):
        while True:

            breaks_list = self.breaks
            # print("self.breaks: ", self.breaks)
            # print("breaks_list: ", breaks_list)
            temp_break_list = breaks_list.copy()
            pot_new_minutes = int(basic_min) + 60*int(basic_hour) + 90
            cur_break_min = 0
            break_index = 0

            # print(f"\nStarting hour: {basic_hour}:{basic_min}")

            for j in range(len(temp_break_list)):
                if temp_break_list is not None:
                    break_min = temp_break_list[j].term.minute + 60*temp_break_list[j].term.hour
                    # print(f"break time: {temp_break_list[j].term.hour}:{temp_break_list[j].term.minute}")
                    # print(f"break: {temp_break_list[j]}")
                    if int(basic_min + 60*basic_hour) <= break_min < pot_new_minutes:
                        if int(basic_min + 60*basic_hour) == break_min:
                            cur_break_min = -1
                            break_index = j
                            break
                        # print("Zaszedł if")
                        cur_break_min = break_min
                        pot_new_minutes = break_min
                        potm = int(pot_new_minutes % 60)
                        poth = int(int(pot_new_minutes - potm) / 60)
                        # print(f"potencjalna nowa godzina zakończenia lekcji: {poth}:{potm}")
                        break_index = j
                        temp_break_list[j] = None

            old_minutes = pot_new_minutes

            # print(f"breaks_list: {breaks_list}")
            new_minutes = pot_new_minutes
            if cur_break_min == 0:
                basic_minutes = pot_new_minutes
            elif cur_break_min == -1:
                # print("Zaszedł cur_break_min == -1")
                temp_old = basic_minutes
                basic_minutes += breaks_list[break_index].term.duration
                new_minutes = temp_old
                new_min = int(new_minutes % 60)
                new_hour = int(int(new_minutes - new_min) / 60)
                basic_min = int(basic_minutes % 60)
                basic_hour = int(int(basic_minutes - basic_min) / 60)
                temp_new_min = str(new_min)
                temp_basic_min = str(basic_min)
                if basic_min == 0:
                    # print("Działam")
                    temp_basic_min = "00"
                if new_min == 0:
                    # print("Działam")
                    temp_new_min = "00"
                new_set = str(f"{new_hour}:{temp_new_min} - {basic_hour}:{temp_basic_min}")
                output += "\n"
                output += f"{new_set:15} {str(breaks_list[break_index])}"
                output += f"\n{star * defa_len}"

                continue
            else:
                # print("Dodaję duration")
                # print(f"cur_break_min: {cur_break_min}")
                basic_minutes = pot_new_minutes + breaks_list[break_index].term.duration

            new_min = int(new_minutes % 60)
            new_hour = int(int(new_minutes - new_min)/60)

            temp_new_min = str(new_min)
            temp_basic_min = str(basic_min)
            if basic_min == 0:
                print("Działam")
                temp_basic_min = "00"
            if new_min == 0:
                print("Działam")
                temp_new_min = "00"

            new_set = str(f"{basic_hour}:{temp_basic_min} - {new_hour}:{temp_new_min}")
            output += "\n"
            output += f"{new_set:15}"


            # basic_min = int(basic_minutes % 60)
            # basic_hour = int(int(basic_minutes - basic_min) / 60)


            # minutes = 90 * i
            # new_min = int(minutes % 60)
            # hours = int(8 + (int(minutes) - new_min)/60)



            # if i % 2 == 0:
            #     new_set = str(f"{hours}:00 - {hours + 1}:30")
            #     output += f"{new_set:15}"
            # else:
            #     new_set = str(f"{hours}:30 - {hours + 2}:00")
            #     output += f"{new_set:15}"
            # print(f"\n\nhours: {hours}\nnew_min: {new_min}\n\n")

            # print(f"\nStarting hour: {basic_hour}:{basic_min}")

            for j in range(7):
                cur_term = Term(j, basic_hour, basic_min)
                pot_lesson = self.get(cur_term, new_hour, new_min)
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

            basic_min = int(basic_minutes % 60)
            basic_hour = int(int(basic_minutes - basic_min) / 60)

            if cur_break_min != 0:
                new_minutes = old_minutes
                new_min = int(new_minutes % 60)
                new_hour = int(int(new_minutes - new_min) / 60)
                temp_new_min = str(new_min)
                temp_basic_min = str(basic_min)
                if basic_min == 0:
                    print("Działam")
                    temp_basic_min = "00"
                if new_min == 0:
                    print("Działam")
                    temp_new_min = "00"

                output += "\n"
                new_set = f"{new_hour}:{temp_new_min} - {basic_hour}:{temp_basic_min}"
                output += f"{new_set:15} {str(breaks_list[break_index])}"
                output += f"\n{star * defa_len}"

            if basic_hour >= 20 and basic_min >= 0:
                break
        f = open("tabela.txt", "w")
        f.write(output)
        f.close()
        print("Wszystkie lekcje: ", self.timetable)
        return output


# term1 = Term(Day.MON, 9, 30, 10)
# term2 = Term(Day.TUE, 11, 10, 10)
# term3 = Term(Day.MON, 12, 50, 10)
# term4 = Term(Day.MON, 14, 30, 10)
# break1 = Break(term1)
# break2 = Break(term2)
# break3 = Break(term3)
# break4 = Break(term4)
#
#
# break_list = [break1, break2, break3, break4]
# timetable = TimetableWithoutBreaks(break_list)
# print(timetable)
# print("TimetableWithoutBreaks.list: ", timetable.timetable)

