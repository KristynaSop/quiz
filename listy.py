import copy

spam = ["cat","dog","horse","lion"]
print (spam)
del spam [2]
print(spam)
spam = ["A","B","C","D"]
cheese = copy.copy (spam)
cheese [1]=42
print (spam)
print(cheese)

supplies= ["pens","staplers","flame-throwers","binders"]
for i in range(len(supplies)):
    print("index"+str(i)+"in supplies is:"+supplies[i])

supplies.index ("pens")
supplies.append ("catepilar")
supplies.remove ("flame-throwers")
supplies.sort(reverse=True)
print (supplies)



cat = ["fat","black","loud"]
size = cat[0]
color = [1]
disposition = [2]

#size, color, disposition = cat #moze byt aj takto
print (size)

spam = "Hello"
spam+= " world!"
print (spam)

catNames= []
while True:
    print("zadaj meno macky"+ str(len(catNames)+1)+" (or enter nothing to stop.):")
    name = input()
    if name == " ":
        break
    catNames = catNames + [name] #list concatenation
print("the cat names are:")
for name in catNames:
    print (""+ name)



for i in range(3):
    cislo = int(input("zadaj cislo"))
    cisla = cisla + [cislo]


print (cisla)
