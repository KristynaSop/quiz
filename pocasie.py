print ("is it raining?")
answer = input()
if answer == "yes":
    print ("have umberella?")
    umberella = input()
    if umberella == "no":
        while True:
            print("wait a while")
            print ("is raining?")
            znova = input ()
            if znova == "no":
                break

print ("go outside")
