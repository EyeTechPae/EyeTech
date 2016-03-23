from __future__ import print_function
import numpy as np
import cv2
from time import sleep
import sys
import functools as ft
import time
import math


def calculateDistance(x1,y1,x2,y2):
     dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
     return dist


#Inicialització del lector i escriptor de vídeo, monitorització del temps d'execució i creació del background substractor
t=time.time()
cap = cv2.VideoCapture('prova_10min.mp4')
t=time.time()
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output_bg.avi',fourcc, 15.0, (360,240))
outgray = cv2.VideoWriter('output_bg_gray.avi',fourcc, 15.0, (360,240),0)
fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=True)
ret = True
#element estructurant que utilitazrem per l'opening+closing per eliminar falsos positius (matriu quadrada de 8x8 píxels)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(8,8))
kernel_dilation = np.ones((15,15),np.uint8)


while ret:
    
    #lectura i estimació del background
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    
    #operacions morfològiques
    opening = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
    dilation = cv2.dilate(closing,kernel_dilation,iterations = 1)
   
    #estimació de contorns i posterior dibuix dels contorns
    ret,thresh = cv2.threshold(dilation, 127, 255, 0)
    
    im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        #if contours[x] in ([0, 0],[360,210]):
    

    if contours:
        #print (contours[0])
        #CENTROIDS

        centres = []
        for i in range(len(contours)):
            moments = cv2.moments(contours[i])
            centres.append((int(moments['m10']/moments['m00']), int(moments['m01']/moments['m00'])))
            print(centres[0][0])
            #cv2.circle(frame, centres[-1], 3, (0, 0, 0), -1)
            #print(contours)
            if i>0:                
                dist = calculateDistance(centres[i-1][0],centres[i-1][1],centres[i][0],centres[i][1])
                #print (dist)
                area=cv2.contourArea(contours[i])
                prevarea=cv2.contourArea(contours[i-1])
                if dist < 120:                    
                    print (dist)
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
            #print(centres[0][0])
                        rect = cv2.minAreaRect(contours[i])
                        box = cv2.boxPoints(rect)
                        box = np.int0(box)
                        frame = cv2.drawContours(frame,[box],0,(0,0,255),2)

        #print(area)
        #hull = cv2.convexHull(cnt)
        #if area < 100:
       # cv2.drawContours(frame, hull, -1, (0,255,0), 3)

    #estimació del centroide
    #for cnt in contours:
        #rect = cv2.minAreaRect(cnt)
      #  box = cv2.boxPoints(rect)
      #  box = np.int0(box)
      #  frame = cv2.drawContours(frame,[box],0,(0,0,255),2)
    out.write(frame)
    outgray.write(dilation)
    ret, frame = cap.read()
    cv2.imwrite('frame.jpg',fgmask)
    #k = cv2.waitKey(30) & 0xff
    #if k == 27:
        #break
fgmask = fgbg.apply(frame)
out.write(frame)
outgray.write(dilation)
cap.release()
out.release()
outgray.release()
tend=time.time()-t
print(tend)
cv2.destroyAllWindows()
