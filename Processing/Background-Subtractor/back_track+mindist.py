from __future__ import print_function
import numpy as np
import cv2
from time import sleep
import sys
import functools as ft
import time

def find_if_close(cnt1,cnt2):
    row1,row2 = cnt1.shape[0],cnt2.shape[0]
    for i in range(row1):
        for j in range(row2):
            dist = np.linalg.norm(cnt1[i]-cnt2[j])
            if abs(dist) < 50 :
                return True
            elif i==row1-1 and j==row2-1:
                return False

#Inicialització del lector i escriptor de vídeo, monitorització del temps d'execució i creació del background substractor
t=time.time()
cap = cv2.VideoCapture('d5_30a120.mp4')
t=time.time()
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output_bg.avi',fourcc, 15.0, (360,240))
fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=True)
ret = True
#element estructurant que utilitazrem per l'opening+closing per eliminar falsos positius (matriu quadrada de 8x8 píxels)
kernel = np.ones((6,6),np.uint8)


while ret:
    
    #lectura i estimació del background
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    
    #operacions morfològiques
    opening = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
   
    #estimació de contorns i posterior dibuix dels contorns
    ret,thresh = cv2.threshold(closing, 127, 255, 0)
    im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(frame, contours, -1, (0,255,0), 3)
    LENGTH = len(contours)
    status = np.zeros((LENGTH,1))

    for i,cnt1 in enumerate(contours):
        x = i    
        if i != LENGTH-1:
            for j,cnt2 in enumerate(contours[i+1:]):
                x = x+1
                dist = find_if_close(cnt1,cnt2)
                if dist == True:
                    val = min(status[i],status[x])
                    status[x] = status[i] = val
                else:
                    if status[x]==status[i]:
                        status[x] = i+1

    unified = []
    maximum = int(cv2.max(status,0))
    for i in range (maximum):
        pos = np.where(status==i)[0]
        if pos.size != 0:
            cont = np.vstack(contours[i] for i in pos)
            hull = cv2.convexHull(cont)
            unified.append(hull)

    cv2.drawContours(frame,unified,-1,(0,255,0),2)
    cv2.drawContours(thresh,unified,-1,255,-1)
    #estimació del centroide hauria destar en un if
    cx = int(M['m10']/M['m00'])
    cx = int(M['m10']/M['m00'])
    #for cnt in contours:
        #rect = cv2.minAreaRect(cnt)
      #  box = cv2.boxPoints(rect)
      #  box = np.int0(box)
      #  frame = cv2.drawContours(frame,[box],0,(0,0,255),2)
    out.write(frame)
    ret, frame = cap.read()
    cv2.imwrite('frame.jpg',fgmask)
    #k = cv2.waitKey(30) & 0xff
    #if k == 27:
        #break
fgmask = fgbg.apply(frame)
out.write(fgmask)
cap.release()
out.release()
tend=time.time()-t
print(tend)
cv2.destroyAllWindows()
