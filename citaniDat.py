import shelve, pprint, myCats

helloFile = open ("/Users/kristynasopuskova/Documents/pyladies/02/hello.txt")
helloContent = helloFile.read() #readlines() - get a list of values from file
print(helloContent)

helloFile = open("hello.txt","w")
helloFile.write("Slaninka!\n")

helloFile.close()
helloFile = open("hello.txt", "a")
helloFile.write ("kukuricka")

helloFile.close()
helloFile = open("hello.txt")
content=helloFile.read()
helloFile.close()
print(content)

shelfFile = shelve.open("mydata") #vytovi mi binary file s datami
cats = ["Zophie","Pooka", "Simon"]
shelfFile ["cats"] = cats
shelfFile.close()

shelfFile=shelve.open("mydata")
type(shelfFile)
shelfFile["cats"]
shelfFile.close()

shelfFile=shelve.open("mydata")
list(shelfFile.keys()) #vypise keys
list(shelfFile.values()) #vypise values
shelfFile.close()

cats= [{"name":"Zophie","desc": "chuddy"},{"name":"Pooka","desc":"fluffy"}]
pprint.pformat(cats) #daju ich do python formatu
fileObj=open("myCats.py","w") #otvoria na writing
fileObj.write("cats= "+pprint.pformat(cats)+"\n") #pridaju
fileObj.close()

myCats.cats
myCats.cats[0]
myCats.cats[0]["name"]
