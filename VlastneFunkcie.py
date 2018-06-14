import random
def getAnswer (answerNumber):
    if answerNumber == 1:
        return "it is certain"
    elif answerNumber == 2:
        return "yes"
    elif answerNumber == 3:
        return "it is decidedly so"

r = random.randint (1,3)
fortune = getAnswer(r)
print (fortune)

print(getAnswer(random.randint(1,3))) #to iste len skratene

o=None
print(o)

def spam():
    print (eggs)
eggs = 42
spam()
print(eggs)