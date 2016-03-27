from __future__ import print_function
import numpy as np
import cv2
from time import sleep
import sys
import functools as ft
import time
import math


#elements estructurants que utilitzarem per les operacions morfològiques
def get_strelements(size_open, size_dilation):
	open_str = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(size_open,size_open))
	dila_str = np.ones((size_dilation,size_dilation),np.uint8)
	return open_str, dila_str
	


#operacions morfològiques
def operacions_morfològiques (fore_image, strelement_opening, strelement_dilation):
	
	kernel = strelement_opening
	kernel_dilation = strelement_dilation
	opening = cv2.morphologyEx(back_image, cv2.MORPH_OPEN, kernel)
	closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
	dilation = cv2.dilate(closing,kernel_dilation,iterations = 1)
	return dilation

#extracció del background de la imatge:
def create_background:
	fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=True)
	return fgbg


def get_foreground(image):
	fore = fgbg.apply(frame)
	return fore
	
#estimació de contorns i posterior dibuix dels contorns

def get_contours (fore_image):
	ret,thresh = cv2.threshold(fore_image, 127, 255, 0)
	im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	return contours;

#retorna els centroides a partir del vector de contorns
def get_centroids (contours):
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
        	                		frame = cv2.drawContours(frame,[box],0,(0,0,255),2)
        	            		else :
        	                		rect = cv2.minAreaRect(contours[i-1])
						box = cv2.boxPoints(rect)
						box = np.int0(box)
						frame = cv2.drawContours(frame,[box],0,(0,0,255),2)
			else:
 	
				rect = cv2.minAreaRect(contours[i])
				box = cv2.boxPoints(rect)
				box = np.int0(box)
				frame = cv2.drawContours(frame,[box],0,(0,0,255),2)
	
	return centres

		

def calculateDistance(x1,y1,x2,y2):
     dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
     return dist



