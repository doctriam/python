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

CURSOR_UP='\x1b[1A'
ERASE_LINE='\x1b[2K'

def main_menu():
    print("1. Hello world")
    print("2. Print variable")
    print("3. Multiple Assignments")
    print("4. Lists")
    print("5. Modulus")
    print("6. Exponents")
    print("0. Exit")
    menuOption=int(input("Choose a number from the menu above:"))
    options ={1: hello_world,
              2: print_variable,
              3: multiple_assignments,
              4: list_append,
              5: modulus_function,
              6: exponent_function
             }
    for n in range(0,len(options)+2):
        sys.stdout.write(CURSOR_UP)
        sys.stdout.write(ERASE_LINE)
    print()
    if menuOption in range(1,len(options)+1):
        options[menuOption]()
    else:
        sys.exit()
    print(),print()
    main_menu()

# Hello World
def hello_world():
    print("Prints 'Hello, World!")
    print("Hello, World!")

# Print variable
def print_variable():
    print("Prints a string with an inserted variable")
    X = 1
    if X == 1:
        print("X is equal to %s" % X)

# Multiple assignments
def multiple_assignments():
    A, B = 3, 4
    print("Multiple variables assigned on one line")
    print(A, B)

# Lists
def list_append():
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

# MODULUS
def modulus_function():
    print("Perform a modulus function")
    print("Remainder of 11/3")
    MODULUS = 11 % 3
    print(MODULUS)

# Exponents
def exponent_function():
    print("Exponents")
    CUBED = 4 ** 3
    print("4^3 = %s" % CUBED)

main_menu()
