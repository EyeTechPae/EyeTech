class Car(object):

	MAXttl=150 #If car position varition is equal during 150 consecutive fps, the vehicles is considered parked.	

	def __init__(self, pos, aux_pos, ID, ttl, parked):
		self.pos=pos
		self.aux_pos= aux_pos
		self.ID=ID
		self.ttl=0
		self.parked= 0 # 0 indicates that car is not parked.

	def carParked(self):

		if self.pos==self.aux_pos:
			self.ttl=self.ttl+1
		if self.ttl > MAXttl:
			self.aux_pos=self.pos
			self.parked=1
			return self.pos 			
		else:		
			self.aux_pos=self.pos
			self.parked=0			
			return 0		
