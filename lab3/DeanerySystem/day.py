
from enum import Enum, IntEnum


def nthDayFrom(n, day):
    nextd = (n + day.value) % 7
    return Day(nextd)


class Day(IntEnum):
    MON = 0
    TUE = 1
    WED = 2
    THU = 3
    FRI = 4
    SAT = 5
    SUN = 6

    def difference(self, day):
        diff = (day.value - self.value) % 7
        if diff >= 4:
            return diff - 7
        elif diff <= -4:
            return diff + 7
        else:
            return diff
    # print("Zaimportowałem Day")


# print("Day.SAT: ", Day.SAT)
#
# print("Day.SAT.name: ", Day.SAT.name)
#
# print("Day.SAT.value: ", Day.SAT.value)
#
# print("Day(1): ", Day(1))
#
# print("nthDayFrom(1, Day.SAT): ", nthDayFrom(1, Day.SAT))

