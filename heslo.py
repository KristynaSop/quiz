passwordFile = open("SecretPasswordFile.txt")
SecretPassword = passwordFile.read()
print("enter your password")
typedPassword = input ()
if typedPassword == SecretPassword:
    print ("access granted")
elif typedPassword == "1234":
        print("Just idiots use this password")
else:
    print("acces denied")
