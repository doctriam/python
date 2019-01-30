##############################################################################
# TITLE:  Image Basic Edge Detection
# DESCRIPTION:  Uses basic detection of color changes around an pixel that
#               exist outside of a given threshold
# VERSION:  1.0
# VERSION NOTES:
#     ""
# AUTHOR:  Kenny Haynie
##############################################################################

from PIL import Image
from datetime import datetime, date, time

# Load Image
im=Image.open('test.jpg')
pix=im.load()
print(im.size)

# Edge Detection
threshold = 40
range1=1
image1=im.copy()
pix1=image1.load()
for x in range(0,im.size[0]):
    for y in range(0,im.size[1]):
        r,g,b=pix[x,y]
        detected=1
        comparray=[]
        for x1 in range(-range1,range1+1): #create array
            for y1 in range(-range1,range1+1):
                if (x+x1) >= 0 and (x+x1) < im.size[0] and (y+y1) >= 0 \
                   and (y+y1) < im.size[1]:
                    r1,g1,b1=pix[x+x1,y+y1]
                    if ((r-threshold) <= r1 <= (r+threshold)):
                        detected=0
                    if ((g-threshold) <= g1 <= (g+threshold)):
                        detected=0
                    if ((b-threshold) <= b1 <= (b+threshold)):
                        detected=0
                comparray.append(detected)
        printarray=0

        # Convert pixels to black or white
        for n in range(0,9):
            if comparray[n]==1:
                printarray=1
        if printarray==1:
            pix1[x,y]=(255,255,255)
        else:
             pix1[x,y]=(0,0,0)

# Save Image
now=datetime.now()
filename='/home/kenny/GIT/python/Output/imageedge_' + \
    now.strftime("%Y%m%d%H%M%S") + '.jpg'
image1.save(filename)
