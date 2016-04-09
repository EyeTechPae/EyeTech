from __future__ import print_function
import numpy as np
import cv2
from time import sleep
import sys
import functools as ft
import time
import math
import occu_funcions as msk


#elements estructurants que utilitzarem per les operacions morfològiques
def get_strelements(size_open, size_dilation):
	open_str = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(size_open,size_open))
	dila_str = np.ones((size_dilation,size_dilation),np.uint8)
	return open_str, dila_str
	


#operacions morfològiques
def operacions_morfologiques (fore_image, strelement_opening, strelement_dilation):
	opening = cv2.morphologyEx(fore_image, cv2.MORPH_OPEN, strelement_opening)
	closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, strelement_opening)
	dilation = cv2.dilate(closing,strelement_dilation,iterations = 1)
	return dilation

#extracció del background de la imatge:
#def create_background:
#	fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=True)
#	return fgbg


def get_foreground(image, fgbg):
	fore = fgbg.apply(image)
	return fore
	
#estimació de contorns i posterior dibuix dels contorns

def get_contours (fore_image):
	ret,thresh = cv2.threshold(fore_image, 127, 255, 0)
	im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	return contours;

#retorna els centroides a partir del vector de contorns
def get_centroids (contours, frame):
	centres = []
	if contours:
		for i in range(len(contours)):
			moments = cv2.moments(contours[i])
			centres.append((int(moments['m10']/moments['m00']), int(moments['m01']/moments['m00'])))
		
			if i>0:                
				dist = calculateDistance(centres[i-1][0],centres[i-1][1],centres[i][0],centres[i][1])
				area=cv2.contourArea(contours[i])
				prevarea=cv2.contourArea(contours[i-1])
				if dist < 120:                    
					if area > prevarea:
						rect = cv2.minAreaRect(contours[i])
						box = cv2.boxPoints(rect)
						box = np.int0(box)
						print(box)
						frame = cv2.drawContours(frame,[box],0,(0,0,255),2)
					else :
						rect = cv2.minAreaRect(contours[i-1])
						box = cv2.boxPoints(rect)
						box = np.int0(box)
						print(box)
						frame = cv2.drawContours(frame,[box],0,(0,0,255),2)
			else:
 	
				rect = cv2.minAreaRect(contours[i])
				box = cv2.boxPoints(rect)
				box = np.int0(box)
				frame = cv2.drawContours(frame,[box],0,(0,0,255),2)
				print(box)
	return centres, frame

		

def calculateDistance(x1,y1,x2,y2):
     dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
     return dist


#Inicialització del lector i escriptor de vídeo, monitorització del temps d'execució i creació del background substractor
t=time.time()
cap = cv2.VideoCapture('d5-1_mostra.mp4')
t=time.time()
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output_d5_1.avi',fourcc, 15.0, (1280,720))
#outgray = cv2.VideoWriter('output_bg_gray.avi',fourcc, 15.0, (1280,720),0)

fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=True)

ret = True
str_open, str_dila = get_strelements(28,53)
ret, frame = cap.read()
cv2.imwrite('frame.jpg',frame)
skp_frame =0
mask = cv2.imread('mask_d5_1.jpg')
while ret:
    img = msk.masked(frame, mask)
   # if skp_frame == 5:
    fgmask = fgbg.apply(img)
    #print(fgmask)
    img = operacions_morfologiques(fgmask, str_open, str_dila)
    contours = get_contours (img)
    centres, frame = get_centroids (contours, frame)
    skp_frame = 0
    out.write(frame)
    #outgray.write(img)
    ret, frame = cap.read()

    skp_frame = skp_frame + 1

cap.release()
out.release()
#outgray.release()
tend=time.time()-t
print(tend)
cv2.destroyAllWindows()




