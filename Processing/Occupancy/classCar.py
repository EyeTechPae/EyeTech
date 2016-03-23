class Cam(object):
	cars=[]
		
	def __init__(self,camNumber,path):
		self.camNumber=camNumber
		self.cars.append(Car(15,69))
		self.path=path
	def carParked(self):
		if self.cars[0].parked==1:
			self.cars.pop(0)
			#del cars[0]
		else:
			print'Position=', self.cars[0].pos
	def carUnparked(self):
		self.cars.append(Car(25,55))
		print 'hola'
	def displayCars(self):
		for i in self.cars:
			print i.ID
	def opticalFlow
############
class Car(object):
	MAXttl=150 #If car position varition is equal during 150 consecutive fps, the vehicles is considered parked.	
	aux_pos=0
	ttl=0
	parked=0 # 0 indicates that car is not parked.

	def __init__(self, pos, ID):
		self.pos=pos
		self.ID=ID
		
		
	def carParked(self):
		d=detecta()
		if self.pos==self.aux_pos:
			self.ttl=self.ttl+1
		if self.ttl > self.MAXttl:
			aux_pos=self.pos
			parked=1
			print 'aparcao'
			return self.pos 			
		else:		
			aux_pos=self.pos
			parked=0
			print 'The car is moving'			
			return 0		
camara1=Cam(1,"hola")
camara1.carParked()
camara1.cars[0].carParked()
camara1.carUnparked()
camara1.displayCars()



