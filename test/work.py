# This is the first time I've written stuff in Python in months.
# Yayyyyyyy

import string
import collections
from collections import OrderedDict
hashBuffer = 0

def inputScrubber(userString): # Function scrubs user input and gets rid of everything but letters and spaces.
    for i in userString:
        if i not in list(string.ascii_lowercase) and i not in list(string.ascii_uppercase) and i != " ":
            print("Incorrect character input. Start again.")
            return 1 #  It - would - catch all rogue characters, but I made it stop parsing at the first offender.
        elif userString == "q": #   Feel free to breakpoint the block with symbols at different points
                                #   in the input if you're curious.
            return 2
    return 0

def hashCreator(userString): # Creates the hash value.
    hashBuffer = 0  #   Flushes the buffer every time the function's called. I got weird problems otherwise.
    for i in range(len(userString)):
        #print(userString[i])
        index = userString[i]
        if index in lowerCase:  #   This if-else checks if it's upper or lower, and adds the right index value.
            hashBuffer += ((string.ascii_lowercase.index(index)) + 1)   # Added +1 cuz list starts at 0
        elif index in upperCase:
            hashBuffer += ((string.ascii_uppercase.index(index)) + 1)
        else:
            hashBuffer += 31    #   Just adds 31 by default for 'space' characters
    return hashBuffer % 31

def main():
    userInput = ""

    while userInput != "q":
        userInput = input("Input a string of letters and spaces. No symbols or punctuation. Input \"q\" to quit: ")
        buffer = list(userInput)
        action = inputScrubber(buffer)
        if action == 2:
            break
        elif action == 0 and action != 2:
            print("Hash of input is: ", hashCreator(buffer))