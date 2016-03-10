import cv2
import numpy as np
import sys

def occupancy(x, y, ax, ay, varx, vary):
    parking_xP = ax + varx
    parking_yP = ay + vary
    parking_xN = ax - varx
    parking_yN = ay - vary
    if x< parking_xP and x > parking_xN:
        if y < parking_yP and y > parking_yN:
            return True
        else:
            return False
    else:
        return False

arg1=sys.argv[1]
arg2=sys.argv[2]
arg1=int(arg1)
arg2=int(arg2)
ax= 5
ay= 6
varx = 3
vary= 6
ocupat = False
ocupat=occupancy(arg1,arg2,ax,ay,varx,vary)
if ocupat == True:
    condicio = "ocupada"
else:
    condicio = "lliure"
print("La placa esta", condicio)
