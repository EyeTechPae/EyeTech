import cv2
import classParkingPlace as cPP
import Occupancy_functions as occ
import numpy as np
import d5_2 as track

cap=cv2.VideoCapture('d5-2_mostra.mp4')
cont=0
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('outputBG.avi',fourcc, 30.0, (1280,480),0)    
rval, frame = cap.read()
parking1= cPP.ParkingPlace('placa1.jpg', 1, 40)
parking1.setMask(frame)
parking1.setMaskState()
parking2= cPP.ParkingPlace('placa2.jpg', 2, 40)
parking2.setMask(frame)
parking2.setMaskState()
parking3= cPP.ParkingPlace('placa3.jpg', 3, 40)
parking3.setMask(frame)
parking3.setMaskState()
parking4= cPP.ParkingPlace('placa4.jpg', 4, 40)
parking4.setMask(frame)
parking4.setMaskState()
parking5= cPP.ParkingPlace('placa5.jpg', 5, 40)
parking5.setMask(frame)
parking5.setMaskState()
parking6= cPP.ParkingPlace('placa6.jpg', 6, 20)
parking6.setMask(frame)
parking6.setMaskState()
parking7= cPP.ParkingPlace('placa7.jpg', 7, 20)
parking7.setMask(frame)
parking7.setMaskState()
parking8= cPP.ParkingPlace('placa8.jpg', 8, 20)
parking8.setMask(frame)
parking8.setMaskState()
parking9= cPP.ParkingPlace('placa9.jpg', 9, 20)
parking9.setMask(frame)
parking9.setMaskState()
rval, frame = cap.read()
#tracking
str_open, str_dila = track.get_strelements(28,53)
mask = cv2.imread('mask_d5_2.jpg')
fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=False)
mov = False
conta = 0
while rval:

	img = occ.masked_black(frame, mask)
   # if skp_frame == 5:
	fgmask = fgbg.apply(img)
    #print(fgmask)
	img = track.operacions_morfologiques(fgmask, str_open, str_dila)
	contours = track.get_contours (img)
	centres, frame = track.get_centroids (contours, frame)
	if centres:
		if len(centres) == 1:
 			conta = conta+1 
	if conta% is 0: 
	mov = True
	else:
		mov=False

	


	if cont%70 is 0 and mov == False:
		parking1.checkOccupancy(frame)
		parking2.checkOccupancy(frame)
		parking3.checkOccupancy(frame)
		parking4.checkOccupancy(frame)
		parking5.checkOccupancy(frame)
		parking6.checkOccupancy(frame)
		parking7.checkOccupancy(frame)
		parking8.checkOccupancy(frame)
		parking9.checkOccupancy(frame)
		cv2.imwrite('Video.jpg',frame)
	cont=cont+1
	cv2.imwrite('Video.jpg',frame)
	rval, frame = cap.read()
	if cont%10000 is 0:
		parking1.setMask(frame)
		parking1.setMaskState()
		parking2.setMask(frame)
		parking2.setMaskState()
		parking3.setMask(frame)
		parking3.setMaskState()
		parking4.setMask(frame)
		parking4.setMaskState()
		parking5.setMask(frame)
		parking5.setMaskState()
		parking6.setMask(frame)
		parking6.setMaskState()
		parking7.setMask(frame)
		parking7.setMaskState()
		parking8.setMask(frame)
		parking8.setMaskState()
		parking9.setMask(frame)
		parking9.setMaskState()


cap.release()
#out.release()
