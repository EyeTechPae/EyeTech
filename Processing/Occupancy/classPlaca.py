import Gaussian as gauss
import numpy as np
from scipy.interpolate import griddata
import matplotlib.pyplot as plt
import numpy.ma as ma
from numpy.random import uniform, seed
from matplotlib import cm
from scipy import ndimage
class Placa(object):

    SIZE_X=720
    SIZE_Y=480
    gaussian=None
   
    def __init__(self, varx, vary, center, threshold):
        self.varx=varx
        self.vary=vary
        self.center=center
        self.threshold=threshold
        
    def initPlaca(self):
        self.gaussian=gauss.makeGaussian(self.SIZE_X,self.SIZE_Y, self.varx, self.vary, self.center)
    def isParked(self,x, y):
        """Return 0 if car is considered not parked and viceversa"""
     
        if self.gaussian[x,y] < self.threshold:
            print("Car not parked")
            return 0
        else:
            print("Car parked")
            return 1


sizeX=100
sizeY=100
placa=Placa(15, 2, center=None, threshold=0.5)
placa.initPlaca()
#parked=isParked(gaussian, 2, 3)
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_aspect('equal')
plt.imshow(placa.gaussian, interpolation='nearest', cmap=plt.cm.ocean)
plt.colorbar()
plt.show()
#gausstr=np.array2string(gaussian)
#print(gaussian.max())
"""
for i in gaussian:
    text_file=open("Output.txt", "w")
    text_file.write(np.array2string(i))
text_file.close()"""

np.savetxt("output.txt", placa.gaussian)
