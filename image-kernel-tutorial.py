##############################################################################
# TITLE:  Image Kernel
# DESCRIPTION:  Coding a convolutional kernel in python based on C+ code from
#               Code Something on YouTube:  https://youtu.be/oVkCfW_L6Gw
# VERSION:  1.0
# VERSION NOTES:
#     ""
# AUTHOR:  Kenny Haynie
##############################################################################

from PIL import Image
from numpy import *

# Load image for reading pixel values
img=Image.open('test.jpg').convert('LA')
pix=img.load()

# Create new image to write new values
img1=img.copy()
pix1=img1.load()
# img1.show()
xmax,ymax=img.size
print(img.size)

def getPixels(pixelX, pixelY):
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
            p1,p2=pix[i,j]
            tempList.append(p1)
        pixelList.append(tempList)

    pixelMatrix=array(pixelList)
    print(pixelList)
    return pixelMatrix

def gaussianFunction():
    a=0.25
    b=0.125
    c=0.0625
    gaussianKernel=array([[c,b,c],[b,a,b],[c,b,c]])
    return gaussianKernel

def sharpenFunction():
    a=5
    b=-1
    c=0
    gaussianKernel=array([[c,b,c],[b,a,b],[c,b,c]])
    return gaussianKernel

kernel=gaussianFunction()
pixelMatrix=getPixels(random.randint(1,xmax-1), random.randint(1,ymax-1))
finalValue=sum(kernel*pixelMatrix)
print(finalValue)
