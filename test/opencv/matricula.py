#!/usr/bin/python

import cv2
import numpy as np

img = cv2.imread('matricula2.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ker = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
close = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, ker)
sub = cv2.subtract(close, gray)

ker2 = cv2.getStructuringElement(cv2.MORPH_RECT, (9,3))
lol = cv2.morphologyEx(sub, cv2.MORPH_DILATE, ker2)
#lol = cv2.morphologyEx(lol, cv2.MORPH_ERODE, ker2)
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, ker)
mask = cv2.inRange(lol, 100, 255)

cv2.imshow("matriula", sub)
cv2.imwrite("out.png", mask)
cv2.waitKey(0)
