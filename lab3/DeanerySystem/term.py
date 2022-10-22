
import sys

sys.path.append('/home/przemek/PycharmProjects/ps/lab3/DeanerySystem')

from day import Day


def DayToStr(dzien):
    name = ""
    if dzien == 0:
        name = "Poniedziałek"
    elif dzien == 1:
        name = "Wtorek"
    elif dzien == 2:
        name = "Środa"
    elif dzien == 3:
        name = "Czwartek"
    elif dzien == 4:
        name = "Piatek"
    elif dzien == 5:
        name = "Sobota"
    elif dzien == 6:
        name = "Niedziela"
    return name


class Term:

    def __init__(self, day, hour, minute):
        self.hour = hour
        self.minute = minute
        self.duration = 90
        self.__day = day
        # print("self.__day: ", self.__day)
        # print("self.__day.value: ", self.__day.value)

    def __str__(self):
        return f"{DayToStr(self.__day)} {self.hour}:{self.minute} [{self.duration}]"

    def earlierThan(self, termin):
        if self.__day.value < termin.__day.value:
            return True
        elif self.__day.value > termin.__day.value:
            return False
        else:
            mins = self.minute + 60 * self.hour
            mint = termin.minute + 60 * termin.hour

            if mins < mint:
                return True
            else:
                return False

    def laterThan(self, termin):
        if self.__day.value > termin.__day.value:
            return True
        elif self.__day.value < termin.__day.value:
            return False
        else:
            mins = self.minute + 60 * self.hour
            mint = termin.minute + 60 * termin.hour

            if mins > mint:
                return True
            else:
                return False

    def equals(self, termin):
        if self.__day == termin.__day and self.hour == termin.hour and self.minute == termin.minute:
            return True
        else:
            return False

