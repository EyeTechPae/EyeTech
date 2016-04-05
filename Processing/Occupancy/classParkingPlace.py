import cv2
class ParkingPlace(object):

#Mask: path to ParkingPlace mask

    def __init__(self, mask, ID, threshold):
        self.im_mask=cv2.imread(mask, 0)
        self.occupied=False
        self.actualMask=None
	self.ID=ID
	self.threshold=threshold

    def setMask(self, frame_path):
	frame=cv2.cvtColor(frame_path,cv2.COLOR_BGR2GRAY)
        self.actualMask= frame*self.im_mask
        
    def setOccupancy(self, state):
        self.occupied = state

    def checkOccupancy(self, frame):
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame_masked = frame_gray * self.im_mask
        good_matches = surf_algorithm(frame_masked, self.actualMask)
        if good_matches > self.threshold:
            setOccupancy(self.occupied)
        else:
            setOccupancy(not self.occupied)
            setMask(frame)

"""La classe càmera inicialitza les places amb la seva màscara.
Per crear la màscara amb la placa de parking segmentada existeix el metode setMask.
Per canviar la ocupació està el mètode setOccupancy(state), on state és un booleà. 
La classe Cam, per cada plaça, haurà de fer checkOccupancy cada cop que s'hagi detectat moviment en la zona de parking. Podem dividir les zones de Parking i aixi fem menys comparacions cada cop que es mogui, guanyant temps de computacio."""
     
