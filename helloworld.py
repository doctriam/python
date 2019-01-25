# AUTHOR:  Kenneth Haynie, Jr.
# DESCRIPTION:  Walkthroughs of tutorials from learnpython.org
# EDITOR:  VIM 8.0.1453

def endproc():
    # Function for prompting user input
    # and deleting prompt after Enter is pressed 
    input("\nPress Enter to continue")
    CURSOR_UP='\x1b[1A'
    ERASE_LINE='\x1b[2K'
    import sys
    sys.stdout.write(CURSOR_UP)
    sys.stdout.write(ERASE_LINE)
    return

# Hello World
print("Hello, World!")
endproc()

# Print variable
x=1
if x==1:
    print("x is equal to %s" % x)
endproc()

# Multiple assignments
a,b=3,4
print("Multiple variables assigned on one line")
print(a,b)
endproc()

# Lists
print("List of numbers 1,2,3 using individual prints")
mylist=[]
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0])
print(mylist[1])
print(mylist[2])
print("List of numbers 1,2,3 using a for statement")
for x in mylist:
    print(x)
endproc()

# Modulus
print("Remainder of 11/3")
modulus=11%3
print(modulus)
endproc()

# Exponents
print("Exponents")
cubed=4**3
print("4^3 = %s" % cubed)
endproc()
