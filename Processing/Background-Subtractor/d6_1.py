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
	#opening = cv2.morphologyEx(fore_image, cv2.MORPH_OPEN, strelement_opening)
	#closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, strelement_opening)
	closing = cv2.erode(fore_image,strelement_opening,iterations = 2)	
	dilation = cv2.dilate(closing,strelement_dilation,iterations = 3)
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

			area=cv2.contourArea(contours[i])                    
			rect = cv2.minAreaRect(contours[i])
			box = cv2.boxPoints(rect)
			box = np.int0(box)
			frame = cv2.drawContours(frame,[box],0,(0,0,255),2)

			
	return centres, frame

		

def calculateDistance(x1,y1,x2,y2):
     dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
     return dist


#Inicialització del lector i escriptor de vídeo, monitorització del temps d'execució i creació del background substractor
t=time.time()
cap = cv2.VideoCapture('d6-1_mostra.mp4')
t=time.time()
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output_d6_1.avi',fourcc, 15.0, (427, 240))
outgray = cv2.VideoWriter('output_bg_gray.avi',fourcc, 15.0, (427, 240),0)

fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=True)

ret = True
str_open, str_dila = get_strelements(4,12)
ret, frame = cap.read()
frame = cv2.resize(frame, (427, 240)) 
cv2.imwrite('frame.jpg',frame)
skp_frame =0
mask = cv2.imread('mask_d6_1.jpg')
while ret:
    frame = cv2.resize(frame, (427, 240)) 
    img = msk.masked(frame, mask)
   # if skp_frame == 5:
    fgmask = fgbg.apply(img)
    #print(fgmask)
    img = operacions_morfologiques(fgmask, str_open, str_dila)
    contours = get_contours (img)
    centres, frame = get_centroids (contours, frame)
    skp_frame = 0
    out.write(frame)
    outgray.write(img)
    ret, frame = cap.read()
    
    skp_frame = skp_frame + 1

cap.release()
out.release()
outgray.release()
tend=time.time()-t
print(tend)
cv2.destroyAllWindows()




