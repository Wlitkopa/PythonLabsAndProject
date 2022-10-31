
from DeanerySystem import day
from DeanerySystem.day import Day, nthDayFrom
from DeanerySystem import term
from DeanerySystem.term import Term, DayToStr
from enum import Enum, IntEnum


def yeartoString(year):
    if int(year) == 1:
        return "Pierwszy"
    elif int(year) == 2:
        return "Drugi"
    elif int(year) == 3:
        return "Trzeci"
    elif int(year) == 4:
        return "Czwarty"
    elif int(year) == 5:
        return "Piąty"
    elif int(year) == 6:
        return "Szósty"
    elif int(year) == 7:
        return "Siódmy"


def sctoStrign(sc): # sc - studies category (fulltime, parttime)
    if sc:
        return "stacjonarnych"
    else:
        return "niesacjonarnych"


class Lesson:

    #                                              hours for friday
    ft_limit = [Day.MON, Day.THU, [8, 0], [20, 0], [8, 0], [17, 0]]
    pt_limit = [Day.SAT, Day.SUN, [8, 0], [20, 0], [17, 0], [20, 0]]
    entries = []

    def __init__(self, term, name, teacherName, year, fulltime=None):

        self.term = term
        self.name = str(name)
        self.teacherName = str(teacherName)
        self.year = int(year)

        if fulltime is not None:
            self.fulltime = False
        else:
            self.fulltime = True
        Lesson.entries.append(self)

    def __str__(self):
        minutes = int(int(self.term.duration) % 60)
        hours = int((int(self.term.duration) - minutes)/60)
        new_minute = (int(self.term.minute) + minutes) % 60
        new_hour = int(self.term.hour) + hours + int((int(self.term.minute) + minutes - new_minute)/60)

        if new_minute == 0:
            new_minute = str('00')

        return f"{self.name} ({DayToStr(self.term._Term__day)} {self.term.hour}:{self.term.minute} - {new_hour}:{new_minute})" \
               f"\n{yeartoString(self.year)} rok studiów {sctoStrign(self.fulltime)}" \
               f"\nProwadzący: {self.teacherName}"

    @staticmethod
    def busy(termin):
        t_min_start = termin.hour*60 + termin.minute  # godzina rozpoczęcia terminu w minutach
        t_min_end = t_min_start + termin.duration  # godzina zakończenia terminu w minutach

        for lesson in Lesson.entries:
            print("lesson: ", lesson)
            if termin._Term__day == lesson.term._Term__day:
                print("t_min_start: ", t_min_start)
                print("t_min_end: ", t_min_end)
                l_min_start = lesson.term.hour * 60 + lesson.term.minute  # godzina rozpoczęcia lekcji w minutach
                l_min_end = l_min_start + lesson.term.duration  # godzina zakończenia lekcji w minutach
                print("l_min_start: ", l_min_start)
                print("l_min_end: ", l_min_end)
                if t_min_start < l_min_start or t_min_start >= l_min_end:
                    if t_min_end <= l_min_start or t_min_end > l_min_end:
                        if not (t_min_start < l_min_start and t_min_end > l_min_end):
                            pass
                        else:
                            return False
                        pass
                    else:
                        return False
                else:
                    return False
        return True

    @staticmethod
    def fit(termin, fulltime):
        limit = []
        if fulltime:
            limit = Lesson.ft_limit
        else:
            limit = Lesson.pt_limit
        t_min_start = termin.hour * 60 + termin.minute  # godzina rozpoczęcia terminu w minutach
        t_min_end = t_min_start + termin.duration  # godzina zakończenia terminu w minutach
        # print("Lesson.ft_limit[0].value (czyli monday): ", limit[0].value)
        # print("termin._Term__day: ", termin._Term__day)
        # print("Lesson.ft_limit[0].value: ", Lesson.ft_limit[0].value)
        # print("Lesson.ft_limit[1].value: ", Lesson.ft_limit[1].value)

        if limit[0].value <= termin._Term__day <= limit[1].value:
            print("Zaszedł if")
            z_min_start = limit[2][0]*60 + limit[2][1]  # godzina rozpoczęcia zajęć pn-czw w minutach
            z_min_end = limit[3][0]*60 + limit[3][1]  # godzina zakończenia zajęć pn-czw w minutach
            if z_min_start <= t_min_start < z_min_end and z_min_start <= t_min_end < z_min_end:
                return True
        elif termin._Term__day == Day.FRI.value:
            print("Zaszedł elif")
            z_min_start = limit[4][0] * 60 + limit[4][1]  # godzina rozpoczęcia zajęć pt w minutach
            z_min_end = limit[5][0] * 60 + limit[5][1]  # godzina zakończenia zajęć pt w minutach
            if z_min_start <= t_min_start < z_min_end and z_min_start <= t_min_end < z_min_end:
                return True
        return False

    def earlierDay(self):
        Day.new_day = (self.term._Term__day.value + 6) % 7

        temp_term = Term(Day.new_day, self.term.hour, self.term.minute, self.term.duration)

        # print("temp_term: ", temp_term)
        #
        # if self.fulltime:
        #     state = "fulltime"
        # else:
        #     state = "parttime"
        #
        # if Lesson.busy(temp_term):
        #     print("Termin jest wolny")
        # else:
        #     print("Termin jest zajęty")
        #
        # if Lesson.fit(temp_term, self.fulltime):
        #     print(f"Ten termin zawiera się w ograniczeniu czasowym {state}")
        # else:
        #     print(f"Ten termin nie jest w ograniczeniu czasowym {state}")

        if Lesson.busy(temp_term) and Lesson.fit(temp_term, self.fulltime):
            self.term = temp_term
            print(f"\n\nPo zmianach: {self}\n\n")
            return True
        else:
            return False


    def laterDay(self):
        Day.new_day = (self.term._Term__day.value + 1) % 7

        temp_term = Term(Day.new_day, self.term.hour, self.term.minute, self.term.duration)

        # print("temp_term: ", temp_term)
        #
        # if self.fulltime:
        #     state = "fulltime"
        # else:
        #     state = "parttime"
        #
        # if Lesson.busy(temp_term):
        #     print("Termin jest wolny")
        # else:
        #     print("Termin jest zajęty")
        #
        # if Lesson.fit(temp_term, self.fulltime):
        #     print(f"Ten termin zawiera się w ograniczeniu czasowym {state}")
        # else:
        #     print(f"Ten termin nie jest w ograniczeniu czasowym {state}")

        if Lesson.busy(temp_term) and Lesson.fit(temp_term, self.fulltime):
            self.term = temp_term
            print(f"\n\nPo zmianach: {self}\n\n")
            return True
        else:
            return False

    def earlierTime(self):
        minutes = int(int(self.term.duration) % 60)
        hours = int((int(self.term.duration) - minutes) / 60)
        new_minute = int(self.term.minute) - minutes
        if new_minute < 0:
            hours += 1
            new_minute += 60
        new_hour = int(self.term.hour) - hours

        temp_term = Term(self.term._Term__day, new_hour, new_minute, self.term.duration)

        print("temp_term: ", temp_term)

        # print("temp_term: ", temp_term)
        #
        # if self.fulltime:
        #     state = "fulltime"
        # else:
        #     state = "parttime"
        #
        # if Lesson.busy(temp_term):
        #     print("Termin jest wolny")
        # else:
        #     print("Termin jest zajęty")
        #
        # if Lesson.fit(temp_term, self.fulltime):
        #     print(f"Ten termin zawiera się w ograniczeniu czasowym {state}")
        # else:
        #     print(f"Ten termin nie jest w ograniczeniu czasowym {state}")

        if Lesson.busy(temp_term) and Lesson.fit(temp_term, self.fulltime):
            self.term = temp_term
            print(f"\n\nPo zmianach: {self}\n\n")
            return True
        else:
            return False

    def laterTime(self):
        minutes = int(int(self.term.duration) % 60)
        hours = int((int(self.term.duration) - minutes) / 60)
        new_minute = (int(self.term.minute) + minutes) % 60
        new_hour = int(self.term.hour) + hours + int((int(self.term.minute) + minutes - new_minute) / 60)

        temp_term = Term(self.term._Term__day, new_hour, new_minute, self.term.duration)

        print("temp_term: ", temp_term)


        # print("temp_term: ", temp_term)
        #
        # if self.fulltime:
        #     state = "fulltime"
        # else:
        #     state = "parttime"
        #
        # if Lesson.busy(temp_term):
        #     print("Termin jest wolny")
        # else:
        #     print("Termin jest zajęty")
        #
        # if Lesson.fit(temp_term, self.fulltime):
        #     print(f"Ten termin zawiera się w ograniczeniu czasowym {state}")
        # else:
        #     print(f"Ten termin nie jest w ograniczeniu czasowym {state}")

        if Lesson.busy(temp_term) and Lesson.fit(temp_term, self.fulltime):
            self.term = temp_term
            print(f"\n\nPo zmianach: {self}\n\n")
            return True
        else:
            return False

