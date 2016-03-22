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
cap = cv2.VideoCapture('d5_30a120.mp4')
t=time.time()
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output_bg.avi',fourcc, 15.0, (360,240))
outgray = cv2.VideoWriter('output_bg_gray.avi',fourcc, 15.0, (360,240),0)
fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=True)
ret = True
#element estructurant que utilitazrem per l'opening+closing per eliminar falsos positius (matriu quadrada de 8x8 píxels)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(6,6))
kernel_dilation = np.ones((8,8),np.uint8)

# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()
 
# Change thresholds
params.minThreshold = 10;
params.maxThreshold = 256;
 
# Filter by Area.
params.filterByArea = False
params.minArea = 150
 
# Filter by Circularity
params.filterByCircularity = False
params.minCircularity = 0.1
 
# Filter by Convexity
params.filterByConvexity = False
params.minConvexity = 0.87
 
# Filter by Inertia
params.filterByInertia = False
params.minInertiaRatio = 0.01
 
# Create a detector with the parameters
ver = (cv2.__version__).split('.')

detector = cv2.SimpleBlobDetector_create(params)
 



while ret:
    
    #lectura i estimació del background
    ret, frame = cap.read()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    fgmask = fgbg.apply(frame_gray)
    ret,fgmask = cv2.threshold(fgmask,127,255,cv2.THRESH_BINARY)
    
    #operacions morfològiques
    opening = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
    dilation = cv2.dilate(closing,kernel_dilation,iterations = 1)

    #estimació de contorns i posterior dibuix dels contorns
    # Detect blobs.
    keypoints = detector.detect(dilation, True)
    
    print(keypoints)
    # Draw detected blobs as red circles.
    # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
    imtowrite = cv2.drawKeypoints(frame, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    out.write(imtowrite)
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
