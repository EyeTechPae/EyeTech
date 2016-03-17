
import cv2
import numpy as np



#Initialize the video capture object:
cap=cv2.VideoCapture('sample3.mp4')
scaling_factor = 0.5



fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('outputBG.avi',fourcc, 30.0, (720,480))    
rval, frame = cap.read()
   
#Factor that controls the learning rate of the algorithm. Higher values indicates slower learning rate.
history=20
# Create the background substractor object:
bgSubstractor = cv2.createBackgroundSubtractorMOG2()
#Iterate while there is video:
while rval:
    
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #Apply the background substration model:
    mask = bgSubstractor.apply(frame, learningRate=1.0/history)
    output_img= cv2.blur(mask,(10,4))

    cv2.imwrite('provaBG.jpg', output_img)
    out.write(output_img)
    rval, frame = cap.read()

cap.release()
out.release()


       
