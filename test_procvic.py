import math

# Funkce pro výpočet objemu a povrchu krychle
def krychle():
    a = float(input("Zadej délku hrany krychle: "))
    objem = a ** 3
    povrch = 6 * a ** 2
    print("Objem krychle:", objem)
    print("Povrch krychle:", povrch)

# Funkce pro výpočet objemu a povrchu kvádru
def kvadr():
    a = float(input("Zadej délku hrany kvádru: "))
    b = float(input("Zadej šířku kvádru: "))
    c = float(input("Zadej výšku kvádru: "))
    objem = a * b * c
    povrch = 2 * (a * b + a * c + b * c)
    print("Objem kvádru:", objem)
    print("Povrch kvádru:", povrch)

# Funkce pro výpočet objemu a povrchu koule
def koule():
    r = float(input("Zadej poloměr koule: "))
    objem = (4 / 3) * math.pi * r ** 3
    povrch = 4 * math.pi * r ** 2
    print("Objem koule:", objem)
    print("Povrch koule:", povrch)

# Funkce pro výpočet objemu a povrchu válcu
def valc():
    r = float(input("Zadej poloměr základny válce: "))
    v = float(input("Zadej výšku válce: "))
    objem = math.pi * r ** 2 * v
    povrch = 2 * math.pi * r * (r + v)
    print("Objem válce:", objem)
    print("Povrch válce:", povrch)

# Hlavní program
while True:
    print("\n1. Krychle")
    print("2. Kvádr")
    print("3. Koule")
    print("4. Válec")
    print("5. Konec programu")

    volba = input("Zvolte číslo odpovídající tělesu (1-5): ")

    if volba == '1':
        krychle()
    elif volba == '2':
        kvadr()
    elif volba == '3':
        koule()
    elif volba == '4':
        valc()
    elif volba == '5':
        print("Konec programu.")
        break
    else:
        print("Neplatná volba. Zvolte prosím číslo 1-5.")



#############################################################################

def absolutni_hodnota():
    cislo = float(input("Zadej číslo: "))
    if cislo >= 0:
        return cislo
    else:
        return -cislo

# Příklad použití
abs_hodnota = absolutni_hodnota()
print("Absolutní hodnota zadaného čísla je:", abs_hodnota)


#############################################################################

def nejvetsi2(cislo1, cislo2):
    if cislo1 >= cislo2:
        return cislo1
    else:
        return cislo2

# Příklad použití
cislo1 = float(input("Zadej první číslo: "))
cislo2 = float(input("Zadej druhé číslo: "))
print("Větší číslo je:", nejvetsi2(cislo1, cislo2))



#############################################################################

def nejvetsi3(cislo1, cislo2, cislo3):
    nejvyssi = cislo1
    if cislo2 > nejvyssi:
        nejvyssi = cislo2
    if cislo3 > nejvyssi:
        nejvyssi = cislo3
    return nejvyssi

# Příklad použití
cislo1 = float(input("Zadej první číslo: "))
cislo2 = float(input("Zadej druhé číslo: "))
cislo3 = float(input("Zadej třetí číslo: "))
print("Nejvyšší číslo je:", nejvetsi3(cislo1, cislo2, cislo3))



##############################################################################

def nejvetsi(seznam):
    nejvyssi = seznam[0]  # Předpokládáme, že první prvek seznamu je nejvyšší
    for cislo in seznam:
        if cislo > nejvyssi:
            nejvyssi = cislo
    return nejvyssi

# Příklad použití
seznam = [int(x) for x in input("Zadej čísla oddělená mezerami: ").split()]
print("Nejvyšší číslo je:", nejvetsi(seznam))



##############################################################################

def jen_suda(seznam):
    return [cislo for cislo in seznam if cislo % 2 == 0]

# Příklad použití
cisla = [int(x) for x in input("Zadej čísla oddělená mezerami: ").split()]
suda_cisla = jen_suda(cisla)
print("Sudá čísla:", suda_cisla)
