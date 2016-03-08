import random as rand
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    # read frame
    _, frame = cap.read()
   
    # convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (3, 3), 2)

    # image contarst
    aux = np.double(gray.copy())/255 * 2 - 1
    aux = aux * 8 + 0.25
    aux[aux < -1] = -1
    aux[aux > 1] = 1
    aux = np.uint8((aux*0.5+0.5)*255)

    # canny
    canny = cv2.Canny(aux, 100, 200)
    ker = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    #canny = cv2.morphologyEx(canny, cv2.MORPH_DILATE, ker)

    # threshold image
    _, thr = cv2.threshold(aux, 200, 255, cv2.THRESH_BINARY)
    #thr = cv2.adaptiveThreshold(aux, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 127, 4)

    # get contours and operate on hierarchy
    _, conts, hier = cv2.findContours(canny.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    children = []
    invalid_nodes = []
    for i, (_, _, _, parent) in enumerate(hier[0]):
        children.append([])
        x, y, w, h = cv2.boundingRect(conts[i])
        if w < 8 or h < 8:
            invalid_nodes.append(i)
            continue

        if parent >= 0:
            children[parent].append(i) 
            if parent in invalid_nodes:
                invalid_nodes.append(i)

    # find potential license plate nodes
    potential_chars = []
    potential_plates = []
    for i, cont in enumerate(conts):
        if i in invalid_nodes:
            continue

        x, y, w, h = cv2.boundingRect(cont)
        if len(children[i]) <= 2:
            potential = True
            for child in children[i]:
                if len(children[child]) > 0:
                    potential = False
                    break        
    
            if potential:
                potential_chars.append(i)

    for i, cont in enumerate(conts):
        if i in invalid_nodes:
            continue

        x, y, w, h = cv2.boundingRect(cont)
        if w > 256 or h > 256:
            continue

        aspect = w/h
        if aspect > 1 and aspect < 8:
            lol = set(children[i]) & set(potential_chars)            
            lol2 = set(children[i]) - lol
            if len(lol) >= 2 and len(lol2) <= 1:
                potential_plates.append(i)


    # draw contours
    black = np.zeros(frame.shape, dtype='uint8')
    for i, cont in enumerate(conts):
        x, y, w, h = cv2.boundingRect(cont)
        if i in invalid_nodes:
            continue

        color = rand.randint(0, 255), rand.randint(0, 255), rand.randint(0, 255)       
        cv2.drawContours(black, [cont], -1, color, thickness=1)

    for i in potential_plates:
        x, y, w, h = cv2.boundingRect(conts[i])
        color = (0, 255, 0)
        cv2.putText(black, '0', (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, color)
        cv2.rectangle(frame, (x, y), (x+w, y+h), color, thickness=2)
    
    # display image
    comp = np.zeros((480, 640*2, 3), dtype='uint8')
    comp[0:480, 0:640] = frame
    comp[0:480, 640:640*2] = black
    cv2.imshow('output', comp)

    # exit look
    if cv2.waitKey(1) & 255 == ord('q'):
        break

cap.release()
