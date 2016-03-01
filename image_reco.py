#!/usr/bin/python
import cv2
import numpy as np

vc = cv2.imread('car.jpg', 0)
car_cascade = cv2.CascadeClassifier('cars3.xml')
cars = car_cascade.detectMultiScale(vc, 1.1, 1)
ncars = 0    
for (x,y,w,h) in cars:
        cv2.rectangle(vc,(x,y),(x+w,y+h),0,2)
        ncars = ncars + 1
    
cv2.imwrite('imatge.png', vc) 
    
 
