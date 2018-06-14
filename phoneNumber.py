import re
def isPhoneNumber(text):
    if len(text)!= 12:
        False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != "-":
        return False
    for i in range (4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != "-":
        return False
    for i in range (8,12):
        if not text[i].isdecimal():
            return False
    return True

print("456-765-8767 is a phone number:")
print(isPhoneNumber("456-765-8767"))
print("Moshi Moshi is a phone number:")
print(isPhoneNumber("Moshi Moshi"))

message= "Call me at 345-345-3456 tomorrow. 345-987-0456 is my office."
for i in range(len(message)):
    chunk=message[i:i+12]
    if isPhoneNumber(chunk):
        print("Phone number found: "+ chunk)
print("done")

phoneNumRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")#Regex a re.compile funguju spolu (udaju ci hladat)
mo = phoneNumRegex.search("My number is 345-345-4982") #.search - v tomto to budu hladat
print("Ny phone number is:"+mo.group()) #.group() - ulozi a vypise co naslo


hladamRegex=re.compile(r"sa \w+")
text = hladamRegex.sub("LA","Ahoj ako sa mas? Ja sa mam dobre ale dnes sa mi nepaci vobec pocasie. Vonku je 38 stupnov. Na 100% dnes nebude prsat vonku.")







