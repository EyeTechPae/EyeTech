#!/usr/bin/python

import cv2
import numpy as np

class Foo:
    att = 42
    def bar(self, i):
        att = i
    def foo(self):
        print(att)
    def lol(self):
        return Foo()

x = Foo()
img = cv2.imread('matricula2.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#gray = cv2.GaussianBlur(gray, (3,3), 3)
ker = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
close = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, ker)
sub = cv2.subtract(close, gray)

ker2 = cv2.getStructuringElement(cv2.MORPH_RECT, (9,3))
lol = cv2.morphologyEx(sub, cv2.MORPH_DILATE, ker2)
#lol = cv2.morphologyEx(lol, cv2.MORPH_ERODE, ker2)
#lol = cv2.GaussianBlur(lol, (5,5), 3)
mask = cv2.inRange(lol, 100, 255)
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, ker)

cv2.imshow("matriula", sub)
cv2.imwrite("out.png", sub)
cv2.waitKey(0)
