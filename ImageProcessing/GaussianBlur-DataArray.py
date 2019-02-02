##############################################################################
# TITLE:  Gaussian Blur on Data Array
# DESCRIPTION:  Gaussian blur algorithm derived from
#               https://youtu.be/BQyMZ0caFbg (starts at 8:17) by user M
# VERSION:  1.1
# VERSION NOTES:
#   01/31/2019 - Finished Gaussian blur of data array
#   02/01/2019 - Removed excess code and reorganized
# AUTHOR:  Kenny Haynie
##############################################################################

from numpy import *

# Basic Gaussian Blur (8:17)
def getPixels(pixelX, pixelY,  data, kernel, finalList):
    # This function calculates the Gaussian-blurred pixel value for a single
    # pixel and passes it to the main function

    # Create matrix of pixel values in kernel range
    kernelRange=1
    lowX=pixelX-kernelRange
    highX=pixelX+kernelRange+1 # +1 for range end
    lowY=pixelY-kernelRange
    highY=pixelY+kernelRange+1 # +1 for range end

    # Grab 3x3 matrix of pixel values surrounding focused pixel as list
    pixelList=list([])
    for i in range(lowY,highY):
        tempList=list([])
        for j in range(lowX,highX):
            if i!=-1 and i!=len(data) and j!=-1 and j!=len(data[0]):
                # Grab values for cells within the image
                p1=data[i,j]
                tempList.append(p1)
            else:
                # Grab nearest cell values for cells outside of image
                if i==-1:
                    tempi=0
                elif i==len(data[0]):
                    tempi=len(data[0])-1
                else:
                    tempi=i
                if j==-1:
                    tempj=0
                elif j==len(data):
                    tempj=len(data)-1
                else:
                    tempj=j
                p1=data[tempi,tempj]
                tempList.append(p1)
        pixelList.append(tempList)

    # Convert pixel matrix list to array
    pixelMatrix=array(pixelList)

    # Calculate final pixel value
    finalpixel=sum(pixelMatrix*kernel)
    return finalpixel

# Create data array
a,b=0,100
data=array([[b,b,b,b,b],[b,a,a,a,b],[b,a,a,a,b],[b,a,a,a,b],[b,b,b,b,b]])
width,height=len(data),len(data[0])
print("Data Array:")
print(data)
print("")

# Create Gaussian kernel
a,b,c=0.0625,0.125,0.25
kernel=array([[a,b,a],[b,c,b],[a,b,a]])
print("Gaussian Blur Kernel:")
print(kernel)
print("")

# Generate list of new array values
finalList=list([])
for x in range(0,width):
    rowList=list([])
    for y in range(0,height):
        pixel=getPixels(x,y,data,kernel,finalList)
        rowList.append(pixel)
    finalList.append(rowList)

# Convert list of array values to final array of blurred matrix
finalMatrix=array(finalList)
print("Gaussian-Blurred Matrix:")
print(finalMatrix)
