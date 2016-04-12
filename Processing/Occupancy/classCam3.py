from abc import ABCMeta, abstractmethod
import ClassCam as Cam

class Cam3(Cam):
# Masks order: Mask In, Mask Out, Mask Parking Up, Mask Parking Down
    def __init__(self, masks, ID, parksUp, parksDown):
        for mask, index in zip(masks,range(len(masks))):
            self.masks[index]=cv2.imread(mask, 0)
        for parkUp, index in zip(parksUp, range(len(parksUp))):
            self.parksUp[index]=parkUp
        for parkDown, index in zip(parksDown, range(len(parksUp))):
            self.parksDown[index]=parkDown
        self.ID=ID

    def isZoneIn(self): #override 
        pass #TODO

    def isZoneOut(self):  #override 
        pass #TODO

    def isParkingDown(self): #override 
        pass #TODO

    def isParkingUp(self): #override 
        pass #TODO

    def checkCamState(self): #override 
        if isParkingDown():
            for parkDown in self.parksDown:
                parkDown.checkOccupancyState()
        if isParkingUp():
            for parkUp in self.parksUp:
                parkUp.checkOccupancyState()






