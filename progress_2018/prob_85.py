#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 12:36:57 2018

@author: simon
"""

import numpy as np

# The solution of the number of rectangles simplifies to the product
# of the Lth and Wth triangle numbers for a rectangle of length L and 
# width w.
# So construct a large array via numpy, get the difference from 2 million 
# And find the element which is least.

max_tri = 1000

q = np.arange(0,max_tri+1)
qplus1 = q + 1
tris = np.divide(np.multiply(q,qplus1),2).astype(np.int)
#print(tris)

tris_lst = []

for i in range(0,max_tri+1):
    tris_lst.append(tris)

tris_square = np.vstack(tris_lst)

rects = np.multiply(tris_square, tris_square.T)

diff = np.abs(rects - 2*10**6)

gap = np.min(diff)
anstup = np.where(diff==np.min(diff))
print(anstup, gap)
ans = (anstup[0][0], anstup[1][0])

print(ans[0]*ans[1]) # area of the answer rectangle