
import sys

# print("__name__: ", __name__)
# setg = {'kot': 123, 'pies': [2, 3, 4]}
# setg['lama'] = 131
#
# # data = ['max_attendants': 0, 'max_courses': 0]
# # chetny = ['kurs': input 0, 'person': 1]
#
# if 123 in setg:
#     print("Działa in")
#
# print("len(test): ", len(setg))
#
# print("setg: ", setg)


def enroll(courses, chetny, data):
    if chetny[0] in courses:
        print("len(courses[chetny[0]]): ", len(courses[chetny[0]]))
        print("Data: ", data)
        print("int(data[0])", int(data[0]))
        if len(courses[chetny[0]]) < int(data[0]):
            courses[chetny[0]].append(chetny[1])
        else:
            print("Ten kurs ma maksymalną liczbę uczestników")
            return
    else:
        if len(courses) < int(data[1]):
            courses[chetny[0]] = [chetny[1]]
        else:
            print("Osiągnięto maksymalną liczbę kursów")
            return


def wypisanie_z_kursu(courses, chetny, data):
    if chetny[0] not in courses:
        print("Nie ma takiego kursu")
        return
    else:
        if chetny[1] in courses[chetny[0]]:
            courses[chetny[0]].pop(courses[chetny[0]].index(chetny[1]))
        else:
            print("Nie ma takiej osoby na tym kursie")
            return


def course_delete(courses, kurs):
    if kurs in courses:
        del courses[kurs]
    else:
        print("Nie ma takiego kursu")
        return


def print_course(courses):
    print(courses)


def rename_course(courses, rename):
    if rename[0] in courses:
        temp = courses[rename[0]]
        del courses[rename[0]]
        courses[rename[1]] = temp
    else:
        print("Nie ma takiego kursu")
        return


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("ilość arg: ", len(sys.argv))
        print("Podaj argumenty: <maksymalny rozmiar grupy> <maksymalna ilość kursów>")
        exit()
    courses = {}
    data = sys.argv
    data.pop(0)
    print("data: ", data)
    choice = [1, 2, 3, 4, 5]
    while True:
        try:
            print("Jaką operację chcesz wykonać:"
                  " \n 1: Dodanie osoby do kursu"
                  " \n 2: Usunięcie osoby z kursu"
                  " \n 3: Usunięcie kursu "
                  " \n 4: Zmiana nazwy kursu "
                  " \n 5: Wypisanie kursów i ich uczestników")
            pr = input()
            try:
                inp = int(pr)
            except ValueError:
                print("Wybierz odpowiednią opcję")
                continue
            print("Choice: ", choice)
            match inp:
                case 1:
                    li = input("<kurs> <osoba>: ")
                    chetny = li.split()
                    enroll(courses, chetny, data)
                    break
                case 2:
                    li = input("<kurs> <osoba>: ")
                    chetny = li.split()
                    wypisanie_z_kursu(courses, chetny, data)
                    break
                case 3:
                    li = input("<kurs>: ")
                    course_delete(courses, li)
                    break
                case 4:
                    li = input("<kurs> <nowa_nazwa_kursu>: ")
                    rename = li.split()
                    rename_course(courses, rename)
                    break
                case 5:
                    print_course(courses)
                    break
                case _:
                    print("Wybierz odpowiednią opcję")

        except EOFError:
            exit()
