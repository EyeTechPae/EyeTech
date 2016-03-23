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

def locate(img, flow, step=16):
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
		if abs(flowx)>1:
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
def good_track(posx, posy):
	Z = np.vstack((posx,posy))
	print(Z)
	# convert to np.float32
	Z = np.float32(Z)

	# define criteria and apply kmeans()
	criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
	ret,label,center=cv2.kmeans(Z,2,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
	#if center is not None:
	#	print (center[:,0])
	return center

def good_points(posx, posy):
	#Implementacio començada només per "x" i ja vorem despres x fer-ho en "y"
	i=0
	good_pointsx = []
	good_pointsy = []
	if len(posx) == 0:
		print("list is empty")
	#Hi hauran problemes, pensar una forma de comparar els punts bons del frame anterior o algo aixi...
	elif len(posx) < 2:
		print("not enough points")	
	else:
		for x in posx:
			distx = x - posx[i]
			#Hauriem de mirar quina distacia agafem, jo crec que estaria entre 20-25....
			if distx<10:
				good_pointsx.append(posx[i])
			i=i+1
		i=0
		for y in posy:
			disty = y - posy[i]
				
			#Hauriem de mirar quina distacia agafem, jo crec que estaria entre 20-25....
			if disty<30:
				good_pointsy.append(posy[i])
			i=i+1
		
	#print(good_pointsx, good_pointsy)
	return good_pointsx, good_pointsy

def draw_rectangles(img, goodx, goody, antx, anty):
	vis = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
	x = antx
	y = anty
	if len(goodx) != 0:
		x = goodx[0]
		y = goody[0]

	cv2.rectangle(vis,(x,y),(x+20,y+20),(0,0,255),2)
	return vis, x, y

def draw_centroids(img, center, pastcenter):
	vis = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
	pos = []
	i = 0
	for centroid in center:
		pos.append(np.int32(centroid[0]))
		i = i + 1
		if i==2:
			cv2.rectangle(vis,(pos[0],pos[1]),(pos[0]+20,pos[1]+20),(0,0,255),2)
			del pos[:]
			i = 0
	return vis


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
sk_frame = 0
z=0
antx = 0
anty = 0
while rval:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    if z>=sk_frame:
        flow = cv2.calcOpticalFlowFarneback(prevgray, gray, None, 0.5, 2, 20, 3, 7, 1.5, flags=cv2.OPTFLOW_FARNEBACK_GAUSSIAN)
        prevgray = gray
        #x, y = getDisplacement(gray, flow)
        #draw_img, lines=draw_flow(gray,flow)
        #print("es mou!!!")
        posx, posy = locate(gray,flow)
        center = good_track(posx, posy)
        if center is not None:
            draw_img = draw_centroids(gray, center, antx)
        else:
            draw_img = gray

        #goodx, goody = good_points(posx, posy)
        #draw_img, antx, anty = draw_rectangles(gray, goodx, goody, antx, anty)
        #print(x,y)
        z=0;
    else:
        z=z+1
        draw_img = gray
    
    cv2.imwrite('prova.jpg', draw_img)
    out.write(draw_img)
    rval, img = vc.read()
    
vc.release()
out.release()
tend=time.time()-t
print(tend)

