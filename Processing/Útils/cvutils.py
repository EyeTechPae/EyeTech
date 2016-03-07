#!/usr/bin/python

import numpy as np
import cv2

def reconstruct (src, mark, ker, its=32):
    mark_copy = mark.copy()
    rec_limit_step(src, mark_copy)

    for i in range(its):
        mark_copy = rec_dilate_step(mark_copy, ker)
        mark_copy = rec_limit_step(src, mark_copy)
    
    return mark_copy

def rec_dilate_step (mark, ker):
    mark = cv2.morphologyEx(mark, cv2.MORPH_DILATE, ker)
    return mark

def rec_limit_step (src, mark):
    mask = mark > src
    mark[mask] = src[mask]
    return mark
