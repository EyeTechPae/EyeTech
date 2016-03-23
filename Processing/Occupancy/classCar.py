class Car(object):
	MAXttl=150 #If car position varition is equal during 150 consecutive fps, the vehicles is considered parked.	
	aux_pos=0
	ttl=0
	parked=0 # 0 indicates that car is not parked.

	def __init__(self, pos, ID):
		self.pos=pos
		self.ID=ID
		
		
	def carParked(self):
		
		if self.pos==self.aux_pos:
			self.ttl=self.ttl+1
		if self.ttl > self.MAXttl:
			aux_pos=self.pos
			parked=1
			print ('aparcao')
			return self.pos 			
		else:		
			aux_pos=self.pos
			parked=0
			print ('The car is moving')			
			return 0		






