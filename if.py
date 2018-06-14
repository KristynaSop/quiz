while True:
    strana = float(input('Zadej stranu čtverce v centimetrech: '))
    if strana >= 0:
        print('Obvod čtverce se stranou', strana, 'je', 4 * strana, 'cm')
        print('Obsah čtverce se stranou', strana, 'je', strana * strana, 'cm2')
        break
    else:
        print ("Zadaj kladné číslo")
