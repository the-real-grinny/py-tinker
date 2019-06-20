"""
WHEN, IN THE COURSE OF HUMAN HISTORY

I FEEL LIKE MAKING A PYTHON MYSQLDB INTERFACE

THIS HAPPENS
"""

userInput = ""
inputList = []
menuInput = ""

def debugPrint(stuff):
    print("This is a debug print: ", end='')
    print(stuff)

def menuLoop(menuInput):
    print("PySQL Database Interface\nChoose an option")
    userInput = input("1)Select Database\n"
        +"2)Select user account\n"
        +"3)Quit\n")
    debugPrint(userInput)
    menuInput = userInput

while(True):
    if (menuLoop(menuInput) == "quitquery"):
        break
        