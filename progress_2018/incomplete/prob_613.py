#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 21:33:13 2018

@author: simon
"""
import numpy as np

# Monte Carlo simulation for Q613

# Generate the random attributes

from math import cos, sin

#np.random.seed(0)

counts = []

maxRun = 10
sims = 10**4

def minpos(arraylike):
    results = np.where(arraylike>0, arraylike, arraylike.max()).argmin(axis=1)
#    return np.where(arraylike>0,arraylike,arraylike.max()).min()
    unique, counts = np.unique(results, return_counts=True)
    return np.asarray((unique, counts)).T

for i in range(0,maxRun):

    angle = np.random.uniform(0, 2*np.pi, sims)
    Xs = np.random.uniform(0, 30, sims)
    Ys = np.array([np.random.uniform(0, (4/3)*x) for x in Xs])
    assert np.all(Ys < (4/3)*Xs)
    

    
    a1, a2 = 3,4
    #numerator = Ys*a1 - Xs*a2
    #denominator = a2*np.cos(angle) - a1*np.sin(angle)
    #fraction = np.divide(numerator, denominator)
    #assert np.allclose(fraction[0], (Ys[0]*a1 - Xs[0]*a2)/(a2*cos(angle[0]) - a1*sin(angle[0])))
    
    Xs = np.vstack([Xs, Xs, Xs])
    Ys = np.vstack([Ys, Ys, Ys])
    angle = np.vstack([angle, angle, angle])
    a1s = np.array([[3.0/np.sqrt(3.**2+4**2)],[3.0/3],[0.0]])
    a2s = np.array([[4./np.sqrt(3.**2 + 4**2)],[0.],[4./4]])
    
    b1s = np.array([[0.],[0.],[30.]])
    b1s = np.tile(b1s, sims)
    
    numerator = np.multiply(Ys,a1s) - np.multiply(Xs,a2s) + np. multiply(b1s,a2s)
    denominator = np.multiply(np.cos(angle), a2s) - np.multiply(np.sin(angle), a1s)
    assert numerator.shape == (3,sims)
    assert denominator.shape == (3,sims)
    fraction = np.divide(numerator, denominator)
    
    assert np.allclose(fraction[0,0], (Ys[0,0]*a1 - Xs[0,0]*a2)/(a2*cos(angle[0,0]) - a1*sin(angle[0,0])))
    assert np.allclose(Ys[1,:] + np.multiply(fraction[1,:], np.sin(angle[1,:])), np.tile(0., sims))
    assert np.allclose(Xs[2,:] + np.multiply(fraction[2,:], np.cos(angle[2,:])), np.tile(30., sims))
    assert np.allclose(Ys[0,:] + np.multiply(fraction[0,:], np.sin(angle[0,:])), (4/3)*(Xs[0,:] + np.multiply(fraction[0,:], np.cos(angle[0,:]))))
    assert np.where(fraction.T>0, fraction.T, fraction.T.max()).min(axis=1).max() < 50
    assert np.where(fraction.T>0, fraction.T, fraction.T.max()).min(axis=1).min() > 0
    counts += [minpos(fraction.T)]


#print(counts)
total = sims*maxRun
hyp_count = sum([x[0,1] for x in counts])
prob = hyp_count/total
print('probability = {}'.format(prob))
print('{} runs of {} trials'.format(maxRun, sims))

# Getting the answer as 0.4060438
# It seems the actual answer here is 0.391672...
# From here https://euler.stephan-brumme.com/613/


#print(Xs.T[0,:])
#print(Ys.T[0,:])
#print(angle.T[0,:])
#print(fraction.T[0,:])



