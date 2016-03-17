# Python 2/3 compatibility
from __future__ import print_function
import numpy as np
import cv2
from time import sleep
import sys
import functools as ft
import time

def dist(x,y):   
	return numpy.sqrt(numpy.sum((x-y)**2))

def sort_points(posx, posy):

	i=0
	for i in range(len(posx)):
		coord = np.array((posx[i] ,posy[i]))
		for j in range(len(posx)):
			coord2 = np.array((posx[j] , posy[j]))
			dst = dist(coord, coord2)
			if dst<x and i=!j:
				good_pointsx[i] = coord[0]
				good_pointsy[i]	= coord[1]


def locate(img, flow, step=32):
	#print(lines)
	h, w = img.shape[:2]
	y, x = np.mgrid[step/2:h:step, step/2:w:step].reshape(2,-1).astype(int)
	#print(x,y)
	fx, fy = flow[y,x].T
	vis = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
	i=0, j=0
	contador=0
	for flowx in fx:
		#print(flowx)
		if abs(flowx)>1.5:
			#if flowx<0:
				#print("direccio correcte")
			#else:
				#print("va al reves!!")
			posx[j]=x[i]
			posy[j]=y[i]


	return posx, posy

	 
t=time.time()
fourcc = cv2.VideoWriter_fourcc(*'XVID')
vc = cv2.VideoCapture('sample2.mp4')
out = cv2.VideoWriter('output_flow.avi',fourcc, 30.0, (720,480))
rval, prev = vc.read()
prevgray = cv2.cvtColor(prev, cv2.COLOR_BGR2GRAY)
show_hsv = False
show_glitch = False
cur_glitch = prev.copy()
rval, img = vc.read()
sk_frame = 5
z=0
while rval:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    if z>=sk_frame:
        flow = cv2.calcOpticalFlowFarneback(prevgray, gray, None, 0.5, 2, 20, 3, 7, 1.5, flags=cv2.OPTFLOW_FARNEBACK_GAUSSIAN)
        prevgray = gray

        #x, y = getDisplacement(gray, flow)
        #draw_img, lines=draw_flow(gray,flow)
        #print("es mou!!!")
        posx, posy = locate(gray,flow)
        out.write(draw_img)
        #print(x,y)
        z=0;
    else:
        z=z+1
        draw_img = gray
        out.write(draw_img)
    
    cv2.imwrite('prova.jpg', draw_img)
#    out.write(draw_img)
    rval, img = vc.read()
    
vc.release()
out.release()
tend=time.time()-t
print(tend)

