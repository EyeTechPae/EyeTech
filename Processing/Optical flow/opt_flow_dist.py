# Python 2/3 compatibility
from __future__ import print_function
import numpy as np
import cv2
from time import sleep
import sys
import functools as ft
import time
#Mirar multithread per anar més ràpid
#Opció 1: Analitzar els frames de 2 en 2 o de 3 en 3 .....
#Opció 2: 1 thread x calcular optical flow i un altre per calcular els punts que es mouen (good_points)

def locate(img, flow, step=32):
	posx = []
	posy = []
	#print(lines)
	h, w = img.shape[:2]
	y, x = np.mgrid[step/2:h:step, step/2:w:step].reshape(2,-1).astype(int)
	#print(x,y)
	fx, fy = flow[y,x].T
	vis = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
	i=0
	j=0
	for flowx in fx:
		#print(flowx)
		#Plantejar agafar un THRESHOLD més alt aixi pude no fa falta el good_points, tot i que estaria bé deixar-ho
		if abs(flowx)>1.5:
			#if flowx<0:
				#print("direccio correcte")
			#else:
				#print("va al reves!!")
			posx.append(x[i])
			posy.append(y[i])
			#print(posx[j])
		#print(posx,posy)
			#if posy>50 and posy<480:
			#	cv2.rectangle(vis,(posx,posy),(posx+20,posy+20),(0,0,255),2)
		i=i+1

	
	return posx, posy

def good_points(posx, posy):
	#Implementacio començada només per "x" i ja vorem despres x fer-ho en "y"
	good_points = []
	if len(posx) == 0:
		print("list is empty")
	#Hi hauran problemes, pensar una forma de comparar els punts bons del frame anterior o algo aixi...
	#Hi ha algun moment que nomes es detecti un punt que es mou del cotxe??????????
	elif len(posx) < 2:
		good_points.append(posx[0])	
	else:
		for x in posx:
			dist = x - posx[i]
			#Hauriem de mirar quina distacia agafem, jo crec que estaria entre 20-25....
			if dist<"algun numero":
				good_points.append(posx[i])
			i=i+1
		
	print(posx)
	return good_points
	


t=time.time()
fourcc = cv2.VideoWriter_fourcc(*'XVID')
vc = cv2.VideoCapture('foscam.mp4')
out = cv2.VideoWriter('output.avi',fourcc, 30.0, (360,240))
rval, prev = vc.read()
prevgray = cv2.cvtColor(prev, cv2.COLOR_BGR2GRAY)
show_hsv = False
show_glitch = False
cur_glitch = prev.copy()
rval, img = vc.read()
sk_frame = 6
z=0;
while rval:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    if z>=sk_frame:
        flow = cv2.calcOpticalFlowFarneback(prevgray, gray, None, 0.5, 2, 20, 3, 7, 1.5, flags=cv2.OPTFLOW_FARNEBACK_GAUSSIAN)
        prevgray = gray
        #x, y = getDisplacement(gray, flow)
        #draw_img, lines=draw_flow(gray,flow)
        #print("es mou!!!")
        posx, posy = locate(gray,flow)
        posx = good_points(posx, posy)
        #print(x,y)
        z=0;
    else:
        z=z+1
        #draw_img = gray
    
    #cv2.imwrite('prova.jpg', draw_img)
    #out.write(draw_img)
    rval, img = vc.read()
    
vc.release()
out.release()
tend=time.time()-t
print(tend)

