from __future__ import print_function
import numpy as np
import cv2
from time import sleep
import sys
import functools as ft
import time

t=time.time()
cap = cv2.VideoCapture('pae1.mp4')
t=time.time()
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output_bg.avi',fourcc, 30.0, (854,480))
fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=True)
ret = True
kernel = np.ones((8,8),np.uint8)
while ret:
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    
    opening = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
    ret,thresh = cv2.threshold(closing, 127, 255, 0)
    im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame, contours, -1, (0,255,0), 3)
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
