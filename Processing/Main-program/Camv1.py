from random import randint
class Cam(object):
	def __init__(self,camNumber,videoPath,parks,camMasks):
		self.camNumber=camNumber
		self.videoPath=videoPath
		self.parks=parks
		self.camMasks=camMasks
#[cv2.cvtColor(camMask, cv2.COLOR_BGR2GRAY) for camMask in self.camMasks]
	def movDetectedUP(self):
		#detecta moviment a la zona de dalt amb la primera maskara del vector camMasks		
		
		return true
	def movDetectedDOWN(self):
		#igual
	def writeStates(self):
		file=open("states.txt","w")
		for park in self.parks:
			
			## TODO iteate for each line
			file.write(str(park.occupied))
			file.close()
	

