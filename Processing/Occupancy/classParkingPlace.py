import cv2
class ParkingPlace(object):

#Mask: path to ParkingPlace mask

    def __init__(self, mask):
        self.im_mask=cv2.imread(mask, 0)
        self.occupied=False
        self.actualMask=None

    def getMask(self, frame):
        
        self.actualMask= frame*self.im_mask
        self.actualMask = cv2.cvtColor(self.actualMask, cv2.COLOR_BGR2GRAY)
        return self.actualMask
        
    def setOccupancy(self, state):
        self.occupied = state
 

"""La classe càmera inicialitza les places amb la seva màscara.
Per accedir a la màscara de la plaça existeix el mètode getMask.
Per canviar la ocupació està el mètode setOccupancy(state), on state és un booleà. 
La classe Cam ha de controlar quin és l'estat de la Plaça mitjançamt mètodes de correlació (o altres)"""
     
