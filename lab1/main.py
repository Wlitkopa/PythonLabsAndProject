import cmath
from fractions import Fraction

# def char_check(arg1):
#     if type(arg1) == type(str()):


def sum(arg1, arg2):

    sum_output = int()
    if (type(arg1) and type(arg2)) == type(complex()):
        sum_output = arg1 + arg2
    elif (type(arg1) and type(arg2)) == type(Fraction()):
        sum_output = arg1 + arg2
    else:
        sum_output = float(arg1) + float(arg2)

    return sum_output


a = 3
b = 5

# a = int(input("Podaj liczbę całkowitą: "))
# b = int(input("Podaj liczbę całkowitą: "))
# print("__name__ = ", __name__)

if __name__ == '__main__':
    print("Suma = ", sum(a, b))

# liczba = 1
#
# if "1" == liczba:
#     print("Python ma typowanie dynamiczne słabe")
# else:
#     print("Python ma typowanie dynamiczne silne")
