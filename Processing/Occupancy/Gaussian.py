import numpy as np

def makeGaussian(size, fwhm = 3, center=None):
    """ Make a square gaussian kernel.

    size is the length of a side of the square
    fwhm is full-width-half-maximum, which
    can be thought of as an effective radius.
    """

    x = np.arange(0, size, 1, float)
    y = x[:,np.newaxis]

    if center is None:
        x0 = y0 = size // 2
    else:
        x0 = center[0]
        y0 = center[1]

    return np.exp(-4*np.log(2) * ((x-x0)**2 + (y-y0)**2) / fwhm**2)


def isParked(gaussian, x, y):
    """Return 0 if car is considered not parked and viceversa"""
     
    if gaussian[x,y] < 0.5:
        print("Car not parked")
        return 0
    else:
        print("Car parked")
        return 1

size=4
gaussian=makeGaussian(size, fwhm=3, center=None)
print(gaussian)
parked=isParked(gaussian, 3, 3)
