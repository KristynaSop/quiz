def nacti_cislo():
    while True:
        odpoved = input('Zadej číslo: ')
        try:
            return int(odpoved)
        except ValueError:
            print('To nebylo číslo! Zkus to znovu.')
