def main():
	#init cameras:
	#TODO define positionIN, positionOUT of each camera
	#cam0 only check if a vehicle is in the entrance of the parking
	cam0=Cam(0,"video1.avi",
	cam1=Cam(1,"video2.avi,
	cam2=Cam(2,"video3.avi",
	cam3=Cam(3,"video4.avi,
	cam4=Cam(4,"video5.avi",
	while 1:
		if(cam1.detectCar and cam0.carOUT):
			cam1.carIN()
			cam1.carOUT()
			cam1.carUnparked
			....
		if(cam2.detectCar and cam1.carOUT):
			cam2.carIN()
			cam2.carOUT()
