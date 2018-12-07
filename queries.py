"""
WHEN, IS THE COURSE OF HUMAN HISTORY

I FEEL LIKE MAKING A PYTHON MYSQLDB INTERFACE

THIS HAPPENS
"""

userInput = ""
inputList = []

def debugPrint(stuff):
    print("This is a debug print: ", end='')
    print(stuff)

while userInput != "quitquery":
    userInput = ""
    inputList = []

    print("PySQL Database Interface\nChoose an option")
    userInput = input("1)Select Database\n"
        +"2)Select user account\n"
        +"3)Quit")
    debugPrint(userInput)