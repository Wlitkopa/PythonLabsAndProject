
import sys
from datetime import date

# print(date("kot"))


class kot:

    def __init__(self):
        self.karma = [1, 2, 3]
        self.dzien = "poniedzialek"

    def check(self, burek):
        burek.printwsz(self)
        print("po zmianie:")
        print("dachowiec.karma: ", self.karma)
        print("dachowiec.dzien: ", self.dzien)



class pies:

    def __init__(self, stysia):
        self.timetable = stysia

    def printwsz(self, kot):
        print(f"przed zmianą: {kot.karma}")
        kot.karma = [8, 9]
        print("Działa")

# print(list(123))


if isinstance("kot", int):
    print("True")
else:
    print("False")

dachowiec = kot()
# dachowiec.append()

Burek = pies(dachowiec)
dachowiec.check(Burek)
# Burek.printwsz()
# dachowiec.karma = [1, 2, 3, 4, 5]
# Burek.printwsz()
