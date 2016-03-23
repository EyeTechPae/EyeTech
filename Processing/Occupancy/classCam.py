import classCar as EyeTechCar

class Cam(object):
    cars=[]
		
    def __init__(self,camNumber,path):
        self.camNumber=camNumber
        self.cars.append(EyeTechCar.Car(15,69))
        self.path=path
    def carParked(self):
        if self.cars[0].parked==1:
            self.cars.pop(0)
			#del cars[0]
        else:
            print('Position=', self.cars[0].pos)
    def carUnparked(self):
        self.cars.append(EyeTechCar.Car(25,55))
        print ('hola')
    def displayCars(self):
        for i in self.cars:
            print (i.ID)

camara1=Cam(1,"hola")
camara1.carParked()
camara1.cars[0].carParked()
camara1.carUnparked()
camara1.displayCars()

