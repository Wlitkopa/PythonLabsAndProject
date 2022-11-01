
import unittest
from zad4 import Dealer


class Test_comparison(unittest.TestCase):

    mag = open(f"mag.txt")

    for line in mag:
        Dealer.parseFileLine(line)
    mag.close()

    def test_parseInputLine(self):

        self.assertEqual(Dealer.parseInputLine("Ala ma kota 123"), ['Ala', 'ma', 'kota', '123'])

    def test_rent(self):
        Dealer.rent('Jan', 'ford', '23-10-2002', '25-10-2002')

        print("======\n\nDealer.wyp: {}\n\n=========".format(Dealer.wyp))

        self.assertEqual(Dealer.wyp, [[['Jan', 'ford'], ['23', '10', '2002'], ['25', '10', '2002'], 500]])

        Dealer.rent('Ala', 'audi', '28-2-2004', '1-3-2004')

        self.assertEqual(Dealer.wyp, [[['Jan', 'ford'], ['23', '10', '2002'], ['25', '10', '2002'], 500], [['Ala', 'audi'], ['28', '2', '2004'], ['1', '3', '2004'], 300]])
        self.assertEqual(Dealer.rent('Janek', 'ford', '23-20-2002', '20-10-2002'), 1)
        self.assertEqual(Dealer.rent('Janek', 'ford', '23-10-2002', '20-10-2002'), 2)
        self.assertEqual(Dealer.rent('Janek', 'opel', '23-10-2002', '25-10-2002'), 3)
        self.assertEqual(Dealer.rent('Stefan', 'audi', '23-10-2002', '25-10-2002'), 4)
        self.assertEqual(Dealer.mag[0][1], 0)
        self.assertEqual(Dealer.mag[2][1], 2)

    def test_retur(self):
        Dealer.retur('Ala', 'audi')
        self.assertEqual(Dealer.wyp, [[['Jan', 'ford'], ['23', '10', '2002'], ['25', '10', '2002'], 500]])
        self.assertEqual(Dealer.mag[0][1], 1)
        self.assertEqual(Dealer.retur('kot', 'audi'), 2)
        self.assertEqual(Dealer.retur('Jan', 'opel'), 2)

    def test_sell(self):
        Dealer.sell('Adam', 'fiat')
        self.assertEqual(Dealer.kup, [['Adam', 'fiat', 4000]])
        self.assertEqual(Dealer.mag[1][1], 4)
        self.assertEqual(Dealer.sell('Adam', 'opel'), 1)
        Dealer.sell('Adam', 'audi')
        self.assertEqual(Dealer.sell('Adam', 'audi'), 2)


if __name__ == '__main__':
    unittest.main()
