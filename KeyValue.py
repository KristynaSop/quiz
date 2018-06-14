myCat = {"size":"fat","color":"gray","disposition":"loud"}
print(myCat["size"])

spam = {"Alice":"Apr 1","Bob":"Dec 21","Carol":"Mar 4"}
for v in spam.values(): #spam.keys - vypise keys
    print(v)
for i in spam.items():
    print(i)
spam.setdefault ("Kika","July 24") #ak by tam ten key bol, vypisalo by to datum (nic by sa nemenilo)
print (spam)

message = "Ahoj Volam sa Kristyna a mam 24 rokov"
count= {}
for charakter in message:
    count.setdefault(charakter,0)
    count[charakter]=count[charakter]+1
print(count) #pprint.pprint(count)- prehladnesjie to vyzera (musim importovat pprint z kniznice)


birthday = {"Alice":"Apr 1","Bob":"Dec 21","Carol":"Mar 4"}
while True:
    print("Enter the name")
    name = input()
    if name ==" ":
        break

    if name in birthday:
        print(birthday[name]+ "is the birthday of " + name)
    else:
        print ("I do not have information for"+ name)
        print("when is their birthday?")
        bday=input()
        birthday[name]=bday
        print("birhtday datbase updated")
print(birthday)