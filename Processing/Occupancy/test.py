import cv2
import classParkingPlace as cPP
import Occupancy_functions as occ
import numpy as np

cap=cv2.VideoCapture('cotxeVerd.mp4')
cont=0
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('outputBG.avi',fourcc, 30.0, (1280,480),0)    
rval, frame = cap.read()

parking= cPP.ParkingPlace('placa9.jpg', 2, 20)
parking.setMask(frame)
parking.setMaskState()
rval, frame = cap.read()
while rval:
	if cont%30 is 0:
		parking.checkOccupancy(frame)
	cont=cont+1
	cv2.imwrite('Video.jpg',frame)
	rval, frame = cap.read()

cap.release()
#out.release()
