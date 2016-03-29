class ParkingPlace(object):

#Mask: path to ParkingPlace mask
    occupied=False

    def __init__(self, mask):
        self.mask=mask  

    def getMask(self):
        return cv2.imread(mask, 0)

    def setOccupancy(state):
        occupied = state
     
