
import sys

print('Ładowanie modułu "{0}"'.format(__name__))

lista = []


def zapisz(lista, args):
    for i in range(len(args)):
        try:
            li = int(args[i])
            if len(lista) == 0:
                lista.append([li, 1])
            else:
                for j in range(len(lista)):
                    if li == lista[j][0]:
                        lista[j][1] += 1
                        break
                    elif j == len(lista) - 1:
                        lista.append([li, 1])
        except ValueError:
            pass


def wypisz(lista):
    print('Wywołano funkcję "wypisz()" modułu "{0}"'.format(__name__))
    output = str("")

    for i in range(len(lista)):
        output += f"{lista[i][0]}: {lista[i][1]}, "

    output = output[:-2]
    return output


print('Załadowano moduł "{0}"'.format(__name__))

if __name__ == "__main__":
    sys.argv.pop(0)
    zapisz(lista, sys.argv)
    print(wypisz(lista))
