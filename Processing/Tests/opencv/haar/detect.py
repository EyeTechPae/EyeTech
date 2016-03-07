
import cv2
import numpy as np

faces_haar = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
eyes_haar = cv2.CascadeClassifier('eyes.xml')
plates_haar = cv2.CascadeClassifier('licenseplates.xml')
video = cv2.VideoCapture(0)

while True:
    _, frame = video.read()
    
    # convert to grayscale and detect faces
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #gray = cv2.resize(gray, (320, 240))
    #frame = cv2.resize(frame, (320, 240))
    faces = faces_haar.detectMultiScale(gray, 1.3, 5)
    plates = plates_haar.detectMultiScale(gray)
    
    # draw rectangle in detected faces
    for x, y, w, h in faces:
        face = gray[y:y+h, x:x+w]
        eyes = eyes_haar.detectMultiScale(face, 1.3, 5)
        for ex, ey, ew, eh in eyes:
            cv2.rectangle(frame, ((x+ex), (y+ey)), ((x+ex+ew), (y+ey+eh)), (255, 0, 0), thickness=1)
        #if len(eyes) > 0:
            cv2.rectangle(frame, (x, y), ((x+w), (y+h)), (0, 255, 0), thickness=2)
    
    # same for plates
    for x, y, w, h in plates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 255), thickness=2)
    
    # display image in window
    #frame = cv2.resize(frame, (640, 480))
    cv2.imshow('Haar', frame)

    # exit
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
