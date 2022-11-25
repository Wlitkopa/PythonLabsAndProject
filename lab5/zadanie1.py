

def argumenty(attr):

    def wew(func):
        # print("wew_lista: ", lista)

        def wrapper(*f_args, **kwargs):

            lista = getattr(f_args[0], attr)
            # print("self.__class__.argumentySuma: ", f_args)
            default_arg_count = func.__code__.co_argcount
            given_args_count = len(f_args)
            missing = default_arg_count - given_args_count
            loop_limit = min(len(lista), missing)
            new_args = tuple(lista[i] for i in range(loop_limit))
            f_args += new_args
            if (len(lista) - loop_limit) != 0:
                first_not_used = lista[-(len(lista) - loop_limit)]
            else:
                first_not_used = "All used"
            # print(f"first_not_used: {first_not_used}")

            if len(f_args) != 0:

                # print(f"new_args: ", new_args)
                # print(f"missing: {missing}")
                # for num in f_args:
                #     print(f"num: {num}")
                try:
                    func(*f_args)
                    return first_not_used
                except TypeError:
                    raise TypeError(f"{func.__name__}() takes exactly {default_arg_count} arguments ({len(f_args)} given)")

        return wrapper

    return wew


class Operacje:

    argumentySuma = [4, 5]
    argumentyRoznica = [4, 5, 6]
    data = {'suma': argumentySuma, 'roznica': argumentyRoznica}

    @argumenty('argumentySuma')
    def suma(self, a, b, c):
        # print(f"Operacje.argumentySuma {Operacje.argumentySuma}")
        print("%d + %d + %d = %d" % (a, b, c, a + b + c))

    @argumenty('argumentyRoznica')
    def roznica(self, x, y):
        # print(f"Operacje.argumentyRoznica: {Operacje.argumentyRoznica}")
        print("%d - %d = %d" % (x, y, x - y))

    def __setitem__(self, key, value):
        if key == 'suma':
            Operacje.argumentySuma = value
            # print(f"Operacje.argumentySuma: {Operacje.argumentySuma}")

        elif key == 'roznica':
            Operacje.argumentyRoznica = value
            # print(f"Operacje.argumentyRoznica: {Operacje.argumentyRoznica}")

        else:
            print("Inappropriate key")
        self.data[key] = value
        # print("__setitem__ called")

    def __getitem__(self, item):
        # print("__getitem__ called")
        return self.data[item]


# op = Operacje()
# op.suma()

if __name__ == "__main__":


    op = Operacje()
    op.suma(1, 2, 3)  # Wypisze: 1+2+3=6
    op.suma(1, 2)  # Wypisze: 1+2+4=7 - 4 jest pobierana z tablicy 'argumentySuma'
    op.suma(1)  # Wypisze: 1+4+5=10 - 4 i 5 są pobierane z tablicy 'argumentySuma'
    # op.suma()  # TypeError: suma() takes exactly 3 arguments (2 given)
    op.roznica(2, 1)  # Wypisze: 2-1=1
    op.roznica(2)  # Wypisze: 2-4=-2
    # op.roznica()
    wynik = op.roznica()  # Wypisze: 4-5=-1
    print("wynik: ", wynik)  # Wypisze: 6

    # Zmiana zawartości listy argumentów dekoratora  dla metody 'suma'
    op['suma'] = [1, 2]
    # oznacza, że   argumentySuma=[1,2]

    # Zmiana zawartości listy argumentów dekoratora  dla metody 'roznica'
    op['roznica'] = [1, 2, 3]
    # oznacza, że   argumentyRoznica=[1,2,3]

    op.suma(1, 2, 3)  # Wypisze: 1+2+3=6
    op.suma(1, 2)  # Wypisze: 1+2+1=4 - 1 jest pobierana z tablicy 'argumentySuma'
    op.suma(1)  # Wypisze: 1+1+2=4 - 1 i 2 są pobierane z tablicy 'argumentySuma'
    # op.suma()  # TypeError: suma() takes exactly 3 arguments (2 given)
    op.roznica(2, 1)  # Wypisze: 2-1=1
    op.roznica(2)  # Wypisze: 2-1=1
    wynik = op.roznica()  # Wypisze: 1-2=-1
    print("wynik: ", wynik)  # Wypisze: 3

