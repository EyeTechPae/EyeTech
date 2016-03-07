import numpy as np
import cv2



img1 = cv2.imread('carsol.jpg',0)
img2 = cv2.imread('car.jpg',0)
w, h = img1.shape[::-1]

surf = cv2.xfeatures2d.SURF_create(1000)

kp1, des1 = surf.detectAndCompute(img1,None)
kp2, des2 = surf.detectAndCompute(img2,None)



FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks = 50)

flann = cv2.FlannBasedMatcher(index_params, search_params)

matches = flann.knnMatch(des1,des2,k=2)



good_matches = []

for m,n in matches:
  print(m.distance)
  print(n.distance)
  if m.distance < 0.75*n.distance:
    good_matches.append(m)

print(len(good_matches))

src_pts = np.float32([ kp1[m.queryIdx].pt for m in good_matches ]).reshape(-1,1,2)
dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good_matches ]).reshape(-1,1,2)

print(dst_pts)
M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)
matchesMask = mask.ravel().tolist()

pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
dst = cv2.perspectiveTransform(pts,M)


img2 = cv2.polylines(img2,[np.int32(dst)],True,255,3)


#img2 = cv2.drawKeypoints(img2, kp2, np.array([]), (0,0,255), 2)

#img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,matches,None,flags=2)
cv2.imwrite('surfdetection.jpg',img2)
