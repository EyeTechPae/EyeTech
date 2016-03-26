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

