def spam (devidedBy):
    try:
        return 42 / devidedBy
    except ZeroDivisionError:
        print ("Error:Invalid argument")
print (spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

