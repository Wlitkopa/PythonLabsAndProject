
from klasa import Klasa

obiekt1 = Klasa(['a', 'b', 'c'])
obiekt2 = Klasa(['x', 'y', 'z'])
print('*' * 30)
print("Po utworzeniu obiektów")
print('\tKlasa.tab   ->', Klasa.tab)
print('\tobiekt1.tab ->', obiekt1.tab)
print('\tobiekt2.tab ->', obiekt2.tab)
print('-' * 10)
Klasa.tab = [4, 5, 6]
print("Po wykonaniu instrukcji \u001b[31mKlasa.tab = [4, 5, 6]\u001b[0m'")
print('\tKlasa.tab   ->', Klasa.tab)
print('\tobiekt1.tab ->', obiekt1.tab)
print('\tobiekt2.tab ->', obiekt2.tab)
print('-' * 10)
print("Po wykonaniu instrukcji \u001b[31mobiekt1.tab = [7, 8, 9]\u001b[0m'")
obiekt1.tab = [7, 8, 9]
print('\tKlasa.tab   ->', Klasa.tab)
print('\tobiekt1.tab ->', obiekt1.tab)
print('\tobiekt2.tab ->', obiekt2.tab)
print('-' * 10)
print(
    "Po wykonaniu instrukcji '\u001b[31mobiekt2.tab = [-3, -2, -1]\u001b[0m'")
obiekt2.tab = [-3, -2, -1]
print('\tKlasa.tab   ->', Klasa.tab)
print('\tobiekt1.tab ->', obiekt1.tab)
print('\tobiekt2.tab ->', obiekt2.tab)
print('*' * 30)

# Zadanie 7
# Na początku, po utworzeniu obiektów, main.py nie zmienił wartości zmiennej tab. Więc zarówno w klasie Klasa jak i w
# przypadku każdego z obiektów klasy Klasa, czyli obiekt1 i obiekt2, wartość tab pozostała taka sama.
# Gdy zmieniło się wartość zminnej statycznej tab (odwołując się bezpośrednio do niej odwołaniem Klasa.tab),
# to wartość tej zmiennej zmieniła się w klasie Klasa, a więc i obiekty tej klasy, odowłując się do zmiennej statycznej
# 'tab', przyjęły nową wartość dla zmiennej tab. Jednakże później main.py zmieniał jedynie wartość pola obiektu obiekt1
# (a później obiektu obiekt2), co nie miało wpływu na zmienną statyczną, ponieważ nie do niej nastapiło odwołanie.
# Zatem wtedy była zmieniona jedynie wartość pola obiekt1.tab (później również obiekt2.tab)

# Zadanie 10
# Tym razem na samym początku obiekty obiekt1 oraz obiekt2 posiadały już swoje zmienne instancyjne tab. Dlatego, gdy
# została zmieniona wartość zminnej statycznej tab, to nie zmieniła się wartość zmiennych instancyjnych tab, do których
# można odwołać się tylko poprzez obiekt, do którego przynależą

