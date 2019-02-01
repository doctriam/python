##############################################################################
# TITLE:  Image Convolution Tutorial
# DESCRIPTION:  Examples from https://youtu.be/BQyMZ0caFbg by user M
# VERSION:  1.0
# VERSION NOTES:
#   Finished Gaussian blur of data array.  Added Gaussian blur, sharpening,
#   and edge detection for 'test.jpg' image.
# AUTHOR:  Kenny Haynie
##############################################################################

from numpy import *
from PIL import Image

# Basic Gaussian Blur (8:17)
# - getPixelsData and basicGaussianBlurData performs a Gaussian blur
# - on a 5x5 integer array
def getPixelsData(pixelX, pixelY,  data, gaussian, finalList):
    # Create matrix of pixel values in kernel range
    kernelRange=1
    lowX=pixelX-kernelRange
    highX=pixelX+kernelRange+1 # +1 for range end
    lowY=pixelY-kernelRange
    highY=pixelY+kernelRange+1 # +1 for range end
    print("Pixel("+str(pixelX)+", "+str(pixelY)+")")

    # Grab pixel values as a matrix
    pixelList=list([])
    for i in range(lowY,highY):
        tempList=list([])
        for j in range(lowX,highX):
            if i!=-1 and i!=len(data) and j!=-1 and j!=len(data[0]):
                p1=data[i,j]
                tempList.append(p1)
            else:
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
        print(tempList)
        pixelList.append(tempList)
    pixelMatrix=array(pixelList)
    print("Pixel Matrix:")
    print(pixelMatrix)

    finalpixel=sum(pixelMatrix*gaussian)
#    print(pixelList)
    return finalpixel

def basicGaussianBlurData():
    # Create image
    a,b=0,100
    data=array([[b,b,b,b,b],[b,a,a,a,b],[b,a,a,a,b],[b,a,a,a,b],[b,b,b,b,b]])
    width,height=len(data),len(data[0])
    print("Data Array:")
    print(data)

    # Create Gaussian kernel
    a,b,c=0.0625,0.125,0.25
    gaussian=array([[a,b,a],[b,c,b],[a,b,a]])
    print("Kernel:")
    print(gaussian)
    print("")

    finalList=list([])
    for x in range(0,width):
        rowList=list([])
        for y in range(0,height):
            pixel=getPixelsData(x,y,data,gaussian,finalList)
            rowList.append(pixel)
        finalList.append(rowList)

    finalMatrix=array(finalList)
    print(finalMatrix)

# - basicGaussianBlur() and setPixels() performs Gaussian blur or
# - Gaussian sharpening on a test image.  Load an image labelled 'test.jpg'
# - into same folder as code
def basicGaussianBlur():
    # Load image + copy
    img=Image.open('test.jpg').convert('L')
    pix=img.load()
    img1=img.copy()
    pix1=img1.load()

    # Create Gaussian kernel
    a,b,c=0.0625,0.125,0.25 # Uncomment for Gaussian blur
#    a,b,c=0,-1,5 # Uncomment for Gaussian sharpen
#    a,b,c=-1,-1,8 # Uncomment for edge detection
    kernel=array([[a,b,a],[b,c,b],[a,b,a]])

    # Create needed variables
    width,height=img.size
    width=round(width/2)

    for x in range(0,width):
        for y in range(0,height):
            pixelValue=setPixels(x,y,width,height,pix,pix1,kernel)
            pix1[x,y]=int(pixelValue)
    for y in range(0,height):
        pix1[width,y]=0
        pix1[width+1,y]=0

    img1.show()
    img1.save('test1.jpg')

def setPixels(pixelX, pixelY, width, height, pix, pix1, kernel):
    # Create matrix of pixel values in kernel range
    kernelRange=1
    lowX=pixelX-kernelRange
    highX=pixelX+kernelRange+1 # +1 for range end
    lowY=pixelY-kernelRange
    highY=pixelY+kernelRange+1 # +1 for range end

    # Grab pixel values as a matrix
    pixelList=[]
    for i in range(lowX,highX):
        tempList=[]
        for j in range(lowY,highY):
            if i!=-1 and i!=width and j!=-1 and j!=height:
                p1=pix[i,j]
            else:
                if i==-1:
                    tempi=0
                elif i==width:
                    tempi=width-1
                else:
                    tempi=i
                if j==-1:
                    tempj=0
                elif j==height:
                    tempj=height-1
                else:
                    tempj=j
                p1=pix[tempi,tempj]
            tempList.append(p1)
        pixelList.append(tempList)
    pixelMatrix=array(pixelList)

    pixelValue=sum(pixelMatrix*kernel)
    return pixelValue


# basicGaussianBlur() # Uncomment to perform blur on 'test.jpg'
basicGaussianBlurData() # Uncomment to perform blur on data array
