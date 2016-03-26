import numpy as np
from scipy.interpolate import griddata
import matplotlib.pyplot as plt
import numpy.ma as ma
from numpy.random import uniform, seed
from matplotlib import cm
from scipy import ndimage

def makeGaussian(sizeX, sizeY, fwhmx = 3, fwhmy=3,center=None):
    """ Make a rectangular gaussian kernel.

    size is the length of a side of the square
    fwhm is full-width-half-maximum, which
    can be thought of as an effective radius.
    """

    gaussian=np.zeros((sizeX,sizeY))
    #x = np.arange(0, sizeX, 1, float)
    #y = x[:,np.newaxis]

    if center is None:
       gaussian[sizeX // 2,sizeY // 2]= 1 # Delta 
    else:
        gaussian[center[0],center[1]]= 1 # Delta


    return ndimage.filters.gaussian_filter(gaussian, [fwhmx,fwhmy])


def isParked(gaussian, x, y, threshold):
    """Return 0 if car is considered not parked and viceversa"""
     
    if gaussian[x,y] < threshold:
        print("Car not parked")
        return 0
    else:
        print("Car parked")
        return 1


sizeX=100
sizeY=100
gaussian=makeGaussian(sizeX,sizeY, 15, 2, center=None)
#parked=isParked(gaussian, 2, 3)
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_aspect('equal')
plt.imshow(gaussian, interpolation='nearest', cmap=plt.cm.ocean)
plt.colorbar()
plt.show()
#gausstr=np.array2string(gaussian)
#print(gaussian.max())
"""
for i in gaussian:
    text_file=open("Output.txt", "w")
    text_file.write(np.array2string(i))
text_file.close()"""

np.savetxt("output.txt", gaussian)
