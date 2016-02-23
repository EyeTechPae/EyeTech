#!/usr/bin/python

import cv2
import numpy as np

img = cv2.imread('matricula.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ker = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
close = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, ker)

cv2.imshow("matriula", close)
cv2.waitKey(0)
