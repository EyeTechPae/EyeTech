import numpy as np
import cv2
import os, sys

def listfiles():
	# Open a file
	path = "/...PATH.../"
	#dirs is a list of Strings
	dirs = os.listdir( path )
	return dirs

def maskreader(num):
	#Make a list with filenames of the masks
	dirs = listfiles()
	#Select the place, the number of the place must be specified
	mask_name = dirs[num]
	#Read image
	mask = cv2.imread(mask_name)
	return mask
	
def masked(frame, mask):
	#Mask the frame
	masked_img = frame * mask
	#Gray scale transformation for SURF performance
	output_img = cv2.cvtColor(masked_img, cv2.COLOR_BGR2GRAY)
	return output_img

def computeSurfFeatures(masked_img):
	#Create SURF, the alpha coeficient must be specified
	surf = cv2.xfeatures2d.SURF_create(500)
	#Detect and Compute the keypoints
	kp, des = surf.detectAndCompute(masked_img,None)
	return kp,des

def matcher(des1, des2):
	#Inicialize Flann Matcher
	FLANN_INDEX_KDTREE = 0
	index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
	search_params = dict(checks = 50)
	flann = cv2.FlannBasedMatcher(index_params, search_params)
	#Compute Flann Matches
	matches = flann.knnMatch(des1, des2, k=2)
	return matches

def matcher_select(matches):
	#Select good matches (OPCIONAL!!!!!!! JA ESTEM FENT MASCARES XDDDD)
	good_matches = []
	for m,n in matches:
		if m.distance < 0.75*n.distance:
			good_matches.append(m)
	return good_matches

def computeGoodMatches(frame, kp1, des1):
	#Masking current frame (now), the number of place must be specified
	mask = maskreader(num_place)
	masked_frame = masked(frame,mask)
	#Extract SURF Features from current masked frame
	kp2, des2 = computeSurfFeatures(masked_frame)
	#FlanBasedMatcher to select some matches with a certain distance
	matches = matcher(des1,des2)
	#Select good matches
	good_matches = matcher_select(matches)
	return good_matches
	
	



