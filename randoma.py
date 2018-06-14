from random import randrange

cislo = randrange(0, 3)
while True:
    ciselko = int(input("zadaj cislo na ktoré myslím"))
    if cislo == ciselko:
        print('uhadol si')
        break
    else:
        print('neuhadol si')
