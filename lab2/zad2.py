
import re
import math


def maximum(int1, int2):
    if int1 >= int2:
        return int1
    else:
        return int2


def recognize(inp):

    words = re.findall(r"[^0-9]+", inp)
    numbers = re.findall(r"[0-9]+", inp)

    wcnt = len(words)
    ncnt = len(numbers)
    output = str()

    for i in range(maximum(wcnt, ncnt)):
        if re.match(r"[^0-9]", inp):
            if i < wcnt:
                output += f"  Wyraz: {words[i]}\n"
                # print("  Wyraz: ", words[i])
            if i < ncnt:
                output += f"  Liczba: {numbers[i]}\n"
                # print("  Liczba: ", numbers[i])
        else:
            if i < ncnt:
                output += f"  Liczba: {numbers[i]}\n"
                # print("  Liczba: ", numbers[i])
            if i < wcnt:
                output += f"  Wyraz: {words[i]}\n"
                # print("  Wyraz: ", words[i])

    output = output[:-1]
    return output


if __name__ == "__main__":
    while True:
        try:
            try:
                uinp = str(input())
                print(recognize(uinp))
            except TypeError:
                print("Inputem ma być string")
        except EOFError:
            exit()

# Wielki string: 123abc4Alama567kotów8Ӂ ӅӤԔ88۞2ܫ17012ܫ aqwrqwqt12݉
