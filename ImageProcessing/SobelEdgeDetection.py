"""############################################################################
# TITLE:  Gaussian Kernel Image Processing
# DESCRIPTION:  Gaussian blur,  sharpen,  and edge detection
# VERSION:  1.0
# VERSION NOTES:
#   Finished Gaussian blur of data array.  Added Gaussian blur,  sharpening,
#   and edge detection for 'test.jpg' image.
# AUTHOR:  Kenny Haynie
############################################################################"""

import sys
from numpy import *
from PIL import Image

CURSOR_UP = '\x1b[1A'
ERASE_LINE = '\x1b[2K'

# File management
testImageLocation = 'TestImages/test-fry-small.jpeg' # Set as your test image
saveLocation = 'Output/sobel'

# Load image + copy
img = Image.open(testImageLocation).convert('L')
pix = img.load()
img1 = img.copy()
pix1 = img1.load()

# Create needed variables
width, height = img.size
width = round(width/2)

# Choose Gaussian kernel
print()
print()
kernelX = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
kernelY = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]


# ---------------FUNCTIONS-----------------
def setPixels(pixelX, pixelY):
    """ Passes kernel over the pixels """
    if pixelY == width:
        for i in range(0, 2):
            sys.stdout.write(CURSOR_UP)
            sys.stdout.write(ERASE_LINE)
        print("Completion: %.2f %%" % (pixelX/width*100))
        print("[Row:  %.0f of %.0f]" % (pixelX, width))

    # Create matrix of pixel values in kernel range
    kernelRange = 1
    lowX = pixelX-kernelRange
    highX = pixelX+kernelRange+1 # +1 for range end
    lowY = pixelY-kernelRange
    highY = pixelY+kernelRange+1 # +1 for range end

    # Grab pixel values as a matrix
    pixelList = []
    for i in range(lowX, highX):
        tempList = []
        for j in range(lowY, highY):
            if i != -1 and i != width and j != -1 and j != height:
                p1 = pix[i, j]
            else:
                if i == -1:
                    tempi = 0
                elif i == width:
                    tempi = width-1
                else:
                    tempi = i
                if j == -1:
                    tempj = 0
                elif j == height:
                    tempj = height-1
                else:
                    tempj = j
                p1 = pix[tempi, tempj]
            tempList.append(p1)
        pixelList.append(tempList)
    pixelMatrix = array(pixelList)

    outX = sum(pixelMatrix*kernelX)
    outY = sum(pixelMatrix*kernelY)
    output = sqrt(outX**2 + outY**2)
    return output
# ---------------FUNCTIONS-----------------


# Process Pixels
for x in range(0, width):
    for y in range(0, height):
        pixelValue = setPixels(x, y)
        pix1[x, y] = int(pixelValue)

# Print a black line to separate edge detection from original picture
for y in range(0, height):
    pix1[width, y] = 0
    pix1[width+1, y] = 0

# Save and display output
img1.save(str(saveLocation)+'.jpg')
img1.show()
