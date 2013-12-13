#d = img.show()

#from skimage import filter, transform, io
#img = io.imread("pics/DSC_1515.jpg", True)
#img = transform.resize(img, (64,48))
#c = filter.canny(img)



#print 'Detecting ellpises...'
#ellipse = transform.hough_ellipse(c)

#print ellipse

from SimpleCV import *

disp = Display()
img = Image("pics/DSC_1525.jpg")
img = img.resize(640,480)

color_img = img.colorDistance( (127, 19, 68) ).binarize(40)

#glass = img - color_img
#img.show()
color_img.show()
#glass.show()

while disp.isNotDone():
    pass