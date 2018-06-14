import random

cislo = random.randint (1,10)
print (cislo)


while True:

    ciselko = int(input("vloz cislo"))
    if ciselko < cislo:
        print("cislo je velmi nizke")
    elif ciselko > cislo:
        print ("cislo je velmi vysoke")
    else:
        break
print ("uhadel si, cool-cool")



