import random as rand
import cv2
import numpy as np
import sys

try:
    path = sys.argv[1]
except:
    path = 'car.png'

frame = cv2.imread(path)

# convert to grayscale
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
lap = cv2.Laplacian(gray, cv2.CV_64F)
gray = np.double(gray)
gray = cv2.addWeighted(gray, 1, lap, -1.25, 0)
gray[gray < 0] = 0
gray[gray > 255] = 255
gray = np.uint8(gray)
enhanced = gray.copy();
gray = cv2.GaussianBlur(gray, (5, 5), 3)

# top hat
#ker = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 5))
#clos = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, ker)
#gray = cv2.subtract(clos, gray)

# image contarst
aux = np.double(gray.copy())/255 * 2 - 1
aux = (aux + 0.0) * 1
aux[aux < -1] = -1
aux[aux > 1] = 1
gray = np.uint8((aux*0.5+0.5)*255)
#_, gray = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
#gray = cv2.Canny(gray, 127, 255)
#gray = cv2.Canny(gray, 75, 200)
gray = cv2.Canny(gray, 175, 200)

# compute sobel
sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0)
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1)
sobel_x[sobel_x < 0] = -sobel_x[sobel_x < 0]
sobel_y[sobel_y < 0] = -sobel_y[sobel_y < 0]
sobel_add = cv2.add(sobel_x, sobel_y)
ker = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
#sobel_add = cv2.morphologyEx(sobel_add, cv2.MORPH_DILATE, ker)

# threshold gradingt
print(sobel_add.max())
sobel_add[sobel_add <= 300] = 0
sobel_add[sobel_add > 300] = 1

# compute density
ker = np.ones((7, 63), dtype='float64')
dens = cv2.filter2D(sobel_add, cv2.CV_64F, ker)
dens = cv2.GaussianBlur(dens, (9, 9), 7)
print(dens.max())
print()

# threshold density
dens[dens <= 150] = 0
dens[dens > 150] = 1

# find contours
dens = np.uint8(dens*255)
_, conts, _ = cv2.findContours(dens.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE) 
for cont in conts:
    x, y, w, h = cv2.boundingRect(cont)
    if w > 300 or w < 32 or h > 100 or h < 16:
        continue
    if  w/h > 1 and w/h < 8:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)

cv2.imshow('asd', frame)   
cv2.imwrite('processed/{}'.format(path), frame)

# exit look
while cv2.waitKey(0) & 0xff != ord('q'):
    pass
