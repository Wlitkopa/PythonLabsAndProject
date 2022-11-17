
from abc import ABC, abstractmethod
from datetime import date
import sys

import idna.codec

print(str(date.today()))
print(repr(date.today()))
print(str('Ala\nma kota'))
print(repr('Ala\nma kota'))


# marka ilość sprzedaż wypożyczenie

class BasicVeh(ABC):

    def __init__(self, dataw=None, dataz=None):
        self.cenas = None
        self.cenaw = None
        self.dataw = dataw
        self.dataz = dataz
        self.clientid = None
        self.zwrot = False
        self.history = []

    @property
    def dataw(self):
        return self.__dataw

    @dataw.setter
    def dataw(self, dataw):
        temp = []
        if isinstance(dataw, str) or dataw is None:
            pass
        else:
            print("Niepoprawnie podano datę. Powinno być: dzień-miesiąc-rok")
            exit(1)
        if dataw is not None:
            temp = dataw.split("-")
            if len(temp) != 3:
                print("Niepoprawnie podano datę. Powinno być: dzień-miesiąc-rok")
                exit(2)
            try:
                date(int(temp[2]), int(temp[1]), int(temp[0]))
            except TypeError or ValueError:
                print("Niepoprawnie podano datę. Powinno być: dzień-miesiąc-rok")
                exit(3)
        self.__dataw = dataw

    @property
    def dataz(self):
        return self.__dataz

    @dataz.setter
    def dataz(self, dataz):
        temp = []
        if isinstance(dataz, str) or dataz is None:
            pass
        else:
            print("Niepoprawnie podano datę. Powinno być: dzień-miesiąc-rok")
            exit(1)
        if dataz is not None:
            temp = dataz.split("-")
            if len(temp) != 3:
                print("Niepoprawnie podano datę. Powinno być: dzień-miesiąc-rok")
                exit(1)
            try:
                date(int(temp[2]), int(temp[1]), int(temp[0]))
            except TypeError or ValueError:
                print("Niepoprawnie podano datę. Powinno być: dzień-miesiąc-rok")
                exit(1)
        self.__dataz = dataz

    def show_history(self):
        outcome = ""
        for i in range(len(self.history)):
            outcome += f"\nWypożyczający: {self.history[i][0].imie} {self.history[i][0].nazwisko}\n" \
                      f"Data wypożyczenia: {self.history[i][1]}\n" \
                      f"Data zwrotu: {self.history[i][2]}\n"
            if isinstance(self, Trailer) and len(self.history[i]) == 4:
                outcome += f"Przejechane km: {self.history[i][3]}\n"

        return outcome


class Trailer(BasicVeh):
    cnt = 0
    iden = None
    trailers = []

    def __init__(self, dataw=None, dataz=None, km=None):
        super().__init__(dataw, dataz)
        self.km = None

        if Trailer.iden is None and Trailer.cnt != 0:
            self.id = 1
            Trailer.iden = 1
            Trailer.trailers.append(self)
        elif Trailer.cnt != 0:
            self.id = Trailer.iden + 1
            Trailer.iden += 1
            Trailer.trailers.append(self)
        else:
            Trailer.cnt += 1

    # def show_history(self):
    #     output = super().show_history()
    #     return output
        # print("Dodano przyczepę: ", self)

    def __repr__(self):
        return "przyczepa = Trailer(clientid, cena sprzedaży, cena wypożyczenia, data wypożyczenia, data zwrotu)"

    def __str__(self):
        output = ""
        ind = 0
        for trailer in Trailer.trailers:
            # if ind == 0:
            #     continue
            print("Po continue")
            output += f"\nIdentyfikator przyczepy: {trailer.id}\n"
            if trailer.km is not None:
                output += f"Idetyfikator klienta: {trailer.clientid}\n"
            else:
                pass
            if trailer.cenas is not None:
                output += f"Cena sprzedaży: {trailer.cenas}\n"
            elif trailer.cenaw is not None:
                output += f"Cena wypożyczenia: {trailer.cenaw}\n"
            if trailer.dataw is not None:
                output += f"Data wypożyczenia: {trailer.dataw}\n" \
                          f"Data zwrotu: {trailer.dataz}\n"
            if trailer.zwrot:
                output += f"Ilość przejechanych km: {trailer.km}\n"
            elif trailer.km is None:
                output += f"Przyczepa jeszcze nie została zwrócona, więc nie wiadomo ile km przejechała\n"
            else:
                output += f"przyczepa nie została jeszcze wypożyczona\n"
            ind += 1

        return output


class Car(BasicVeh):
    iden = {}
    cars = []

    def __init__(self, marka=None, dataw=None, dataz=None):
        super().__init__(dataw, dataz)
        self.marka = marka
        # self.cenas = None
        # self.cenaw = None
        # self.dataw = dataw
        # self.dataz = dataz
        # self.clientid = None
        # self.zwrot = False

        if Car.iden.get(marka) is None:
            self.id = 1
            Car.iden[marka] = 1
        else:
            self.id = Car.iden.get(marka) + 1
            Car.iden[marka] += 1

        Car.cars.append(self)

    @property
    def marka(self):
        return self.__marka

    @marka.setter
    def marka(self, marka):
        if isinstance(marka, str) or marka is None:
            self.__marka = marka
        else:
            print("Niepoprawine podano markę")
            exit(1)

    def __repr__(self):
        return 'obiekt = Car(clientid, marka, cena sprzedaży, cena wypożyczenia, data wypożyczenia, data zwrotu)'

    def __str__(self):
        output = ""
        for car in Car.cars:
            if car.marka is not None:
                output += f"\nMarka: {car.marka}\n" \
                          f"Identyfikator auta: {car.id}\n" \
                          f"Idetyfikator klienta: {car.clientid}\n"
            else:
                pass
            if car.cenas is not None:
                output += f"Cena sprzedaży: {car.cenas}\n"
            elif car.cenaw is not None:
                output += f"Cena wypożyczenia: {car.cenaw}\n"
            if car.dataw is not None:
                output += f"Data wypożyczenia: {car.dataw}\n" \
                          f"Data zwrotu: {car.dataw}\n"

        return output


class Client:
    iden = {}
    clients = []

    def __init__(self, kto=None, adres=None):

        if kto is not None:
            kto = kto.split(" ")
            print("kto: ", kto)

            self.imie = kto[0]
            self.nazwisko = kto[1]
            self.adres = adres

            if Client.iden.get(kto[1]) is None:
                self.id = 1
                Client.iden[kto[1]] = 1
            else:
                self.id = Client.iden.get(kto[1]) + 1
                Client.iden[kto[1]] += 1

            Client.clients.append(self)

    @property
    def imie(self):
        return self.__imie

    @imie.setter
    def imie(self, imie):
        print("Imie: ", imie)

        if len(imie) == 0:
            print("Podaj imię")
            exit(1)
        if isinstance(imie, str):
            self.__imie = imie
        else:
            print("Niepoprawnie podano imie")
            exit(1)
        self.__imie = imie

    @property
    def nazwisko(self):
        return self.__nazwisko

    @nazwisko.setter
    def nazwisko(self, nazwisko):

        print("nazwisko: ", nazwisko)
        print("len(nazwisko): ", len(nazwisko))

        if len(nazwisko) == 0:
            print("Podaj nazwisko")
            exit(1)
        if isinstance(nazwisko, str):
            self.__nazwisko = nazwisko
        else:
            print("Niepoprawnie podano nazwisko")
            exit(1)
        self.__nazwisko = nazwisko

    @property
    def adres(self):
        return self.__adres

    @adres.setter
    def adres(self, adres):

        if len(adres) == 0:
            print("Podaj adres")
            exit(1)
        if isinstance(adres, str):
            self.__adres = adres
        else:
            print("Niepoprawnie podano adres")
            exit(1)
        self.__adres = adres

    def __str__(self):
        output = ""
        for i in range(len(Client.clients)):
            output += f"\nImie: {Client.clients[i].imie}\nNazwisko: {Client.clients[i].nazwisko}\nAdres: {Client.clients[i].adres}\nId: {Client.clients[i].id}\n"
        return output

    def __repr__(self):
        output = f"Imie: {self.imie}\nNazwisko: {self.nazwisko}\nAdres: {self.adres}\n"
        return output

    def __lshift__(self, car):
        Dealer.rent(self, car)

    def __rshift__(self, car):

        Dealer.retur(self, car)

    def __add__(self, car):
        Dealer.sell(self, car)


class Dealer:
    ev_cus = 0
    dane = []
    mag = []
    wyp = []
    kup = []
    all = []
    idenc = {}
    idena = {}

    @staticmethod
    def rent(client, car):

        # print(f"\n============ Nazwisko klienta: {client.nazwisko} ================\n")

        nazwisko = client.nazwisko
        # marka = car.marka
        dataw = car.dataw
        dataz = car.dataz

        # print(f"\n============ Nazwisko w funkcji: {nazwisko} ================\n")
        # print("dataw: ", dataw)
        # print("dataz: ", dataz)

        if dataw is None or dataz is None:
            print("Nie sprecyzowano dat wypożyczenia i zwrotu (albo jednej z nich)")
            return 3

        cl_id = f"{client.id}"
        # cr_id = f"{car.marka}{car.id}"
        car.clientid = cl_id

        car.history.append([client, dataw, dataz])

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

        if isinstance(car, Car):
            print("car to autoaudi")

            marka = car.marka
            cr_id = f"{car.marka}{car.id}"

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

            koszt = int(delta.days) * int(Dealer.mag[msc][3])
            Dealer.ev_cus += koszt
            koszt = koszt
            car.cenaw = koszt

            kupuje = f"{nazwisko}{cl_id}"

            auto = f"{marka}{cr_id}"

            # kupuje = Client(kto, adres)
            # auto = Car(cl_id, marka, None, Dealer.mag[msc][3], d0, d1)

            for i in range(len(Dealer.all)):
                # print("Działa ta pętla")
                # print(f"Id sprawdzane: {dealer.all[i][0].nazwisko}{dealer.all[i][0].id}")
                # print(f"Id funkcji: {nazwisko}{cl_id}")
                if f"{dealer.all[i][0].nazwisko}{dealer.all[i][0].id}" == f"{nazwisko}{cl_id}":
                    # print("Działa ten if")
                    Dealer.all[i][1] = str(int(Dealer.all[i][1]) + int(koszt))
                    Dealer.all[i].append(car)
                    break
                elif i == len(Dealer.all) - 1:
                    # print("Działa ten elif")
                    cus = kupuje
                    sum_koszt = koszt
                    Dealer.all.append([client, sum_koszt, car])
                    break

            if len(Dealer.all) == 0:
                print("Do teraz nic nie było kupione")
                cus = kupuje
                sum_koszt = koszt
                Dealer.all.append([client, sum_koszt, car])

        elif isinstance(car, Trailer):
            print("Działa ten isinstance")

            tr_id = f"przyczepa{car.id}"
            for i in range(len(Dealer.mag)):
                if Dealer.mag[i][0] == "przyczepa":
                    msc = i
                    break
            else:
                print("Nie przyczepy na liście magazynu")
                return 3
            if Dealer.mag[msc][1] == 0:
                print("Nie można wypożyczyć przyczepy. Brak na stanie")
                return 4
            else:
                Dealer.mag[msc][1] = int(Dealer.mag[msc][1]) - 1

            koszt = int(delta.days) * int(Dealer.mag[msc][3])
            Dealer.ev_cus += koszt
            koszt = koszt
            car.cenaw = koszt

            kupuje = f"{nazwisko}{cl_id}"
            print("kupuje: ", kupuje)

            for i in range(len(Dealer.all)):
                print("Działa ta pętla")
                print(f"Id sprawdzane: {dealer.all[i][0].nazwisko}{dealer.all[i][0].id}")
                print(f"Id funkcji: {nazwisko}{cl_id}")
                if f"{dealer.all[i][0].nazwisko}{dealer.all[i][0].id}" == f"{nazwisko}{cl_id}":
                    # print("Działa ten if")
                    Dealer.all[i][1] = str(int(Dealer.all[i][1]) + int(koszt))
                    Dealer.all[i].append(car)
                    print("Dodano do Dealer.all, klient już wcześniej korzystał z usług Dealera")
                    break
                elif i == len(Dealer.all) - 1:
                    # print("Działa ten elif")
                    sum_koszt = koszt
                    Dealer.all.append([client, sum_koszt, car])
                    print("Dodano do Dealer.all po raz pierwszy")
                    break

            if len(Dealer.all) == 0:
                print("Do teraz nic nie było kupione")
                # cus = kupuje
                sum_koszt = koszt
                Dealer.all.append([client, sum_koszt, car])

        else:
            print("Nie rozpoznano klasy obiektu")

        # print("Dealer.all: ", Dealer.all)

    @staticmethod
    def sell(client, car):

        print("Działa sell")

        imie = client.imie
        nazwisko = client.nazwisko
        marka = car.marka

        cl_id = client.id
        cr_id = car.id
        car.clientid = cl_id

        for i in range(len(Dealer.mag)):
            if str(Dealer.mag[i][0]) == str(marka):
                msc = i
                print("msc: ", msc)
                break
        else:
            print("Nie ma takiego samochodu w liście magazynu")
            return 1
        if Dealer.mag[msc][1] == 0:
            print("Nie można kupić auta. Brak na stanie")
            return 2
        else:
            print("Odjęto auto")
            Dealer.mag[msc][1] = int(Dealer.mag[msc][1]) - 1

        kupuje = f"{nazwisko}{cl_id}"
        auto = f"{marka}{cr_id}"

        koszt = Dealer.mag[msc][2]
        car.cenas = koszt
        Dealer.ev_cus += int(koszt)

        # print("Jestem w tym miejscu")

        for i in range(len(Dealer.all)):
            # print("Działa ta pętla")
            if f"{dealer.all[i][0].nazwisko}{dealer.all[i][0].id}" == f"{nazwisko}{cl_id}":
                # print("Działa ten if")
                Dealer.all[i][1] = str(int(Dealer.all[i][1]) + int(koszt))
                Dealer.all[i].append(car)
                break
            elif i == len(Dealer.all) - 1:
                # print("Działa ten elif")
                cus = kupuje
                sum_koszt = koszt
                Dealer.all.append([client, sum_koszt, car])
                break

        if len(Dealer.all) == 0:
            print("Do teraz nic nie było kupione")
            cus = kupuje
            sum_koszt = koszt
            Dealer.all.append([client, sum_koszt, car])

        # print("Dealer.all: ", Dealer.all)

    @staticmethod
    def retur(client, car):

        kto_id = f"{client.nazwisko}{client.id}"
        print("kto_id: ", kto_id)
        marka_id = ""
        marka = ""

        if isinstance(car, Car):
            marka_id = f"{car.marka}{car.id}"
            marka = car.marka
        elif isinstance(car, Trailer):
            marka_id = f"przyczepa{car.id}"
            marka = "przyczepa"

        else:
            print("Nie rozpoznano klasy obiektu przy zwrocie")

        for i in range(len(Dealer.all)):
            out = 0
            pot_cl_id = f"{Dealer.all[i][0].nazwisko}{Dealer.all[i][0].id}"
            if kto_id == pot_cl_id:

                for k in range(len(Dealer.all[i]) - 2):
                    pot_car_id = ""
                    if isinstance(Dealer.all[i][k + 2], Car):
                        pot_car_id = f"{Dealer.all[i][k + 2].marka}{Dealer.all[i][k + 2].id}"
                    elif isinstance(Dealer.all[i][k + 2], Trailer):
                        pot_car_id = f"przyczepa{Dealer.all[i][k + 2].id}"
                    if pot_car_id == marka_id:

                        print("Zaszedł if")
                        for j in range(len(Dealer.mag)):
                            if Dealer.mag[j][0] == marka:
                                out = 1
                                msc = j
                                Dealer.mag[msc][1] = int(Dealer.mag[msc][1]) + 1
                                print("Dealer.mag: ", Dealer.mag)
                                # print(f"Dealer.all[{i}] przed popem: {Dealer.all[i]}")
                                Dealer.all[i][k + 2].zwrot = True
                                # print(f"Dealer.all[{i}] po popie: {Dealer.all[i]}")
                                if isinstance(car, Trailer):
                                    km = int(input("Podaj ilość km, którą przejechała przyczepa: "))
                                    Dealer.all[i][k + 2].km = km
                                    for p in range(len(car.history)):
                                        if client == car.history[p][0]:
                                            car.history[p].append(km)
                                            break
                                break
                        else:
                            if i == len(Dealer.mag):
                                print("Nie ma takiej marki samochodu wpisanej na listę magazynu")
                                return 1
                        break
                    elif k == len(Dealer.all[i]) - 2:
                        print("Ten klient nie kupił takiego samochodu")
                        break
            if i == len(Dealer.all) - 1 and out == 0:
                print("Nie ma takiego wypożyczającego (klienta)")
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

    def __str__(self):
        # Dealer.all.append([client, sum_koszt, car])
        output = ""
        for i in range(len(Dealer.all)):
            # print(f"\n============ i: {i} ==============\n")
            # print(f"Dealer[{i}]: ", Dealer.all[i])
            output += f"\nWypożyczający: {Dealer.all[i][0].imie} {Dealer.all[i][0].nazwisko}\n" \
                      f"Id klienta: {Dealer.all[i][0].id}\n"
            # print("output: ", output)
            for j in range(len(Dealer.all[i]) - 2):

                # print(f"Dealer.all[{i}][{j} + 2]: ", Dealer.all[i][j + 2])

                if Dealer.all[i][j + 2].cenas is not None:
                    output += f"    Kupione auto: {Dealer.all[i][j + 2].marka}\n" \
                              f"    Id auta: {Dealer.all[i][j + 2].id}\n" \
                              f"    Koszt zakupu tego samochodu: {Dealer.all[i][j + 2].cenas}\n  =======\n"
                elif Dealer.all[i][j + 2].cenaw is not None:
                    if isinstance(Dealer.all[i][j + 2], Car):
                        output += f"    Wypożyczone auto: {Dealer.all[i][j + 2].marka}\n" \
                                  f"    Id auta: {Dealer.all[i][j + 2].id}\n" \
                                  f"    Data wypożyczenia: {Dealer.all[i][j + 2].dataw}\n" \
                                  f"    Data zwrotu: {Dealer.all[i][j + 2].dataz}\n" \
                                  f"    Koszt wypożyczenia tego samochodu: {Dealer.all[i][j + 2].cenaw}\n"
                    elif isinstance(Dealer.all[i][j + 2], Trailer):
                        output += f"    Id przyczepy: {Dealer.all[i][j + 2].id}\n" \
                                  f"    Ilość przejechanych kilometrów: {Dealer.all[i][j + 2].km}\n" \
                                  f"    Data wypożyczenia: {Dealer.all[i][j + 2].dataw}\n" \
                                  f"    Data zwrotu: {Dealer.all[i][j + 2].dataz}\n" \
                                  f"    Koszt wypożyczenia tej przyczepy: {Dealer.all[i][j + 2].cenaw}\n"
                    else:
                        print("Nie rozpoznano klasy po zakupie")

                    if dealer.all[i][j + 2].zwrot:
                        output += f"    (Zwrócono ten samochód/przyczepę)\n"
                    output += f"  =======\n"
            output += f"Łączny poniesiony koszt: {Dealer.all[i][1]}\n"

        output += f"Wszyscy łącznie zapłacili: {Dealer.ev_cus}\n"

        return output


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

    clients = Client()
    dealer = Dealer()
    cars = Car()
    trailers = Trailer()
