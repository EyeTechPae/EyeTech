

def cars_in_road(centroids, limy_up, limy_down, limy_down2):
#Calcula centroides que estan dins de la carretera, es limita la zona de carretera per limy_up i limy_down, 
#sent limit superior i inferior de la imatge respectivament. També els centroides 
#La funció retorna una list amb els centroides dels cotxes trobats a la carretera
	car_center_road = []
	car_center_parking = []
	for center in centroids:
		if center[1]<limy_down and center[1]>limy_up:
			car_center_road.append(center[0], center[1])
		elif ((center[1]<limy_down2 and center[1]>limy_down) or (center[1]<limy_up)):
			car_center_parking.append(center[0], center[1])
			
	return car_center_road, car_center_parking

def car_in_out(car_center_road, car_center_parking, limx_in, limx_out):
#A partir de la sortida de cars_in_road aquesta funció determina si el cotxe esta entran o sortint a partir dels limits especificats.
#La funcio retorna dues list dels cotxes entrants i sortints.
	i = 0
	for center in car_center_road:
		if center[i]>limx and center[i+1]<limy:
			car_center_in.append(center[i], center[i+1])
		elif center[i]<limx_out and center[i+1]<limy:
			car_center_out.append(center[i], center[i+1])
	return car_center_in, car_center_out


#implementacio:

i = 0
#Mirar cada x frames(x exemple 10...)

    if i==10:

#ComputeBackgroundSubtractor(...) aquesta funcio hauria de retornar els centroides com a: 
#Llista que dintre de cada casella contingui la posició (x,y) en la imatge.
#  si veiem ke es chungo adaptem les funcions cars_in_road
        centroids = ComputeBackgroundSubtractor(...) 
        centr_road, centr_parking = cars_in_road(centroids, cam.limy_up, cam.limy_down, cam.limy_down2)
        centr_in, centr_out = car_in_out(centr_road, centr_parking, cam.limx_in, cam.limx_out)

        




			
			

