
import sys

print('Ładowanie modułu "{0}"'.format(__name__))

slownik = {}


def zapisz(slownik, args):
    for i in range(len(args)):
        try:
            li = int(args[i])
            if slownik.get(li) is not None:
                slownik[li] += 1
            else:
                slownik[li] = 1
        except ValueError:
            pass


def wypisz(slownik):
    print('Wywołano funkcję "wypisz()" modułu "{0}"'.format(__name__))

    output = str("")

    for key in slownik:
        output += f"{key}: {slownik[key]}, "

    output = output[:-2]
    return output


print('Załadowano moduł "{0}"'.format(__name__))

if __name__ == "__main__":
    sys.argv.pop(0)
    zapisz(slownik, sys.argv)
    print(wypisz(slownik))

