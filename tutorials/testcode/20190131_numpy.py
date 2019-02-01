##############################################################################
# TITLE:  01/31/2019 - Numpy Test Code
# DESCRIPTION:  Just trying to figure out how arrays work in numpy
# AUTHOR:  Kenny Haynie
##############################################################################

from numpy import *
# Create array
x=array([[1,2,3],[4,5,6],[7,8,9]])
print("Original Array")
print(x)

# Delete array row - Tested: Working
    # Deletes row(axis=0) at row index  = (0)
def deleterow(x):
    x=delete(x,(0),axis=0)
    print("Delete Row 0:")
    print(x)
    return

# Delete array column - Tested: Working
    # Deletes column(axis=1) at column index = (0)
def deletecol(x):
    x=delete(x,(0),axis=1)
    print("Delete Column 0:")
    print(x)
    return

# Show what happens when i is out of data range
    # index = -1: loops backwards from end of data = 5
    # index = 5: throws out of index range error
def kerneltest():
    data=array([1,2,3,4,5])
    kernel=array([0,1,0])
    for i in range(-1,6):
        p1=data[i]
        print(p1)
    return

deleterow(x)
deletecol(x)
