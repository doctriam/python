##############################################################################
# TITLE:  Gaussian Kernel Image Processing
# DESCRIPTION:  Gaussian blur, sharpen, and edge detection
# VERSION:  1.0
# VERSION NOTES:
#   Finished Gaussian blur of data array.  Added Gaussian blur, sharpening,
#   and edge detection for 'test.jpg' image.
# AUTHOR:  Kenny Haynie
##############################################################################

from numpy import *
from PIL import Image

testImageLocation='TestImages/test-fry.jpg' # Set as your test image
saveLocation='Output/'
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

# Load image + copy
img=Image.open(testImageLocation).convert('L')
pix=img.load()
img1=img.copy()
pix1=img1.load()

# Choose Gaussian kernel
kernelType=input("[B]lur, [S]harpen, or [E]dge detection?")
blur=list([0.0625,0.125,0.25])
sharpen=list([0,-1,5])
edge=list([-1,-1,8])
if kernelType==('s' or 'S'):
    a,b,c=sharpen
    saveLocation=str(saveLocation) + 'gauss-sharp'
elif kernelType==('e' or 'E'):
    a,b,c=edge
    saveLocation=str(saveLocation) + 'gauss-edge'
else:
    a,b,c=blur
    saveLocation=str(saveLocation) + 'gauss-blur'
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
img1.save(str(saveLocation)+'.jpg')
