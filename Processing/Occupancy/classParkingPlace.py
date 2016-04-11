import cv2
import Occupancy_functions as occ
class ParkingPlace(object):

#Mask: path to ParkingPlace mask

    def __init__(self, mask, ID, threshold):
        self.im_mask=cv2.imread(mask, 0)
        self.occupied=False
        self.actualMask=None
        self.ID=ID
        self.threshold=threshold
        self.kp=None
        self.des=None

    def setMask(self, frame_path):
        frame=cv2.cvtColor(frame_path,cv2.COLOR_BGR2GRAY)
        self.actualMask= frame*self.im_mask
        self.kp,self.des=occ.computeSurfFeatures(self.actualMask)
        cv2.imwrite('Placa.jpg',self.actualMask)
       

    def setOccupancyState(self, state):
        self.occupied = state
    
    def setMaskState(self):
        self.maskState=self.occupied

    def checkOccupancy(self, frame):
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame_masked = frame_gray * self.im_mask
        kp, des= occ.computeSurfFeatures(frame_masked)
        good_matches = occ.computeGoodMatches(frame_masked, self.kp, self.des)
        if not self.maskState:
            if good_matches > self.threshold:
                self.setOccupancy(False)
            else:
                self.setOccupancy(True)
            #self.actualMask= frame*self.im_mask
                cv2.imwrite('Placa.jpg',frame_masked)
          #  self.setMask(frame)
            print("Placa "+ str(self.ID) + " ocupada?" + str(self.occupied)+ " " + str(good_matches))
        if self.maskState:
            if good_matches > self.threshold:
                self.setOccupancy(True)
            else:
                self.setOccupancy(False)
            #self.actualMask= frame*self.im_mask
                cv2.imwrite('Placa.jpg',frame_masked)
          #  self.setMask(frame)
            print("Placa "+ str(self.ID) + " ocupada?" + str(self.occupied)+ " " + str(good_matches))

"""La classe càmera inicialitza les places amb la seva màscara.
Per crear la màscara amb la placa de parking segmentada existeix el metode setMask.
Per canviar la ocupació està el mètode setOccupancy(state), on state és un booleà. 
La classe Cam, per cada plaça, haurà de fer checkOccupancy cada cop que s'hagi detectat moviment en la zona de parking. Podem dividir les zones de Parking i aixi fem menys comparacions cada cop que es mogui, guanyant temps de computacio."""
     
