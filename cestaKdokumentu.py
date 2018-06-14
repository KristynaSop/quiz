import os

os.makedirs("//Users//kristynasopuskova//Docments//pyladies//delicious//walnut//waffles") #vytvori mi folder
myfilees = ["accounts.txt", "profile.pdf"]
for filename in myfilees:
    print (os.path.join("/Users/kristynasopuskova",filename))

print(os.getcwd()) #ukaze kde som
print(os.path.relpath("//Documents", "//"))

calcFilePath="//Users//kristynasopuskova//Documents//pyladies//02//accounts.txt" #rozdeli to
os.path.split(calcFilePath)
os.path.getsize("//Users//kristynasopuskova//Documents//pyladies//02//accounts.txt") #ukaze velkost suboru
os.listdir("//Users//kristynasopuskova//Documents") #mena suborov v tom

