zvierata="!".join(["cat","rats","bads"]) #prida vykrisnik medzi ne
print(zvierata)

haha="My name is Simon".split("m") #na mieste kde je m tak da ciarku
print(haha)

conan= "Hello".rjust(20) #odsadi o 20 mm
print (conan)

kenda= "Hello".ljust(20,"-") #.center(20?"-")
print (kenda)

while True:
    print("enter your age:")
    age = input()
    if age.isdecimal():
        break
    print ("please eneter a number for your age.")

while True:
    print ("Select a new passwort (letters and numbers only:)")
    password = input()
    if password.isdecimal():
        break
    print("Password can only have letters and numbers")