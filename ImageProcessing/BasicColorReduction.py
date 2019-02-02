##############################################################################
# TITLE:  Image Test
# DESCRIPTION:  Down-convert color range from full color to 8 colors
# VERSION:  1.1
# VERSION NOTES:
#     Added show image at end at set file locations as variables
# AUTHOR:  Kenny Haynie
##############################################################################

from PIL import Image
from datetime import datetime

testImageLocation='TestImages/test-lola.jpg'
saveLocation='Output/imageRGBredux'

# Load Image
im=Image.open(testImageLocation)
pix=im.load()
print(im.size)

# Reduce image colors to 8 colors
for x in range(0, im.size[0]-1):
    for y in range(0, im.size[1]-1):
        r,g,b=pix[x,y]
        if r > 122:
            r0=255
        else:
            r0=0
        if g > 122:
           g0=255;
        else:
            g0=0
        if b > 122:
            b0=255
        else:
            b0=0
        pix[x,y]=(r0,g0,b0)

# Save Image
now=datetime.now()
filename=str(saveLocation) + '_' + now.strftime("%Y%m%d%H%M%S")+'.jpg'
im.save(filename)
im.show()
