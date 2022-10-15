
# -*- coding: utf-8 -*-
# Necessary in Python2

# In Python 3, UTF-8 is the default source encoding (see PEP 3120), so Unicode characters can be used anywhere

# Epikur - list do Menoikeusa (fragment)

lancuch1 = str('''
Niechaj młodzieniec nie zaniedbuje filozofii, a i starzec niech się nie czuje niezdolnym już do dalszego jej studiowania.
Dla nikogo bowiem nie jest ani za wcześnie, ani za późno zacząć troszczyć się o zdrowie swej duszy. Kto zatem twierdzi,
że pora do filozofowania jeszcze dla niego nie nadeszła, albo że już minęła, podobny jest do tego, co twierdzi, że pora 
do szczęścia jeszcze nie nadeszła, albo że już przeminęła. Powinni przeto filozofować zarówno młodzi, jak i starzy: ci, 
ażeby starzejąc się czuli się młodymi, przywodząc na pamięć dobra, którymi ich obdarzył w przeszłości los, tamci znów, 
ażeby pomimo swej młodości czuli się nieustraszeni wobec przyszłości, jak ludzie w podeszłym wieku.
''')

lancuch2 = str('''
A zatem bezustannie zabiegać o to, co nam może przysporzyć szczęścia; kto bowiem posiadł szczęście, ma wszystko,
co w ogóle mieć można, kogo zaś szczęście ominęło, ten robi wszystko, by je zdobyć.
Staraj się postępować w myśl tego, co ci bezustannie doradzałem, i myśl ciągle o tym, pamiętając,
że to są podstawowe zasady chwalebnego życia. Przede wszystkim uważaj bóstwo za istotę niezniszczalną i szczęśliwą 
zgodnie z powszechnym wyobrażeniem bóstwa i nie przypisuj mu cech, które by się sprzeciwiały jego nieśmiertelności 
albo były niezgodne z jego szczęściem. Dołóż starań, ażeby twoje pojęcie bóstwa obejmowało to wszystko, co 
może zachować jego nieśmiertelność i szczęśliwość. 
''')

lancuch = str('Bogowie wszakże istnieją, a ich poznanie jest faktem oczywistym; '
              'nie istnieją jednak w ten sposób, jak to sobie tłum wyobraża; wyobrażenia tłumu są zmienne.')

print((lancuch1 + lancuch2)*3)

print(lancuch[0])
print(lancuch[:2])
print(lancuch[3:])
print(lancuch[-2])
print(lancuch[-3:])
print(lancuch[::2])

try:
    lancuch[0] = 'K'
    print("Można modelować dowolny element łańcucha znaków")

except TypeError:
    print("Nie można zamieniać dowolnego elementu w łańcuchu znaków")




