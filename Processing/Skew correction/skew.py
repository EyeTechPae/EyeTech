import cv2
import cv
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.pyplot import plot
#from scipy.weave.accelerate_tools import Vector
from ctypes.test.test_functions import POINT
from Tkconstants import BOTH
from ctypes.test.test_as_parameter import POINT

center = (0,0)

def computeIntersect(a, b) :
    print 'a=', a,'a[0]=', a[0]
    x1 = a[0]
    print x1
    y1 = a[1]
    x2 = a[2]    
    y2 = a[3]
    x3 = b[0]
    y3 = b[1]
    x4 = b[2]
    y4 = b[3]
    
      
        
        
    d = (float) ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
    pt= POINT
    pt.x = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / d
    pt.y = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / d
    return pt;
# }
# else
    #    return cv::Point2f(-1, -1);
#}

def sortCorners (corners, center) :
   
    print(corners)
    print center 
   
    top = []
    bot = []
    for i in range(len(corners)):
        
        if corners[i].y < center.y :
            top.append(corners[i])
            
        else : bot.append(corners[i])
   
    print 'top:'
    print top   
    print 'bot:'   
    print bot 
    
    corners.clear();
    
    if top.size() == 2 and bot.size() == 2 :
        
        tl = min(top[0].x , top[1].x)
        tr = max(top[0].x , top[1].x)
        bl = min(bot[0].x , bot[1].x) 
        br = max(bot[0].x , bot[1].x)
        
        corners.append(tl);
        corners.append(tr);
        corners.append(br);
        corners.append(bl);
    

img = cv2.imread('im7.png')

#if img.empty():
#   exit

cv2.imshow('img',img)
bw= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('bw',bw)
##find contours
kernel = np.ones((5,5),np.uint8)
cv2.morphologyEx(bw, cv2.MORPH_OPEN, kernel)
cv2.morphologyEx(bw, cv2.MORPH_CLOSE, np.array(0), kernel)
contours = cv2.findContours(bw, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
print contours
cv2.drawContours(img, contours, 3, (0,255,0), 3)
cv2.imwrite('CONTOURS.jpg',CONTOURS)
ret,bwt = cv2.threshold(bw,170,255,cv2.THRESH_BINARY)
#bwt = cv2.adaptiveThreshold(bw,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)
cv2.imwrite('binarization.jpg',bwt)
bbw= cv2.blur(bwt, (3, 3))
cv2.imshow('bbw',bbw)
cv2.imwrite('blur.jpg',bbw)
can= cv2.Canny(bwt, 100, 100, 3)
cv2.imshow('can',can)
cv2.imwrite('canny.jpg',can)
#lines= cv2.HoughLinesP(can, 1, np.pi/720.0, 10, 20, 10) #HE CANVIAT CV_PI PER 3.14

#print lines
#lines.transpose()
#print lines

#lines = cv2.HoughLines(can,1,np.pi/180,200)

lines = cv2.HoughLinesP(can,1,np.pi/180, 35, 15, 5 )
print lines

for x1,y1,x2,y2 in lines[0]:
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

cv2.imwrite('houghlines5.jpg',img)



#cv2.imwrite('houghlines3.jpg',img)
#cv2.imshow(img)
corners = []
#(m,n)=lines.shape
print(lines)
for i in range(lines.shape[1]):
    j=i+1
    for k in range(j, lines.shape[1]):
        print lines.shape[1]-j
    
    #print lines[i,0]
    #aux = lines[i]
    #j=i
    #print lines[i,j]
    #j=i+1
    
    #print lines [i,j]
    #k=j
    #print 'k=', k 

#for i in range(np.size(lines[1])) : 
        
        print i
        print k
        print lines[0, i]
        print lines[0, k]

      
        pt = computeIntersect(lines[0, i], lines[0, k]);
        if pt.x >= 0 and pt.y >= 0 :
            corners.append(pt)
            
        


approx = []
#cv2.approxPolyDP(corners, approx, cv2.arcLength(corners, True)  * 0.02, True)
# en 3rlloc hi havia aixo : cv::arcLength(cv::Mat(corners), true)

if approx.size() != 4 :

    print "The object is not quadrilateral!" 
    exit

    
#Get mass center

for i in range(len(corners)) :
    center += corners[i]
    center *= (1. / corners.size())

    sortCorners(corners, center);
    
    if (corners.size() == 0):
        
        print "The corners were not sorted correctly!" 
        exit
    
dst = img

#// Draw lines
for i in range(len(lines)) :
    
    v = lines[i]
    cv2.line(dst, (v[0], v[1]), (v[2], v[3]), (0,255,0))
    

#// Draw corner points
cv2.circle(dst, corners[0], 3, (255,0,0), 2)
cv2.circle(dst, corners[1], 3, (0,255,0), 2)
cv2.circle(dst, corners[2], 3, (0,0,255), 2)
cv2.circle(dst, corners[3], 3, (255,255,255), 2)

#// Draw mass center
cv2.circle(dst, center, 3, (255,255,0), 2);

quad = np.zeros(300, 220, np.uint8)

quad_pts=[]
quad_pts.append((0, 0));
quad_pts.append((quad.cols, 0));
quad_pts.append((quad.cols, quad.rows));
quad_pts.append((0, quad.rows));

transmtx = cv2.getPerspectiveTransform(corners, quad_pts)
cv2.warpPerspective(img, quad, transmtx, quad.size())

cv2.imshow("image", dst);
cv2.imshow("quadrilateral", quad);
cv2.waitKey();
exit


 
#############################################
