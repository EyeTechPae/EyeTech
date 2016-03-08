# import the necessary packages
import numpy as np
import argparse
#import imutils
import cv2
 
# construct the argument parser and parse the arguments

ap = argparse.ArgumentParser()
ap.add_argument("-t", "--template", required = True,
	help = "Path to the template image")  
#	Template y letter son los paths a la imagen template y letter


ap.add_argument("-l", "--letter", required = True,
	help = "Path to the letter image")
args = vars(ap.parse_args())
 
# load the template and letter images

template = cv2.imread(args["template"])
letter= cv2.imread(args["letter"])
(letterHeight, letterWidth) = letter.shape[:2]

# find the letter in the template
result = cv2.matchTemplate(template, letter, cv2.TM_CCOEFF)
(_, _, minLoc, maxLoc) = cv2.minMaxLoc(result)
print(maxLoc)

#cv2. CV_TM_SQDIFF CV_TM_SQDIFF_NORMED CV_TM_CCORR CV_TM_CCORR_NORMED CV_TM_CCOEFF CV_TM_CCOEFF_NORMED
#Estos son los metodos posibles de template matching.

#Para ejecutarlo
 #python find_letter.py --pathtemplate template.png --letter letter.png
