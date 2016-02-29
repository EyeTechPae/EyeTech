#!/usr/bin/env python

import os

# all the negative files images
files = os.listdir('neg')

# file where the negative images will be listed
out = open('neg.txt', 'w')

# write files
for neg in files:
    out.write('neg/'+neg+'\n')

# close file
out.close()
