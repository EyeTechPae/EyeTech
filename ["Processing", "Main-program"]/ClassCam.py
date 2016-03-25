#import all the functions form eyeTech.py
import eyeTech

class Cam(object):
	cars=[]
	notifyNextCam=0
	camNotified=0
	def __init__(self,camNumber,path,positionIN[],positionOUT[]):
		self.camNumber=camNumber
		self.cars.append(Car())
		self.path=path
		self.positionIN=[]	
		self.positionOUT=[]

	def detectCar	
		#return true when a CAR is detected
		return eyeTech.carDetected()
	def carIN
		#create Car if a car is detected in the IN zone
		if eyeTech.carIN(self.positionIN[]):
		self.cars.append(Car())
		
	def carOUT
		#return true when a CAR is detected in the OUT zone
		#notify next CAM 
		#remove Car
		if eyeTech.carOUT(self.positionOUT[]):
		notifyNextCam=1
		#TODO remove the nearest car to the OUT zone
		self.cars.remove(cars[123213])
		return 1
		else:
		notifyNextCam=0
		return 0
	def carUnparked	
		#when a CAR is detected AND the other camera don't notify:
		#create Car
		#write 0 in the data.txt 
		if (eyeTech.carDetected and camNotified=0):
		self.cars.append(Car())
		data=open("places.txt","w")
		places.write("0")
		places.close()
		return 1
		else:
		return 0
	def updateCars
		for i in self.cars
			i.updatePosition()

#TODO carParked()
	def carParked(self):  
		
########## Other testing functions########
		
	def displayCars(self):
		for i in self.cars:
			print i.pos

	
############
class Car(object):
	pos=0
	def __init__(self):
				
		
#TODO carParked
	def carParked(self):
#TODO updatePosition
	def updatePosition(self):
		
########### testing###########		
camara1=Cam(1,"hola")
camara1.carParked()
camara1.cars[0].carParked()
camara1.carUnparked()
camara1.displayCars()




