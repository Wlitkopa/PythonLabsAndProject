
from datetime import date
import sys

import idna.codec

print(str(date.today()))
print(repr(date.today()))
print(str('Ala\nma kota'))
print(repr('Ala\nma kota'))

# marka ilość sprzedaż wypożyczenie


class Car:

    iden = {}
    cars = []

    def __init__(self, clientid, marka, cenas, cenaw, dataw, dataz):
        self.marka = marka
        self.cenas = cenas
        self.cenaw = cenaw
        self.dataw = dataw
        self.dataz = dataz
        self.clientid = clientid

        if Car.iden.get(marka) is None:
            self.id = 1
            Car.iden[marka] = 1
        else:
            self.id = Car.iden.get(marka) + 1
            Car.iden[marka] += 1

        Car.cars.append(self)

        def __repr__(self):
            return 'obiekt = Car(clientid, marka, cena sprzedaży, cena wypożyczenia, data wypożyczenia, data zwrotu'

        def __str__(self):
            output = ""
            for car in Car.cars:
                output += f"Identyfikator auta: {car.id}\n" \
                          f"Idetyfikator klienta: {car.clientid}" \
                          f"Marka: {car.marka}" \
                          f"Cena sprzedaży: {car.cenas}" \
                          f"Cena wypożyczenia: {car.cenaw}" \
                          f"Data wypożyczenia: {car.dataw}" \
                          f"Data zwrotu: {car.dataw}"
            return output

class Client:

    iden = {}
    clients = []

    def __init__(self, imie, nazwisko, adres):

        self.imie = imie
        self.nazwisko = nazwisko
        self.adres = adres

        if Client.iden.get(nazwisko) is None:
            self.id = 1
            Client.iden[nazwisko] = 1
        else:
            self.id = Client.iden.get(nazwisko) + 1
            Client.iden[nazwisko] += 1

        Client.clients.append(self)


class Dealer:

    ev_cus = 0
    dane = []
    mag = []
    wyp = []
    kup = []

    def __init__(self, kto, marka, wyb):
        self.cus = [kto, marka]

    @staticmethod
    def rent(kto, marka, dataw, dataz):
        msc = 0
        # self.kto = kto
        # self.marka = marka

        cus = [kto, marka]
        dataw = dataw.split("-")
        dataz = dataz.split("-")
        print("dataw: ", dataw)
        print("dataz: ", dataz)
        try:
            d0 = date(int(dataw[2]), int(dataw[1]), int(dataw[0]))
            d1 = date(int(dataz[2]), int(dataz[1]), int(dataz[0]))
        except ValueError:
            print("Miesiąc ma od 1 do 31 dni oraz miesięcy jest 12")
            return 1

        d0 = date(int(dataw[2]), int(dataw[1]), int(dataw[0]))
        d1 = date(int(dataz[2]), int(dataz[1]), int(dataz[0]))
        delta = d1 - d0
        if delta.days <= 0:
            print("Różnica dat jest mniejsza bądź równa zeru")
            return 2
        print("delta: ", delta)
        print("delta.days: ", delta.days)
        for i in range(len(Dealer.mag)):
            if Dealer.mag[i][0] == marka:
                msc = i
                break
        else:
            print("marka: ", marka)
            print("Nie ma takiego samochodu w liście magazynu")
            return 3
        if Dealer.mag[msc][1] == 0:
            print("Nie można wypożyczyć auta. Brak na stanie")
            return 4
        else:
            Dealer.mag[msc][1] = int(Dealer.mag[msc][1]) - 1

        koszt = int(delta.days)*int(Dealer.mag[msc][3])
        Dealer.ev_cus += koszt
        koszt = koszt
        Dealer.wyp.append([cus, dataw, dataz, koszt])
        print("Dealer.wyp: ", Dealer.wyp)

    @staticmethod
    def sell(kto, marka):
        # self.kto = kto
        # self.marka = marka
        msc = 0
        # cus = [kto, marka]
        for i in range(len(Dealer.mag)):
            if Dealer.mag[i][0] == marka:
                msc = i
                break
        else:
            print("Nie ma takiego samochodu w liście magazynu")
            return 1
        if Dealer.mag[msc][1] == 0:
            print("Nie można kupić auta. Brak na stanie")
            return 2
        else:
            Dealer.mag[msc][1] = int(Dealer.mag[msc][1]) - 1

        koszt = Dealer.mag[msc][2]
        Dealer.ev_cus += int(koszt)
        Dealer.kup.append([kto, marka, int(koszt)])
        print("Dealer.kup: ", Dealer.kup)

    @staticmethod
    def retur(kto, marka):
        msc = 0

        for i in range(len(Dealer.wyp)):

            if kto == Dealer.wyp[i][0][0] and marka == Dealer.wyp[i][0][1]:
                print("Zaszedł if")
                for j in range(len(Dealer.mag)):
                    if Dealer.mag[j][0] == marka:
                        msc = j
                        Dealer.mag[msc][1] = int(Dealer.mag[msc][1]) + 1
                        print("Dealer.mag: ", Dealer.mag)
                        Dealer.wyp.pop(i)
                        print("Dealer.wyp po popie: ", Dealer.wyp)
                        break
                else:
                    if i == len(Dealer.wyp):
                        print("Nie ma takiej marki samochodu wpisanej w liście magazynu")
                        return 1
                break
        else:
            print("Nie ma takiego wypożyczającego lub marki samochodu")
            return 2

    @staticmethod
    def parseFileLine(linia):
        new = linia.split()
        Dealer.mag.append(new)
        print("Dealer.mag: ", Dealer.mag)

    @staticmethod
    def parseInputLine(linia):
        new = linia.split()
        print("new: ", new)
        return new


if __name__ == "__main__":
    sys.argv.pop(0)
    dane = []
    if len(sys.argv) != 1:
        print("sys.argv: ", sys.argv)
        print("Nie podano nazwy pliku")
        exit()
    mag = open(f"{sys.argv[0]}")

    for line in mag:
        Dealer.parseFileLine(line)
    mag.close()
    while True:
        try:
            choice = input("Wybierz operację:\n1: rent\n2: return\n3. sell\n")
            try:
                int(choice)
            except ValueError:
                print("Nie wybrano odpowiedniej opcji")
                continue
            if int(choice) == 1:
                print("Magazyn: ", Dealer.mag)
                print("kto, marka, dzienw-mscw-rokw, dzienz-mscz-rokz")
                cdata = input()
                pcus = Dealer.parseInputLine(cdata)
                if len(pcus) != 4:
                    print("Nie podano odpowiedniej ilości argumentów")
                else:
                    Dealer.rent(pcus[0], pcus[1], pcus[2], pcus[3])
                    print("pcus: ", pcus)
            elif int(choice) == 2:
                print("Wypożyczone auta: ", Dealer.wyp)
                print("kto, marka")
                kto = input()
                kto = Dealer.parseInputLine(kto)
                if len(kto) != 2:
                    print("Nie podano odpowiedniej ilości argumentów")
                else:
                    Dealer.retur(kto[0], kto[1])
            elif int(choice) == 3:
                print("kto, marka")
                cdata = input()
                pcus = Dealer.parseInputLine(cdata)
                if len(pcus) != 2:
                    print("Nie podano odpowiedniej ilości argumentów")
                else:
                    Dealer.sell(pcus[0], pcus[1])

        except EOFError:
            for i in range(len(Dealer.wyp)):
                print(f"\n Wypożyczjący: {Dealer.wyp[i][0][0]}\n Marka: {Dealer.wyp[i][0][1]}\n Data wypożyczenia:"
                      f" {Dealer.wyp[i][1][0]}-{Dealer.wyp[i][1][1]}-{Dealer.wyp[i][1][2]}\n"
                      f" Data zwrotu: {Dealer.wyp[i][2][0]}-{Dealer.wyp[i][2][1]}-{Dealer.wyp[i][2][2]}\n"
                      f" Koszt: {Dealer.wyp[i][3]}\n")
            for i in range(len(Dealer.kup)):
                print(f"\n Kupujący: {Dealer.kup[i][0]}\n "
                      f"Kupione auto: {Dealer.kup[i][1]}\n "
                      f"Koszt: {Dealer.kup[i][2]}\n")
            print(f"Łącznie wszyscy zapłacili: {Dealer.ev_cus}")
            exit()
