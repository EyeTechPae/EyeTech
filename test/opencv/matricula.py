#!/usr/bin/python

import cv2
import numpy as np

img = cv2.imread('matricula.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#gray = cv2.GaussianBlur(gray, (3,3), 4)
ker = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
close = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, ker)
sub = cv2.subtract(close, gray)
mask = cv2.inRange(sub, 64, 255)
print(sub.shape)

cv2.imshow("matriula", mask)
cv2.waitKey(0)
