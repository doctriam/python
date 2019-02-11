"""
AUTHOR:  Kenneth Haynie, Jr.
TITLE:  helloworld.py
VERSION:  1.0
  VERSION NOTES:
    LearnPython.org tutorials through String Formatting;
    created endproc() function to clean up and simplify the continue prompt;
    comment changes for testing git/github
DESCRIPTION:  Walkthroughs of python tutorials from learnpython.org
EDITOR:  VIM 8.0.1453 """

import sys

def endproc():
    """Function for prompting user input and deleting prompt after Enter is pressed"""
    print()
    input("Press Enter to continue")
    cursor_up = '\x1b[1A'
    erase_line = '\x1b[2K'
    sys.stdout.write(cursor_up)
    sys.stdout.write(erase_line)

# Hello World
print("Hello, World!")
endproc()

# Print variable
X = 1
if X == 1:
    print("X is equal to %s" % X)
endproc()

# Multiple assignments
A, B = 3, 4
print("Multiple variables assigned on one line")
print(A, B)
endproc()

# Lists
print("List of numbers 1,2,3 using individual prints")
MYLIST = []
MYLIST.append(1)
MYLIST.append(2)
MYLIST.append(3)
print(MYLIST[0])
print(MYLIST[1])
print(MYLIST[2])
print("List of numbers 1,2,3 using a for statement")
for x in MYLIST:
    print(x)
endproc()

# MODULUS
print("Remainder of 11/3")
MODULUS = 11 % 3
print(MODULUS)
endproc()

# Exponents
print("Exponents")
CUBED = 4 ** 3
print("4^3 = %s" % CUBED)
endproc()
