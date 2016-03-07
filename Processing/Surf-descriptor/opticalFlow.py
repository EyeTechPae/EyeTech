#!/usr/bin/python

import cv2
import numpy as np

#Downsampling factor for the image
scaling_factor = 0.5

#Number of frames to keep in the buffer when you are tracking.
#If you increase it, feature points will have more "inertia".
num_frames_to_track = 5

#Skip every 'n' frames. This is just to increase the speed.
num_frames_jump = 10

tracking_paths = []
frame_index = 0

tracking_params = dict(winSize = (15,15), maxLevel = 2, criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

fourcc = cv2.VideoWriter_fourcc(*'XVID')
vc = cv2.VideoCapture('sample2.mp4')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 30.0, (720,480))
rval, frame = vc.read()
print(frame)
while rval:
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    output_img = frame.copy()
    print("imatge gris")
    if len(tracking_paths) > 0:
        prev_img, current_img = prev_gray, frame_gray
        feat_points0 = np.float32([tp[-1] for tp in tracking_paths]).reshape(-1,1,2)

        #Compute feature points (optical flow)
        feat_points1, _, _= cv2.calcOpticalFlowPyrLK(prev_img, current_img, feat_points0, None, **tracking_params)
        feat_points0_rev, _, _= cv2.calcOpticalFlowPyrLK(current_img, prev_img, feat_points1, None, **tracking_params)
        print("featpoints")
        #Compute the difference of the feature points
        diff_feat_points = abs(feat_points0 - feat_points0_rev).reshape(-1,2).max(-1)

        #Threshold and keep good points
        good_points = diff_feat_points < 0.25

        new_tracking_paths = []

        for tp, (x, y), good_points_flag in zip(tracking_paths, feat_points1.reshape(-1,2), good_points):
            if not good_points_flag:
                continue
  
            tp.append((x,y))

            #Using the queue structure (first in, first out)
            if len(tp) > num_frames_to_track:
                del tp[0]
            new_tracking_paths.append(tp)

            #Draw circles on top of output image
            #cv2.circle(output_img, (x, y), 3, (0, 255, 0), -1)

        tracking_paths = new_tracking_paths
        print((x,y))
 
        #Draw lines on top of the output image
        cv2.polylines(output_img, [np.int32(tp) for tp in tracking_paths], False, (0, 150, 0),2)

        #Speed up. skip every 'n'th frame
    if not frame_index % num_frames_jump:
        mask = np.zeros_like(frame_gray)
        mask[:] = 255
        for x, y in [np.int32(tp[-1]) for tp in tracking_paths]:
            cv2.circle(mask, (x, y), 6, 0, -1)
                 
        #Extract good features to track
        feat_points = cv2.goodFeaturesToTrack(frame_gray, mask = mask, maxCorners = 500, qualityLevel = 0.3, minDistance = 7, blockSize = 7)

        if feat_points is not None:
            for x, y in np.float32(feat_points).reshape(-1,2):
                tracking_paths.append([(x, y)])

    frame_index = frame_index + 1
    prev_gray = frame_gray
    cv2.imwrite('prova.jpg', output_img)
    out.write(output_img)
    rval, frame = vc.read()

  
    
vc.release()
out.release()
