def obvod_obdelnika(sirka, vyska):
    return 2 * (sirka + vyska)

print(obvod_obdelnika(4, 2))

def napis_hlasku(nazev, skore):

    print(nazev, 'skóre je', str(skore))
    if skore > 1000:
        print('Světový rekord!')
    elif skore > 100:
        print('Skvělé!')
    elif skore > 10:
        print('Ucházející.')
    elif skore > 1:
        print('Aspoň něco')
    else:
        print('Snad příště.')

napis_hlasku('Tvoje', 256)
napis_hlasku('Protivníkovo', 5)


def obsah_stvorca (strana):
    return 4 * (strana)
print (obsah_stvorca (int(input())))


def vzorec (a,b):
    return 2 * (a) + 3 * (b)
print (vzorec(3,4))
