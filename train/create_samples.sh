#!/usr/bin/env bash

opencv_createsamples -vec pos.vec -img pos/mat.jpg -num 500 -w 128 -h 32 -maxxangle 0.25 -maxyangle 0.25 -maxzangle 0.25 $1
