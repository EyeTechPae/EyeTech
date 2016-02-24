#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

import cvutils
import cv2

#A = cv2.imread('lena.png')
#A = cv2.cvtColor(A, cv2.COLOR_BGR2GRAY)

#M = np.zeros(A.shape, dtype="uint8")
#M[255:256, 255:256] = 255;

#KER = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
#R = cvutils.reconstruct(A, M, KER, its=256)

SIZE = (640, 480)
DOWN = (int(640/4), int(480/4))
cap = cv2.VideoCapture(0)

mark = np.zeros((DOWN[0], DOWN[1]), dtype="uint8")
mark[DOWN[0]/2, DOWN[1]/2] = 255
ker = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

combined = np.zeros((SIZE[1]*2, SIZE[0]*2), dtype="uint8")

while True:
    _, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.resize(gray, (DOWN[1], DOWN[0]))
    rec = cvutils.reconstruct(frame, mark, ker, its=128)

    rec = cv2.resize(rec, SIZE)
    cv2.line(rec, (0, 0), SIZE, (0, 255, 0))
    cv2.line(rec, (0, SIZE[1]), (SIZE[0], 0), (0, 255, 0))

    ranger = cv2.inRange(rec, 127, 255)

    combined[0:480, 0:640] = rec
    combined[0:480, 640:640*2] = gray
    combined[480:480*2, 0:640] = ranger
    cv2.imshow("capture", combined);
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()

'''
cv2.imwrite('recons.png', R)

plt.figure()
plt.subplot(1, 3, 1)
plt.imshow(A, cmap="gray")
plt.subplot(1, 3, 2)
plt.imshow(M, cmap="gray")
plt.subplot(1, 3, 3)
plt.imshow(R, cmap="gray")
plt.show()
'''
