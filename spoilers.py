#!/usr/bin/env python
# coding: utf-8

import clipboard
import os

def spoiler(separator):
    """Turns any user strings' characters into spoilers"""

    while(True):
        copy_string = ""
        user_input = input("Input string: ")

        #Allows for the user to clear the console they are using
        if user_input == 'clear': 
            os.system('cls' if os.name=='nt' else 'clear')

        for x in range(len(user_input)):
            if user_input[x].isspace():
                divider = f"{separator} "
            else:
                if user_input[x-1].isspace() or x == 0:
                    divider = f"{separator}"
                else:
                    divider = f"{separator}{separator}"
            copy_string = copy_string + divider + user_input[x]

        copy_string += f"{separator}"
        clipboard.copy(copy_string)

if __name__ == '__main__':
    separator = "||"
    spoiler(separator)
