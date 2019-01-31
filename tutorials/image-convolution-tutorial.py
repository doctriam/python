##############################################################################
# TITLE:  Image Convolution Tutorial
# DESCRIPTION:  Examples from https://youtu.be/BQyMZ0caFbg by user M
# VERSION:  0.5
# VERSION NOTES:
#     Gaussian works for all but outer edges; need to solve those
# AUTHOR:  Kenny Haynie
##############################################################################

from numpy import *

# Basic Gaussian Blur (8:17)
def getPixels(pixelX, pixelY, data, gaussian, finalList):
    # Create matrix of pixel values in kernel range
    kernelRange=1
    lowX=pixelX-kernelRange
    highX=pixelX+kernelRange+1
    lowY=pixelY-kernelRange
    highY=pixelY+kernelRange+1

    # Grab pixel values
    pixelList=list([])
    for i in range(lowX,highX):
        tempList=list([])
        for j in range(lowY,highY):
            p1=data[i,j]
            tempList.append(p1)
        pixelList.append(tempList)

    pixelMatrix=array(pixelList)
    finalpixel=sum(pixelMatrix*gaussian)

#    print(pixelList)
    return finalpixel

def basicGaussianBlur():
    # Create image
    a,b=0,100
    data=array([[b,b,b,b,b],[b,a,a,a,b],[b,a,a,a,b],[b,a,a,a,b],[b,b,b,b,b]])
    width,height=len(data),len(data[0])
    print(data)

    # Create Gaussian kernel
    a,b,c=0.0625,0.125,0.25
    gaussian=array([[a,b,a],[b,c,b],[a,b,a]])
    print(gaussian)

    finalList=list([])
    for x in range(1,width-1):
        rowList=list([])
        for y in range(1,height-1):
            pixel=getPixels(x,y,data,gaussian,finalList)
            rowList.append(pixel)
        finalList.append(rowList)

    finalMatrix=array(finalList)
    print(finalMatrix)

basicGaussianBlur()
