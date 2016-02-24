#!/usr/bin/python

import numpy as np
import cv2

def reconstruct (src, mark, ker, its=32):
    # perform a reconstruction of the image src given a marker
    # the number of iterations is specified by the attribute its    
    # the dilation step is performed using the kernel ker

    # create a copy of the marker
    mark_copy = mark.copy()
    
    # important kickstarter (avoids surprises)
    rec_limit_step(src, mark_copy)

    # iterate reconstruction
    for i in range(its):
        mark_copy = rec_dilate_step(mark_copy, ker)
        mark_copy = rec_limit_step(src, mark_copy)
    
    return mark_copy

def rec_dilate_step (mark, ker):
    # dilate marker using morphologic kernel. The result
    # is eventually stored in aux
    mark = cv2.morphologyEx(mark, cv2.MORPH_DILATE, ker)
    return mark

def rec_limit_step (src, mark):
    mask = mark > src
    mark[mask] = src[mask]
    return mark

def hello (src, mark, ker):
    print('Hello world!')

if __name__ == "__main__":
    print('This is meant to be a module')
