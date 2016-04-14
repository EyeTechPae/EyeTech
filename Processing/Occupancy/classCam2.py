import sys
import d6_1 as camera2
import cv2

class Cam2(object):

	def __init__(self, masks, ID, parksDown, parksUp):
		for mask,index in zip(masks, range(len(masks))):
			self.masks[index]=cv2.imread(mask, 0)
		for parkUp, index in zip(parksUp, range(len(parksUp))):
			self.parksUp[index]=parkUp
		for parkDown, index in zip(parksDown, range(len(parksUp))):
			self.parksDown[index]=parkDown
		self.ID=ID

	def isZoneIn(self, frame): #override 
		frame_applied= frame*self.masks[0]		
		fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=True)
		ret = True
		str_open, str_dila = camera2.get_strelements(28,53)
		fgmask = fgbg.apply(frame_applied)
		img = camera2.operacions_morfologiques(fgmask, str_open, str_dila)
		contours = camera2.get_contours (img)
		centres, frame_applied = camera2.get_centroids (contours, frame_applied)
		if len(centres)>0:
			return True
		else:
			return False

	def isZoneOut(self):  #override 
		frame_applied= frame*self.masks[1]		
		fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=True)
		ret = True
		str_open, str_dila = camera2.get_strelements(28,53)
		fgmask = fgbg.apply(frame_applied)
		img = camera2.operacions_morfologiques(fgmask, str_open, str_dila)
		contours = camera2.get_contours (img)
		centres, frame_applied = camera2.get_centroids (contours, frame_applied)
		if len(centres)>0:
			return True
		else:
			return False

	def isParkingDown(self): #override 
		frame_applied= frame*self.masks[2]		
		fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=True)
		ret = True
		str_open, str_dila = camera2.get_strelements(28,53)
		fgmask = fgbg.apply(frame_applied)
		img = camera2.operacions_morfologiques(fgmask, str_open, str_dila)
		contours = camera2.get_contours (img)
		centres, frame_applied = camera2.get_centroids (contours, frame_applied)
		if len(centres)>0:
			return True
		else:
			return False

	def isParkingUp(self): #override 
		frame_applied= frame*self.masks[3]		
		fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=True)
		ret = True
		str_open, str_dila = camera2.get_strelements(28,53)
		fgmask = fgbg.apply(frame_applied)
		img = camera2.operacions_morfologiques(fgmask, str_open, str_dila)
		contours = camera2.get_contours (img)
		centres, frame_applied = camera2.get_centroids (contours, frame_applied)
		if len(centres)>0:
			return True
		else:
			return False

	def checkCamState(self): #override 

		if isParkingDown():
			for parkDown in self.parksDown:
				parkDown.checkOccupancyState()

		if isParkingUp():
			for parkUp in self.parksUp:
				parkUp.checkOccupancyState()
