from __future__ import print_function
import numpy as np
import cv2
from time import sleep
import sys
import functools as ft
import time



#Inicialització del lector i escriptor de vídeo, monitorització del temps d'execució i creació del background substractor
t=time.time()
cap = cv2.VideoCapture('d5_30a120.mp4')
t=time.time()
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output_bg.avi',fourcc, 15.0, (360,240))
fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=True)
ret = True
#element estructurant que utilitazrem per l'opening+closing per eliminar falsos positius (matriu quadrada de 8x8 píxels)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(6,6))
kernel_dilation = np.ones((8,8),np.uint8)


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
    
    #print (contours)
    if contours:
        #CENTROIDS
        #centres = []
        #for i in range(len(contours)):
           # moments = cv2.moments(contours[i])
            #centres.append((int(moments['m10']/moments['m00']), int(moments['m01']/moments['m00'])))
            #cv2.circle(frame, centres[-1], 3, (0, 0, 0), -1)
        cnt = contours[0]
        area = cv2.contourArea(cnt)
        print(area)
        hull = cv2.convexHull(cnt)
        #if area < 100:
        cv2.drawContours(frame, hull, -1, (0,255,0), 3)

    #estimació del centroide

    out.write(frame)
    ret, frame = cap.read()
    cv2.imwrite('frame.jpg',fgmask)
    #k = cv2.waitKey(30) & 0xff
    #if k == 27:
        #break
fgmask = fgbg.apply(frame)
out.write(frame)
cap.release()
out.release()
tend=time.time()-t
print(tend)
cv2.destroyAllWindows()
