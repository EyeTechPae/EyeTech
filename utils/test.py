#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

import cvutils
import cv2

A = cv2.imread('lena.png')
A = cv2.cvtColor(A, cv2.COLOR_BGR2GRAY)
#A = np.double(A)/255.0

M = np.zeros(A.shape, dtype="uint8")
M[255:256, 255:256] = 255;

KER = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
R = cvutils.reconstruct(A, M, KER, its=512)

plt.figure()
plt.subplot(1, 3, 1)
plt.imshow(A, cmap="gray")
plt.subplot(1, 3, 2)
plt.imshow(M, cmap="gray")
plt.subplot(1, 3, 3)
plt.imshow(R, cmap="gray")
plt.show()
