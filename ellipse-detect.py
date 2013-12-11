#d = img.show()

from skimage import filter, transform, io
img = io.imread("pics/DSC_1515.jpg", True)
img = transform.resize(img, (64,48))
c = filter.canny(img)

print 'Detecting ellpises...'
ellipse = transform.hough_ellipse(c)

print ellipse