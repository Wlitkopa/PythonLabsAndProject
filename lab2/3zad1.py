
import sys
import lista
import slownik


if __name__ == "__main__":
    sys.argv.pop(0)
    # print(sys.argv)
    if len(sys.argv) < 1:
        print("Use option --help")
        exit()
    if str(sys.argv[0]) == '--lista':
        listzad = []
        lista.zapisz(listzad, sys.argv)
        print(lista.wypisz(listzad))
    elif str(sys.argv[0]) == '--slownik':
        slownikzad = {}
        slownik.zapisz(slownikzad, sys.argv)
        print(slownik.wypisz(slownikzad))
    elif sys.argv[0] == '--help':
        print("\nTo run 3zad1.py you need to use this syntax: "
              "python3 3zad1.py <option> arg1 arg2 ..."
              "\n\n"
              "OPTIONS\n"
              "--slownik : uses dictionary to store the frequency of numbers given as the arguments\n"
              "--lista   : uses list to store the frequency of numbers given as the arguments")
    else:
        print("Use option --help ")
