
import getopt
import sys
import lista
import slownik


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], '', ['module=', 'help'])
    except getopt.GetoptError as err:
        print(err)
        sys.exit(2)

    if len(opts) != 1:
        print("Use only one option")
        exit()

    if opts[0][0] in ("--help", "-h"):
        print("\nTo run 3zad2.py you need to use this syntax: "
              "python3 3zad2.py <option> arg1 arg2 ..."
              "\n\n"
              "OPTIONS\n"
              "--module=\n"
              "     lista    : uses list to store the frequency of numbers given as the arguments\n"
              "     slownik  : uses dictionary to store the frequency of numbers given as the arguments\n")
    elif opts[0][0] in ("--module", "-m"):
        if opts[0][1] == "lista":
            listzad = []
            lista.zapisz(listzad, args)
            print(lista.wypisz(listzad))
        elif opts[0][1] == "slownik":
            slownikzad = {}
            slownik.zapisz(slownikzad, args)
            print(slownik.wypisz(slownikzad))
        else:
            print(f"Unrecognisable option argument: '{opts[0][1]}'")


if __name__ == "__main__":
    main()
