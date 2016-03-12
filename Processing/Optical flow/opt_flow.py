# Python 2/3 compatibility
from __future__ import print_function
import numpy as np
import cv2
from time import sleep
import sys
import functools as ft
def locate(img, flow, step=64):
	#print(lines)
	h, w = img.shape[:2]
	y, x = np.mgrid[step/2:h:step, step/2:w:step].reshape(2,-1).astype(int)
	#print(x,y)
	fx, fy = flow[y,x].T
	vis = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
	i=0
	for flowx in fx:
		print(flowx)
		if abs(flowx)>0.9:
			posx=x[i]
			posy=y[i]
			print(posx,posy)
			cv2.rectangle(vis,(posx,posy),(posx+20,posy+20),(0,0,255),2)
		i=i+1

		#print(x,y)
		#if x>0:
		#print(x2,y2)


	return vis

	

def draw_flow(img, flow, step=16):
	h, w = img.shape[:2]
	y, x = np.mgrid[step/2:h:step, step/2:w:step].reshape(2,-1).astype(int)
	#print(x,y)
	fx, fy = flow[y,x].T
	lines = np.vstack([x, y, x+fx, y+fy]).T.reshape(-1, 2, 2)
	lines = np.int32(lines + 0.5)
	#print(len(fx), len(x))
	vis = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
	#cv2.polylines(vis, lines, 0, (0, 255, 0))
	#for (x1, y1), (x2, y2) in lines:
	#	cv2.circle(vis, (x1, y1), 1, (0, 255, 0), -1)
		#print(x1,y1)
	return vis, lines

def getDisplacement(img, flow, step=16):
	h, w = img.shape[:2]
	y, x = np.mgrid[step/2:h:step, step/2:w:step].reshape(2,-1).astype(int)
	fx, fy = flow[y,x].T
	#print(fx,fy)
	return (ft.reduce(lambda x, y: x + y, fx) / len(fx), ft.reduce(lambda x, y: x + y, fy) / len(fy))

fourcc = cv2.VideoWriter_fourcc(*'XVID')
vc = cv2.VideoCapture('sample3.mp4')
out = cv2.VideoWriter('output.avi',fourcc, 30.0, (720,480))
rval, prev = vc.read()
prevgray = cv2.cvtColor(prev, cv2.COLOR_BGR2GRAY)
show_hsv = False
show_glitch = False
cur_glitch = prev.copy()
rval, img = vc.read()
while rval:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    flow = cv2.calcOpticalFlowFarneback(prevgray, gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)
    prevgray = gray
    #x, y = getDisplacement(gray, flow)
    #draw_img, lines=draw_flow(gray,flow)
    print("es mou!!!")
    draw_img = locate(gray,flow)
    #print(x,y)
    
    cv2.imwrite('prova.jpg', draw_img)
    out.write(draw_img)
    rval, img = vc.read()
    
vc.release()
out.release()

