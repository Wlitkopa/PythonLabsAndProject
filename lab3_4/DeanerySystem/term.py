
import sys

sys.path.append('/lab3_4/DeanerySystem')


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
        name = "Piątek"
    elif dzien == 5:
        name = "Sobota"
    elif dzien == 6:
        name = "Niedziela"
    return name


class BasicTerm:

    def __init__(self, hour, minute, duration=None):
        self.hour = hour
        self.minute = minute
        self.duration = duration

    @property
    def hour(self):
        return self.__hour

    @hour.setter
    def hour(self, hour):
        self.__hour = hour

    @property
    def minute(self):
        return self.__minute

    @minute.setter
    def minute(self, minute):
        self.__minute = minute

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, duration):
        if duration is not None:
            self.__duration = duration
        else:
            self.__duration = 90


class Term(BasicTerm):

    def __init__(self, day, hour, minute, duration=None):
        super().__init__(hour, minute, duration)
        self.day = day
        # print("self.__day: ", self.__day)
        # print("self.__day.value: ", self.__day.value)

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, day):
        self.__day = day

    def __str__(self):
        return f"{DayToStr(self.__day)} {self.hour}:{self.minute} [{self.duration}]"

    def __hash__(self):
        first = hash(self.day)
        second = hash(first + self.hour)
        third = hash(second + self.minute)
        fourth = hash(third + self.duration)
        return fourth

    def __eq__(self, other):
        # return self.__hash__() == other.hash()
        return hasattr(other, 'day') and self.day == other.day and self.hour == other.hour and self.minute == other.minute and self.duration == other.duration

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

    def __lt__(self, other):
        return Term.earlierThan(self, other)

    def __le__(self, other):
        return Term.earlierThan(self, other)

    def __gt__(self, other):
        return Term.laterThan(self, other)

    def __ge__(self, other):
        return Term.laterThan(self, other)

    def __eq__(self, other):
        return Term.equals(self, other)

    def __sub__(self, other):
        sel_min = (int(self.__day.value) - 1)*24*60 + int(self.hour)*60 + self.minute + self.duration
        oth_min = (int(other.__day.value) - 1)*24*60 + int(other.hour)*60 + other.minute
        diff = sel_min - oth_min
        return Term(other.__day, other.hour, other.minute, diff)
