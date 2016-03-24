import cv2
import numpy as np



#Initialize the video capture object:
cap=cv2.VideoCapture('sample3.mp4')
scaling_factor = 0.5



fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('outputBG.avi',fourcc, 30.0, (720,480),0)    
rval, frame = cap.read()
   
#Factor that controls the learning rate of the algorithm. Higher values indicates slower learning rate.
history=150
# Create the background substractor object:
bgSubstractor = cv2.createBackgroundSubtractorMOG2()
#Iterate while there is video:
while rval:
    print('Analizing')
    #frame=cv2.resize(frame, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #Apply the background substration model:
    mask = bgSubstractor.apply(frame, learningRate=1.0/history)
    #gray_out=cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
    output_img= cv2.medianBlur(mask,5)
    
    cv2.imwrite('original.jpg',frame)
    cv2.imwrite('provaBG.jpg', output_img)
    out.write(output_img)
    rval, frame = cap.read()

cap.release()
out.release()






       
