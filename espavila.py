#!/usr/bin/python
import cv2
import numpy as np

vc = cv2.VideoCapture('video2.avi')
fps = 15
capSize = (320,240) # this is the size of my source video
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
out.vout = cv2.VideoWriter()
success = self.vout.open('output.mov',fourcc,fps,capSize,True) 
rval, frame = vc.read()
while rval:
    self.vout.write(frame) 
    rval, frame = vc.read()
        #cv2.imshow("Result",frame)
        #cv2.waitKey(1);
    
    
    
vout.release()
self.vout = None
vc.release
