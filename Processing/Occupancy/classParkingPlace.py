class ParkingPlace(object):

#Mask: path to ParkingPlace mask
    occupied=False

    def __init__(self, mask):
        self.mask=mask  

    def getMask(self):
        self.mask=cv2.imread(mask, 0)
        return self.mask
    def setOccupancy(self, state):
        self.occupied = state

"""La classe càmera inicialitza les places amb la seva màscara.
Per accedir a la màscara de la plaça existeix el mètode getMask.
Per canviar la ocupació està el mètode setOccupancy(state), on state és un booleà. 
La classe Cam ha de controlar quin és l'estat de la Plaça mitjançamt mètodes de correlació (o altres)"""
     
