from abc import ABCMeta, abstractmethod

class Cam(metaclass=ABCMeta):

	def __init__(self, masks, ID, parksUp, parksDown): #abstract method
		pass	

	def isZoneIn(self): #abstract method
		pass
	
	def isZoneOut(self):  #abstract method
		pass

	def isParkingDown(self): #abstract method
		pass

	def isParkingUp(self): #abstract method
		pass

	def checkCamState(self): #abstract method
		pass
