import sys
import math


def is_prime(num):
    if num < 2:
        return None
    for i in range(2, math.ceil((num / 2) + 1)):
        if num % i == 0:
            return None
    return num


def primes(list):
    for i in range(len(list)):
        try:
            a = int(list[i])
            if is_prime(a) != None:
                print(is_prime(a))

        except ValueError:
            pass


if __name__ == "__main__":
    if len(sys.argv) > 1:
        sys.argv.pop(0)
        primes(sys.argv)
    else:
        print("Podaj argumenty w command line")
else:
    pass
