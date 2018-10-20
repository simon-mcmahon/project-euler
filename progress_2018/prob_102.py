#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 18:12:30 2018

@author: simon
"""

import numpy as np

# Test triangles

#A(-340,495), B(-153,-910), C(835,-947) CORRECT = True
#p0 = (-340,495)
#p1 = (-153,-910)
#p2 = (835,-947)

#X(-175,41), Y(-421,-714), Z(574,-645) CORRECT = False
#p0 = (-175,41)
#p1 = (-421,-714)
#p2 = (574,-645)

# Use https://stackoverflow.com/questions/2049582/how-to-determine-if-a-point-is-in-a-2d-triangle
# for algorihtm
# p = p0 + (p1 - p0) * s + (p2 - p0) * t
# (p1 - p0) * s + (p2 - p0) * t = (p-p0)
# 0<=s,t <=1 and s+t <= 1 for p inside triangle
# Ax = b
origs = []
with open('p102_triangles.txt', 'r') as tri_file:
    for line in tri_file:
        pnts = line.split(',')
        pnts = list(map(int, pnts))
        p0 = (pnts[0], pnts[1])
        p1 = (pnts[2],pnts[3])
        p2 = (pnts[4], pnts[5])

        A = np.array([[p1[0]-p0[0], p2[0]-p0[0]],[p1[1]-p0[1], p2[1]-p0[1]]])
        b = np.array([0-p0[0],0-p0[1]])
        
        x = np.linalg.solve(A,b)
        s = x[0]
        t = x[1]
        
        if (s>=0) and (t>=0) and (s+t<=1):
            origs.append(True)
        else:
            origs.append(False)
        

print(sum(origs))