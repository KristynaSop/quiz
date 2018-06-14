import random

theBoard= {"top-L":" ","top-M":" ","top-R":" ",
           "mid-L": " ","mid-M": " ","mid-R": " ",
           "low-L": " ","low-M": " ","low-R": " ",}

def printBoard(board):
    print (board["top-L"]+"|" + board["top-M"]+"|"+ board["top-R"])
    print("-+-+-")
    print(board["mid-L"]+"|" + board["mid-M"]+"|"+ board["mid-R"])
    print("-+-+-")
    print(board["low-L"] + "|" + board["low-M"] + "|" + board["low-R"])
printBoard(theBoard)

def hrac():
    myturn = "X"
    for i in range(1):
        printBoard(theBoard)
        print("Turn for " + myturn + ". Move on which space?")
        move = input()
        theBoard[move]=myturn

def pc():
    pcturn = "O"
    answers = ["top-L","top-M","top-R","mid-L","mid-M","mid-R","low-L","low-M","low-R"]
    for i in range(1):
        printBoard(theBoard)
        move2 = random.choice(answers)
        theBoard[move2]= pcturn

while True:
    hrac()
    pc()







printBoard(theBoard)